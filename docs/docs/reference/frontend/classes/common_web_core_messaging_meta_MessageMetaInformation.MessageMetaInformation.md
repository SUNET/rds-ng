---
id: "common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation"
title: "Class: MessageMetaInformation"
sidebar_label: "MessageMetaInformation"
custom_edit_url: null
---

[common/web/core/messaging/meta/MessageMetaInformation](../modules/common_web_core_messaging_meta_MessageMetaInformation.md).MessageMetaInformation

Stores additional information necessary for message dispatching.

When a message is emitted, additional information is required to be able to properly handle it.
This includes its entrypoint into the system, as well as whether the message type requires a reply.

## Hierarchy

- **`MessageMetaInformation`**

  ↳ [`CommandMetaInformation`](common_web_core_messaging_meta_CommandMetaInformation.CommandMetaInformation.md)

  ↳ [`CommandReplyMetaInformation`](common_web_core_messaging_meta_CommandReplyMetaInformation.CommandReplyMetaInformation.md)

  ↳ [`EventMetaInformation`](common_web_core_messaging_meta_EventMetaInformation.EventMetaInformation.md)

## Constructors

### constructor

• **new MessageMetaInformation**(`entrypoint`, `requiresReply?`): [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `entrypoint` | [`MessageEntrypoint`](../enums/common_web_core_messaging_meta_MessageMetaInformation.MessageEntrypoint.md) | `undefined` | From where the message entered the system (locally or remotely). |
| `requiresReply` | `boolean` | `false` | Whether a reply is expected. |

#### Returns

[`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

## Properties

### entrypoint

• `Readonly` **entrypoint**: [`MessageEntrypoint`](../enums/common_web_core_messaging_meta_MessageMetaInformation.MessageEntrypoint.md)

From where the message entered the system (locally or remotely).

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

___

### requiresReply

• `Readonly` **requiresReply**: `boolean` = `false`

Whether a reply is expected.

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

## Accessors

### isHandledExternally

• `get` **isHandledExternally**(): `boolean`

Whether the message is handled outside the message bus.

#### Returns

`boolean`

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformation.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L27)
