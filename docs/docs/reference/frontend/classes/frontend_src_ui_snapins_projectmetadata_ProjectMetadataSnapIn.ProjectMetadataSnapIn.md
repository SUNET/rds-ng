---
id: "frontend_src_ui_snapins_projectmetadata_ProjectMetadataSnapIn.ProjectMetadataSnapIn"
title: "Class: ProjectMetadataSnapIn"
sidebar_label: "ProjectMetadataSnapIn"
custom_edit_url: null
---

[frontend/src/ui/snapins/projectmetadata/ProjectMetadataSnapIn](../modules/frontend_src_ui_snapins_projectmetadata_ProjectMetadataSnapIn.md).ProjectMetadataSnapIn

A snap-in represents a certain feature aspect of a project that integrates itself automatically into the UI.

## Hierarchy

- [`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)

  ↳ **`ProjectMetadataSnapIn`**

## Constructors

### constructor

• **new ProjectMetadataSnapIn**(): [`ProjectMetadataSnapIn`](frontend_src_ui_snapins_projectmetadata_ProjectMetadataSnapIn.ProjectMetadataSnapIn.md)

#### Returns

[`ProjectMetadataSnapIn`](frontend_src_ui_snapins_projectmetadata_ProjectMetadataSnapIn.ProjectMetadataSnapIn.md)

#### Overrides

[SnapIn](frontend_src_ui_snapins_SnapIn.SnapIn.md).[constructor](frontend_src_ui_snapins_SnapIn.SnapIn.md#constructor)

#### Defined in

[src/frontend/src/ui/snapins/projectmetadata/ProjectMetadataSnapIn.ts:6](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/projectmetadata/ProjectMetadataSnapIn.ts#L6)

## Properties

### SnapInID

▪ `Static` `Readonly` **SnapInID**: `string` = `"metadata"`

#### Defined in

[src/frontend/src/ui/snapins/projectmetadata/ProjectMetadataSnapIn.ts:4](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/projectmetadata/ProjectMetadataSnapIn.ts#L4)

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
