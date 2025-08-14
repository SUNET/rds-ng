---
id: "frontend_src_ui_snapins_SnapInsCatalog.SnapInsCatalog"
title: "Class: SnapInsCatalog"
sidebar_label: "SnapInsCatalog"
custom_edit_url: null
---

[frontend/src/ui/snapins/SnapInsCatalog](../modules/frontend_src_ui_snapins_SnapInsCatalog.md).SnapInsCatalog

Global catalog of all registered snap-ins.

This is a globally accessible list of all snap-ins, associated with their respective IDs.

## Hierarchy

- [`ItemsCatalog`](common_web_utils_ItemsCatalog.ItemsCatalog.md)<[`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)\>

  ↳ **`SnapInsCatalog`**

## Constructors

### constructor

• **new SnapInsCatalog**(): [`SnapInsCatalog`](frontend_src_ui_snapins_SnapInsCatalog.SnapInsCatalog.md)

#### Returns

[`SnapInsCatalog`](frontend_src_ui_snapins_SnapInsCatalog.SnapInsCatalog.md)

#### Inherited from

[ItemsCatalog](common_web_utils_ItemsCatalog.ItemsCatalog.md).[constructor](common_web_utils_ItemsCatalog.ItemsCatalog.md#constructor)

## Accessors

### items

• `get` **items**(): `Record`<`string`, `ItemType`\>

Retrieves all stored items.

#### Returns

`Record`<`string`, `ItemType`\>

#### Inherited from

ItemsCatalog.items

#### Defined in

[src/common/web/utils/ItemsCatalog.ts:60](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ItemsCatalog.ts#L60)

## Methods

### allOptionals

▸ **allOptionals**(): [`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)[]

Retrieve all optional snap-ins.

#### Returns

[`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)[]

#### Defined in

[src/frontend/src/ui/snapins/SnapInsCatalog.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapInsCatalog.ts#L24)

___

### allWithTabPanel

▸ **allWithTabPanel**(): [`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)[]

Retrieve all snap-ins with a tab panel.

#### Returns

[`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)[]

#### Defined in

[src/frontend/src/ui/snapins/SnapInsCatalog.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapInsCatalog.ts#L31)

___

### define

▸ **define**(): `Function`

A decorator to define a new item catalog.

Notes:
    This decorator must always be used for new item catalogs; otherwise, data corruption might occur.

#### Returns

`Function`

#### Inherited from

[ItemsCatalog](common_web_utils_ItemsCatalog.ItemsCatalog.md).[define](common_web_utils_ItemsCatalog.ItemsCatalog.md#define)

#### Defined in

[src/common/web/utils/ItemsCatalog.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ItemsCatalog.ts#L18)

___

### filter

▸ **filter**(`predicate`): [`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)[]

Select certain snap-ins that satisfy the given predicate.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `predicate` | (`snapIn`: [`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)) => `boolean` | The selection criterium. |

#### Returns

[`SnapIn`](frontend_src_ui_snapins_SnapIn.SnapIn.md)[]

#### Defined in

[src/frontend/src/ui/snapins/SnapInsCatalog.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/snapins/SnapInsCatalog.ts#L17)

___

### findItem

▸ **findItem**(`name`): `any`

Finds the item associated with the given ``name``.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | The item name. |

#### Returns

`any`

- The associated item, if any.

#### Inherited from

[ItemsCatalog](common_web_utils_ItemsCatalog.ItemsCatalog.md).[findItem](common_web_utils_ItemsCatalog.ItemsCatalog.md#finditem)

#### Defined in

[src/common/web/utils/ItemsCatalog.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ItemsCatalog.ts#L52)

___

### registerItem

▸ **registerItem**(`name`, `item`): `void`

Registers a new item.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | The item name. |
| `item` | `ItemType` | The item. |

#### Returns

`void`

#### Inherited from

[ItemsCatalog](common_web_utils_ItemsCatalog.ItemsCatalog.md).[registerItem](common_web_utils_ItemsCatalog.ItemsCatalog.md#registeritem)

#### Defined in

[src/common/web/utils/ItemsCatalog.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ItemsCatalog.ts#L34)
