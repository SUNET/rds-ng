---
id: "common_web_core_messaging_MessagePayload.MessagePayload"
title: "Class: MessagePayload"
sidebar_label: "MessagePayload"
custom_edit_url: null
---

[common/web/core/messaging/MessagePayload](../modules/common_web_core_messaging_MessagePayload.md).MessagePayload

Class holding arbitrary payload data (as key-value pairs) of a message.

## Constructors

### constructor

• **new MessagePayload**(): [`MessagePayload`](common_web_core_messaging_MessagePayload.MessagePayload.md)

#### Returns

[`MessagePayload`](common_web_core_messaging_MessagePayload.MessagePayload.md)

## Properties

### \_payload

• `Private` **\_payload**: [`Payload`](../modules/common_web_core_messaging_MessagePayload.md#payload) = `{}`

#### Defined in

[src/common/web/core/messaging/MessagePayload.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessagePayload.ts#L10)

## Methods

### clear

▸ **clear**(`key?`): `void`

Removes an item or clears the entire payload.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `key` | `undefined` \| `string` | `undefined` | The key of the item; if set to *None*, all items will be removed. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/MessagePayload.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessagePayload.ts#L46)

___

### contains

▸ **contains**(`key`): `boolean`

Checks if an item exists.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `key` | `string` | The key of the item. |

#### Returns

`boolean`

#### Defined in

[src/common/web/core/messaging/MessagePayload.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessagePayload.ts#L37)

___

### decode

▸ **decode**(`payload`): `void`

Decodes the payload from message passing.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | [`Payload`](../modules/common_web_core_messaging_MessagePayload.md#payload) | The incoming payload. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/MessagePayload.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessagePayload.ts#L70)

___

### encode

▸ **encode**(): [`Payload`](../modules/common_web_core_messaging_MessagePayload.md#payload)

Encodes the payload for message passing.

#### Returns

[`Payload`](../modules/common_web_core_messaging_MessagePayload.md#payload)

- The encoded data.

#### Defined in

[src/common/web/core/messaging/MessagePayload.ts:61](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessagePayload.ts#L61)

___

### get

▸ **get**(`key`): `any`

Retrieves a payload item.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `key` | `string` | The key of the item. |

#### Returns

`any`

- The item data or *None* otherwise.

#### Defined in

[src/common/web/core/messaging/MessagePayload.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessagePayload.ts#L28)

___

### set

▸ **set**(`key`, `data`): `void`

Sets a payload item.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `key` | `string` | The key of the item. |
| `data` | `any` | The item data. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/MessagePayload.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessagePayload.ts#L17)

___

### toString

▸ **toString**(): `string`

#### Returns

`string`

#### Defined in

[src/common/web/core/messaging/MessagePayload.ts:74](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessagePayload.ts#L74)
