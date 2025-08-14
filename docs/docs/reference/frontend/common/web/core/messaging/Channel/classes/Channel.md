# Class: Channel

Defined in: [src/common/web/core/messaging/Channel.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Channel.ts#L17)

The target of a message.

Message targets are represented by so-called *channels*. These can be *local* for messages that will only
be dispatched locally and not across the network or *direct* for specific (remote) targets.

## Constructors

### Constructor

> **new Channel**(`type`, `target?`): `Channel`

Defined in: [src/common/web/core/messaging/Channel.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Channel.ts#L22)

#### Parameters

##### type

`string`

The channel type.

##### target?

`string`

The actual target in case of a direct channel.

#### Returns

`Channel`

## Properties

### target?

> `readonly` `optional` **target**: `string`

Defined in: [src/common/web/core/messaging/Channel.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Channel.ts#L22)

The actual target in case of a direct channel.

***

### type

> `readonly` **type**: `string`

Defined in: [src/common/web/core/messaging/Channel.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Channel.ts#L22)

The channel type.

## Accessors

### isDirect

#### Get Signature

> **get** **isDirect**(): `boolean`

Defined in: [src/common/web/core/messaging/Channel.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Channel.ts#L48)

Whether this is a direct channel.

##### Returns

`boolean`

***

### isLocal

#### Get Signature

> **get** **isLocal**(): `boolean`

Defined in: [src/common/web/core/messaging/Channel.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Channel.ts#L41)

Whether this is a local channel.

##### Returns

`boolean`

***

### targetID

#### Get Signature

> **get** **targetID**(): `null` \| [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/Channel.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Channel.ts#L30)

Generates a ``UnitID`` from the target of this channel.

##### Returns

`null` \| [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

- The component ID of the target, if any.

## Methods

### toString()

> **toString**(): `string`

Defined in: [src/common/web/core/messaging/Channel.ts:55](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Channel.ts#L55)

Gets the string representation of this channel.

#### Returns

`string`

***

### direct()

> `static` **direct**(`target`): `Channel`

Defined in: [src/common/web/core/messaging/Channel.ts:69](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Channel.ts#L69)

Creates a new direct channel.

#### Parameters

##### target

`string` | [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

#### Returns

`Channel`

***

### local()

> `static` **local**(): `Channel`

Defined in: [src/common/web/core/messaging/Channel.ts:62](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Channel.ts#L62)

Creates a new local channel.

#### Returns

`Channel`
