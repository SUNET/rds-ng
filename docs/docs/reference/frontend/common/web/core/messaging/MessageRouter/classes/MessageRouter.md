# Class: MessageRouter

Defined in: [src/common/web/core/messaging/MessageRouter.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessageRouter.ts#L11)

Message routing rules and logic.

When a message enters the message bus, it is first checked for its validity.
Afterwards, the router decides through which channels (local, remote) it needs to be sent.

## Constructors

### Constructor

> **new MessageRouter**(`compID`): `MessageRouter`

Defined in: [src/common/web/core/messaging/MessageRouter.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessageRouter.ts#L17)

#### Parameters

##### compID

[`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

The component id (required to decide whether we match a given direct target).

#### Returns

`MessageRouter`

## Methods

### checkLocalRouting()

> **checkLocalRouting**(`msg`, `msgMeta`): `boolean`

Defined in: [src/common/web/core/messaging/MessageRouter.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessageRouter.ts#L43)

Checks if the message should be routed locally.

#### Parameters

##### msg

[`Message`](../../Message/classes/Message.md)

The message.

##### msgMeta

[`MessageMetaInformation`](../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

The message meta information.

#### Returns

`boolean`

***

### checkRemoteRouting()

> **checkRemoteRouting**(`msg`, `msgMeta`): `boolean`

Defined in: [src/common/web/core/messaging/MessageRouter.ts:61](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessageRouter.ts#L61)

Checks if the message should be routed remotely.

#### Parameters

##### msg

[`Message`](../../Message/classes/Message.md)

The message.

##### msgMeta

[`MessageMetaInformation`](../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

The message meta information.

#### Returns

`boolean`

***

### verifyMessage()

> **verifyMessage**(`msg`, `msgMeta`): `void`

Defined in: [src/common/web/core/messaging/MessageRouter.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessageRouter.ts#L29)

Verifies whether a message may enter the message bus.

#### Parameters

##### msg

[`Message`](../../Message/classes/Message.md)

The message that wants to enter the network engine.

##### msgMeta

[`MessageMetaInformation`](../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

The message meta information.

#### Returns

`void`

#### Throws

Error - In case the message is not valid to enter the message bus.
