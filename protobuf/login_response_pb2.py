# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/login-response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/login-response.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dprotobuf/login-response.proto\"#\n\x07UDPNode\x12\n\n\x02ip\x18\x01 \x02(\t\x12\x0c\n\x04port\x18\x02 \x02(\r\"\"\n\x08UDPNodes\x12\x16\n\x04node\x18\x01 \x03(\x0b\x32\x08.UDPNode\"9\n\x04\x41PIs\x12\x16\n\x0etodaysplan_url\x18\x01 \x01(\t\x12\x19\n\x11trainingpeaks_url\x18\x02 \x01(\t\"\\\n\nServerInfo\x12\x11\n\trelay_url\x18\x01 \x02(\t\x12\x13\n\x04\x61pis\x18\x02 \x02(\x0b\x32\x05.APIs\x12\x0c\n\x04time\x18\x03 \x02(\x04\x12\x18\n\x05nodes\x18\x04 \x01(\x0b\x32\t.UDPNodes\"A\n\rLoginResponse\x12\x15\n\rsession_state\x18\x01 \x02(\t\x12\x19\n\x04info\x18\x02 \x02(\x0b\x32\x0b.ServerInfo'
)




_UDPNODE = _descriptor.Descriptor(
  name='UDPNode',
  full_name='UDPNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='UDPNode.ip', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='UDPNode.port', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=68,
)


_UDPNODES = _descriptor.Descriptor(
  name='UDPNodes',
  full_name='UDPNodes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='UDPNodes.node', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=104,
)


_APIS = _descriptor.Descriptor(
  name='APIs',
  full_name='APIs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='todaysplan_url', full_name='APIs.todaysplan_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trainingpeaks_url', full_name='APIs.trainingpeaks_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=163,
)


_SERVERINFO = _descriptor.Descriptor(
  name='ServerInfo',
  full_name='ServerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='relay_url', full_name='ServerInfo.relay_url', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='apis', full_name='ServerInfo.apis', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='ServerInfo.time', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='ServerInfo.nodes', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=257,
)


_LOGINRESPONSE = _descriptor.Descriptor(
  name='LoginResponse',
  full_name='LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_state', full_name='LoginResponse.session_state', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='LoginResponse.info', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=324,
)

_UDPNODES.fields_by_name['node'].message_type = _UDPNODE
_SERVERINFO.fields_by_name['apis'].message_type = _APIS
_SERVERINFO.fields_by_name['nodes'].message_type = _UDPNODES
_LOGINRESPONSE.fields_by_name['info'].message_type = _SERVERINFO
DESCRIPTOR.message_types_by_name['UDPNode'] = _UDPNODE
DESCRIPTOR.message_types_by_name['UDPNodes'] = _UDPNODES
DESCRIPTOR.message_types_by_name['APIs'] = _APIS
DESCRIPTOR.message_types_by_name['ServerInfo'] = _SERVERINFO
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UDPNode = _reflection.GeneratedProtocolMessageType('UDPNode', (_message.Message,), {
  'DESCRIPTOR' : _UDPNODE,
  '__module__' : 'protobuf.login_response_pb2'
  # @@protoc_insertion_point(class_scope:UDPNode)
  })
_sym_db.RegisterMessage(UDPNode)

UDPNodes = _reflection.GeneratedProtocolMessageType('UDPNodes', (_message.Message,), {
  'DESCRIPTOR' : _UDPNODES,
  '__module__' : 'protobuf.login_response_pb2'
  # @@protoc_insertion_point(class_scope:UDPNodes)
  })
_sym_db.RegisterMessage(UDPNodes)

APIs = _reflection.GeneratedProtocolMessageType('APIs', (_message.Message,), {
  'DESCRIPTOR' : _APIS,
  '__module__' : 'protobuf.login_response_pb2'
  # @@protoc_insertion_point(class_scope:APIs)
  })
_sym_db.RegisterMessage(APIs)

ServerInfo = _reflection.GeneratedProtocolMessageType('ServerInfo', (_message.Message,), {
  'DESCRIPTOR' : _SERVERINFO,
  '__module__' : 'protobuf.login_response_pb2'
  # @@protoc_insertion_point(class_scope:ServerInfo)
  })
_sym_db.RegisterMessage(ServerInfo)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'protobuf.login_response_pb2'
  # @@protoc_insertion_point(class_scope:LoginResponse)
  })
_sym_db.RegisterMessage(LoginResponse)


# @@protoc_insertion_point(module_scope)
