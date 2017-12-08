# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PushData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='PushData.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0ePushData.proto\"=\n\x08UserInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x17\n\x06status\x18\x03 \x01(\x0e\x32\x07.Status\"a\n\x0fSendMessageInfo\x12\x11\n\tsender_id\x18\x01 \x01(\x04\x12\x13\n\x0breceiver_id\x18\x02 \x03(\x04\x12\x14\n\x0cmessage_data\x18\x03 \x01(\t\x12\x10\n\x08is_board\x18\x04 \x01(\x08\"/\n\x0cResponseInfo\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x11\n\tjson_data\x18\x02 \x01(\t*!\n\x06Status\x12\n\n\x06Online\x10\x00\x12\x0b\n\x07Offline\x10\x01\x32\x66\n\x0bPushService\x12%\n\x05Login\x12\t.UserInfo\x1a\r.ResponseInfo\"\x00\x30\x01\x12\x30\n\x0bSendMessage\x12\x10.SendMessageInfo\x1a\r.ResponseInfo\"\x00\x62\x06proto3')
)

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Online', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Offline', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=229,
  serialized_end=262,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
Online = 0
Offline = 1



_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='UserInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='UserInfo.id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='UserInfo.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=79,
)


_SENDMESSAGEINFO = _descriptor.Descriptor(
  name='SendMessageInfo',
  full_name='SendMessageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender_id', full_name='SendMessageInfo.sender_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiver_id', full_name='SendMessageInfo.receiver_id', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_data', full_name='SendMessageInfo.message_data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_board', full_name='SendMessageInfo.is_board', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=178,
)


_RESPONSEINFO = _descriptor.Descriptor(
  name='ResponseInfo',
  full_name='ResponseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='ResponseInfo.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='json_data', full_name='ResponseInfo.json_data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=227,
)

_USERINFO.fields_by_name['status'].enum_type = _STATUS
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['SendMessageInfo'] = _SENDMESSAGEINFO
DESCRIPTOR.message_types_by_name['ResponseInfo'] = _RESPONSEINFO
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERINFO,
  __module__ = 'PushData_pb2'
  # @@protoc_insertion_point(class_scope:UserInfo)
  ))
_sym_db.RegisterMessage(UserInfo)

SendMessageInfo = _reflection.GeneratedProtocolMessageType('SendMessageInfo', (_message.Message,), dict(
  DESCRIPTOR = _SENDMESSAGEINFO,
  __module__ = 'PushData_pb2'
  # @@protoc_insertion_point(class_scope:SendMessageInfo)
  ))
_sym_db.RegisterMessage(SendMessageInfo)

ResponseInfo = _reflection.GeneratedProtocolMessageType('ResponseInfo', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEINFO,
  __module__ = 'PushData_pb2'
  # @@protoc_insertion_point(class_scope:ResponseInfo)
  ))
_sym_db.RegisterMessage(ResponseInfo)



_PUSHSERVICE = _descriptor.ServiceDescriptor(
  name='PushService',
  full_name='PushService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=264,
  serialized_end=366,
  methods=[
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='PushService.Login',
    index=0,
    containing_service=None,
    input_type=_USERINFO,
    output_type=_RESPONSEINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='PushService.SendMessage',
    index=1,
    containing_service=None,
    input_type=_SENDMESSAGEINFO,
    output_type=_RESPONSEINFO,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PUSHSERVICE)

DESCRIPTOR.services_by_name['PushService'] = _PUSHSERVICE

# @@protoc_insertion_point(module_scope)