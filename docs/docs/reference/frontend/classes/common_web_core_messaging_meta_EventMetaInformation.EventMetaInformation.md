---
id: "common_web_core_messaging_meta_EventMetaInformation.EventMetaInformation"
title: "Class: EventMetaInformation"
sidebar_label: "EventMetaInformation"
custom_edit_url: null
---

[common/web/core/messaging/meta/EventMetaInformation](../modules/common_web_core_messaging_meta_EventMetaInformation.md).EventMetaInformation

Message meta information specific to ``Event``.

## Hierarchy

- [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

  ↳ **`EventMetaInformation`**

## Constructors

### constructor

• **new EventMetaInformation**(`entrypoint`, `requiresReply?`): [`EventMetaInformation`](common_web_core_messaging_meta_EventMetaInformation.EventMetaInformation.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `entrypoint` | [`MessageEntrypoint`](../enums/common_web_core_messaging_meta_MessageMetaInformation.MessageEntrypoint.md) | `undefined` | From where the message entered the system (locally or remotely). |
| `requiresReply` | `boolean` | `false` | Whether a reply is expected. |

#### Returns

[`EventMetaInformation`](common_web_core_messaging_meta_EventMetaInformation.EventMetaInformation.md)

#### Inherited from

[MessageMetaInformation](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md).[constructor](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md#constructor)

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

## Properties

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

#### Inherited from

MessageMetaInformation.isHandledExternally

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformation.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L27)
