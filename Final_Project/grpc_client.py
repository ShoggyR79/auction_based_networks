  #  Author: Aniruddha Gokhale
#  Created: Fall 2023
#
#  Purpose: demonstrate serialization of a user-defined data structure using
#  Protocol Buffers combined with gRPC. Note that here we
#  are more interested in how a serialized packet gets sent over the network
#  and retrieved. To that end, we really don't care even if the client and
#  server were both on the same machine or remote to each other.

# This one implements the client functionality
#

# Note that this code mimics what we did with FlatBufs+ZeroMQ but this time
# we mix Protocol Buffers and gRPC

# The different packages we need in this Python driver code
import os
import sys
import time  # needed for timing measurements and sleep
import math

import random  # random number generator
import argparse  # argument parser

import logging

import grpc   # for gRPC

# import generated packages
import schema_pb2 as spb
import schema_pb2_grpc as spb_grpc

##################################
#        Driver program
##################################

def driver (name, iters, vec_len, port, server_ip):

  print ("Driver program: Name = {}, Num Iters = {}, Peer port = {}".format (name, iters, vec_len, port))

  # first obtain a peer and initialize it
  print ("Driver program: create handle to the client and then run the code")
  try:

    # Use the insecure channel to establish connection with server
    print ("Instantiate insecure channel")
    channel = grpc.insecure_channel(f"{server_ip}:{port}")

    print ("Obtain a proxy object to the server")
    stub = spb_grpc.FridgeServiceStub (channel)     # TODO Change

    # now send the serialized custom message for the number of desired iterations
    print ("Allocate the Request object that we will then populate in every iteration")
    
    starts = []
    ends = []
    for i in range (iters):
      req = spb.Request ()
      req.type = spb.RequestType.QUERY_REQ
      # send request to get current balance and available resources to bid
      _resp = stub.method (req)
      available = [r.id for r in _resp.query_response.resources]
      print(f"Available: {available}")
      total_available = sum(available)
      balance = _resp.query_response.balance
      print(f"Balance: {balance}")
      resources = []
      # choose a random subset 
      for a in available:
        # 50% chance, may change this later
        # more chance == more aggressive scheduling
        # make this a cli argument or something
        r = random.randint(0,1)
        if r == 1:
           resources.append(a)
      if len(resources) == 0:
        # wait for next iter
        time.sleep(10)
        continue
      utility = sum(resources)
      price = math.floor((utility/total_available)*(balance))
      duration = random.randint(1,5)
      print(f"Bid: price: {price}, duration: {duration}, resources: {resources}")
      req = spb.Request()
      req.type = spb.RequestType.BID_REQ
      bid_req = spb.BidRequest()
      bid_req.price = price
      bid_req.duration = duration
      bid_req.resources.extend([spb.Resource(id=r) for r in resources])
      req.bid_request.CopyFrom(bid_req)
      _resp = stub.method (req)
      print(_resp.bid_response.status)
      

      # sleep a while before we send the next serialization so it is not
      # extremely fast
      time.sleep (0.050)  # 50 msec

  except Exception as e:
    print(e)
    return
  

  latencies = [end - start for start, end in zip(starts, ends)]

  # Append mean latency to file
  with open('auction_averages_grpc.txt', 'a') as file:
      file.write(','.join(latencies))




  
##################################
# Command line parsing
##################################
def parseCmdLineArgs ():
    # parse the command line
    parser = argparse.ArgumentParser ()

    # add optional arguments
    parser.add_argument ("-i", "--iters", type=int, default=10, help="Number of iterations to run (default: 10)")
    parser.add_argument ("-l", "--veclen", type=int, default=20, help="Length of the vector field (default: 20; contents are irrelevant)")
    parser.add_argument ("-n", "--name", default="ProtoBuf gRPC Demo", help="Name to include in each message")
    parser.add_argument ("-p", "--port", type=int, default=5577, help="Port where the server part of the peer listens and client side connects to (default: 5577)")
    parser.add_argument( "-s", "--server_ip", default="localhost", help="IP address of the server (default: localhost)")
    
    # parse the args
    args = parser.parse_args ()

    return args
    
#------------------------------------------
# main function
def main ():
  """ Main program """

  print("Demo program for Protocol Buffers with gRPC serialization/deserialization")

  # first parse the command line args
  parsed_args = parseCmdLineArgs ()
    
  # start the driver code
  driver (parsed_args.name, parsed_args.iters, parsed_args.veclen, parsed_args.port, parsed_args.server_ip)

#----------------------------------------------
if __name__ == '__main__':
    main ()
