#  Author: Aniruddha Gokhale
#  Created: Fall 2023
#
#  Purpose: demonstrate serialization of a user-defined data structure using
#  Protocol Buffers combined with gRPC. Note that here we
#  are more interested in how a serialized packet gets sent over the network
#  and retrieved. To that end, we really don't care even if the client and
#  server were both on the same machine or remote to each other. Thus,
#  to simplify coding, we have mixed both the client and server in the same
#  code so that they run on the same machine. Hence, we term this as a Peer
#  which can don both roles.  When writing code for distributed client and
#  server, just separate the two pieces.
#

# Note that this code mimics what we did with FlatBufs+ZeroMQ but this time
# we mix Protocol Buffers and gRPC

# The different packages we need in this Python driver code
import os
import sys
import time  # needed for timing measurements and sleep

import random  # random number generator
import argparse  # argument parser

from concurrent import futures   # needed for thread pool
import logging

import grpc   # for gRPC
# import generated packages
import schema_pb2 as spb
import schema_pb2_grpc as spb_grpc

import heapq
import threading
import datetime

def log(str):
  print(f"[{datetime.datetime.now().time()}] {str}")


class Bank(object):
  BASE_CURRENCY = 100
  TAX_RATE = 0.2
  TAX_THRESHOLD = 50
  users = dict()
  total_bid_collected = 0
  total_user_collected = 0
  def __init__(self):
      pass
  
  def get_balance(self, user):
    if user not in self.users:
      self.users[user] = {
        'balance': self.BASE_CURRENCY,
        'resources': []
      }
    return self.users[user]['balance']

  # return true if the bid is valid, false otherwise
  # if new user, then load their account with the base amount of currency
  def verify_user(self, user, bid):
    if user not in self.users:
      self.users[user] = {
        'balance': self.BASE_CURRENCY,
        'resources': []
      }
      return True
    else:
      if self.users[user]['balance'] < bid.price:
        return False
      else:
        return True
  
  def reset_collect_bid(self):
    self.total_bid_collected = 0
    self.total_user_collected = 0

  def collect_bid(self, user, bid):
    self.total_bid_collected += bid.price
    self.total_user_collected += 1
    self.users[user]['balance'] -= bid.price
  
  def redistribute_bid(self, user):
    if self.total_user_collected == 0:
      return
    self.users[user]['balance'] += self.total_bid_collected/self.total_user_collected

  def collect_tax(self):
    total_currency = 0
    for user in self.users.keys():
      total_currency += self.users[user]['balance']
    self.TAX_THRESHOLD = total_currency/len(self.users.keys())
    users_not_taxed = []
    tax_pool = 0
    for user in self.users.keys():
      if self.users[user]['balance'] > self.TAX_THRESHOLD:
        tax_pool += self.TAX_RATE*self.users[user]['balance']
        self.users[user]['balance'] -= self.TAX_RATE*self.users[user]['balance']
      else:
        users_not_taxed.append(user)
    # redistribute
    for user in users_not_taxed:
      self.users[user]['balance'] += tax_pool/len(users_not_taxed)

class Bid(object):
  def __init__(self, price, duration, resources):
    self.price = price
    self.duration = duration
    self.resources = resources

