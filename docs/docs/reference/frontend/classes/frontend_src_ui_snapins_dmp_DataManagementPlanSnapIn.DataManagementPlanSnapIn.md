---
id: "frontend_src_ui_snapins_dmp_DataManagementPlanSnapIn.DataManagementPlanSnapIn"
title: "Class: DataManagementPlanSnapIn"
sidebar_label: "DataManagementPlanSnapIn"
custom_edit_url: null
---

[frontend/src/ui/snapins/dmp/DataManagementPlanSnapIn](../modules/frontend_src_ui_snapins_dmp_DataManagementPlanSnapIn.md).DataManagementPlanSnapIn

A snap-in represents a certain feature aspect of a project that integrates itself automatically into the UI.

## Hierarchy

- [`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)

  ↳ **`DataManagementPlanSnapIn`**

## Constructors

### constructor

• **new DataManagementPlanSnapIn**(): [`DataManagementPlanSnapIn`](frontend_src_ui_snapins_dmp_DataManagementPlanSnapIn.DataManagementPlanSnapIn.md)

#### Returns

[`DataManagementPlanSnapIn`](frontend_src_ui_snapins_dmp_DataManagementPlanSnapIn.DataManagementPlanSnapIn.md)

#### Overrides

[SnapIn](frontend_src_ui_snapins_SnapIn.SnapIn.md).[constructor](frontend_src_ui_snapins_SnapIn.SnapIn.md#constructor)

#### Defined in

[src/frontend/src/ui/snapins/dmp/DataManagementPlanSnapIn.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/dmp/DataManagementPlanSnapIn.ts#L8)

## Properties

### SnapInID

▪ `Static` `Readonly` **SnapInID**: `string` = `"dmp"`

#### Defined in

[src/frontend/src/ui/snapins/dmp/DataManagementPlanSnapIn.ts:6](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/dmp/DataManagementPlanSnapIn.ts#L6)

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
