# Class: ProjectExporterDescriptor

Defined in: [src/common/web/data/exporters/ProjectExporterDescriptor.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L29)

Describes a project exporter. This class is used to easily transfer information about an exporter.

## Param

The global exporter ID.

## Param

The display name.

## Param

The exporter's description.

## Param

The extension of exported files.

## Param

The scope where the exporter applies; if empty, it applies to the overall project.

## Param

A default scope when exporting if none is given.

## Param

A default filename used when none is given.

## Constructors

### Constructor

> **new ProjectExporterDescriptor**(`exporterID`, `name`, `description`, `extension`, `scope`, `capabilities`, `defaultScope`, `defaultFilename`): `ProjectExporterDescriptor`

Defined in: [src/common/web/data/exporters/ProjectExporterDescriptor.ts:45](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L45)

#### Parameters

##### exporterID

`string`

##### name

`string`

##### description

`string`

##### extension

`string`

##### scope

`string`[]

##### capabilities

[`ProjectExporterCapabilities`](../enumerations/ProjectExporterCapabilities.md) = `ProjectExporterCapabilities.None`

##### defaultScope

`undefined` | `string`

##### defaultFilename

`string` = `""`

#### Returns

`ProjectExporterDescriptor`

## Properties

### capabilities

> `readonly` **capabilities**: [`ProjectExporterCapabilities`](../enumerations/ProjectExporterCapabilities.md)

Defined in: [src/common/web/data/exporters/ProjectExporterDescriptor.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L40)

***

### default\_filename

> `readonly` **default\_filename**: `string`

Defined in: [src/common/web/data/exporters/ProjectExporterDescriptor.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L43)

***

### default\_scope

> `readonly` **default\_scope**: `undefined` \| `string`

Defined in: [src/common/web/data/exporters/ProjectExporterDescriptor.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L42)

***

### description

> `readonly` **description**: `string`

Defined in: [src/common/web/data/exporters/ProjectExporterDescriptor.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L33)

***

### exporter\_id

> `readonly` **exporter\_id**: `string`

Defined in: [src/common/web/data/exporters/ProjectExporterDescriptor.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L30)

***

### extension

> `readonly` **extension**: `string`

Defined in: [src/common/web/data/exporters/ProjectExporterDescriptor.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L34)

***

### name

> `readonly` **name**: `string`

Defined in: [src/common/web/data/exporters/ProjectExporterDescriptor.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L32)

***

### scope

> `readonly` **scope**: `string`[]

Defined in: [src/common/web/data/exporters/ProjectExporterDescriptor.ts:38](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/exporters/ProjectExporterDescriptor.ts#L38)
