# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ExecutionSpecificationMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import vts.proto.ComponentSpecificationMessage_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ExecutionSpecificationMessage.proto',
  package='android.vts',
  serialized_pb='\n#ExecutionSpecificationMessage.proto\x12\x0b\x61ndroid.vts\x1a-vts/proto/ComponentSpecificationMessage.proto\"W\n\x1d\x45xecutionSpecificationMessage\x12\x36\n\x03\x61pi\x18\x01 \x03(\x0b\x32).android.vts.FunctionSpecificationMessage')




_EXECUTIONSPECIFICATIONMESSAGE = _descriptor.Descriptor(
  name='ExecutionSpecificationMessage',
  full_name='android.vts.ExecutionSpecificationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api', full_name='android.vts.ExecutionSpecificationMessage.api', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=99,
  serialized_end=186,
)

_EXECUTIONSPECIFICATIONMESSAGE.fields_by_name['api'].message_type = vts.proto.ComponentSpecificationMessage_pb2._FUNCTIONSPECIFICATIONMESSAGE
DESCRIPTOR.message_types_by_name['ExecutionSpecificationMessage'] = _EXECUTIONSPECIFICATIONMESSAGE

class ExecutionSpecificationMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXECUTIONSPECIFICATIONMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.ExecutionSpecificationMessage)


# @@protoc_insertion_point(module_scope)
