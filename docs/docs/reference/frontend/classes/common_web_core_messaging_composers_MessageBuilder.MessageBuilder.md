---
id: "common_web_core_messaging_composers_MessageBuilder.MessageBuilder"
title: "Class: MessageBuilder"
sidebar_label: "MessageBuilder"
custom_edit_url: null
---

[common/web/core/messaging/composers/MessageBuilder](../modules/common_web_core_messaging_composers_MessageBuilder.md).MessageBuilder

A helper class to easily build and emit new messages.

This class stores a reference to the global message bus and offers methods to easily create new messages and send them through the bus.

## Constructors

### constructor

• **new MessageBuilder**(`originID`, `messageBus`): [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `originID` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | The component identifier of the origin of newly created messages. |
| `messageBus` | [`MessageBusProtocol`](../interfaces/common_web_core_messaging_MessageBusProtocol.MessageBusProtocol.md) | The global message bus to use. |

#### Returns

[`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Defined in

[src/common/web/core/messaging/composers/MessageBuilder.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageBuilder.ts#L26)

## Properties

### \_counters

• `Private` `Readonly` **\_counters**: `Record`<`string`, `number`\> = `{}`

#### Defined in

[src/common/web/core/messaging/composers/MessageBuilder.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageBuilder.ts#L20)

___

### \_messageBus

• `Private` `Readonly` **\_messageBus**: [`MessageBusProtocol`](../interfaces/common_web_core_messaging_MessageBusProtocol.MessageBusProtocol.md)

#### Defined in

[src/common/web/core/messaging/composers/MessageBuilder.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageBuilder.ts#L18)

___

### \_originID

• `Private` `Readonly` **\_originID**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Defined in

[src/common/web/core/messaging/composers/MessageBuilder.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageBuilder.ts#L17)

## Methods

### buildCommand

▸ **buildCommand**<`MsgType`\>(`cmdType`, `values?`, `chain?`): [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`MsgType`\>

Builds a new command.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `MsgType` | extends [`Command`](common_web_core_messaging_Command.Command.md) |

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `cmdType` | [`ConstructableMessage`](../interfaces/common_web_core_messaging_Message.ConstructableMessage.md)<`MsgType`\> | `undefined` | The command type (i.e., a subclass of ``Command``). |
| `values` | `Record`<`string`, `any`\> | `{}` | Additional message values. |
| `chain` | ``null`` \| [`Message`](common_web_core_messaging_Message.Message.md) | `null` | A message that acts as the *predecessor* of the new message. Used to keep the same trace for multiple messages. |

#### Returns

[`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`MsgType`\>

- The newly created command.

**`Throws`**

Error - If an unknown value was provided in ``values`.

#### Defined in

[src/common/web/core/messaging/composers/MessageBuilder.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageBuilder.ts#L46)

___

### buildCommandReply

▸ **buildCommandReply**<`MsgType`\>(`replyType`, `command`, `success?`, `message?`, `values?`): [`CommandReplyComposer`](common_web_core_messaging_composers_CommandReplyComposer.CommandReplyComposer.md)<`MsgType`\>

Builds a new command reply.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `MsgType` | extends [`CommandReply`](common_web_core_messaging_CommandReply.CommandReply.md) |

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `replyType` | [`ConstructableMessage`](../interfaces/common_web_core_messaging_Message.ConstructableMessage.md)<`MsgType`\> | `undefined` | The command reply type (i.e., a subclass of ``CommandReply``). |
| `command` | [`Command`](common_web_core_messaging_Command.Command.md) | `undefined` | The ``Command`` this reply is based on. |
| `success` | `boolean` | `true` | Whether the command *succeeded* or not (how this is interpreted depends on the command). |
| `message` | `string` | `""` | Additional message to include in the reply. |
| `values` | `Record`<`string`, `any`\> | `{}` | Additional message values. |

#### Returns

[`CommandReplyComposer`](common_web_core_messaging_composers_CommandReplyComposer.CommandReplyComposer.md)<`MsgType`\>

- The newly created command reply.

**`Throws`**

Error - If an unknown value was provided in ``values`.

#### Defined in

[src/common/web/core/messaging/composers/MessageBuilder.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageBuilder.ts#L66)

___

### buildEvent

▸ **buildEvent**<`MsgType`\>(`eventType`, `values?`, `chain?`): [`EventComposer`](common_web_core_messaging_composers_EventComposer.EventComposer.md)<`MsgType`\>

Builds a new event.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `MsgType` | extends [`Event`](common_web_core_messaging_Event.Event.md) |

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `eventType` | [`ConstructableMessage`](../interfaces/common_web_core_messaging_Message.ConstructableMessage.md)<`MsgType`\> | `undefined` | The event type (i.e., a subclass of ``Event``). |
| `values` | `Record`<`string`, `any`\> | `{}` | Additional message values. |
| `chain` | ``null`` \| [`Message`](common_web_core_messaging_Message.Message.md) | `null` | A message that acts as the *predecessor* of the new message. Used to keep the same trace for multiple messages. |

#### Returns

[`EventComposer`](common_web_core_messaging_composers_EventComposer.EventComposer.md)<`MsgType`\>

- The newly created event.

**`Throws`**

Error - If an unknown value was provided in ``values`.

#### Defined in

[src/common/web/core/messaging/composers/MessageBuilder.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageBuilder.ts#L89)

___

### getMessageCount

▸ **getMessageCount**(`counter`): `number`

Gets how many messages of specific message types have been created.

The message builder keeps track of how many messages of the three major types ``Command``, ``CommandReply`` and
``Event`` have been created.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `counter` | `string` | The message type to get the count of. Must be either ``Command``, ``CommandReply`` or ``Event``. |

#### Returns

`number`

- The number of messages already built of the specified type.

#### Defined in

[src/common/web/core/messaging/composers/MessageBuilder.ts:106](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageBuilder.ts#L106)
