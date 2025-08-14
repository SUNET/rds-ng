# Class: MessageBus

Defined in: [src/common/web/core/messaging/MessageBus.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessageBus.ts#L31)

Bus for dispatching messages.

The message bus is probably the most central aspect of the system as a whole. It not only invokes local message handlers (which are basically
callback functions), it also sends messages across the network to other components if necessary. The message bus on the remote side will then
decide what to do with the incoming message: Dispatch it locally there, send it to yet another component, or just ignore it.

Message handlers are always registered through a ``MessageService``. When a message gets dispatched locally by the bus, it will call any handlers
associated with the message (via its name). If a message needs to be sent to another component, the bus will invoke the ``NetworkEngine`` to do
so.

To be error tolerant, any exceptions that arise during message handling will be logged but won't result in program termination.

## Constructors

### Constructor

> **new MessageBus**(`compData`): `MessageBus`

Defined in: [src/common/web/core/messaging/MessageBus.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessageBus.ts#L42)

#### Parameters

##### compData

[`WebComponentData`](../../../../component/WebComponentData/classes/WebComponentData.md)

The global component data.

#### Returns

`MessageBus`

## Methods

### addService()

> **addService**\<`CtxType`\>(`svc`): `boolean`

Defined in: [src/common/web/core/messaging/MessageBus.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessageBus.ts#L66)

Adds a new message service to the bus.

#### Type Parameters

##### CtxType

`CtxType` *extends* [`MessageContext`](../../handlers/MessageContext/classes/MessageContext.md)

#### Parameters

##### svc

[`MessageService`](../../handlers/MessageService/classes/MessageService.md)\<`CtxType`\>

The message service to add.

#### Returns

`boolean`

- Whether the message service was added.

***

### dispatch()

> **dispatch**(`msg`, `msgMeta`): `void`

Defined in: [src/common/web/core/messaging/MessageBus.ts:110](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessageBus.ts#L110)

Dispatches a message.

To do so, the message is first checked for validity (whether it actually *may* be dispatched). If it is valid,
the ``MessageRouter`` will determine if it needs to be dispatched to another component or locally (or both).

#### Parameters

##### msg

[`Message`](../../Message/classes/Message.md)

The message to be dispatched.

##### msgMeta

[`MessageMetaInformation`](../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

The message meta information.

#### Returns

`void`

***

### removeService()

> **removeService**\<`CtxType`\>(`svc`): `boolean`

Defined in: [src/common/web/core/messaging/MessageBus.ts:82](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessageBus.ts#L82)

Removes a message service from the bus.

#### Type Parameters

##### CtxType

`CtxType` *extends* [`MessageContext`](../../handlers/MessageContext/classes/MessageContext.md)

#### Parameters

##### svc

[`MessageService`](../../handlers/MessageService/classes/MessageService.md)\<`CtxType`\>

svc: The message service to remove.

#### Returns

`boolean`

- Whether the message service was removed.

***

### run()

> **run**(): `void`

Defined in: [src/common/web/core/messaging/MessageBus.ts:95](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessageBus.ts#L95)

Initiates periodic tasks performed by the bus.

#### Returns

`void`
