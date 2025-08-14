---
id: "frontend_src_ui_snapins_resourcesmetadata_ResourcesMetadataSnapIn.ResourcesMetadataSnapIn"
title: "Class: ResourcesMetadataSnapIn"
sidebar_label: "ResourcesMetadataSnapIn"
custom_edit_url: null
---

[frontend/src/ui/snapins/resourcesmetadata/ResourcesMetadataSnapIn](../modules/frontend_src_ui_snapins_resourcesmetadata_ResourcesMetadataSnapIn.md).ResourcesMetadataSnapIn

A snap-in represents a certain feature aspect of a project that integrates itself automatically into the UI.

## Hierarchy

- [`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)

  ↳ **`ResourcesMetadataSnapIn`**

## Constructors

### constructor

• **new ResourcesMetadataSnapIn**(): [`ResourcesMetadataSnapIn`](frontend_src_ui_snapins_resourcesmetadata_ResourcesMetadataSnapIn.ResourcesMetadataSnapIn.md)

#### Returns

[`ResourcesMetadataSnapIn`](frontend_src_ui_snapins_resourcesmetadata_ResourcesMetadataSnapIn.ResourcesMetadataSnapIn.md)

#### Overrides

[SnapIn](frontend_src_ui_snapins_SnapIn.SnapIn.md).[constructor](frontend_src_ui_snapins_SnapIn.SnapIn.md#constructor)

#### Defined in

[src/frontend/src/ui/snapins/resourcesmetadata/ResourcesMetadataSnapIn.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/resourcesmetadata/ResourcesMetadataSnapIn.ts#L8)

## Properties

### SnapInID

▪ `Static` `Readonly` **SnapInID**: `string` = `"resources_metadata"`

#### Defined in

[src/frontend/src/ui/snapins/resourcesmetadata/ResourcesMetadataSnapIn.ts:6](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/resourcesmetadata/ResourcesMetadataSnapIn.ts#L6)

## Accessors

### options

• `get` **options**(): [`SnapInOptions`](../interfaces/frontend_src_ui_snapins_SnapIn.SnapInOptions.md)

The snap-in options.

#### Returns

[`SnapInOptions`](../interfaces/frontend_src_ui_snapins_SnapIn.SnapInOptions.md)

#### Inherited from

SnapIn.options

#### Defined in

[src/frontend/src/ui/snapins/SnapIn.ts:71](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapIn.ts#L71)

___

### snapInID

• `get` **snapInID**(): `string`

The ID of the snap-in.

#### Returns

`string`

#### Inherited from

SnapIn.snapInID

#### Defined in

[src/frontend/src/ui/snapins/SnapIn.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapIn.ts#L64)

## Methods

### hasTabPanel

▸ **hasTabPanel**(): `boolean`

Whether this snap-in has a tab panel.

#### Returns

`boolean`

#### Inherited from

[SnapIn](frontend_src_ui_snapins_SnapIn.SnapIn.md).[hasTabPanel](frontend_src_ui_snapins_SnapIn.SnapIn.md#hastabpanel)

#### Defined in

[src/frontend/src/ui/snapins/SnapIn.ts:85](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapIn.ts#L85)

___

### isOptional

▸ **isOptional**(): `boolean`

Whether this snap-in is optional.

#### Returns

`boolean`

#### Inherited from

[SnapIn](frontend_src_ui_snapins_SnapIn.SnapIn.md).[isOptional](frontend_src_ui_snapins_SnapIn.SnapIn.md#isoptional)

#### Defined in

[src/frontend/src/ui/snapins/SnapIn.ts:78](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapIn.ts#L78)
