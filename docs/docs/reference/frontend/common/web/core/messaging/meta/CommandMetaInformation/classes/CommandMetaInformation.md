# Class: CommandMetaInformation

Defined in: [src/common/web/core/messaging/meta/CommandMetaInformation.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/CommandMetaInformation.ts#L7)

Message meta information specific to ``Command``.

## Extends

- [`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md)

## Constructors

### Constructor

> **new CommandMetaInformation**(`entrypoint`, `doneCallbacks`, `failCallbacks`, `timeout`): `CommandMetaInformation`

Defined in: [src/common/web/core/messaging/meta/CommandMetaInformation.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/CommandMetaInformation.ts#L14)

#### Parameters

##### entrypoint

[`MessageEntrypoint`](../../MessageMetaInformation/enumerations/MessageEntrypoint.md)

From where the message entered the system (locally or remotely).

##### doneCallbacks

[`CommandDoneCallback`](../../../CommandReply/type-aliases/CommandDoneCallback.md)[] = `[]`

Called when a reply was received for this command.

##### failCallbacks

[`CommandFailCallback`](../../../CommandReply/type-aliases/CommandFailCallback.md)[] = `[]`

Called when no reply was received for this command or an exception occurred.

##### timeout

`number` = `0.0`

The timeout (in seconds) before a command is deemed not replied.

#### Returns

`CommandMetaInformation`

#### Overrides

[`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md).[`constructor`](../../MessageMetaInformation/classes/MessageMetaInformation.md#constructor)

## Properties

### doneCallbacks

> `readonly` **doneCallbacks**: [`CommandDoneCallback`](../../../CommandReply/type-aliases/CommandDoneCallback.md)[] = `[]`

Defined in: [src/common/web/core/messaging/meta/CommandMetaInformation.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/CommandMetaInformation.ts#L15)

Called when a reply was received for this command.

***

### entrypoint

> `readonly` **entrypoint**: [`MessageEntrypoint`](../../MessageMetaInformation/enumerations/MessageEntrypoint.md)

Defined in: [src/common/web/core/messaging/meta/CommandMetaInformation.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/CommandMetaInformation.ts#L14)

From where the message entered the system (locally or remotely).

#### Inherited from

[`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md).[`entrypoint`](../../MessageMetaInformation/classes/MessageMetaInformation.md#entrypoint)

***

### failCallbacks

> `readonly` **failCallbacks**: [`CommandFailCallback`](../../../CommandReply/type-aliases/CommandFailCallback.md)[] = `[]`

Defined in: [src/common/web/core/messaging/meta/CommandMetaInformation.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/CommandMetaInformation.ts#L16)

Called when no reply was received for this command or an exception occurred.

***

### requiresReply

> `readonly` **requiresReply**: `boolean` = `false`

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

Whether a reply is expected.

#### Inherited from

[`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md).[`requiresReply`](../../MessageMetaInformation/classes/MessageMetaInformation.md#requiresreply)

***

### timeout

> `readonly` **timeout**: `number` = `0.0`

Defined in: [src/common/web/core/messaging/meta/CommandMetaInformation.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/CommandMetaInformation.ts#L17)

The timeout (in seconds) before a command is deemed not replied.

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
