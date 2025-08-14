# Class: CommandReplyMetaInformation

Defined in: [src/common/web/core/messaging/meta/CommandReplyMetaInformation.ts:6](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/CommandReplyMetaInformation.ts#L6)

Message meta information specific to ``CommandReply``.

## Extends

- [`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md)

## Constructors

### Constructor

> **new CommandReplyMetaInformation**(`entrypoint`, `requiresReply`): `CommandReplyMetaInformation`

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

#### Parameters

##### entrypoint

[`MessageEntrypoint`](../../MessageMetaInformation/enumerations/MessageEntrypoint.md)

From where the message entered the system (locally or remotely).

##### requiresReply

`boolean` = `false`

Whether a reply is expected.

#### Returns

`CommandReplyMetaInformation`

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

Defined in: [src/common/web/core/messaging/meta/CommandReplyMetaInformation.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/CommandReplyMetaInformation.ts#L12)

Whether the message is handled outside the message bus.

##### Returns

`boolean`

#### Set Signature

> **set** **isHandledExternally**(`handled`): `void`

Defined in: [src/common/web/core/messaging/meta/CommandReplyMetaInformation.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/CommandReplyMetaInformation.ts#L19)

Sets whether the message is handled outside the message bus.

##### Parameters

###### handled

`boolean`

##### Returns

`void`

#### Overrides

[`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md).[`isHandledExternally`](../../MessageMetaInformation/classes/MessageMetaInformation.md#ishandledexternally)
