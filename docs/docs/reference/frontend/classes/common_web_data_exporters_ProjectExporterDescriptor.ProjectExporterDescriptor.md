---
id: "common_web_data_exporters_ProjectExporterDescriptor.ProjectExporterDescriptor"
title: "Class: ProjectExporterDescriptor"
sidebar_label: "ProjectExporterDescriptor"
custom_edit_url: null
---

[common/web/data/exporters/ProjectExporterDescriptor](../modules/common_web_data_exporters_ProjectExporterDescriptor.md).ProjectExporterDescriptor

Describes a project exporter. This class is used to easily transfer information about an exporter.

**`Param`**

The global exporter ID.

**`Param`**

The display name.

**`Param`**

The exporter's description.

**`Param`**

The extension of exported files.

**`Param`**

The scope where the exporter applies; if empty, it applies to the overall project.

**`Param`**

A default scope when exporting if none is given.

**`Param`**

A default filename used when none is given.

## Constructors

### constructor

• **new ProjectExporterDescriptor**(`exporterID`, `name`, `description`, `extension`, `scope`, `capabilities?`, `defaultScope?`, `defaultFilename?`): [`ProjectExporterDescriptor`](common_web_data_exporters_ProjectExporterDescriptor.ProjectExporterDescriptor.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `exporterID` | `string` | `undefined` |
| `name` | `string` | `undefined` |
| `description` | `string` | `undefined` |
| `extension` | `string` | `undefined` |
| `scope` | `string`[] | `undefined` |
| `capabilities` | [`ProjectExporterCapabilities`](../enums/common_web_data_exporters_ProjectExporterDescriptor.ProjectExporterCapabilities.md) | `ProjectExporterCapabilities.None` |
| `defaultScope` | `undefined` \| `string` | `undefined` |
| `defaultFilename` | `string` | `""` |

#### Returns

[`ProjectExporterDescriptor`](common_web_data_exporters_ProjectExporterDescriptor.ProjectExporterDescriptor.md)

#### Defined in

[src/common/web/data/exporters/ProjectExporterDescriptor.ts:45](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L45)

## Properties

### capabilities

• `Readonly` **capabilities**: [`ProjectExporterCapabilities`](../enums/common_web_data_exporters_ProjectExporterDescriptor.ProjectExporterCapabilities.md)

#### Defined in

[src/common/web/data/exporters/ProjectExporterDescriptor.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L40)

___

### default\_filename

• `Readonly` **default\_filename**: `string`

#### Defined in

[src/common/web/data/exporters/ProjectExporterDescriptor.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L43)

___

### default\_scope

• `Readonly` **default\_scope**: `undefined` \| `string`

#### Defined in

[src/common/web/data/exporters/ProjectExporterDescriptor.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L42)

___

### description

• `Readonly` **description**: `string`

#### Defined in

[src/common/web/data/exporters/ProjectExporterDescriptor.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L33)

___

### exporter\_id

• `Readonly` **exporter\_id**: `string`

#### Defined in

[src/common/web/data/exporters/ProjectExporterDescriptor.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L30)

___

### extension

• `Readonly` **extension**: `string`

#### Defined in

[src/common/web/data/exporters/ProjectExporterDescriptor.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L34)

___

### name

• `Readonly` **name**: `string`

#### Defined in

[src/common/web/data/exporters/ProjectExporterDescriptor.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L32)

___

### scope

• `Readonly` **scope**: `string`[]

#### Defined in

[src/common/web/data/exporters/ProjectExporterDescriptor.ts:38](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L38)
