# Class: MessageMetaInformation

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformation.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L16)

Stores additional information necessary for message dispatching.

When a message is emitted, additional information is required to be able to properly handle it.
This includes its entrypoint into the system, as well as whether the message type requires a reply.

## Extended by

- [`CommandMetaInformation`](../../CommandMetaInformation/classes/CommandMetaInformation.md)
- [`CommandReplyMetaInformation`](../../CommandReplyMetaInformation/classes/CommandReplyMetaInformation.md)
- [`EventMetaInformation`](../../EventMetaInformation/classes/EventMetaInformation.md)

## Constructors

### Constructor

> **new MessageMetaInformation**(`entrypoint`, `requiresReply`): `MessageMetaInformation`

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

#### Parameters

##### entrypoint

[`MessageEntrypoint`](../enumerations/MessageEntrypoint.md)

From where the message entered the system (locally or remotely).

##### requiresReply

`boolean` = `false`

Whether a reply is expected.

#### Returns

`MessageMetaInformation`

## Properties

### entrypoint

> `readonly` **entrypoint**: [`MessageEntrypoint`](../enumerations/MessageEntrypoint.md)

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

From where the message entered the system (locally or remotely).

***

### requiresReply

> `readonly` **requiresReply**: `boolean` = `false`

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

Whether a reply is expected.

## Accessors

### isHandledExternally

#### Get Signature

> **get** **isHandledExternally**(): `boolean`

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformation.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L27)

Whether the message is handled outside the message bus.

##### Returns

`boolean`
