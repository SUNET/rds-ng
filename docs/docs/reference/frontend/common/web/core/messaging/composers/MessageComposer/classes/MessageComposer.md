# Abstract Class: MessageComposer\<MsgType\>

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L13)

A class to collect all information necessary to create and emit a message.

## Extended by

- [`CommandComposer`](../../CommandComposer/classes/CommandComposer.md)
- [`CommandReplyComposer`](../../CommandReplyComposer/classes/CommandReplyComposer.md)
- [`EventComposer`](../../EventComposer/classes/EventComposer.md)

## Type Parameters

### MsgType

`MsgType` *extends* [`Message`](../../../Message/classes/Message.md)

## Constructors

### Constructor

> **new MessageComposer**\<`MsgType`\>(`originID`, `messageBus`, `msgType`, `params`, `chain`): `MessageComposer`\<`MsgType`\>

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L31)

#### Parameters

##### originID

[`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

The component identifier of the origin of newly created messages.

##### messageBus

[`MessageBusProtocol`](../../../MessageBusProtocol/interfaces/MessageBusProtocol.md)

The global message bus to use.

##### msgType

[`ConstructableMessage`](../../../Message/interfaces/ConstructableMessage.md)\<`MsgType`\>

The message type.

##### params

`Record`\<`string`, `any`\> = `{}`

Additional message parameters.

##### chain

A message that acts as the *predecessor* of the new message. Used to keep the same trace for multiple messages.

`null` | [`Message`](../../../Message/classes/Message.md)

#### Returns

`MessageComposer`\<`MsgType`\>

## Properties

### \_chain

> `protected` **\_chain**: `null` \| [`Message`](../../../Message/classes/Message.md)

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L20)

***

### \_messageBus

> `protected` **\_messageBus**: [`MessageBusProtocol`](../../../MessageBusProtocol/interfaces/MessageBusProtocol.md)

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L15)

***

### \_msgType

> `protected` **\_msgType**: [`ConstructableMessage`](../../../Message/interfaces/ConstructableMessage.md)\<`MsgType`\>

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L17)

***

### \_originID

> `protected` **\_originID**: [`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L14)

***

### \_params

> `protected` **\_params**: `Record`\<`string`, `any`\>

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L18)

***

### \_payload

> `protected` **\_payload**: [`Payload`](../../../MessagePayload/type-aliases/Payload.md) = `{}`

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L19)

## Methods

### addPayload()

> **addPayload**(`key`, `data`): `void`

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L52)

Adds a payload item to the message.

#### Parameters

##### key

`string`

The item key.

##### data

`any`

The item data.

#### Returns

`void`

***

### before()

> **before**(`cb`): `this`

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L63)

Adds a callback that will be called immediately before the message is dispatched.

#### Parameters

##### cb

[`BeforeDispatchCallback`](../type-aliases/BeforeDispatchCallback.md)

The callback to add.

#### Returns

`this`

- This composer instance to allow call chaining.

***

### compose()

> `protected` **compose**(): `void`

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L89)

#### Returns

`void`

***

### createMetaInformation()

> `abstract` `protected` **createMetaInformation**(): [`MessageMetaInformation`](../../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:91](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L91)

#### Returns

[`MessageMetaInformation`](../../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

***

### emit()

> **emit**(`target`): `void`

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:73](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L73)

Sends the built message through the message bus.

#### Parameters

##### target

[`Channel`](../../../Channel/classes/Channel.md)

The target of the message.

#### Returns

`void`

***

### verify()

> `protected` **verify**(): `void`

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:87](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L87)

#### Returns

`void`
