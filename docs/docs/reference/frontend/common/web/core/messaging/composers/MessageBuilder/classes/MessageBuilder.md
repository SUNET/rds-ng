# Class: MessageBuilder

Defined in: [src/common/web/core/messaging/composers/MessageBuilder.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageBuilder.ts#L16)

A helper class to easily build and emit new messages.

This class stores a reference to the global message bus and offers methods to easily create new messages and send them through the bus.

## Constructors

### Constructor

> **new MessageBuilder**(`originID`, `messageBus`): `MessageBuilder`

Defined in: [src/common/web/core/messaging/composers/MessageBuilder.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageBuilder.ts#L26)

#### Parameters

##### originID

[`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

The component identifier of the origin of newly created messages.

##### messageBus

[`MessageBusProtocol`](../../../MessageBusProtocol/interfaces/MessageBusProtocol.md)

The global message bus to use.

#### Returns

`MessageBuilder`

## Methods

### buildCommand()

> **buildCommand**\<`MsgType`\>(`cmdType`, `values`, `chain`): [`CommandComposer`](../../CommandComposer/classes/CommandComposer.md)\<`MsgType`\>

Defined in: [src/common/web/core/messaging/composers/MessageBuilder.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageBuilder.ts#L46)

Builds a new command.

#### Type Parameters

##### MsgType

`MsgType` *extends* [`Command`](../../../Command/classes/Command.md)

#### Parameters

##### cmdType

[`ConstructableMessage`](../../../Message/interfaces/ConstructableMessage.md)\<`MsgType`\>

The command type (i.e., a subclass of ``Command``).

##### values

`Record`\<`string`, `any`\> = `{}`

Additional message values.

##### chain

A message that acts as the *predecessor* of the new message. Used to keep the same trace for multiple messages.

`null` | [`Message`](../../../Message/classes/Message.md)

#### Returns

[`CommandComposer`](../../CommandComposer/classes/CommandComposer.md)\<`MsgType`\>

- The newly created command.

#### Throws

Error - If an unknown value was provided in ``values`.

***

### buildCommandReply()

> **buildCommandReply**\<`MsgType`\>(`replyType`, `command`, `success`, `message`, `values`): [`CommandReplyComposer`](../../CommandReplyComposer/classes/CommandReplyComposer.md)\<`MsgType`\>

Defined in: [src/common/web/core/messaging/composers/MessageBuilder.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageBuilder.ts#L66)

Builds a new command reply.

#### Type Parameters

##### MsgType

`MsgType` *extends* [`CommandReply`](../../../CommandReply/classes/CommandReply.md)

#### Parameters

##### replyType

[`ConstructableMessage`](../../../Message/interfaces/ConstructableMessage.md)\<`MsgType`\>

The command reply type (i.e., a subclass of ``CommandReply``).

##### command

[`Command`](../../../Command/classes/Command.md)

The ``Command`` this reply is based on.

##### success

`boolean` = `true`

Whether the command *succeeded* or not (how this is interpreted depends on the command).

##### message

`string` = `""`

Additional message to include in the reply.

##### values

`Record`\<`string`, `any`\> = `{}`

Additional message values.

#### Returns

[`CommandReplyComposer`](../../CommandReplyComposer/classes/CommandReplyComposer.md)\<`MsgType`\>

- The newly created command reply.

#### Throws

Error - If an unknown value was provided in ``values`.

***

### buildEvent()

> **buildEvent**\<`MsgType`\>(`eventType`, `values`, `chain`): [`EventComposer`](../../EventComposer/classes/EventComposer.md)\<`MsgType`\>

Defined in: [src/common/web/core/messaging/composers/MessageBuilder.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageBuilder.ts#L89)

Builds a new event.

#### Type Parameters

##### MsgType

`MsgType` *extends* [`Event`](../../../Event/classes/Event.md)

#### Parameters

##### eventType

[`ConstructableMessage`](../../../Message/interfaces/ConstructableMessage.md)\<`MsgType`\>

The event type (i.e., a subclass of ``Event``).

##### values

`Record`\<`string`, `any`\> = `{}`

Additional message values.

##### chain

A message that acts as the *predecessor* of the new message. Used to keep the same trace for multiple messages.

`null` | [`Message`](../../../Message/classes/Message.md)

#### Returns

[`EventComposer`](../../EventComposer/classes/EventComposer.md)\<`MsgType`\>

- The newly created event.

#### Throws

Error - If an unknown value was provided in ``values`.

***

### getMessageCount()

> **getMessageCount**(`counter`): `number`

Defined in: [src/common/web/core/messaging/composers/MessageBuilder.ts:106](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageBuilder.ts#L106)

Gets how many messages of specific message types have been created.

The message builder keeps track of how many messages of the three major types ``Command``, ``CommandReply`` and
``Event`` have been created.

#### Parameters

##### counter

`string`

The message type to get the count of. Must be either ``Command``, ``CommandReply`` or ``Event``.

#### Returns

`number`

- The number of messages already built of the specified type.
