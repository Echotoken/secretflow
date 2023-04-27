# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: secretflow/protos/component/node_def.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from secretflow.protos.component import comp_def_pb2 as secretflow_dot_protos_dot_component_dot_comp__def__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='secretflow/protos/component/node_def.proto',
  package='secretflow.component',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*secretflow/protos/component/node_def.proto\x12\x14secretflow.component\x1a*secretflow/protos/component/comp_def.proto\"\x7f\n\rNodeParameter\x12\x10\n\x08prefixes\x18\x01 \x03(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x35\n\x06\x61tomic\x18\x03 \x01(\x0b\x32%.secretflow.component.AtomicParameter\x12\x17\n\x0funion_selection\x18\x04 \x01(\t\"4\n\x15IndivialTableMetadata\x12\r\n\x05party\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"D\n\"VeriticalPartitioningTableMetaData\x12\x0f\n\x07parties\x18\x01 \x03(\t\x12\r\n\x05paths\x18\x02 \x03(\t\"\xd6\x01\n\rTableMetadata\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.secretflow.component.TableType\x12=\n\x08indivial\x18\x02 \x01(\x0b\x32+.secretflow.component.IndivialTableMetadata\x12W\n\x15vertical_partitioning\x18\x03 \x01(\x0b\x32\x38.secretflow.component.VeriticalPartitioningTableMetaData\"S\n\rModelMetadata\x12\x18\n\x10public_file_path\x18\x01 \x01(\t\x12\x0f\n\x07parties\x18\x02 \x03(\t\x12\x17\n\x0fparty_dir_paths\x18\x03 \x03(\t\"\x0e\n\x0cRuleMetadata\"\x10\n\x0eReportMetadata\"\xf6\x01\n\x0bTableParams\x12\x42\n\ncol_params\x18\x01 \x03(\x0b\x32..secretflow.component.TableParams.ColParameter\x1a=\n\x06Params\x12\x33\n\x06values\x18\x01 \x03(\x0b\x32#.secretflow.component.NodeParameter\x1a\x64\n\x0c\x43olParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ols\x18\x02 \x03(\t\x12\x38\n\x06params\x18\x03 \x03(\x0b\x32(.secretflow.component.TableParams.Params\"\xf3\x02\n\x06NodeIo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x04type\x18\x02 \x01(\x0e\x32 .secretflow.component.SFDataType\x12\x37\n\x0ctable_params\x18\x03 \x01(\x0b\x32!.secretflow.component.TableParams\x12;\n\x0etable_metadata\x18\x04 \x01(\x0b\x32#.secretflow.component.TableMetadata\x12;\n\x0emodel_metadata\x18\x05 \x01(\x0b\x32#.secretflow.component.ModelMetadata\x12\x39\n\rrule_metadata\x18\x06 \x01(\x0b\x32\".secretflow.component.RuleMetadata\x12=\n\x0freport_metadata\x18\x07 \x01(\x0b\x32$.secretflow.component.ReportMetadata\"\xd6\x01\n\x07NodeDef\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x33\n\x06params\x18\x05 \x03(\x0b\x32#.secretflow.component.NodeParameter\x12,\n\x06inputs\x18\x06 \x03(\x0b\x32\x1c.secretflow.component.NodeIo\x12-\n\x07outputs\x18\x07 \x03(\x0b\x32\x1c.secretflow.component.NodeIob\x06proto3'
  ,
  dependencies=[secretflow_dot_protos_dot_component_dot_comp__def__pb2.DESCRIPTOR,])




_NODEPARAMETER = _descriptor.Descriptor(
  name='NodeParameter',
  full_name='secretflow.component.NodeParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='prefixes', full_name='secretflow.component.NodeParameter.prefixes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='secretflow.component.NodeParameter.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='atomic', full_name='secretflow.component.NodeParameter.atomic', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='union_selection', full_name='secretflow.component.NodeParameter.union_selection', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=112,
  serialized_end=239,
)


_INDIVIALTABLEMETADATA = _descriptor.Descriptor(
  name='IndivialTableMetadata',
  full_name='secretflow.component.IndivialTableMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='party', full_name='secretflow.component.IndivialTableMetadata.party', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='secretflow.component.IndivialTableMetadata.path', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=293,
)


_VERITICALPARTITIONINGTABLEMETADATA = _descriptor.Descriptor(
  name='VeriticalPartitioningTableMetaData',
  full_name='secretflow.component.VeriticalPartitioningTableMetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parties', full_name='secretflow.component.VeriticalPartitioningTableMetaData.parties', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paths', full_name='secretflow.component.VeriticalPartitioningTableMetaData.paths', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=363,
)


_TABLEMETADATA = _descriptor.Descriptor(
  name='TableMetadata',
  full_name='secretflow.component.TableMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='secretflow.component.TableMetadata.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='indivial', full_name='secretflow.component.TableMetadata.indivial', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertical_partitioning', full_name='secretflow.component.TableMetadata.vertical_partitioning', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=366,
  serialized_end=580,
)


