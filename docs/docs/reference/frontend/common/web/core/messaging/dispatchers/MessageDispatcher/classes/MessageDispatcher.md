# Abstract Class: MessageDispatcher\<MsgType, MetaInfoType\>

Defined in: [src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L13)

Base message dispatcher responsible for sending messages to registered handlers.

Dispatching a message (locally) is done by passing the message to one or more registered message handlers within a ``Service``.
The message dispatcher also performs pre- and post-dispatching tasks and takes care of catching errors raised in a handler.

## Extended by

- [`CommandDispatcher`](../../CommandDispatcher/classes/CommandDispatcher.md)
- [`CommandReplyDispatcher`](../../CommandReplyDispatcher/classes/CommandReplyDispatcher.md)
- [`EventDispatcher`](../../EventDispatcher/classes/EventDispatcher.md)

## Type Parameters

### MsgType

`MsgType` *extends* [`Message`](../../../Message/classes/Message.md)

### MetaInfoType

`MetaInfoType` *extends* [`MessageMetaInformation`](../../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

## Constructors

### Constructor

> **new MessageDispatcher**\<`MsgType`, `MetaInfoType`\>(): `MessageDispatcher`\<`MsgType`, `MetaInfoType`\>

#### Returns

`MessageDispatcher`\<`MsgType`, `MetaInfoType`\>

## Properties

### \_metaInformationList

> `protected` `static` **\_metaInformationList**: [`MessageMetaInformationList`](../../../meta/MessageMetaInformationList/classes/MessageMetaInformationList.md)

Defined in: [src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L14)

## Methods

### contextError()

> `protected` **contextError**(`err`, `msg`, `msgMeta`): `void`

Defined in: [src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:75](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L75)

#### Parameters

##### err

`any`

##### msg

`MsgType`

##### msgMeta

`MetaInfoType`

#### Returns

`void`

***

### dispatch()

> **dispatch**\<`CtxType`\>(`msg`, `msgMeta`, `handler`, `ctx`): `void`

Defined in: [src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L46)

Dispatches a message to locally registered message handlers.

Notes:
    Exceptions arising within a message handler will not interrupt the running program; instead, such errors will only be logged.

#### Type Parameters

##### CtxType

`CtxType` *extends* [`MessageContext`](../../../handlers/MessageContext/classes/MessageContext.md)

#### Parameters

##### msg

`MsgType`

The message to be dispatched.

##### msgMeta

`MetaInfoType`

The message meta information.

##### handler

[`MessageHandlerMapping`](../../../handlers/MessageHandler/classes/MessageHandlerMapping.md)

The handler to be invoked.

##### ctx

`CtxType`

The message context.

#### Returns

`void`

#### Throws

Error - If the handler requires a different message type.

***

### postDispatch()

> **postDispatch**(`msg`, `msgMeta`): `void`

Defined in: [src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L72)

Called to perform tasks *after* sending a message.

This method is called after any service-registered message handler have been invoked.

#### Parameters

##### msg

`MsgType`

The message that is about to be dispatched.

##### msgMeta

`MetaInfoType`

The message meta information.

#### Returns

`void`

***

### preDispatch()

> **preDispatch**(`msg`, `msgMeta`): `void`

Defined in: [src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L30)

Called to perform tasks *before* sending a message.

This method is called before any service-registered message handler is invoked.

#### Parameters

##### msg

`MsgType`

The message that is about to be dispatched.

##### msgMeta

`MetaInfoType`

The message meta information.

#### Returns

`void`

***

### process()

> **process**(): `void`

Defined in: [src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L19)

Called to perform periodic tasks.

#### Returns

`void`
