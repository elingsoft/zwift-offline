# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/goal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/goal.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13protobuf/goal.proto\"\x80\x02\n\x04Goal\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x11\n\tplayer_id\x18\x02 \x01(\x04\x12\n\n\x02\x66\x33\x18\x03 \x01(\r\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\r\x12\x13\n\x0bperiodicity\x18\x06 \x01(\r\x12\x17\n\x0ftarget_distance\x18\x07 \x01(\x02\x12\x17\n\x0ftarget_duration\x18\x08 \x01(\x02\x12\x17\n\x0f\x61\x63tual_distance\x18\t \x01(\x02\x12\x17\n\x0f\x61\x63tual_duration\x18\n \x01(\x02\x12\x12\n\ncreated_on\x18\x0b \x01(\x04\x12\x17\n\x0fperiod_end_date\x18\x0c \x01(\x04\x12\x0b\n\x03\x66\x31\x33\x18\r \x01(\x04\"\x1d\n\x05Goals\x12\x14\n\x05goals\x18\x01 \x03(\x0b\x32\x05.Goal'
)




_GOAL = _descriptor.Descriptor(
  name='Goal',
  full_name='Goal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Goal.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='Goal.player_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f3', full_name='Goal.f3', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Goal.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='Goal.type', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='periodicity', full_name='Goal.periodicity', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_distance', full_name='Goal.target_distance', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_duration', full_name='Goal.target_duration', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actual_distance', full_name='Goal.actual_distance', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actual_duration', full_name='Goal.actual_duration', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_on', full_name='Goal.created_on', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period_end_date', full_name='Goal.period_end_date', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f13', full_name='Goal.f13', index=12,
      number=13, type=4, cpp_type=4, label=1,
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
  serialized_start=24,
  serialized_end=280,
)


_GOALS = _descriptor.Descriptor(
  name='Goals',
  full_name='Goals',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='goals', full_name='Goals.goals', index=0,
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
  serialized_start=282,
  serialized_end=311,
)

_GOALS.fields_by_name['goals'].message_type = _GOAL
DESCRIPTOR.message_types_by_name['Goal'] = _GOAL
DESCRIPTOR.message_types_by_name['Goals'] = _GOALS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Goal = _reflection.GeneratedProtocolMessageType('Goal', (_message.Message,), {
  'DESCRIPTOR' : _GOAL,
  '__module__' : 'protobuf.goal_pb2'
  # @@protoc_insertion_point(class_scope:Goal)
  })
_sym_db.RegisterMessage(Goal)

Goals = _reflection.GeneratedProtocolMessageType('Goals', (_message.Message,), {
  'DESCRIPTOR' : _GOALS,
  '__module__' : 'protobuf.goal_pb2'
  # @@protoc_insertion_point(class_scope:Goals)
  })
_sym_db.RegisterMessage(Goals)


# @@protoc_insertion_point(module_scope)
