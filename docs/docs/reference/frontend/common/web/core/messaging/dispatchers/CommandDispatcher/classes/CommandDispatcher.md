# Class: CommandDispatcher

Defined in: [src/common/web/core/messaging/dispatchers/CommandDispatcher.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/CommandDispatcher.ts#L12)

Message dispatcher specific to ``Command``.

## Extends

- [`MessageDispatcher`](../../MessageDispatcher/classes/MessageDispatcher.md)\<[`Command`](../../../Command/classes/Command.md), [`CommandMetaInformation`](../../../meta/CommandMetaInformation/classes/CommandMetaInformation.md)\>

## Constructors

### Constructor

> **new CommandDispatcher**(): `CommandDispatcher`

#### Returns

`CommandDispatcher`

#### Inherited from

[`MessageDispatcher`](../../MessageDispatcher/classes/MessageDispatcher.md).[`constructor`](../../MessageDispatcher/classes/MessageDispatcher.md#constructor)

## Properties

### \_metaInformationList

> `protected` `static` **\_metaInformationList**: [`MessageMetaInformationList`](../../../meta/MessageMetaInformationList/classes/MessageMetaInformationList.md)

Defined in: [src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L14)

#### Inherited from

[`MessageDispatcher`](../../MessageDispatcher/classes/MessageDispatcher.md).[`_metaInformationList`](../../MessageDispatcher/classes/MessageDispatcher.md#_metainformationlist)

## Methods

### contextError()

> `protected` **contextError**(`err`, `msg`, `msgMeta`): `void`

Defined in: [src/common/web/core/messaging/dispatchers/CommandDispatcher.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/CommandDispatcher.ts#L41)

#### Parameters

##### err

`any`

##### msg

[`Command`](../../../Command/classes/Command.md)

##### msgMeta

[`CommandMetaInformation`](../../../meta/CommandMetaInformation/classes/CommandMetaInformation.md)

#### Returns

`void`

#### Overrides

[`MessageDispatcher`](../../MessageDispatcher/classes/MessageDispatcher.md).[`contextError`](../../MessageDispatcher/classes/MessageDispatcher.md#contexterror)

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

[`Command`](../../../Command/classes/Command.md)

The message to be dispatched.

##### msgMeta

[`CommandMetaInformation`](../../../meta/CommandMetaInformation/classes/CommandMetaInformation.md)

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

#### Inherited from

[`MessageDispatcher`](../../MessageDispatcher/classes/MessageDispatcher.md).[`dispatch`](../../MessageDispatcher/classes/MessageDispatcher.md#dispatch)

***

### postDispatch()

> **postDispatch**(`msg`, `msgMeta`): `void`

Defined in: [src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L72)

Called to perform tasks *after* sending a message.

This method is called after any service-registered message handler have been invoked.

#### Parameters

##### msg

[`Command`](../../../Command/classes/Command.md)

The message that is about to be dispatched.

##### msgMeta

[`CommandMetaInformation`](../../../meta/CommandMetaInformation/classes/CommandMetaInformation.md)

The message meta information.

#### Returns

`void`

#### Inherited from

[`MessageDispatcher`](../../MessageDispatcher/classes/MessageDispatcher.md).[`postDispatch`](../../MessageDispatcher/classes/MessageDispatcher.md#postdispatch)

***

### preDispatch()

> **preDispatch**(`msg`, `msgMeta`): `void`

Defined in: [src/common/web/core/messaging/dispatchers/CommandDispatcher.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/CommandDispatcher.ts#L35)

Called to perform tasks *before* sending a message.

This method is called before any service-registered message handler is invoked.

#### Parameters

##### msg

[`Command`](../../../Command/classes/Command.md)

The message that is about to be dispatched.

##### msgMeta

[`CommandMetaInformation`](../../../meta/CommandMetaInformation/classes/CommandMetaInformation.md)

The message meta information.

#### Returns

`void`

#### Throws

Error - If the meta information type is invalid.

#### Overrides

[`MessageDispatcher`](../../MessageDispatcher/classes/MessageDispatcher.md).[`preDispatch`](../../MessageDispatcher/classes/MessageDispatcher.md#predispatch)

***

### process()

> **process**(): `void`

Defined in: [src/common/web/core/messaging/dispatchers/CommandDispatcher.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/CommandDispatcher.ts#L16)

Takes care of checking whether issued commands have already timed out.

#### Returns

`void`

#### Overrides

[`MessageDispatcher`](../../MessageDispatcher/classes/MessageDispatcher.md).[`process`](../../MessageDispatcher/classes/MessageDispatcher.md#process)

***

### invokeReplyCallbacks()

> `static` **invokeReplyCallbacks**(`unique`, `reply`, `replyMeta`, `failType`, `failMsg`): `void`

Defined in: [src/common/web/core/messaging/dispatchers/CommandDispatcher.ts:58](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/CommandDispatcher.ts#L58)

Invokes command reply handlers.

 When emitting a command, it is possible to specify reply callbacks that are invoked beside message handlers. This method will call the correct
 callback and take care of intercepting exceptions.

#### Parameters

##### unique

`string`

The unique trace of the command.

##### reply

The received command reply (if any).

`null` | [`CommandReply`](../../../CommandReply/classes/CommandReply.md)

##### replyMeta

The reply meta information (if any).

`null` | [`CommandReplyMetaInformation`](../../../meta/CommandReplyMetaInformation/classes/CommandReplyMetaInformation.md)

##### failType

[`CommandFailType`](../../../CommandReply/enumerations/CommandFailType.md) = `CommandFailType.None`

The type of the command failure (in case of a timeout or exception).

##### failMsg

`string` = `""`

The failure message.

#### Returns

`void`
