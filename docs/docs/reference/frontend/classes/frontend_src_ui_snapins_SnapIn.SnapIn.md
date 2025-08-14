---
id: "frontend_src_ui_snapins_SnapIn.SnapIn"
title: "Class: SnapIn"
sidebar_label: "SnapIn"
custom_edit_url: null
---

[frontend/src/ui/snapins/SnapIn](../modules/frontend_src_ui_snapins_SnapIn.md).SnapIn

A snap-in represents a certain feature aspect of a project that integrates itself automatically into the UI.

## Hierarchy

- **`SnapIn`**

  ↳ [`DataManagementPlanSnapIn`](frontend_src_ui_snapins_dmp_DataManagementPlanSnapIn.DataManagementPlanSnapIn.md)

  ↳ [`ProjectMetadataSnapIn`](frontend_src_ui_snapins_projectmetadata_ProjectMetadataSnapIn.ProjectMetadataSnapIn.md)

  ↳ [`ResourcesMetadataSnapIn`](frontend_src_ui_snapins_resourcesmetadata_ResourcesMetadataSnapIn.ResourcesMetadataSnapIn.md)

  ↳ [`SummarySnapIn`](frontend_src_ui_snapins_summary_SummarySnapIn.SummarySnapIn.md)

## Constructors

### constructor

• **new SnapIn**(`snapInID`, `options`): [`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `snapInID` | `string` | The ID of the snap-in. |
| `options` | [`SnapInOptions`](../interfaces/frontend_src_ui_snapins_SnapIn.SnapInOptions.md) | The snap-in options. |

#### Returns

[`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)

#### Defined in

[src/frontend/src/ui/snapins/SnapIn.ts:56](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapIn.ts#L56)

## Properties

### \_options

• `Private` `Readonly` **\_options**: [`SnapInOptions`](../interfaces/frontend_src_ui_snapins_SnapIn.SnapInOptions.md)

#### Defined in

[src/frontend/src/ui/snapins/SnapIn.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapIn.ts#L50)

___

### \_snapInID

• `Private` `Readonly` **\_snapInID**: `string`

#### Defined in

[src/frontend/src/ui/snapins/SnapIn.ts:49](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapIn.ts#L49)

## Accessors

### options

• `get` **options**(): [`SnapInOptions`](../interfaces/frontend_src_ui_snapins_SnapIn.SnapInOptions.md)

The snap-in options.

#### Returns

[`SnapInOptions`](../interfaces/frontend_src_ui_snapins_SnapIn.SnapInOptions.md)

#### Defined in

[src/frontend/src/ui/snapins/SnapIn.ts:71](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapIn.ts#L71)

___

### snapInID

• `get` **snapInID**(): `string`

The ID of the snap-in.

#### Returns

`string`

#### Defined in

[src/frontend/src/ui/snapins/SnapIn.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapIn.ts#L64)

## Methods

### hasTabPanel

▸ **hasTabPanel**(): `boolean`

Whether this snap-in has a tab panel.

#### Returns

`boolean`

#### Defined in

[src/frontend/src/ui/snapins/SnapIn.ts:85](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapIn.ts#L85)

___

### isOptional

▸ **isOptional**(): `boolean`

Whether this snap-in is optional.

#### Returns

`boolean`

#### Defined in

[src/frontend/src/ui/snapins/SnapIn.ts:78](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapIn.ts#L78)
