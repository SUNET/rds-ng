# Class: CommandReplyComposer\<MsgType\>

Defined in: [src/common/web/core/messaging/composers/CommandReplyComposer.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/CommandReplyComposer.ts#L14)

Composer for ``CommandReply`` messages.

## Extends

- [`MessageComposer`](../../MessageComposer/classes/MessageComposer.md)\<`MsgType`\>

## Type Parameters

### MsgType

`MsgType` *extends* [`CommandReply`](../../../CommandReply/classes/CommandReply.md)

## Constructors

### Constructor

> **new CommandReplyComposer**\<`MsgType`\>(`originID`, `messageBus`, `msgType`, `cmd`, `params`): `CommandReplyComposer`\<`MsgType`\>

Defined in: [src/common/web/core/messaging/composers/CommandReplyComposer.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/CommandReplyComposer.ts#L17)

#### Parameters

##### originID

[`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

##### messageBus

[`MessageBusProtocol`](../../../MessageBusProtocol/interfaces/MessageBusProtocol.md)

##### msgType

[`ConstructableMessage`](../../../Message/interfaces/ConstructableMessage.md)\<`MsgType`\>

##### cmd

[`Command`](../../../Command/classes/Command.md)

##### params

`Record`\<`string`, `any`\> = `{}`

#### Returns

`CommandReplyComposer`\<`MsgType`\>

#### Overrides

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`constructor`](../../MessageComposer/classes/MessageComposer.md#constructor)

## Properties

### \_chain

> `protected` **\_chain**: `null` \| [`Message`](../../../Message/classes/Message.md)

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L20)

#### Inherited from

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`_chain`](../../MessageComposer/classes/MessageComposer.md#_chain)

***

### \_messageBus

> `protected` **\_messageBus**: [`MessageBusProtocol`](../../../MessageBusProtocol/interfaces/MessageBusProtocol.md)

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L15)

#### Inherited from

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`_messageBus`](../../MessageComposer/classes/MessageComposer.md#_messagebus)

***

### \_msgType

> `protected` **\_msgType**: [`ConstructableMessage`](../../../Message/interfaces/ConstructableMessage.md)\<`MsgType`\>

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L17)

#### Inherited from

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`_msgType`](../../MessageComposer/classes/MessageComposer.md#_msgtype)

***

### \_originID

> `protected` **\_originID**: [`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L14)

#### Inherited from

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`_originID`](../../MessageComposer/classes/MessageComposer.md#_originid)

***

### \_params

> `protected` **\_params**: `Record`\<`string`, `any`\>

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L18)

#### Inherited from

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`_params`](../../MessageComposer/classes/MessageComposer.md#_params)

***

### \_payload

> `protected` **\_payload**: [`Payload`](../../../MessagePayload/type-aliases/Payload.md) = `{}`

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L19)

#### Inherited from

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`_payload`](../../MessageComposer/classes/MessageComposer.md#_payload)

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

#### Inherited from

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`addPayload`](../../MessageComposer/classes/MessageComposer.md#addpayload)

***

### before()

> **before**(`cb`): `this`

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L63)

Adds a callback that will be called immediately before the message is dispatched.

#### Parameters

##### cb

[`BeforeDispatchCallback`](../../MessageComposer/type-aliases/BeforeDispatchCallback.md)

The callback to add.

#### Returns

`this`

- This composer instance to allow call chaining.

#### Inherited from

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`before`](../../MessageComposer/classes/MessageComposer.md#before)

***

### compose()

> `protected` **compose**(): `void`

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L89)

#### Returns

`void`

#### Inherited from

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`compose`](../../MessageComposer/classes/MessageComposer.md#compose)

***

### createMetaInformation()

> `protected` **createMetaInformation**(): [`MessageMetaInformation`](../../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

Defined in: [src/common/web/core/messaging/composers/CommandReplyComposer.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/CommandReplyComposer.ts#L32)

#### Returns

[`MessageMetaInformation`](../../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

#### Overrides

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`createMetaInformation`](../../MessageComposer/classes/MessageComposer.md#createmetainformation)

***

### emit()

> **emit**(): `void`

Defined in: [src/common/web/core/messaging/composers/CommandReplyComposer.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/CommandReplyComposer.ts#L27)

Sends the built message through the message bus.

#### Returns

`void`

#### Overrides

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`emit`](../../MessageComposer/classes/MessageComposer.md#emit)

***

### verify()

> `protected` **verify**(): `void`

Defined in: [src/common/web/core/messaging/composers/MessageComposer.ts:87](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/MessageComposer.ts#L87)

#### Returns

`void`

#### Inherited from

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`verify`](../../MessageComposer/classes/MessageComposer.md#verify)
