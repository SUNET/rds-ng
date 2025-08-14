---
id: "frontend_src_integration_IntegrationSchemesCatalog.IntegrationSchemesCatalog"
title: "Class: IntegrationSchemesCatalog"
sidebar_label: "IntegrationSchemesCatalog"
custom_edit_url: null
---

[frontend/src/integration/IntegrationSchemesCatalog](../modules/frontend_src_integration_IntegrationSchemesCatalog.md).IntegrationSchemesCatalog

Global catalog of all supported integration schemes.

## Hierarchy

- [`ItemsCatalog`](common_web_utils_ItemsCatalog.ItemsCatalog.md)<[`Constructable`](../interfaces/common_web_utils_Types.Constructable.md)<[`IntegrationScheme`](frontend_src_integration_IntegrationScheme.IntegrationScheme.md)\>\>

  ↳ **`IntegrationSchemesCatalog`**

## Constructors

### constructor

• **new IntegrationSchemesCatalog**(): [`IntegrationSchemesCatalog`](frontend_src_integration_IntegrationSchemesCatalog.IntegrationSchemesCatalog.md)

#### Returns

[`IntegrationSchemesCatalog`](frontend_src_integration_IntegrationSchemesCatalog.IntegrationSchemesCatalog.md)

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
