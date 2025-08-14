# Class: EventDispatcher

Defined in: [src/common/web/core/messaging/dispatchers/EventDispatcher.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/EventDispatcher.ts#L8)

Message dispatcher specific to ``Event``.

## Extends

- [`MessageDispatcher`](../../MessageDispatcher/classes/MessageDispatcher.md)\<[`Event`](../../../Event/classes/Event.md), [`EventMetaInformation`](../../../meta/EventMetaInformation/classes/EventMetaInformation.md)\>

## Constructors

### Constructor

> **new EventDispatcher**(): `EventDispatcher`

#### Returns

`EventDispatcher`

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

Defined in: [src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:75](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L75)

#### Parameters

##### err

`any`

##### msg

[`Event`](../../../Event/classes/Event.md)

##### msgMeta

[`EventMetaInformation`](../../../meta/EventMetaInformation/classes/EventMetaInformation.md)

#### Returns

`void`

#### Inherited from

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

[`Event`](../../../Event/classes/Event.md)

The message to be dispatched.

##### msgMeta

[`EventMetaInformation`](../../../meta/EventMetaInformation/classes/EventMetaInformation.md)

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

[`Event`](../../../Event/classes/Event.md)

The message that is about to be dispatched.

##### msgMeta

[`EventMetaInformation`](../../../meta/EventMetaInformation/classes/EventMetaInformation.md)

The message meta information.

#### Returns

`void`

#### Inherited from

[`MessageDispatcher`](../../MessageDispatcher/classes/MessageDispatcher.md).[`postDispatch`](../../MessageDispatcher/classes/MessageDispatcher.md#postdispatch)

***

### preDispatch()

> **preDispatch**\<`MsgType`\>(`msg`, `msgMeta`): `void`

Defined in: [src/common/web/core/messaging/dispatchers/EventDispatcher.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/EventDispatcher.ts#L19)

Called to perform tasks *before* sending a message.

This method is called before any service-registered message handler is invoked.

#### Type Parameters

##### MsgType

`MsgType` *extends* [`Event`](../../../Event/classes/Event.md)

#### Parameters

##### msg

`MsgType`

The message that is about to be dispatched.

##### msgMeta

[`EventMetaInformation`](../../../meta/EventMetaInformation/classes/EventMetaInformation.md)

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

Defined in: [src/common/web/core/messaging/dispatchers/MessageDispatcher.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/dispatchers/MessageDispatcher.ts#L19)

Called to perform periodic tasks.

#### Returns

`void`

#### Inherited from

[`MessageDispatcher`](../../MessageDispatcher/classes/MessageDispatcher.md).[`process`](../../MessageDispatcher/classes/MessageDispatcher.md#process)
