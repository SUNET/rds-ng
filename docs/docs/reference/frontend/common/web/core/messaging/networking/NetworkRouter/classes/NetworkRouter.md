# Class: NetworkRouter

Defined in: [src/common/web/core/messaging/networking/NetworkRouter.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/NetworkRouter.ts#L19)

Network routing rules and logic.

When a message enters the network engine in order to be sent to remote targets, it is first checked for its
validity. Afterwards, the router decides through which channels (local, client) it needs to be sent.

## Constructors

### Constructor

> **new NetworkRouter**(`compID`): `NetworkRouter`

Defined in: [src/common/web/core/messaging/networking/NetworkRouter.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/NetworkRouter.ts#L25)

#### Parameters

##### compID

[`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

The component id (required to decide whether we match a given direct target).

#### Returns

`NetworkRouter`

## Methods

### checkClientRouting()

> **checkClientRouting**(`direction`, `msg`, `msgMeta`): `boolean`

Defined in: [src/common/web/core/messaging/networking/NetworkRouter.ts:75](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/NetworkRouter.ts#L75)

Checks if the message should be routed through the client.

#### Parameters

##### direction

[`NetworkRouterDirection`](../enumerations/NetworkRouterDirection.md)

The direction (*IN* or *OUT*) of the message.

##### msg

[`Message`](../../../Message/classes/Message.md)

The actual message.

##### msgMeta

[`MessageMetaInformation`](../../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

The message meta information.

#### Returns

`boolean`

Whether client routing should happen.

***

### checkLocalRouting()

> **checkLocalRouting**(`direction`, `msg`, `msgMeta`): `boolean`

Defined in: [src/common/web/core/messaging/networking/NetworkRouter.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/NetworkRouter.ts#L54)

Checks if the message should be routed locally (dispatched via the message bus).

#### Parameters

##### direction

[`NetworkRouterDirection`](../enumerations/NetworkRouterDirection.md)

The direction (*IN* or *OUT*) of the message.

##### msg

[`Message`](../../../Message/classes/Message.md)

The actual message.

##### msgMeta

[`MessageMetaInformation`](../../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

The message meta information.

#### Returns

`boolean`

Whether local routing should happen.

***

### verifyMessage()

> **verifyMessage**(`direction`, `msg`): `void`

Defined in: [src/common/web/core/messaging/networking/NetworkRouter.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/NetworkRouter.ts#L37)

Verifies whether a message may enter the network engine.

#### Parameters

##### direction

[`NetworkRouterDirection`](../enumerations/NetworkRouterDirection.md)

The direction (*IN* or *OUT*) of the message.

##### msg

[`Message`](../../../Message/classes/Message.md)

The message that wants to enter the network engine.

#### Returns

`void`

#### Throws

Error - In case the message is not valid to enter the network engine.
