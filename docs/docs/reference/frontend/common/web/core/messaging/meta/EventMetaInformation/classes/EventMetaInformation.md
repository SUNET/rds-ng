# Class: EventMetaInformation

Defined in: [src/common/web/core/messaging/meta/EventMetaInformation.ts:6](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/EventMetaInformation.ts#L6)

Message meta information specific to ``Event``.

## Extends

- [`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md)

## Constructors

### Constructor

> **new EventMetaInformation**(`entrypoint`, `requiresReply`): `EventMetaInformation`

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

#### Parameters

##### entrypoint

[`MessageEntrypoint`](../../MessageMetaInformation/enumerations/MessageEntrypoint.md)

From where the message entered the system (locally or remotely).

##### requiresReply

`boolean` = `false`

Whether a reply is expected.

#### Returns

`EventMetaInformation`

#### Inherited from

[`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md).[`constructor`](../../MessageMetaInformation/classes/MessageMetaInformation.md#constructor)

## Properties

### entrypoint

> `readonly` **entrypoint**: [`MessageEntrypoint`](../../MessageMetaInformation/enumerations/MessageEntrypoint.md)

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

From where the message entered the system (locally or remotely).

#### Inherited from

[`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md).[`entrypoint`](../../MessageMetaInformation/classes/MessageMetaInformation.md#entrypoint)

***

### requiresReply

> `readonly` **requiresReply**: `boolean` = `false`

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

Whether a reply is expected.

#### Inherited from

[`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md).[`requiresReply`](../../MessageMetaInformation/classes/MessageMetaInformation.md#requiresreply)

## Accessors

### isHandledExternally

#### Get Signature

> **get** **isHandledExternally**(): `boolean`

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformation.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L27)

Whether the message is handled outside the message bus.

##### Returns

`boolean`

#### Inherited from

[`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md).[`isHandledExternally`](../../MessageMetaInformation/classes/MessageMetaInformation.md#ishandledexternally)
