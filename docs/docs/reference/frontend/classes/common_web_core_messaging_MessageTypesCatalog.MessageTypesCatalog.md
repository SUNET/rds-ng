---
id: "common_web_core_messaging_MessageTypesCatalog.MessageTypesCatalog"
title: "Class: MessageTypesCatalog"
sidebar_label: "MessageTypesCatalog"
custom_edit_url: null
---

[common/web/core/messaging/MessageTypesCatalog](../modules/common_web_core_messaging_MessageTypesCatalog.md).MessageTypesCatalog

Global catalog of all registered message types.

This is a globally accessible list of all message types, associated with their respective message names.
It's mainly used to create proper message objects from incoming network messages.

## Hierarchy

- [`ItemsCatalog`](common_web_utils_ItemsCatalog.ItemsCatalog.md)<[`ConstructableMessage`](../interfaces/common_web_core_messaging_Message.ConstructableMessage.md)\>

  ↳ **`MessageTypesCatalog`**

## Constructors

### constructor

• **new MessageTypesCatalog**(): [`MessageTypesCatalog`](common_web_core_messaging_MessageTypesCatalog.MessageTypesCatalog.md)

#### Returns

[`MessageTypesCatalog`](common_web_core_messaging_MessageTypesCatalog.MessageTypesCatalog.md)

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
