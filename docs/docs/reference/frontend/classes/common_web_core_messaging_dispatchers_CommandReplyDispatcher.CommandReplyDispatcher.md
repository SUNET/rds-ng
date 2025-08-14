---
id: "common_web_core_messaging_dispatchers_CommandReplyDispatcher.CommandReplyDispatcher"
title: "Class: CommandReplyDispatcher"
sidebar_label: "CommandReplyDispatcher"
custom_edit_url: null
---

[common/web/core/messaging/dispatchers/CommandReplyDispatcher](../modules/common_web_core_messaging_dispatchers_CommandReplyDispatcher.md).CommandReplyDispatcher

Message dispatcher specific to ``CommandReply``.

## Hierarchy

- [`MessageDispatcher`](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md)<[`CommandReply`](common_web_core_messaging_CommandReply.CommandReply.md), [`CommandReplyMetaInformation`](common_web_core_messaging_meta_CommandReplyMetaInformation.CommandReplyMetaInformation.md)\>

  ↳ **`CommandReplyDispatcher`**

## Constructors

### constructor

• **new CommandReplyDispatcher**(): [`CommandReplyDispatcher`](common_web_core_messaging_dispatchers_CommandReplyDispatcher.CommandReplyDispatcher.md)

#### Returns

[`CommandReplyDispatcher`](common_web_core_messaging_dispatchers_CommandReplyDispatcher.CommandReplyDispatcher.md)

#### Inherited from

[MessageDispatcher](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md).[constructor](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md#constructor)

## Properties

### \_metaInformationList

▪ `Static` `Protected` **\_metaInformationList**: [`MessageMetaInformationList`](common_web_core_messaging_meta_MessageMetaInformationList.MessageMetaInformationList.md)

#### Inherited from

[MessageDispatcher](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md).[_metaInformationList](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md#_metainformationlist)

#### Defined in

[src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L14)

## Methods

### contextError

▸ **contextError**(`err`, `msg`, `msgMeta`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `err` | `any` |
| `msg` | [`CommandReply`](common_web_core_messaging_CommandReply.CommandReply.md) |
| `msgMeta` | [`CommandReplyMetaInformation`](common_web_core_messaging_meta_CommandReplyMetaInformation.CommandReplyMetaInformation.md) |

#### Returns

`void`

#### Inherited from

[MessageDispatcher](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md).[contextError](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md#contexterror)

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
| `msg` | [`CommandReply`](common_web_core_messaging_CommandReply.CommandReply.md) | The message to be dispatched. |
| `msgMeta` | [`CommandReplyMetaInformation`](common_web_core_messaging_meta_CommandReplyMetaInformation.CommandReplyMetaInformation.md) | The message meta information. |
| `handler` | [`MessageHandlerMapping`](common_web_core_messaging_handlers_MessageHandler.MessageHandlerMapping.md) | The handler to be invoked. |
| `ctx` | `CtxType` | The message context. |

#### Returns

`void`

**`Throws`**

Error - If the handler requires a different message type.

#### Inherited from

[MessageDispatcher](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md).[dispatch](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md#dispatch)

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
| `msg` | [`CommandReply`](common_web_core_messaging_CommandReply.CommandReply.md) | The message that is about to be dispatched. |
| `msgMeta` | [`CommandReplyMetaInformation`](common_web_core_messaging_meta_CommandReplyMetaInformation.CommandReplyMetaInformation.md) | The message meta information. |

#### Returns

`void`

#### Inherited from

[MessageDispatcher](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md).[postDispatch](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md#postdispatch)

#### Defined in

[src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L72)

___

### preDispatch

▸ **preDispatch**<`MsgType`\>(`msg`, `msgMeta`): `void`

Called to perform tasks *before* sending a message.

This method is called before any service-registered message handler is invoked.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `MsgType` | extends [`CommandReply`](common_web_core_messaging_CommandReply.CommandReply.md) |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msg` | `MsgType` | The message that is about to be dispatched. |
| `msgMeta` | [`CommandReplyMetaInformation`](common_web_core_messaging_meta_CommandReplyMetaInformation.CommandReplyMetaInformation.md) | The message meta information. |

#### Returns

`void`

**`Throws`**

Error - If the meta information type is invalid.

#### Overrides

[MessageDispatcher](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md).[preDispatch](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md#predispatch)

#### Defined in

[src/common/web/core/messaging/dispatchers/CommandReplyDispatcher.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/CommandReplyDispatcher.ts#L20)

___

### process

▸ **process**(): `void`

Called to perform periodic tasks.

#### Returns

`void`

#### Inherited from

[MessageDispatcher](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md).[process](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md#process)

#### Defined in

[src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L19)