_MODELMETADATA = _descriptor.Descriptor(
  name='ModelMetadata',
  full_name='secretflow.component.ModelMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_file_path', full_name='secretflow.component.ModelMetadata.public_file_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parties', full_name='secretflow.component.ModelMetadata.parties', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='party_dir_paths', full_name='secretflow.component.ModelMetadata.party_dir_paths', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=582,
  serialized_end=665,
)


_RULEMETADATA = _descriptor.Descriptor(
  name='RuleMetadata',
  full_name='secretflow.component.RuleMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=667,
  serialized_end=681,
)


_REPORTMETADATA = _descriptor.Descriptor(
  name='ReportMetadata',
  full_name='secretflow.component.ReportMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=683,
  serialized_end=699,
)


_TABLEPARAMS_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='secretflow.component.TableParams.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='secretflow.component.TableParams.Params.values', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=785,
  serialized_end=846,
)

_TABLEPARAMS_COLPARAMETER = _descriptor.Descriptor(
  name='ColParameter',
  full_name='secretflow.component.TableParams.ColParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='secretflow.component.TableParams.ColParameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cols', full_name='secretflow.component.TableParams.ColParameter.cols', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='secretflow.component.TableParams.ColParameter.params', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=848,
  serialized_end=948,
)

_TABLEPARAMS = _descriptor.Descriptor(
  name='TableParams',
  full_name='secretflow.component.TableParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='col_params', full_name='secretflow.component.TableParams.col_params', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TABLEPARAMS_PARAMS, _TABLEPARAMS_COLPARAMETER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=948,
)


_NODEIO = _descriptor.Descriptor(
  name='NodeIo',
  full_name='secretflow.component.NodeIo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='secretflow.component.NodeIo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='secretflow.component.NodeIo.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='table_params', full_name='secretflow.component.NodeIo.table_params', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='table_metadata', full_name='secretflow.component.NodeIo.table_metadata', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_metadata', full_name='secretflow.component.NodeIo.model_metadata', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rule_metadata', full_name='secretflow.component.NodeIo.rule_metadata', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='report_metadata', full_name='secretflow.component.NodeIo.report_metadata', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=951,
  serialized_end=1322,
)


_NODEDEF = _descriptor.Descriptor(
  name='NodeDef',
  full_name='secretflow.component.NodeDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='secretflow.component.NodeDef.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain', full_name='secretflow.component.NodeDef.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='secretflow.component.NodeDef.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='secretflow.component.NodeDef.version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='secretflow.component.NodeDef.params', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='secretflow.component.NodeDef.inputs', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='secretflow.component.NodeDef.outputs', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1325,
  serialized_end=1539,
)

_NODEPARAMETER.fields_by_name['atomic'].message_type = secretflow_dot_protos_dot_component_dot_comp__def__pb2._ATOMICPARAMETER
_TABLEMETADATA.fields_by_name['type'].enum_type = secretflow_dot_protos_dot_component_dot_comp__def__pb2._TABLETYPE
_TABLEMETADATA.fields_by_name['indivial'].message_type = _INDIVIALTABLEMETADATA
_TABLEMETADATA.fields_by_name['vertical_partitioning'].message_type = _VERITICALPARTITIONINGTABLEMETADATA
_TABLEPARAMS_PARAMS.fields_by_name['values'].message_type = _NODEPARAMETER
_TABLEPARAMS_PARAMS.containing_type = _TABLEPARAMS
_TABLEPARAMS_COLPARAMETER.fields_by_name['params'].message_type = _TABLEPARAMS_PARAMS
_TABLEPARAMS_COLPARAMETER.containing_type = _TABLEPARAMS
_TABLEPARAMS.fields_by_name['col_params'].message_type = _TABLEPARAMS_COLPARAMETER
_NODEIO.fields_by_name['type'].enum_type = secretflow_dot_protos_dot_component_dot_comp__def__pb2._SFDATATYPE
_NODEIO.fields_by_name['table_params'].message_type = _TABLEPARAMS
_NODEIO.fields_by_name['table_metadata'].message_type = _TABLEMETADATA
_NODEIO.fields_by_name['model_metadata'].message_type = _MODELMETADATA
_NODEIO.fields_by_name['rule_metadata'].message_type = _RULEMETADATA
_NODEIO.fields_by_name['report_metadata'].message_type = _REPORTMETADATA
_NODEDEF.fields_by_name['params'].message_type = _NODEPARAMETER
_NODEDEF.fields_by_name['inputs'].message_type = _NODEIO
_NODEDEF.fields_by_name['outputs'].message_type = _NODEIO
DESCRIPTOR.message_types_by_name['NodeParameter'] = _NODEPARAMETER
DESCRIPTOR.message_types_by_name['IndivialTableMetadata'] = _INDIVIALTABLEMETADATA
DESCRIPTOR.message_types_by_name['VeriticalPartitioningTableMetaData'] = _VERITICALPARTITIONINGTABLEMETADATA
DESCRIPTOR.message_types_by_name['TableMetadata'] = _TABLEMETADATA
DESCRIPTOR.message_types_by_name['ModelMetadata'] = _MODELMETADATA
DESCRIPTOR.message_types_by_name['RuleMetadata'] = _RULEMETADATA
DESCRIPTOR.message_types_by_name['ReportMetadata'] = _REPORTMETADATA
DESCRIPTOR.message_types_by_name['TableParams'] = _TABLEPARAMS
DESCRIPTOR.message_types_by_name['NodeIo'] = _NODEIO
DESCRIPTOR.message_types_by_name['NodeDef'] = _NODEDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeParameter = _reflection.GeneratedProtocolMessageType('NodeParameter', (_message.Message,), {
  'DESCRIPTOR' : _NODEPARAMETER,
  '__module__' : 'secretflow.protos.component.node_def_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.NodeParameter)
  })
