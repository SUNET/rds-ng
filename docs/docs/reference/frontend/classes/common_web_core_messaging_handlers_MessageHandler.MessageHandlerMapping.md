---
id: "common_web_core_messaging_handlers_MessageHandler.MessageHandlerMapping"
title: "Class: MessageHandlerMapping"
sidebar_label: "MessageHandlerMapping"
custom_edit_url: null
---

[common/web/core/messaging/handlers/MessageHandler](../modules/common_web_core_messaging_handlers_MessageHandler.md).MessageHandlerMapping

Mapping from a message name filter to a message handler.

## Constructors

### constructor

• **new MessageHandlerMapping**(`filter`, `handler`, `messageType`): [`MessageHandlerMapping`](common_web_core_messaging_handlers_MessageHandler.MessageHandlerMapping.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `filter` | `string` | The message name filter. |
| `handler` | [`MessageHandler`](../modules/common_web_core_messaging_handlers_MessageHandler.md#messagehandler) | The message handler. |
| `messageType` | [`Constructable`](../interfaces/common_web_utils_Types.Constructable.md)<`object`\> | The message type the handler expects. |

#### Returns

[`MessageHandlerMapping`](common_web_core_messaging_handlers_MessageHandler.MessageHandlerMapping.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageHandler.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageHandler.ts#L16)

## Properties

### filter

• `Readonly` **filter**: `string`

The message name filter.

#### Defined in

[src/common/web/core/messaging/handlers/MessageHandler.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageHandler.ts#L16)

___

### handler

• `Readonly` **handler**: [`MessageHandler`](../modules/common_web_core_messaging_handlers_MessageHandler.md#messagehandler)

The message handler.

#### Defined in

[src/common/web/core/messaging/handlers/MessageHandler.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageHandler.ts#L16)

___

### messageType

• `Readonly` **messageType**: [`Constructable`](../interfaces/common_web_utils_Types.Constructable.md)<`object`\>

The message type the handler expects.

#### Defined in

[src/common/web/core/messaging/handlers/MessageHandler.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageHandler.ts#L16)

## Methods

### toString

▸ **toString**(): `string`

Gets the string representation of the handler mapping.

#### Returns

`string`

#### Defined in

[src/common/web/core/messaging/handlers/MessageHandler.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageHandler.ts#L22)
