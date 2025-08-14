---
id: "common_web_core_messaging_MessageBus.MessageBus"
title: "Class: MessageBus"
sidebar_label: "MessageBus"
custom_edit_url: null
---

[common/web/core/messaging/MessageBus](../modules/common_web_core_messaging_MessageBus.md).MessageBus

Bus for dispatching messages.

The message bus is probably the most central aspect of the system as a whole. It not only invokes local message handlers (which are basically
callback functions), it also sends messages across the network to other components if necessary. The message bus on the remote side will then
decide what to do with the incoming message: Dispatch it locally there, send it to yet another component, or just ignore it.

Message handlers are always registered through a ``MessageService``. When a message gets dispatched locally by the bus, it will call any handlers
associated with the message (via its name). If a message needs to be sent to another component, the bus will invoke the ``NetworkEngine`` to do
so.

To be error tolerant, any exceptions that arise during message handling will be logged but won't result in program termination.

## Constructors

### constructor

• **new MessageBus**(`compData`): [`MessageBus`](common_web_core_messaging_MessageBus.MessageBus.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `compData` | [`WebComponentData`](common_web_component_WebComponentData.WebComponentData.md) | The global component data. |

#### Returns

[`MessageBus`](common_web_core_messaging_MessageBus.MessageBus.md)

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L42)

## Properties

### \_compData

• `Private` `Readonly` **\_compData**: [`WebComponentData`](common_web_component_WebComponentData.WebComponentData.md)

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L32)

___

### \_dispatchers

• `Private` `Readonly` **\_dispatchers**: `Record`<`string`, [`MessageDispatcher`](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md)<`any`, `any`\>\> = `{}`

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L36)

___

### \_networkEngine

• `Private` `Readonly` **\_networkEngine**: [`NetworkEngine`](common_web_core_messaging_networking_NetworkEngine.NetworkEngine.md)

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L34)

___

### \_router

• `Private` `Readonly` **\_router**: [`MessageRouter`](common_web_core_messaging_MessageRouter.MessageRouter.md)

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L37)

___

### \_services

• `Private` `Readonly` **\_services**: [`MessageService`](common_web_core_messaging_handlers_MessageService.MessageService.md)<`any`\>[] = `[]`

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L35)

## Methods

### addService

▸ **addService**<`CtxType`\>(`svc`): `boolean`

Adds a new message service to the bus.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `CtxType` | extends [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md) |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `svc` | [`MessageService`](common_web_core_messaging_handlers_MessageService.MessageService.md)<`CtxType`\> | The message service to add. |

#### Returns

`boolean`

- Whether the message service was added.

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L66)

___

### createContext

▸ **createContext**<`CtxType`\>(`msg`, `msgMeta`, `svc`): [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md)

#### Type parameters

| Name | Type |
| :------ | :------ |
| `CtxType` | extends [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md) |

#### Parameters

| Name | Type |
| :------ | :------ |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) |
| `svc` | [`MessageService`](common_web_core_messaging_handlers_MessageService.MessageService.md)<`CtxType`\> |

#### Returns

[`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md)

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:181](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L181)

___

### createNetworkEngine

▸ **createNetworkEngine**(): [`NetworkEngine`](common_web_core_messaging_networking_NetworkEngine.NetworkEngine.md)

#### Returns

[`NetworkEngine`](common_web_core_messaging_networking_NetworkEngine.NetworkEngine.md)

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:55](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L55)

___

### dispatch

▸ **dispatch**(`msg`, `msgMeta`): `void`

Dispatches a message.

To do so, the message is first checked for validity (whether it actually *may* be dispatched). If it is valid,
the ``MessageRouter`` will determine if it needs to be dispatched to another component or locally (or both).

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) | The message to be dispatched. |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) | The message meta information. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:110](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L110)

___

### dispatchToService

▸ **dispatchToService**<`DispatcherType`, `CtxType`\>(`dispatcher`, `msg`, `msgMeta`, `svc`): `boolean`

#### Type parameters

| Name | Type |
| :------ | :------ |
| `DispatcherType` | extends [`MessageDispatcher`](common_web_core_messaging_dispatchers_MessageDispatcher.MessageDispatcher.md)<`any`, `any`\> |
| `CtxType` | extends [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md) |

#### Parameters

| Name | Type |
| :------ | :------ |
| `dispatcher` | `DispatcherType` |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) |
| `svc` | [`MessageService`](common_web_core_messaging_handlers_MessageService.MessageService.md)<`CtxType`\> |

#### Returns

`boolean`

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:161](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L161)

___

### localDispatch

▸ **localDispatch**(`msg`, `msgMeta`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:133](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L133)

___

### process

▸ **process**(): `void`

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:125](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L125)

___

### remoteDispatch

▸ **remoteDispatch**(`msg`, `msgMeta`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:157](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L157)

___

### removeService

▸ **removeService**<`CtxType`\>(`svc`): `boolean`

Removes a message service from the bus.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `CtxType` | extends [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md) |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `svc` | [`MessageService`](common_web_core_messaging_handlers_MessageService.MessageService.md)<`CtxType`\> | svc: The message service to remove. |

#### Returns

`boolean`

- Whether the message service was removed.

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:82](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L82)

___

### run

▸ **run**(): `void`

Initiates periodic tasks performed by the bus.

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/MessageBus.ts:95](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageBus.ts#L95)
