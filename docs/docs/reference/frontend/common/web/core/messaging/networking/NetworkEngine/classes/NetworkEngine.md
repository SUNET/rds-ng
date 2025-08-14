# Class: NetworkEngine

Defined in: [src/common/web/core/messaging/networking/NetworkEngine.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/NetworkEngine.ts#L25)

Main network management class.

Messages go out to other components through this class, and new messages come in from the outside world here as well.
The network engine takes care of listening to incoming messages, routing them properly, and sending new messages to other components.

## Constructors

### Constructor

> **new NetworkEngine**(`compData`, `messageBus`): `NetworkEngine`

Defined in: [src/common/web/core/messaging/networking/NetworkEngine.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/NetworkEngine.ts#L39)

#### Parameters

##### compData

[`WebComponentData`](../../../../../component/WebComponentData/classes/WebComponentData.md)

The global component data.

##### messageBus

[`MessageBusProtocol`](../../../MessageBusProtocol/interfaces/MessageBusProtocol.md)

The global message bus.

#### Returns

`NetworkEngine`

## Accessors

### client

#### Get Signature

> **get** **client**(): [`Client`](../../Client/classes/Client.md)

Defined in: [src/common/web/core/messaging/networking/NetworkEngine.ts:141](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/NetworkEngine.ts#L141)

The client instance.

##### Returns

[`Client`](../../Client/classes/Client.md)

## Methods

### process()

> **process**(): `void`

Defined in: [src/common/web/core/messaging/networking/NetworkEngine.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/NetworkEngine.ts#L70)

Called to perform periodic tasks.

#### Returns

`void`

***

### run()

> **run**(): `void`

Defined in: [src/common/web/core/messaging/networking/NetworkEngine.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/NetworkEngine.ts#L59)

Listens to incoming messages in order to properly route them.

#### Returns

`void`

***

### sendMessage()

> **sendMessage**(`msg`, `msgMeta`): `void`

Defined in: [src/common/web/core/messaging/networking/NetworkEngine.ts:83](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/NetworkEngine.ts#L83)

Sends a message across the network.

To do so, the message is first checked for validity (whether it actually *may* be sent). If it is valid, it is routed through the
client (the logic of this can be found in ``NetworkRouter``).

#### Parameters

##### msg

[`Message`](../../../Message/classes/Message.md)

The message to be sent.

##### msgMeta

[`MessageMetaInformation`](../../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

The message meta information.

#### Returns

`void`
