# Class: ProjectMetadataSnapIn

Defined in: [src/frontend/src/ui/snapins/projectmetadata/ProjectMetadataSnapIn.ts:3](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/projectmetadata/ProjectMetadataSnapIn.ts#L3)

A snap-in represents a certain feature aspect of a project that integrates itself automatically into the UI.

## Extends

- [`SnapIn`](../../../SnapIn/classes/SnapIn.md)

## Constructors

### Constructor

> **new ProjectMetadataSnapIn**(): `ProjectMetadataSnapIn`

Defined in: [src/frontend/src/ui/snapins/projectmetadata/ProjectMetadataSnapIn.ts:6](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/projectmetadata/ProjectMetadataSnapIn.ts#L6)

#### Returns

`ProjectMetadataSnapIn`

#### Overrides

[`SnapIn`](../../../SnapIn/classes/SnapIn.md).[`constructor`](../../../SnapIn/classes/SnapIn.md#constructor)

## Properties

### SnapInID

> `readonly` `static` **SnapInID**: `string` = `"metadata"`

Defined in: [src/frontend/src/ui/snapins/projectmetadata/ProjectMetadataSnapIn.ts:4](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/projectmetadata/ProjectMetadataSnapIn.ts#L4)

## Accessors

### options

#### Get Signature

> **get** **options**(): [`SnapInOptions`](../../../SnapIn/interfaces/SnapInOptions.md)

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:71](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L71)

The snap-in options.

##### Returns

[`SnapInOptions`](../../../SnapIn/interfaces/SnapInOptions.md)

#### Inherited from

[`SnapIn`](../../../SnapIn/classes/SnapIn.md).[`options`](../../../SnapIn/classes/SnapIn.md#options)

***

### snapInID

#### Get Signature

> **get** **snapInID**(): `string`

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L64)

The ID of the snap-in.

##### Returns

`string`

#### Inherited from

[`SnapIn`](../../../SnapIn/classes/SnapIn.md).[`snapInID`](../../../SnapIn/classes/SnapIn.md#snapinid)

## Methods

### hasTabPanel()

> **hasTabPanel**(): `boolean`

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:85](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L85)

Whether this snap-in has a tab panel.

#### Returns

`boolean`

#### Inherited from

[`SnapIn`](../../../SnapIn/classes/SnapIn.md).[`hasTabPanel`](../../../SnapIn/classes/SnapIn.md#hastabpanel)

***

### isOptional()

> **isOptional**(): `boolean`

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:78](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L78)

Whether this snap-in is optional.

#### Returns

`boolean`

#### Inherited from

[`SnapIn`](../../../SnapIn/classes/SnapIn.md).[`isOptional`](../../../SnapIn/classes/SnapIn.md#isoptional)
