---
id: "common_web_core_messaging_meta_CommandReplyMetaInformation.CommandReplyMetaInformation"
title: "Class: CommandReplyMetaInformation"
sidebar_label: "CommandReplyMetaInformation"
custom_edit_url: null
---

[common/web/core/messaging/meta/CommandReplyMetaInformation](../modules/common_web_core_messaging_meta_CommandReplyMetaInformation.md).CommandReplyMetaInformation

Message meta information specific to ``CommandReply``.

## Hierarchy

- [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

  ↳ **`CommandReplyMetaInformation`**

## Constructors

### constructor

• **new CommandReplyMetaInformation**(`entrypoint`, `requiresReply?`): [`CommandReplyMetaInformation`](common_web_core_messaging_meta_CommandReplyMetaInformation.CommandReplyMetaInformation.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `entrypoint` | [`MessageEntrypoint`](../enums/common_web_core_messaging_meta_MessageMetaInformation.MessageEntrypoint.md) | `undefined` | From where the message entered the system (locally or remotely). |
| `requiresReply` | `boolean` | `false` | Whether a reply is expected. |

#### Returns

[`CommandReplyMetaInformation`](common_web_core_messaging_meta_CommandReplyMetaInformation.CommandReplyMetaInformation.md)

#### Inherited from

[MessageMetaInformation](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md).[constructor](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md#constructor)

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

## Properties

### \_isHandledExternally

• `Private` **\_isHandledExternally**: `boolean` = `false`

#### Defined in

[src/common/web/core/messaging/meta/CommandReplyMetaInformation.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/CommandReplyMetaInformation.ts#L7)

___

### entrypoint

• `Readonly` **entrypoint**: [`MessageEntrypoint`](../enums/common_web_core_messaging_meta_MessageMetaInformation.MessageEntrypoint.md)

From where the message entered the system (locally or remotely).

#### Inherited from

[MessageMetaInformation](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md).[entrypoint](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md#entrypoint)

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

___

### requiresReply

• `Readonly` **requiresReply**: `boolean` = `false`

Whether a reply is expected.

#### Inherited from

[MessageMetaInformation](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md).[requiresReply](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md#requiresreply)

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

## Accessors

### isHandledExternally

• `get` **isHandledExternally**(): `boolean`

Whether the message is handled outside the message bus.

#### Returns

`boolean`

#### Overrides

MessageMetaInformation.isHandledExternally

#### Defined in

[src/common/web/core/messaging/meta/CommandReplyMetaInformation.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/CommandReplyMetaInformation.ts#L12)

• `set` **isHandledExternally**(`handled`): `void`

Sets whether the message is handled outside the message bus.

#### Parameters

| Name | Type |
| :------ | :------ |
| `handled` | `boolean` |

#### Returns

`void`

#### Overrides

MessageMetaInformation.isHandledExternally

#### Defined in

[src/common/web/core/messaging/meta/CommandReplyMetaInformation.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/CommandReplyMetaInformation.ts#L19)