class Auction(object):
  heap = []
  winners = []
  bids = dict()
  def __init__(self):
    pass

  def accept_bid(self, user, bid):
    mutex.acquire()
    # bid is an object of the form {price, duration, resources (list)}
    if not bank.verify_user(user, bid):
      return False
    score = bid.price/(bid.duration*sum([load_balancer.get_load_factor(r) for r in bid.resources]))
    heapq.heappush(self.heap, (-score, user))
    self.bids[user] = bid
    log(f"Bid submitted by {user} - price: {bid.price}, duration: {bid.duration}, resources: {bid.resources}")
    mutex.release()
    return True
  
  def settle_bids(self):
    self.winners = []
    available = load_balancer.get_available_resources()
    bank.reset_collect_bid()
    redistributed_users = set()
    while len(self.heap) > 0:
      _, user = heapq.heappop(self.heap)
      can_schedule = True
      for r in self.bids[user].resources:
        if r not in available:
          can_schedule = False
          break
      if can_schedule:
        bank.collect_bid(user, self.bids[user])
        self.winners.append(user)
        for r in self.bids[user].resources:
          available.remove(r)
          load_balancer.schedule(r, user, self.bids[user].duration)
      else:
        redistributed_users.add(user)
    for user in redistributed_users:
      bank.redistribute_bid(user)
    # reset
    self.heap = []
    self.bids = dict()
    return
  
  def is_winner(self, user):
    return user in self.winners


class LoadBalancer(object):
  resources = {
    1: {
      'user': '',
      'load_factor': 1,
      'duration': 0 # duration until which the user has access
    },
    2: {
      'user': '',
      'load_factor': 1,
      'duration': 0 # duration until which the user has access
    },
    3: {
      'user': '',
      'load_factor': 1,
      'duration': 0 # duration until which the user has access
    },
    4: {
      'user': '',
      'load_factor': 1,
      'duration': 0 # duration until which the user has access
    },
    5: {
      'user': '',
      'load_factor': 1,
      'duration': 0 # duration until which the user has access
    }
  }
  def __init__(self):
    pass

  def get_load_factor(self, resource):
    return self.resources[resource]['load_factor']
  
  def get_available_resources(self):
    available = []
    for k,v in self.resources.items():
      if v['user'] == '':
        available.append(k)
    return available
  
  def schedule(self, resource, user, duration):
    self.resources[resource]['user'] = user
    self.resources[resource]['duration'] = duration
  
  def get_resource_compute(self, user):
    resource_compute = 0
    for k, v in self.resources.items():
      if v['user'] == user:
        resource_compute += k
    # +1 to avoid no compute
    return 1+resource_compute

  def get_resource_ownerships(self):
    for r, v in self.resources.items():
      if v['user'] == '':
        print(f"Resource {r} is free")
      else:
        print(f"Resource {r} is used by {v['user']}")
  
  def tick(self):
    for r in self.resources.keys():
      if self.resources[r]['duration'] == 0:
        continue
      self.resources[r]['duration'] -= 1
      if self.resources[r]['duration'] == 0:
        self.resources[r]['user'] = ''
    
def timer_update():
  global requests_processed
  tick = 0
  time.sleep(15)
  while True:
      # update line chart
      requests_processed_history.append(requests_processed)

      with open("auction_requests_processed.txt", "a") as file:
        file.write(str(requests_processed))
        file.write("\n")

      log(f"Number of processed requests: {requests_processed}")
      mutex.acquire()
      tick = (tick+1)%3
      with condition:
        load_balancer.tick()
        # settle bids every 10 seconds
        auction.settle_bids()
        log("Bids settled")
        log("Current Resrouce Usage:")
        load_balancer.get_resource_ownerships()
        condition.notify_all()
      # collect tax every 30 seconds
      if tick%3 == 0:
        bank.collect_tax()
        log("Tax collected")
      mutex.release()
      print("----------------------------------------------------------")
      time.sleep(10)

bank = Bank()
auction = Auction()
load_balancer = LoadBalancer()
# synchronize accepting bids vs settling bids
mutex = threading.Lock()
condition = threading.Condition()

# keep track of how many requests we have processed
requests_processed = 0
# keep track of a line chart or something
requests_processed_history = []