_sym_db.RegisterMessage(NodeParameter)

IndivialTableMetadata = _reflection.GeneratedProtocolMessageType('IndivialTableMetadata', (_message.Message,), {
  'DESCRIPTOR' : _INDIVIALTABLEMETADATA,
  '__module__' : 'secretflow.protos.component.node_def_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.IndivialTableMetadata)
  })
_sym_db.RegisterMessage(IndivialTableMetadata)

VeriticalPartitioningTableMetaData = _reflection.GeneratedProtocolMessageType('VeriticalPartitioningTableMetaData', (_message.Message,), {
  'DESCRIPTOR' : _VERITICALPARTITIONINGTABLEMETADATA,
  '__module__' : 'secretflow.protos.component.node_def_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.VeriticalPartitioningTableMetaData)
  })
_sym_db.RegisterMessage(VeriticalPartitioningTableMetaData)

TableMetadata = _reflection.GeneratedProtocolMessageType('TableMetadata', (_message.Message,), {
  'DESCRIPTOR' : _TABLEMETADATA,
  '__module__' : 'secretflow.protos.component.node_def_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.TableMetadata)
  })
_sym_db.RegisterMessage(TableMetadata)

ModelMetadata = _reflection.GeneratedProtocolMessageType('ModelMetadata', (_message.Message,), {
  'DESCRIPTOR' : _MODELMETADATA,
  '__module__' : 'secretflow.protos.component.node_def_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.ModelMetadata)
  })
_sym_db.RegisterMessage(ModelMetadata)

RuleMetadata = _reflection.GeneratedProtocolMessageType('RuleMetadata', (_message.Message,), {
  'DESCRIPTOR' : _RULEMETADATA,
  '__module__' : 'secretflow.protos.component.node_def_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.RuleMetadata)
  })
_sym_db.RegisterMessage(RuleMetadata)

ReportMetadata = _reflection.GeneratedProtocolMessageType('ReportMetadata', (_message.Message,), {
  'DESCRIPTOR' : _REPORTMETADATA,
  '__module__' : 'secretflow.protos.component.node_def_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.ReportMetadata)
  })
_sym_db.RegisterMessage(ReportMetadata)

TableParams = _reflection.GeneratedProtocolMessageType('TableParams', (_message.Message,), {

  'Params' : _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
    'DESCRIPTOR' : _TABLEPARAMS_PARAMS,
    '__module__' : 'secretflow.protos.component.node_def_pb2'
    # @@protoc_insertion_point(class_scope:secretflow.component.TableParams.Params)
    })
  ,

  'ColParameter' : _reflection.GeneratedProtocolMessageType('ColParameter', (_message.Message,), {
    'DESCRIPTOR' : _TABLEPARAMS_COLPARAMETER,
    '__module__' : 'secretflow.protos.component.node_def_pb2'
    # @@protoc_insertion_point(class_scope:secretflow.component.TableParams.ColParameter)
    })
  ,
  'DESCRIPTOR' : _TABLEPARAMS,
  '__module__' : 'secretflow.protos.component.node_def_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.TableParams)
  })
_sym_db.RegisterMessage(TableParams)
_sym_db.RegisterMessage(TableParams.Params)
_sym_db.RegisterMessage(TableParams.ColParameter)

NodeIo = _reflection.GeneratedProtocolMessageType('NodeIo', (_message.Message,), {
  'DESCRIPTOR' : _NODEIO,
  '__module__' : 'secretflow.protos.component.node_def_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.NodeIo)
  })
_sym_db.RegisterMessage(NodeIo)

NodeDef = _reflection.GeneratedProtocolMessageType('NodeDef', (_message.Message,), {
  'DESCRIPTOR' : _NODEDEF,
  '__module__' : 'secretflow.protos.component.node_def_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.component.NodeDef)
  })
_sym_db.RegisterMessage(NodeDef)


# @@protoc_insertion_point(module_scope)