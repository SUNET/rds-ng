---
id: "common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher"
title: "Class: MessageDispatcher<MsgType, MetaInfoType>"
sidebar_label: "MessageDispatcher"
custom_edit_url: null
---

[common/web/core/messaging/dispatchers/MessageDispatcher](../modules/common_web_core_messaging_dispatchers_MessageDispatcher.md).MessageDispatcher

Base message dispatcher responsible for sending messages to registered handlers.

Dispatching a message (locally) is done by passing the message to one or more registered message handlers within a ``Service``.
The message dispatcher also performs pre- and post-dispatching tasks and takes care of catching errors raised in a handler.

## Type parameters

| Name | Type |
| :------ | :------ |
| `MsgType` | extends [`Message`](common_web_core_messaging_Message.Message.md) |
| `MetaInfoType` | extends [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) |

## Hierarchy

- **`MessageDispatcher`**

  ↳ [`CommandDispatcher`](common_web_core_messaging_dispatchers_CommandDispatcher.CommandDispatcher.md)

  ↳ [`CommandReplyDispatcher`](common_web_core_messaging_dispatchers_CommandReplyDispatcher.CommandReplyDispatcher.md)

  ↳ [`EventDispatcher`](common_web_core_messaging_dispatchers_EventDispatcher.EventDispatcher.md)

## Constructors

### constructor

• **new MessageDispatcher**<`MsgType`, `MetaInfoType`\>(): [`MessageDispatcher`](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md)<`MsgType`, `MetaInfoType`\>

#### Type parameters

| Name | Type |
| :------ | :------ |
| `MsgType` | extends [`Message`](common_web_core_messaging_Message.Message.md) |
| `MetaInfoType` | extends [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) |

#### Returns

[`MessageDispatcher`](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md)<`MsgType`, `MetaInfoType`\>

## Properties

### \_metaInformationList

▪ `Static` `Protected` **\_metaInformationList**: [`MessageMetaInformationList`](common_web_core_messaging_meta_MessageMetaInformationList.MessageMetaInformationList.md)

#### Defined in

[src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L14)

## Methods

### contextError

▸ **contextError**(`err`, `msg`, `msgMeta`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `err` | `any` |
| `msg` | `MsgType` |
| `msgMeta` | `MetaInfoType` |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:75](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L75)

___

### dispatch

▸ **dispatch**<`CtxType`\>(`msg`, `msgMeta`, `handler`, `ctx`): `void`

Dispatches a message to locally registered message handlers.

Notes:
    Exceptions arising within a message handler will not interrupt the running program; instead, such errors will only be logged.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `CtxType` | extends [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md) |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msg` | `MsgType` | The message to be dispatched. |
| `msgMeta` | `MetaInfoType` | The message meta information. |
| `handler` | [`MessageHandlerMapping`](common_web_core_messaging_handlers_MessageHandler.MessageHandlerMapping.md) | The handler to be invoked. |
| `ctx` | `CtxType` | The message context. |

#### Returns

`void`

**`Throws`**

Error - If the handler requires a different message type.

#### Defined in

[src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L46)

___

### postDispatch

▸ **postDispatch**(`msg`, `msgMeta`): `void`

Called to perform tasks *after* sending a message.

This method is called after any service-registered message handler have been invoked.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msg` | `MsgType` | The message that is about to be dispatched. |
| `msgMeta` | `MetaInfoType` | The message meta information. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L72)

___

### preDispatch

▸ **preDispatch**(`msg`, `msgMeta`): `void`

Called to perform tasks *before* sending a message.

This method is called before any service-registered message handler is invoked.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msg` | `MsgType` | The message that is about to be dispatched. |
| `msgMeta` | `MetaInfoType` | The message meta information. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L30)

___

### process

▸ **process**(): `void`

Called to perform periodic tasks.

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L19)
