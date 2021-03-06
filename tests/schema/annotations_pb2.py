# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema/annotations.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from schema import schema_pb2 as schema_dot_schema__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='schema/annotations.proto',
  package='v',
  syntax='proto3',
  serialized_pb=_b('\n\x18schema/annotations.proto\x12\x01v\x1a google/protobuf/descriptor.proto\x1a\x13schema/schema.proto:>\n\x06schema\x12\x1d.google.protobuf.FieldOptions\x18\xcd\x8e\x03 \x01(\x0b\x32\r.v.JSONSchema:6\n\x0b\x64\x65scription\x12\x1f.google.protobuf.MessageOptions\x18\xc3\x8e\x03 \x01(\t:J\n\x07request\x12\x1e.google.protobuf.MethodOptions\x18\xd7\x8e\x03 \x01(\x0b\x32\x17.v.RequestSchemaOptionsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,schema_dot_schema__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


SCHEMA_FIELD_NUMBER = 51021
schema = _descriptor.FieldDescriptor(
  name='schema', full_name='v.schema', index=0,
  number=51021, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
DESCRIPTION_FIELD_NUMBER = 51011
description = _descriptor.FieldDescriptor(
  name='description', full_name='v.description', index=1,
  number=51011, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
REQUEST_FIELD_NUMBER = 51031
request = _descriptor.FieldDescriptor(
  name='request', full_name='v.request', index=2,
  number=51031, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

DESCRIPTOR.extensions_by_name['schema'] = schema
DESCRIPTOR.extensions_by_name['description'] = description
DESCRIPTOR.extensions_by_name['request'] = request

schema.message_type = schema_dot_schema__pb2._JSONSCHEMA
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(schema)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(description)
request.message_type = schema_dot_schema__pb2._REQUESTSCHEMAOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(request)

# @@protoc_insertion_point(module_scope)
