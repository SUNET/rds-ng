# Class: CommandComposer\<MsgType\>

Defined in: [src/common/web/core/messaging/composers/CommandComposer.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/CommandComposer.ts#L17)

Composer for ``Command`` messages.

## Extends

- [`MessageComposer`](../../MessageComposer/classes/MessageComposer.md)\<`MsgType`\>

## Type Parameters

### MsgType

`MsgType` *extends* [`Command`](../../../Command/classes/Command.md)

## Constructors

### Constructor

> **new CommandComposer**\<`MsgType`\>(`originID`, `messageBus`, `msgType`, `params`, `chain`): `CommandComposer`\<`MsgType`\>

Defined in: [src/common/web/core/messaging/composers/CommandComposer.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/CommandComposer.ts#L22)

#### Parameters

##### originID

[`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

##### messageBus

[`MessageBusProtocol`](../../../MessageBusProtocol/interfaces/MessageBusProtocol.md)

##### msgType

[`ConstructableMessage`](../../../Message/interfaces/ConstructableMessage.md)\<`MsgType`\>

##### params

`Record`\<`string`, `any`\> = `{}`

##### chain

`null` | [`Message`](../../../Message/classes/Message.md)

#### Returns

`CommandComposer`\<`MsgType`\>

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

Defined in: [src/common/web/core/messaging/composers/CommandComposer.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/CommandComposer.ts#L76)

#### Returns

[`MessageMetaInformation`](../../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

#### Overrides

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`createMetaInformation`](../../MessageComposer/classes/MessageComposer.md#createmetainformation)

***

### done()

> **done**(`cb`): `this`

Defined in: [src/common/web/core/messaging/composers/CommandComposer.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/CommandComposer.ts#L41)

Adds a *Done* callback.

#### Parameters

##### cb

[`CommandDoneCallback`](../../../CommandReply/type-aliases/CommandDoneCallback.md)

The callback to add.

#### Returns

`this`

- This composer instance to allow call chaining.

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

#### Inherited from

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`emit`](../../MessageComposer/classes/MessageComposer.md#emit)

***

### failed()

> **failed**(`cb`): `this`

Defined in: [src/common/web/core/messaging/composers/CommandComposer.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/CommandComposer.ts#L53)

Adds a *Fail* callback.

#### Parameters

##### cb

[`CommandFailCallback`](../../../CommandReply/type-aliases/CommandFailCallback.md)

The callback to add.

#### Returns

`this`

- This composer instance to allow call chaining.

***

### timeout()

> **timeout**(`timeout`): `this`

Defined in: [src/common/web/core/messaging/composers/CommandComposer.ts:65](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/CommandComposer.ts#L65)

Assigns a *Done* callback.

#### Parameters

##### timeout

`number`

The timeout (in seconds).

#### Returns

`this`

- This composer instance to allow call chaining.

***

### verify()

> `protected` **verify**(): `void`

Defined in: [src/common/web/core/messaging/composers/CommandComposer.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/composers/CommandComposer.ts#L70)

#### Returns

`void`

#### Overrides

[`MessageComposer`](../../MessageComposer/classes/MessageComposer.md).[`verify`](../../MessageComposer/classes/MessageComposer.md#verify)
