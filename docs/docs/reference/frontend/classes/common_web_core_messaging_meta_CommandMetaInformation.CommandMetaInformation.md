---
id: "common_web_core_messaging_meta_CommandMetaInformation.CommandMetaInformation"
title: "Class: CommandMetaInformation"
sidebar_label: "CommandMetaInformation"
custom_edit_url: null
---

[common/web/core/messaging/meta/CommandMetaInformation](../modules/common_web_core_messaging_meta_CommandMetaInformation.md).CommandMetaInformation

Message meta information specific to ``Command``.

## Hierarchy

- [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

  ↳ **`CommandMetaInformation`**

## Constructors

### constructor

• **new CommandMetaInformation**(`entrypoint`, `doneCallbacks?`, `failCallbacks?`, `timeout?`): [`CommandMetaInformation`](common_web_core_messaging_meta_CommandMetaInformation.CommandMetaInformation.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `entrypoint` | [`MessageEntrypoint`](../enums/common_web_core_messaging_meta_MessageMetaInformation.MessageEntrypoint.md) | `undefined` | From where the message entered the system (locally or remotely). |
| `doneCallbacks` | [`CommandDoneCallback`](../modules/common_web_core_messaging_CommandReply.md#commanddonecallback)[] | `[]` | Called when a reply was received for this command. |
| `failCallbacks` | [`CommandFailCallback`](../modules/common_web_core_messaging_CommandReply.md#commandfailcallback)[] | `[]` | Called when no reply was received for this command or an exception occurred. |
| `timeout` | `number` | `0.0` | The timeout (in seconds) before a command is deemed not replied. |

#### Returns

[`CommandMetaInformation`](common_web_core_messaging_meta_CommandMetaInformation.CommandMetaInformation.md)

#### Overrides

[MessageMetaInformation](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md).[constructor](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md#constructor)

#### Defined in

[src/common/web/core/messaging/meta/CommandMetaInformation.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/CommandMetaInformation.ts#L14)

## Properties

### doneCallbacks

• `Readonly` **doneCallbacks**: [`CommandDoneCallback`](../modules/common_web_core_messaging_CommandReply.md#commanddonecallback)[] = `[]`

Called when a reply was received for this command.

#### Defined in

[src/common/web/core/messaging/meta/CommandMetaInformation.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/CommandMetaInformation.ts#L15)

___

### entrypoint

• `Readonly` **entrypoint**: [`MessageEntrypoint`](../enums/common_web_core_messaging_meta_MessageMetaInformation.MessageEntrypoint.md)

From where the message entered the system (locally or remotely).

#### Inherited from

[MessageMetaInformation](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md).[entrypoint](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md#entrypoint)

#### Defined in

[src/common/web/core/messaging/meta/CommandMetaInformation.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/CommandMetaInformation.ts#L14)

___

### failCallbacks

• `Readonly` **failCallbacks**: [`CommandFailCallback`](../modules/common_web_core_messaging_CommandReply.md#commandfailcallback)[] = `[]`

Called when no reply was received for this command or an exception occurred.

#### Defined in

[src/common/web/core/messaging/meta/CommandMetaInformation.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/CommandMetaInformation.ts#L16)

___

### requiresReply

• `Readonly` **requiresReply**: `boolean` = `false`

Whether a reply is expected.

#### Inherited from

[MessageMetaInformation](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md).[requiresReply](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md#requiresreply)

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformation.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformation.ts#L21)

___

### timeout

• `Readonly` **timeout**: `number` = `0.0`

The timeout (in seconds) before a command is deemed not replied.

#### Defined in

[src/common/web/core/messaging/meta/CommandMetaInformation.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/CommandMetaInformation.ts#L17)

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
