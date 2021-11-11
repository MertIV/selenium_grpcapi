# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: session.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='session.proto',
  package='session',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rsession.proto\x12\x07session\"\x15\n\x07Session\x12\n\n\x02id\x18\x01 \x01(\t\"3\n\x0eSessionRequest\x12!\n\x07session\x18\x01 \x01(\x0b\x32\x10.session.Session\"\x17\n\tIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x1e\n\x0eStringResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t2\xb1\x01\n\x0eSessionService\x12\x33\n\x06\x43reate\x12\x17.session.SessionRequest\x1a\x10.session.Session\x12\x33\n\x06Update\x12\x17.session.SessionRequest\x1a\x10.session.Session\x12\x35\n\x06\x44\x65lete\x12\x12.session.IdRequest\x1a\x17.session.StringResponseb\x06proto3'
)




_SESSION = _descriptor.Descriptor(
  name='Session',
  full_name='session.Session',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='session.Session.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=47,
)


_SESSIONREQUEST = _descriptor.Descriptor(
  name='SessionRequest',
  full_name='session.SessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='session.SessionRequest.session', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=100,
)


_IDREQUEST = _descriptor.Descriptor(
  name='IdRequest',
  full_name='session.IdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='session.IdRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=125,
)


_STRINGRESPONSE = _descriptor.Descriptor(
  name='StringResponse',
  full_name='session.StringResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='session.StringResponse.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=157,
)

_SESSIONREQUEST.fields_by_name['session'].message_type = _SESSION
DESCRIPTOR.message_types_by_name['Session'] = _SESSION
DESCRIPTOR.message_types_by_name['SessionRequest'] = _SESSIONREQUEST
DESCRIPTOR.message_types_by_name['IdRequest'] = _IDREQUEST
DESCRIPTOR.message_types_by_name['StringResponse'] = _STRINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), {
  'DESCRIPTOR' : _SESSION,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:session.Session)
  })
_sym_db.RegisterMessage(Session)

SessionRequest = _reflection.GeneratedProtocolMessageType('SessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:session.SessionRequest)
  })
_sym_db.RegisterMessage(SessionRequest)

IdRequest = _reflection.GeneratedProtocolMessageType('IdRequest', (_message.Message,), {
  'DESCRIPTOR' : _IDREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:session.IdRequest)
  })
_sym_db.RegisterMessage(IdRequest)

StringResponse = _reflection.GeneratedProtocolMessageType('StringResponse', (_message.Message,), {
  'DESCRIPTOR' : _STRINGRESPONSE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:session.StringResponse)
  })
_sym_db.RegisterMessage(StringResponse)



_SESSIONSERVICE = _descriptor.ServiceDescriptor(
  name='SessionService',
  full_name='session.SessionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=160,
  serialized_end=337,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='session.SessionService.Create',
    index=0,
    containing_service=None,
    input_type=_SESSIONREQUEST,
    output_type=_SESSION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='session.SessionService.Update',
    index=1,
    containing_service=None,
    input_type=_SESSIONREQUEST,
    output_type=_SESSION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='session.SessionService.Delete',
    index=2,
    containing_service=None,
    input_type=_IDREQUEST,
    output_type=_STRINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SESSIONSERVICE)

DESCRIPTOR.services_by_name['SessionService'] = _SESSIONSERVICE

# @@protoc_insertion_point(module_scope)