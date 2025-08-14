# Abstract Class: SnapIn

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L48)

A snap-in represents a certain feature aspect of a project that integrates itself automatically into the UI.

## Extended by

- [`DataManagementPlanSnapIn`](../../dmp/DataManagementPlanSnapIn/classes/DataManagementPlanSnapIn.md)
- [`ProjectMetadataSnapIn`](../../projectmetadata/ProjectMetadataSnapIn/classes/ProjectMetadataSnapIn.md)
- [`ResourcesMetadataSnapIn`](../../resourcesmetadata/ResourcesMetadataSnapIn/classes/ResourcesMetadataSnapIn.md)
- [`SummarySnapIn`](../../summary/SummarySnapIn/classes/SummarySnapIn.md)

## Constructors

### Constructor

> `protected` **new SnapIn**(`snapInID`, `options`): `SnapIn`

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:56](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L56)

#### Parameters

##### snapInID

`string`

The ID of the snap-in.

##### options

[`SnapInOptions`](../interfaces/SnapInOptions.md)

The snap-in options.

#### Returns

`SnapIn`

## Accessors

### options

#### Get Signature

> **get** **options**(): [`SnapInOptions`](../interfaces/SnapInOptions.md)

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:71](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L71)

The snap-in options.

##### Returns

[`SnapInOptions`](../interfaces/SnapInOptions.md)

***

### snapInID

#### Get Signature

> **get** **snapInID**(): `string`

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L64)

The ID of the snap-in.

##### Returns

`string`

## Methods

### hasTabPanel()

> **hasTabPanel**(): `boolean`

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:85](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L85)

Whether this snap-in has a tab panel.

#### Returns

`boolean`

***

### isOptional()

> **isOptional**(): `boolean`

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:78](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L78)

Whether this snap-in is optional.

#### Returns

`boolean`
