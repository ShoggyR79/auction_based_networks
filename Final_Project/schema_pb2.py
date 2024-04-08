# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cschema.proto\"1\n\x07Veggies\x12\x17\n\x06veggie\x18\x01 \x01(\x0e\x32\x07.Veggie\x12\r\n\x05value\x18\x02 \x01(\x02\"]\n\x06\x44rinks\x12\x11\n\x03\x63\x61n\x18\x01 \x01(\x0e\x32\x04.Can\x12\x17\n\x06\x62ottle\x18\x02 \x01(\x0e\x32\x07.Bottle\x12\x11\n\tcan_value\x18\x03 \x01(\r\x12\x14\n\x0c\x62ottle_value\x18\x04 \x01(\r\"7\n\x08MilkItem\x12\x1c\n\tmilk_type\x18\x01 \x01(\x0e\x32\t.MilkType\x12\r\n\x05value\x18\x02 \x01(\x02\"&\n\x05Milks\x12\x1d\n\nmilk_items\x18\x01 \x03(\x0b\x32\t.MilkItem\":\n\tBreadItem\x12\x1e\n\nbread_type\x18\x01 \x01(\x0e\x32\n.BreadType\x12\r\n\x05value\x18\x02 \x01(\x02\")\n\x06\x42reads\x12\x1f\n\x0b\x62read_items\x18\x01 \x03(\x0b\x32\n.BreadItem\"7\n\x08MeatItem\x12\x1c\n\tmeat_type\x18\x01 \x01(\x0e\x32\t.MeatType\x12\r\n\x05value\x18\x02 \x01(\x02\"&\n\x05Meats\x12\x1d\n\nmeat_items\x18\x01 \x03(\x0b\x32\t.MeatItem\"\x89\x01\n\x0cOrderRequest\x12\x19\n\x07veggies\x18\x02 \x01(\x0b\x32\x08.Veggies\x12\x17\n\x06\x64rinks\x18\x03 \x01(\x0b\x32\x07.Drinks\x12\x15\n\x05milks\x18\x04 \x01(\x0b\x32\x06.Milks\x12\x17\n\x06\x62reads\x18\x05 \x01(\x0b\x32\x07.Breads\x12\x15\n\x05meats\x18\x06 \x01(\x0b\x32\x06.Meats\"\xd9\x01\n\rHealthRequest\x12#\n\tdispenser\x18\x01 \x01(\x0e\x32\x10.DispenserStatus\x12\x10\n\x08icemaker\x18\x02 \x01(\r\x12$\n\nlight_bulb\x18\x03 \x01(\x0e\x32\x10.LightBulbStatus\x12\x13\n\x0b\x66ridge_temp\x18\x04 \x01(\x05\x12\x14\n\x0c\x66reezer_temp\x18\x05 \x01(\x05\x12$\n\rfridge_sensor\x18\x06 \x01(\x0e\x32\r.SensorStatus\x12\x0b\n\x03yaw\x18\x07 \x01(\x05\x12\r\n\x05stock\x18\x08 \x01(\r\"\x0e\n\x0cQueryRequest\"\x16\n\x08Resource\x12\n\n\x02id\x18\x01 \x01(\x05\"K\n\nBidRequest\x12\r\n\x05price\x18\x01 \x01(\x02\x12\x10\n\x08\x64uration\x18\x02 \x01(\x05\x12\x1c\n\tresources\x18\x03 \x03(\x0b\x32\t.Resource\"\xce\x01\n\x07Request\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.RequestType\x12&\n\rorder_request\x18\x02 \x01(\x0b\x32\r.OrderRequestH\x00\x12(\n\x0ehealth_request\x18\x03 \x01(\x0b\x32\x0e.HealthRequestH\x00\x12&\n\rquery_request\x18\x04 \x01(\x0b\x32\r.QueryRequestH\x00\x12\"\n\x0b\x62id_request\x18\x05 \x01(\x0b\x32\x0b.BidRequestH\x00\x42\t\n\x07request\">\n\rQueryResponse\x12\x1c\n\tresources\x18\x01 \x03(\x0b\x32\t.Resource\x12\x0f\n\x07\x62\x61lance\x18\x02 \x01(\x02\"\x1d\n\x0b\x42idResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\x9f\x01\n\x08Response\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.ResponseType\x12\x1a\n\x10message_response\x18\x02 \x01(\tH\x00\x12(\n\x0equery_response\x18\x03 \x01(\x0b\x32\x0e.QueryResponseH\x00\x12$\n\x0c\x62id_response\x18\x04 \x01(\x0b\x32\x0c.BidResponseH\x00\x42\n\n\x08response*W\n\x06Veggie\x12\x0f\n\x0bNONE_VEGGIE\x10\x00\x12\n\n\x06TOMATO\x10\x01\x12\x0c\n\x08\x43UCUMBER\x10\x02\x12\t\n\x05ONION\x10\x03\x12\x0b\n\x07LETTUCE\x10\x04\x12\n\n\x06PEPPER\x10\x05*5\n\x03\x43\x61n\x12\x0c\n\x08NONE_CAN\x10\x00\x12\x08\n\x04\x43OKE\x10\x01\x12\x08\n\x04\x42\x45\x45R\x10\x02\x12\x0c\n\x08WATERCAN\x10\x03*E\n\x06\x42ottle\x12\x0f\n\x0bNONE_BOTTLE\x10\x00\x12\n\n\x06SPRITE\x10\x01\x12\r\n\tGINGERALE\x10\x02\x12\x0f\n\x0bWATERBOTTLE\x10\x03*.\n\x08MilkType\x12\r\n\tNONE_MILK\x10\x00\x12\x08\n\x04SKIM\x10\x01\x12\t\n\x05WHOLE\x10\x02*1\n\tBreadType\x12\x0e\n\nNONE_BREAD\x10\x00\x12\t\n\x05WHITE\x10\x01\x12\t\n\x05WHEAT\x10\x02*>\n\x08MeatType\x12\r\n\tNONE_MEAT\x10\x00\x12\x07\n\x03HAM\x10\x01\x12\n\n\x06TURKEY\x10\x02\x12\x0e\n\nROAST_BEEF\x10\x03*N\n\x0bRequestType\x12\x0c\n\x08NONE_REQ\x10\x00\x12\t\n\x05ORDER\x10\x01\x12\n\n\x06HEALTH\x10\x02\x12\r\n\tQUERY_REQ\x10\x03\x12\x0b\n\x07\x42ID_REQ\x10\x04*G\n\x0f\x44ispenserStatus\x12\x0c\n\x08NONE_DIS\x10\x00\x12\x0b\n\x07OPTIMAL\x10\x01\x12\x0b\n\x07PARTIAL\x10\x02\x12\x0c\n\x08\x42LOCKAGE\x10\x03*7\n\x0fLightBulbStatus\x12\x0b\n\x07NONE_LB\x10\x00\x12\x0b\n\x07GOOD_LB\x10\x01\x12\n\n\x06\x42\x41\x44_LB\x10\x02*4\n\x0cSensorStatus\x12\x0b\n\x07NONE_SS\x10\x00\x12\x0b\n\x07GOOD_SS\x10\x01\x12\n\n\x06\x42\x41\x44_SS\x10\x02*7\n\x0cResponseType\x12\x0b\n\x07MESSAGE\x10\x00\x12\r\n\tQUERY_RES\x10\x01\x12\x0b\n\x07\x42ID_RES\x10\x02\x32.\n\rFridgeService\x12\x1d\n\x06method\x12\x08.Request\x1a\t.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'schema_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VEGGIE']._serialized_start=1402
  _globals['_VEGGIE']._serialized_end=1489
  _globals['_CAN']._serialized_start=1491
  _globals['_CAN']._serialized_end=1544
  _globals['_BOTTLE']._serialized_start=1546
  _globals['_BOTTLE']._serialized_end=1615
  _globals['_MILKTYPE']._serialized_start=1617
  _globals['_MILKTYPE']._serialized_end=1663
  _globals['_BREADTYPE']._serialized_start=1665
  _globals['_BREADTYPE']._serialized_end=1714
  _globals['_MEATTYPE']._serialized_start=1716
  _globals['_MEATTYPE']._serialized_end=1778
  _globals['_REQUESTTYPE']._serialized_start=1780
  _globals['_REQUESTTYPE']._serialized_end=1858
  _globals['_DISPENSERSTATUS']._serialized_start=1860
  _globals['_DISPENSERSTATUS']._serialized_end=1931
  _globals['_LIGHTBULBSTATUS']._serialized_start=1933
  _globals['_LIGHTBULBSTATUS']._serialized_end=1988
  _globals['_SENSORSTATUS']._serialized_start=1990
  _globals['_SENSORSTATUS']._serialized_end=2042
  _globals['_RESPONSETYPE']._serialized_start=2044
  _globals['_RESPONSETYPE']._serialized_end=2099
  _globals['_VEGGIES']._serialized_start=16
  _globals['_VEGGIES']._serialized_end=65
  _globals['_DRINKS']._serialized_start=67
  _globals['_DRINKS']._serialized_end=160
  _globals['_MILKITEM']._serialized_start=162
  _globals['_MILKITEM']._serialized_end=217
  _globals['_MILKS']._serialized_start=219
  _globals['_MILKS']._serialized_end=257
  _globals['_BREADITEM']._serialized_start=259
  _globals['_BREADITEM']._serialized_end=317
  _globals['_BREADS']._serialized_start=319
  _globals['_BREADS']._serialized_end=360
  _globals['_MEATITEM']._serialized_start=362
  _globals['_MEATITEM']._serialized_end=417
  _globals['_MEATS']._serialized_start=419
  _globals['_MEATS']._serialized_end=457
  _globals['_ORDERREQUEST']._serialized_start=460
  _globals['_ORDERREQUEST']._serialized_end=597
  _globals['_HEALTHREQUEST']._serialized_start=600
  _globals['_HEALTHREQUEST']._serialized_end=817
  _globals['_QUERYREQUEST']._serialized_start=819
  _globals['_QUERYREQUEST']._serialized_end=833
  _globals['_RESOURCE']._serialized_start=835
  _globals['_RESOURCE']._serialized_end=857
  _globals['_BIDREQUEST']._serialized_start=859
  _globals['_BIDREQUEST']._serialized_end=934
  _globals['_REQUEST']._serialized_start=937
  _globals['_REQUEST']._serialized_end=1143
  _globals['_QUERYRESPONSE']._serialized_start=1145
  _globals['_QUERYRESPONSE']._serialized_end=1207
  _globals['_BIDRESPONSE']._serialized_start=1209
  _globals['_BIDRESPONSE']._serialized_end=1238
  _globals['_RESPONSE']._serialized_start=1241
  _globals['_RESPONSE']._serialized_end=1400
  _globals['_FRIDGESERVICE']._serialized_start=2101
  _globals['_FRIDGESERVICE']._serialized_end=2147
# @@protoc_insertion_point(module_scope)