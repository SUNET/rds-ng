---
id: "common_web_core_messaging_handlers_MessageHandlers.MessageHandlers"
title: "Class: MessageHandlers"
sidebar_label: "MessageHandlers"
custom_edit_url: null
---

[common/web/core/messaging/handlers/MessageHandlers](../modules/common_web_core_messaging_handlers_MessageHandlers.md).MessageHandlers

Holds mappings for message handlers.

## Constructors

### constructor

• **new MessageHandlers**(): [`MessageHandlers`](common_web_core_messaging_handlers_MessageHandlers.MessageHandlers.md)

#### Returns

[`MessageHandlers`](common_web_core_messaging_handlers_MessageHandlers.MessageHandlers.md)

## Properties

### \_mappings

• `Private` `Readonly` **\_mappings**: [`MessageHandlerMappings`](../modules/common_web_core_messaging_handlers_MessageHandler.md#messagehandlermappings) = `[]`

#### Defined in

[src/common/web/core/messaging/handlers/MessageHandlers.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageHandlers.ts#L11)

## Methods

### addHandler

▸ **addHandler**(`filter`, `handler`, `messageType`): `void`

Adds a new message handler mapping.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `filter` | `string` | The message name filter. |
| `handler` | [`MessageHandler`](../modules/common_web_core_messaging_handlers_MessageHandler.md#messagehandler) | The message handler. |
| `messageType` | [`Constructable`](../interfaces/common_web_utils_Types.Constructable.md)<`object`\> | The message type the handler expects. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/handlers/MessageHandlers.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageHandlers.ts#L20)

___

### findHandlers

▸ **findHandlers**(`msgName`): [`MessageHandlerMappings`](../modules/common_web_core_messaging_handlers_MessageHandler.md#messagehandlermappings)

Finds all handlers that fit the given ``msg_name``.

The message name filter can be a complete message name, or a wildcard pattern using asterisks (*).

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msgName` | `string` | The message name (pattern). |

#### Returns

[`MessageHandlerMappings`](../modules/common_web_core_messaging_handlers_MessageHandler.md#messagehandlermappings)

- A list of all found message handlers.

#### Defined in

[src/common/web/core/messaging/handlers/MessageHandlers.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageHandlers.ts#L33)

___

### toString

▸ **toString**(): `string`

Gets the string representation of all mapped handlers.

#### Returns

`string`

#### Defined in

[src/common/web/core/messaging/handlers/MessageHandlers.ts:47](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageHandlers.ts#L47)
