# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: compile.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import celaut_pb2 as celaut__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcompile.proto\x12\x07\x63ompile\x1a\x0c\x63\x65laut.proto\"\x85\x06\n\x07Service\x12-\n\tcontainer\x18\x01 \x01(\x0b\x32\x1a.compile.Service.Container\x12 \n\x03\x61pi\x18\x02 \x01(\x0b\x32\x13.celaut.Service.Api\x12&\n\x06tensor\x18\x03 \x01(\x0b\x32\x16.celaut.Service.Tensor\x12&\n\x06ledger\x18\x04 \x01(\x0b\x32\x16.celaut.Service.Ledger\x1a\xd8\x04\n\tContainer\x12\x14\n\x0c\x61rchitecture\x18\x01 \x01(\x0c\x12\x38\n\nfilesystem\x18\x02 \x01(\x0b\x32$.celaut.Service.Container.Filesystem\x12Q\n\x14\x65nviroment_variables\x18\x03 \x03(\x0b\x32\x33.compile.Service.Container.EnviromentVariablesEntry\x12\x12\n\nentrypoint\x18\x04 \x03(\t\x12\x30\n\x06\x63onfig\x18\x05 \x01(\x0b\x32 .celaut.Service.Container.Config\x12\x43\n\x10\x65xpected_gateway\x18\x06 \x01(\x0b\x32).celaut.Service.Container.ExpectedGateway\x1a\xce\x01\n\nFilesystem\x12@\n\x06\x62ranch\x18\x01 \x03(\x0b\x32\x30.compile.Service.Container.Filesystem.ItemBranch\x1a~\n\nItemBranch\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x04\x66ile\x18\x02 \x01(\x0cH\x00\x12\x0e\n\x04link\x18\x03 \x01(\tH\x00\x12:\n\nfilesystem\x18\x04 \x01(\x0b\x32$.celaut.Service.Container.FilesystemH\x00\x42\x06\n\x04item\x1aL\n\x18\x45nviromentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.celaut.FieldDef:\x02\x38\x01\"$\n\x16\x43ompileOutputServiceId\x12\n\n\x02id\x18\x01 \x01(\x0c\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'compile_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY']._loaded_options = None
  _globals['_SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY']._serialized_options = b'8\001'
  _globals['_SERVICE']._serialized_start=41
  _globals['_SERVICE']._serialized_end=814
  _globals['_SERVICE_CONTAINER']._serialized_start=214
  _globals['_SERVICE_CONTAINER']._serialized_end=814
  _globals['_SERVICE_CONTAINER_FILESYSTEM']._serialized_start=530
  _globals['_SERVICE_CONTAINER_FILESYSTEM']._serialized_end=736
  _globals['_SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH']._serialized_start=610
  _globals['_SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH']._serialized_end=736
  _globals['_SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY']._serialized_start=738
  _globals['_SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY']._serialized_end=814
  _globals['_COMPILEOUTPUTSERVICEID']._serialized_start=816
  _globals['_COMPILEOUTPUTSERVICEID']._serialized_end=852
# @@protoc_insertion_point(module_scope)
