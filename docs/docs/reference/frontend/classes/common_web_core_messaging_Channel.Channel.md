---
id: "common_web_core_messaging_Channel.Channel"
title: "Class: Channel"
sidebar_label: "Channel"
custom_edit_url: null
---

[common/web/core/messaging/Channel](../modules/common_web_core_messaging_Channel.md).Channel

The target of a message.

Message targets are represented by so-called *channels*. These can be *local* for messages that will only
be dispatched locally and not across the network or *direct* for specific (remote) targets.

## Constructors

### constructor

• **new Channel**(`type`, `target?`): [`Channel`](common_web_core_messaging_Channel.Channel.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `type` | `string` | The channel type. |
| `target?` | `string` | The actual target in case of a direct channel. |

#### Returns

[`Channel`](common_web_core_messaging_Channel.Channel.md)

#### Defined in

[src/common/web/core/messaging/Channel.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Channel.ts#L22)

## Properties

### target

• `Optional` `Readonly` **target**: `string`

The actual target in case of a direct channel.

#### Defined in

[src/common/web/core/messaging/Channel.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Channel.ts#L22)

___

### type

• `Readonly` **type**: `string`

The channel type.

#### Defined in

[src/common/web/core/messaging/Channel.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Channel.ts#L22)

## Accessors

### isDirect

• `get` **isDirect**(): `boolean`

Whether this is a direct channel.

#### Returns

`boolean`

#### Defined in

[src/common/web/core/messaging/Channel.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Channel.ts#L48)

___

### isLocal

• `get` **isLocal**(): `boolean`

Whether this is a local channel.

#### Returns

`boolean`

#### Defined in

[src/common/web/core/messaging/Channel.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Channel.ts#L41)

___

### targetID

• `get` **targetID**(): ``null`` \| [`UnitID`](common_web_utils_UnitID.UnitID.md)

Generates a ``UnitID`` from the target of this channel.

#### Returns

``null`` \| [`UnitID`](common_web_utils_UnitID.UnitID.md)

- The component ID of the target, if any.

#### Defined in

[src/common/web/core/messaging/Channel.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Channel.ts#L30)

## Methods

### toString

▸ **toString**(): `string`

Gets the string representation of this channel.

#### Returns

`string`

#### Defined in

[src/common/web/core/messaging/Channel.ts:55](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Channel.ts#L55)

___

### direct

▸ **direct**(`target`): [`Channel`](common_web_core_messaging_Channel.Channel.md)

Creates a new direct channel.

#### Parameters

| Name | Type |
| :------ | :------ |
| `target` | `string` \| [`UnitID`](common_web_utils_UnitID.UnitID.md) |

#### Returns

[`Channel`](common_web_core_messaging_Channel.Channel.md)

#### Defined in

[src/common/web/core/messaging/Channel.ts:69](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Channel.ts#L69)

___

### local

▸ **local**(): [`Channel`](common_web_core_messaging_Channel.Channel.md)

Creates a new local channel.

#### Returns

[`Channel`](common_web_core_messaging_Channel.Channel.md)

#### Defined in

[src/common/web/core/messaging/Channel.ts:62](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Channel.ts#L62)
