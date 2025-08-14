---
id: "common_web_core_messaging_dispatchers_CommandDispatcher.CommandDispatcher"
title: "Class: CommandDispatcher"
sidebar_label: "CommandDispatcher"
custom_edit_url: null
---

[common/web/core/messaging/dispatchers/CommandDispatcher](../modules/common_web_core_messaging_dispatchers_CommandDispatcher.md).CommandDispatcher

Message dispatcher specific to ``Command``.

## Hierarchy

- [`MessageDispatcher`](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md)<[`Command`](common_web_core_messaging_Command.Command.md), [`CommandMetaInformation`](common_web_core_messaging_meta_CommandMetaInformation.CommandMetaInformation.md)\>

  ↳ **`CommandDispatcher`**

## Constructors

### constructor

• **new CommandDispatcher**(): [`CommandDispatcher`](common_web_core_messaging_dispatchers_CommandDispatcher.CommandDispatcher.md)

#### Returns

[`CommandDispatcher`](common_web_core_messaging_dispatchers_CommandDispatcher.CommandDispatcher.md)

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
| `msg` | [`Command`](common_web_core_messaging_Command.Command.md) |
| `msgMeta` | [`CommandMetaInformation`](common_web_core_messaging_meta_CommandMetaInformation.CommandMetaInformation.md) |

#### Returns

`void`

#### Overrides

[MessageDispatcher](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md).[contextError](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md#contexterror)

#### Defined in

[src/common/web/core/messaging/dispatchers/CommandDispatcher.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/CommandDispatcher.ts#L41)

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
| `msg` | [`Command`](common_web_core_messaging_Command.Command.md) | The message to be dispatched. |
| `msgMeta` | [`CommandMetaInformation`](common_web_core_messaging_meta_CommandMetaInformation.CommandMetaInformation.md) | The message meta information. |
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
| `msg` | [`Command`](common_web_core_messaging_Command.Command.md) | The message that is about to be dispatched. |
| `msgMeta` | [`CommandMetaInformation`](common_web_core_messaging_meta_CommandMetaInformation.CommandMetaInformation.md) | The message meta information. |

#### Returns

`void`

#### Inherited from

[MessageDispatcher](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md).[postDispatch](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md#postdispatch)

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
| `msg` | [`Command`](common_web_core_messaging_Command.Command.md) | The message that is about to be dispatched. |
| `msgMeta` | [`CommandMetaInformation`](common_web_core_messaging_meta_CommandMetaInformation.CommandMetaInformation.md) | The message meta information. |

#### Returns

`void`

**`Throws`**

Error - If the meta information type is invalid.

#### Overrides

[MessageDispatcher](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md).[preDispatch](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md#predispatch)

#### Defined in

[src/common/web/core/messaging/dispatchers/CommandDispatcher.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/CommandDispatcher.ts#L35)

___

### process

▸ **process**(): `void`

Takes care of checking whether issued commands have already timed out.

#### Returns

`void`

#### Overrides

[MessageDispatcher](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md).[process](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md#process)

#### Defined in

[src/common/web/core/messaging/dispatchers/CommandDispatcher.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/CommandDispatcher.ts#L16)

___

### invokeReplyCallbacks

▸ **invokeReplyCallbacks**(`unique`, `reply?`, `replyMeta?`, `failType?`, `failMsg?`): `void`

Invokes command reply handlers.

 When emitting a command, it is possible to specify reply callbacks that are invoked beside message handlers. This method will call the correct
 callback and take care of intercepting exceptions.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `unique` | `string` | `undefined` | The unique trace of the command. |
| `reply` | ``null`` \| [`CommandReply`](common_web_core_messaging_CommandReply.CommandReply.md) | `null` | The received command reply (if any). |
| `replyMeta` | ``null`` \| [`CommandReplyMetaInformation`](common_web_core_messaging_meta_CommandReplyMetaInformation.CommandReplyMetaInformation.md) | `null` | The reply meta information (if any). |
| `failType` | [`CommandFailType`](../enums/common_web_core_messaging_CommandReply.CommandFailType.md) | `CommandFailType.None` | The type of the command failure (in case of a timeout or exception). |
| `failMsg` | `string` | `""` | The failure message. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/dispatchers/CommandDispatcher.ts:58](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/dispatchers/CommandDispatcher.ts#L58)
