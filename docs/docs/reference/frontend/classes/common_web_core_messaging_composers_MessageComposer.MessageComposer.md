---
id: "common_web_core_messaging_composers_MessageComposer.MessageComposer"
title: "Class: MessageComposer<MsgType>"
sidebar_label: "MessageComposer"
custom_edit_url: null
---

[common/web/core/messaging/composers/MessageComposer](../modules/common_web_core_messaging_composers_MessageComposer.md).MessageComposer

A class to collect all information necessary to create and emit a message.

## Type parameters

| Name | Type |
| :------ | :------ |
| `MsgType` | extends [`Message`](common_web_core_messaging_Message.Message.md) |

## Hierarchy

- **`MessageComposer`**

  ↳ [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)

  ↳ [`CommandReplyComposer`](common_web_core_messaging_composers_CommandReplyComposer.CommandReplyComposer.md)

  ↳ [`EventComposer`](common_web_core_messaging_composers_EventComposer.EventComposer.md)

## Constructors

### constructor

• **new MessageComposer**<`MsgType`\>(`originID`, `messageBus`, `msgType`, `params?`, `chain?`): [`MessageComposer`](common_web_core_messaging_composers_MessageComposer.MessageComposer.md)<`MsgType`\>

#### Type parameters

| Name | Type |
| :------ | :------ |
| `MsgType` | extends [`Message`](common_web_core_messaging_Message.Message.md) |

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `originID` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | `undefined` | The component identifier of the origin of newly created messages. |
| `messageBus` | [`MessageBusProtocol`](../interfaces/common_web_core_messaging_MessageBusProtocol.MessageBusProtocol.md) | `undefined` | The global message bus to use. |
| `msgType` | [`ConstructableMessage`](../interfaces/common_web_core_messaging_Message.ConstructableMessage.md)<`MsgType`\> | `undefined` | The message type. |
| `params` | `Record`<`string`, `any`\> | `{}` | Additional message parameters. |
| `chain` | ``null`` \| [`Message`](common_web_core_messaging_Message.Message.md) | `null` | A message that acts as the *predecessor* of the new message. Used to keep the same trace for multiple messages. |

#### Returns

[`MessageComposer`](common_web_core_messaging_composers_MessageComposer.MessageComposer.md)<`MsgType`\>

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L31)

## Properties

### \_beforeCallbacks

• `Private` **\_beforeCallbacks**: [`BeforeDispatchCallback`](../modules/common_web_core_messaging_composers_MessageComposer.md#beforedispatchcallback)[] = `[]`

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L22)

___

### \_chain

• `Protected` **\_chain**: ``null`` \| [`Message`](common_web_core_messaging_Message.Message.md)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L20)

___

### \_messageBus

• `Protected` **\_messageBus**: [`MessageBusProtocol`](../interfaces/common_web_core_messaging_MessageBusProtocol.MessageBusProtocol.md)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L15)

___

### \_msgType

• `Protected` **\_msgType**: [`ConstructableMessage`](../interfaces/common_web_core_messaging_Message.ConstructableMessage.md)<`MsgType`\>

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L17)

___

### \_originID

• `Protected` **\_originID**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L14)

___

### \_params

• `Protected` **\_params**: `Record`<`string`, `any`\>

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L18)

___

### \_payload

• `Protected` **\_payload**: [`Payload`](../modules/common_web_core_messaging_MessagePayload.md#payload) = `{}`

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L19)

## Methods

### addPayload

▸ **addPayload**(`key`, `data`): `void`

Adds a payload item to the message.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `key` | `string` | The item key. |
| `data` | `any` | The item data. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L52)

___

### before

▸ **before**(`cb`): [`MessageComposer`](common_web_core_messaging_composers_MessageComposer.MessageComposer.md)<`MsgType`\>

Adds a callback that will be called immediately before the message is dispatched.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`BeforeDispatchCallback`](../modules/common_web_core_messaging_composers_MessageComposer.md#beforedispatchcallback) | The callback to add. |

#### Returns

[`MessageComposer`](common_web_core_messaging_composers_MessageComposer.MessageComposer.md)<`MsgType`\>

- This composer instance to allow call chaining.

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L63)

___

### compose

▸ **compose**(): `void`

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L89)

___

### createMessage

▸ **createMessage**(`target`): [`Message`](common_web_core_messaging_Message.Message.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `target` | [`Channel`](common_web_core_messaging_Channel.Channel.md) |

#### Returns

[`Message`](common_web_core_messaging_Message.Message.md)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:93](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L93)

___

### createMetaInformation

▸ **createMetaInformation**(): [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

#### Returns

[`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:91](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L91)

___

### emit

▸ **emit**(`target`): `void`

Sends the built message through the message bus.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `target` | [`Channel`](common_web_core_messaging_Channel.Channel.md) | The target of the message. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:73](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L73)

___

### verify

▸ **verify**(): `void`

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:87](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L87)