##################################
#  The Service implementation class
##################################
class ServiceHandler (spb_grpc.FridgeServiceServicer):
  
  # Implement the method message that gets called on us via an upcall
  # Note, we have to use the same name for the method because it must be an
  # overridden method
  def method (self, request, context):
    global requests_processed
    """ Handle request message """
    try:
      user = context.peer()
      # here, let us just print what we got.
      # log ("Received request - type: {}, user: {}".format(request.type, user))
      
      # Now send response
      resp = spb.Response ()  # allocate the response object. Note it is empty
      if (request.type == spb.RequestType.ORDER) :
        resource_compute = load_balancer.get_resource_compute(user)
        # simulate doing work (more resource compute = faster work)
        time.sleep(10/resource_compute)
        requests_processed += 1
        resp_msg = "order_received"
        resp.message_response = resp_msg
      elif request.type == spb.RequestType.HEALTH:
        resource_compute = load_balancer.get_resource_compute(user)
        # simulate doing work (more resource compute = faster work)
        time.sleep(10/resource_compute)
        requests_processed += 1
        resp_msg = "healthy"
        resp.message_response = resp_msg
      elif request.type == spb.RequestType.QUERY_REQ:
        log(f"Available resources requested by {user}")
        available = load_balancer.get_available_resources()
        balance = bank.get_balance(user)
        query_resp = spb.QueryResponse()
        query_resp.resources.extend([spb.Resource(id=a) for a in available ])
        query_resp.balance = balance
        resp.query_response.CopyFrom(query_resp)
        
      elif request.type == spb.RequestType.BID_REQ:
        price = request.bid_request.price
        duration = request.bid_request.duration
        resources = [r.id for r in request.bid_request.resources]
        bid = Bid(price, duration, resources)
        if not auction.accept_bid(user, bid):
          
          bid_resp = spb.BidResponse()
          bid_resp.status = "Invalid Bid"
          resp.bid_response.CopyFrom(bid_resp)
        else:
          # TODO: this means this worker is blocked until bid is settled
          # might not be very efficient but let's go with this for now
          with condition:
            condition.wait()
            bid_resp = spb.BidResponse()
            if auction.is_winner(user):
              bid_resp.status = "Won Bid"
            else:
              bid_resp.status = "Lost Bid"
            resp.bid_response.CopyFrom(bid_resp)

          
        

    
      return resp   # note that this is what is supposed to be returned
    except:
      log ("Some exception occurred handling method {}".format (sys.exc_info()[0]))
      raise

##################################
#        Driver program
##################################

def driver (port):

  log ("Driver program: Port = {}".format (port))

  # run the program
  log ("Driver program: create and run the server")

  try:
  
    # Create a server handle
    log ("Create a server handle")
    server = grpc.server (futures.ThreadPoolExecutor (max_workers=10))

    # Now create our message handler object
    log ("Instantiate our service handler")
    handler = ServiceHandler ()

    # Make the binding between the stub and the handler
    log ("Make the connection between our handler class and server")
    # TODO: make schema for bids
    spb_grpc.add_FridgeServiceServicer_to_server(handler, server)

    log ("Add port to our server")
    server.add_insecure_port("[::]:" + str (port))

    log ("Set up bank, auction, load balancer")
    t = threading.Thread(target=timer_update)
    t.start()

    log ("Start the server")
    server.start()

    log("Server started, listening on {}".format (port))
    server.wait_for_termination()
    t.join()

  except:
    log ("Some exception occurred {}".format (sys.exc_info()[0]))
    return
  
  
##################################
# Command line parsing
##################################
def parseCmdLineArgs ():
    # parse the command line
    parser = argparse.ArgumentParser ()

    # add optional arguments
    parser.add_argument ("-p", "--port", type=int, default=5577, help="Port where the server part of the peer listens and client side connects to (default: 5577)")
    
    # parse the args
    args = parser.parse_args ()

    return args
    
#------------------------------------------
# main function
def main ():
  """ Main program """

  log("Demo program for Protocol Buffers with gRPC serialization/deserialization")

  # first parse the command line args
  parsed_args = parseCmdLineArgs ()
    
  # start the driver code
  driver (parsed_args.port)

#----------------------------------------------
if __name__ == '__main__':
    main ()
