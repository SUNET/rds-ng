---
id: "common_web_core_messaging_handlers_MessageService.MessageService"
title: "Class: MessageService<CtxType>"
sidebar_label: "MessageService"
custom_edit_url: null
---

[common/web/core/messaging/handlers/MessageService](../modules/common_web_core_messaging_handlers_MessageService.md).MessageService

Base class for all message services.

A *message service* wraps message handlers and proper message context creation (i.e., using a flexible context type). It
is used by the message bus as an encapsulated layer for message dispatching.

## Type parameters

| Name | Type |
| :------ | :------ |
| `CtxType` | extends [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md) = [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md) |

## Hierarchy

- **`MessageService`**

  ↳ [`Service`](common_web_services_Service.Service.md)

## Constructors

### constructor

• **new MessageService**<`CtxType`\>(`compID`, `messageBus`, `contextType?`): [`MessageService`](common_web_core_messaging_handlers_MessageService.MessageService.md)<`CtxType`\>

#### Type parameters

| Name | Type |
| :------ | :------ |
| `CtxType` | extends [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md) = [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md) |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `compID` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | The global component identifier. |
| `messageBus` | [`MessageBusProtocol`](../interfaces/common_web_core_messaging_MessageBusProtocol.MessageBusProtocol.md) | The global message bus. |
| `contextType` | [`Constructable`](../interfaces/common_web_utils_Types.Constructable.md)<`CtxType`\> | The type to use when creating a message context. |

#### Returns

[`MessageService`](common_web_core_messaging_handlers_MessageService.MessageService.md)<`CtxType`\>

#### Defined in

[src/common/web/core/messaging/handlers/MessageService.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageService.ts#L29)

## Properties

### \_compID

• `Private` `Readonly` **\_compID**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageService.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageService.ts#L18)

___

### \_contextType

• `Private` `Readonly` **\_contextType**: [`Constructable`](../interfaces/common_web_utils_Types.Constructable.md)<`CtxType`\>

#### Defined in

[src/common/web/core/messaging/handlers/MessageService.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageService.ts#L22)

___

### \_messageBus

• `Private` `Readonly` **\_messageBus**: [`MessageBusProtocol`](../interfaces/common_web_core_messaging_MessageBusProtocol.MessageBusProtocol.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageService.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageService.ts#L20)

___

### \_messageHandlers

• `Private` `Readonly` **\_messageHandlers**: [`MessageHandlers`](common_web_core_messaging_handlers_MessageHandlers.MessageHandlers.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageService.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageService.ts#L21)

## Accessors

### messageHandlers

• `get` **messageHandlers**(): [`MessageHandlers`](common_web_core_messaging_handlers_MessageHandlers.MessageHandlers.md)

The message handlers maintained by this message service.

#### Returns

[`MessageHandlers`](common_web_core_messaging_handlers_MessageHandlers.MessageHandlers.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageService.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageService.ts#L63)

## Methods

### createContext

▸ **createContext**(`msgMeta`, `msgOrigin`, `logger`, `config`): [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md)

Creates a new service context.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) | The meta information of the message. |
| `msgOrigin` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | The origin of the message. |
| `logger` | [`LoggerProxy`](common_web_core_logging_LoggerProxy.LoggerProxy.md) | The logger to be used within the new context. |
| `config` | [`Configuration`](common_web_utils_config_Configuration.Configuration.md) | The global component configuration. |

#### Returns

[`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md)

- The newly created message context.

#### Defined in

[src/common/web/core/messaging/handlers/MessageService.ts:47](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageService.ts#L47)

___

### createMessageBuilder

▸ **createMessageBuilder**(): [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

Creates a new message builder.

#### Returns

[`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

- The newly created message builder.

#### Defined in

[src/common/web/core/messaging/handlers/MessageService.ts:56](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageService.ts#L56)
