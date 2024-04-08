from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Veggie(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE_VEGGIE: _ClassVar[Veggie]
    TOMATO: _ClassVar[Veggie]
    CUCUMBER: _ClassVar[Veggie]
    ONION: _ClassVar[Veggie]
    LETTUCE: _ClassVar[Veggie]
    PEPPER: _ClassVar[Veggie]

class Can(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE_CAN: _ClassVar[Can]
    COKE: _ClassVar[Can]
    BEER: _ClassVar[Can]
    WATERCAN: _ClassVar[Can]

class Bottle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE_BOTTLE: _ClassVar[Bottle]
    SPRITE: _ClassVar[Bottle]
    GINGERALE: _ClassVar[Bottle]
    WATERBOTTLE: _ClassVar[Bottle]

class MilkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE_MILK: _ClassVar[MilkType]
    SKIM: _ClassVar[MilkType]
    WHOLE: _ClassVar[MilkType]

class BreadType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE_BREAD: _ClassVar[BreadType]
    WHITE: _ClassVar[BreadType]
    WHEAT: _ClassVar[BreadType]

class MeatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE_MEAT: _ClassVar[MeatType]
    HAM: _ClassVar[MeatType]
    TURKEY: _ClassVar[MeatType]
    ROAST_BEEF: _ClassVar[MeatType]

class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE_REQ: _ClassVar[RequestType]
    ORDER: _ClassVar[RequestType]
    HEALTH: _ClassVar[RequestType]
    QUERY_REQ: _ClassVar[RequestType]
    BID_REQ: _ClassVar[RequestType]

class DispenserStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE_DIS: _ClassVar[DispenserStatus]
    OPTIMAL: _ClassVar[DispenserStatus]
    PARTIAL: _ClassVar[DispenserStatus]
    BLOCKAGE: _ClassVar[DispenserStatus]

class LightBulbStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE_LB: _ClassVar[LightBulbStatus]
    GOOD_LB: _ClassVar[LightBulbStatus]
    BAD_LB: _ClassVar[LightBulbStatus]

class SensorStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE_SS: _ClassVar[SensorStatus]
    GOOD_SS: _ClassVar[SensorStatus]
    BAD_SS: _ClassVar[SensorStatus]

class ResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE: _ClassVar[ResponseType]
    QUERY_RES: _ClassVar[ResponseType]
    BID_RES: _ClassVar[ResponseType]
NONE_VEGGIE: Veggie
TOMATO: Veggie
CUCUMBER: Veggie
ONION: Veggie
LETTUCE: Veggie
PEPPER: Veggie
NONE_CAN: Can
COKE: Can
BEER: Can
WATERCAN: Can
NONE_BOTTLE: Bottle
SPRITE: Bottle
GINGERALE: Bottle
WATERBOTTLE: Bottle
NONE_MILK: MilkType
SKIM: MilkType
WHOLE: MilkType
NONE_BREAD: BreadType
WHITE: BreadType
WHEAT: BreadType
NONE_MEAT: MeatType
HAM: MeatType
TURKEY: MeatType
ROAST_BEEF: MeatType
NONE_REQ: RequestType
ORDER: RequestType
HEALTH: RequestType
QUERY_REQ: RequestType
BID_REQ: RequestType
NONE_DIS: DispenserStatus
OPTIMAL: DispenserStatus
PARTIAL: DispenserStatus
BLOCKAGE: DispenserStatus
NONE_LB: LightBulbStatus
GOOD_LB: LightBulbStatus
BAD_LB: LightBulbStatus
NONE_SS: SensorStatus
GOOD_SS: SensorStatus
BAD_SS: SensorStatus
MESSAGE: ResponseType
QUERY_RES: ResponseType
BID_RES: ResponseType

class Veggies(_message.Message):
    __slots__ = ("veggie", "value")
    VEGGIE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    veggie: Veggie
    value: float
    def __init__(self, veggie: _Optional[_Union[Veggie, str]] = ..., value: _Optional[float] = ...) -> None: ...

class Drinks(_message.Message):
    __slots__ = ("can", "bottle", "can_value", "bottle_value")
    CAN_FIELD_NUMBER: _ClassVar[int]
    BOTTLE_FIELD_NUMBER: _ClassVar[int]
    CAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOTTLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    can: Can
    bottle: Bottle
    can_value: int
    bottle_value: int
    def __init__(self, can: _Optional[_Union[Can, str]] = ..., bottle: _Optional[_Union[Bottle, str]] = ..., can_value: _Optional[int] = ..., bottle_value: _Optional[int] = ...) -> None: ...

class MilkItem(_message.Message):
    __slots__ = ("milk_type", "value")
    MILK_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    milk_type: MilkType
    value: float
    def __init__(self, milk_type: _Optional[_Union[MilkType, str]] = ..., value: _Optional[float] = ...) -> None: ...

class Milks(_message.Message):
    __slots__ = ("milk_items",)
    MILK_ITEMS_FIELD_NUMBER: _ClassVar[int]
    milk_items: _containers.RepeatedCompositeFieldContainer[MilkItem]
    def __init__(self, milk_items: _Optional[_Iterable[_Union[MilkItem, _Mapping]]] = ...) -> None: ...

class BreadItem(_message.Message):
    __slots__ = ("bread_type", "value")
    BREAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    bread_type: BreadType
    value: float
    def __init__(self, bread_type: _Optional[_Union[BreadType, str]] = ..., value: _Optional[float] = ...) -> None: ...

class Breads(_message.Message):
    __slots__ = ("bread_items",)
    BREAD_ITEMS_FIELD_NUMBER: _ClassVar[int]
    bread_items: _containers.RepeatedCompositeFieldContainer[BreadItem]
    def __init__(self, bread_items: _Optional[_Iterable[_Union[BreadItem, _Mapping]]] = ...) -> None: ...

class MeatItem(_message.Message):
    __slots__ = ("meat_type", "value")
    MEAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    meat_type: MeatType
    value: float
    def __init__(self, meat_type: _Optional[_Union[MeatType, str]] = ..., value: _Optional[float] = ...) -> None: ...

class Meats(_message.Message):
    __slots__ = ("meat_items",)
    MEAT_ITEMS_FIELD_NUMBER: _ClassVar[int]
    meat_items: _containers.RepeatedCompositeFieldContainer[MeatItem]
    def __init__(self, meat_items: _Optional[_Iterable[_Union[MeatItem, _Mapping]]] = ...) -> None: ...

class OrderRequest(_message.Message):
    __slots__ = ("veggies", "drinks", "milks", "breads", "meats")
    VEGGIES_FIELD_NUMBER: _ClassVar[int]
    DRINKS_FIELD_NUMBER: _ClassVar[int]
    MILKS_FIELD_NUMBER: _ClassVar[int]
    BREADS_FIELD_NUMBER: _ClassVar[int]
    MEATS_FIELD_NUMBER: _ClassVar[int]
    veggies: Veggies
    drinks: Drinks
    milks: Milks
    breads: Breads
    meats: Meats
    def __init__(self, veggies: _Optional[_Union[Veggies, _Mapping]] = ..., drinks: _Optional[_Union[Drinks, _Mapping]] = ..., milks: _Optional[_Union[Milks, _Mapping]] = ..., breads: _Optional[_Union[Breads, _Mapping]] = ..., meats: _Optional[_Union[Meats, _Mapping]] = ...) -> None: ...

class HealthRequest(_message.Message):
    __slots__ = ("dispenser", "icemaker", "light_bulb", "fridge_temp", "freezer_temp", "fridge_sensor", "yaw", "stock")
    DISPENSER_FIELD_NUMBER: _ClassVar[int]
    ICEMAKER_FIELD_NUMBER: _ClassVar[int]
    LIGHT_BULB_FIELD_NUMBER: _ClassVar[int]
    FRIDGE_TEMP_FIELD_NUMBER: _ClassVar[int]
    FREEZER_TEMP_FIELD_NUMBER: _ClassVar[int]
    FRIDGE_SENSOR_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    dispenser: DispenserStatus
    icemaker: int
    light_bulb: LightBulbStatus
    fridge_temp: int
    freezer_temp: int
    fridge_sensor: SensorStatus
    yaw: int
    stock: int
    def __init__(self, dispenser: _Optional[_Union[DispenserStatus, str]] = ..., icemaker: _Optional[int] = ..., light_bulb: _Optional[_Union[LightBulbStatus, str]] = ..., fridge_temp: _Optional[int] = ..., freezer_temp: _Optional[int] = ..., fridge_sensor: _Optional[_Union[SensorStatus, str]] = ..., yaw: _Optional[int] = ..., stock: _Optional[int] = ...) -> None: ...

class QueryRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Resource(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class BidRequest(_message.Message):
    __slots__ = ("price", "duration", "resources")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    price: float
    duration: int
    resources: _containers.RepeatedCompositeFieldContainer[Resource]
    def __init__(self, price: _Optional[float] = ..., duration: _Optional[int] = ..., resources: _Optional[_Iterable[_Union[Resource, _Mapping]]] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ("type", "order_request", "health_request", "query_request", "bid_request")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    HEALTH_REQUEST_FIELD_NUMBER: _ClassVar[int]
    QUERY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BID_REQUEST_FIELD_NUMBER: _ClassVar[int]
    type: RequestType
    order_request: OrderRequest
    health_request: HealthRequest
    query_request: QueryRequest
    bid_request: BidRequest
    def __init__(self, type: _Optional[_Union[RequestType, str]] = ..., order_request: _Optional[_Union[OrderRequest, _Mapping]] = ..., health_request: _Optional[_Union[HealthRequest, _Mapping]] = ..., query_request: _Optional[_Union[QueryRequest, _Mapping]] = ..., bid_request: _Optional[_Union[BidRequest, _Mapping]] = ...) -> None: ...

class QueryResponse(_message.Message):
    __slots__ = ("resources", "balance")
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[Resource]
    balance: float
    def __init__(self, resources: _Optional[_Iterable[_Union[Resource, _Mapping]]] = ..., balance: _Optional[float] = ...) -> None: ...

class BidResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("type", "message_response", "query_response", "bid_response")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    BID_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    type: ResponseType
    message_response: str
    query_response: QueryResponse
    bid_response: BidResponse
    def __init__(self, type: _Optional[_Union[ResponseType, str]] = ..., message_response: _Optional[str] = ..., query_response: _Optional[_Union[QueryResponse, _Mapping]] = ..., bid_response: _Optional[_Union[BidResponse, _Mapping]] = ...) -> None: ...
