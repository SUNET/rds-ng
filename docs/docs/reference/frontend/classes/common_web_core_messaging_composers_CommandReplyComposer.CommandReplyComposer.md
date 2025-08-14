---
id: "common_web_core_messaging_composers_CommandReplyComposer.CommandReplyComposer"
title: "Class: CommandReplyComposer<MsgType>"
sidebar_label: "CommandReplyComposer"
custom_edit_url: null
---

[common/web/core/messaging/composers/CommandReplyComposer](../modules/common_web_core_messaging_composers_CommandReplyComposer.md).CommandReplyComposer

Composer for ``CommandReply`` messages.

## Type parameters

| Name | Type |
| :------ | :------ |
| `MsgType` | extends [`CommandReply`](common_web_core_messaging_CommandReply.CommandReply.md) |

## Hierarchy

- [`MessageComposer`](common_web_core_messaging_composers_MessageComposer.MessageComposer.md)<`MsgType`\>

  ↳ **`CommandReplyComposer`**

## Constructors

### constructor

• **new CommandReplyComposer**<`MsgType`\>(`originID`, `messageBus`, `msgType`, `cmd`, `params?`): [`CommandReplyComposer`](common_web_core_messaging_composers_CommandReplyComposer.CommandReplyComposer.md)<`MsgType`\>

#### Type parameters

| Name | Type |
| :------ | :------ |
| `MsgType` | extends [`CommandReply`](common_web_core_messaging_CommandReply.CommandReply.md) |

#### Parameters

| Name | Type |
| :------ | :------ |
| `originID` | [`UnitID`](common_web_utils_UnitID.UnitID.md) |
| `messageBus` | [`MessageBusProtocol`](../interfaces/common_web_core_messaging_MessageBusProtocol.MessageBusProtocol.md) |
| `msgType` | [`ConstructableMessage`](../interfaces/common_web_core_messaging_Message.ConstructableMessage.md)<`MsgType`\> |
| `cmd` | [`Command`](common_web_core_messaging_Command.Command.md) |
| `params` | `Record`<`string`, `any`\> |

#### Returns

[`CommandReplyComposer`](common_web_core_messaging_composers_CommandReplyComposer.CommandReplyComposer.md)<`MsgType`\>

#### Overrides

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[constructor](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#constructor)

#### Defined in

[src/common/web/core/messaging/composers/CommandReplyComposer.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/CommandReplyComposer.ts#L17)

## Properties

### \_chain

• `Protected` **\_chain**: ``null`` \| [`Message`](common_web_core_messaging_Message.Message.md)

#### Inherited from

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[_chain](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#_chain)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L20)

___

### \_command

• `Private` `Readonly` **\_command**: [`Command`](common_web_core_messaging_Command.Command.md)

#### Defined in

[src/common/web/core/messaging/composers/CommandReplyComposer.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/CommandReplyComposer.ts#L15)

___

### \_messageBus

• `Protected` **\_messageBus**: [`MessageBusProtocol`](../interfaces/common_web_core_messaging_MessageBusProtocol.MessageBusProtocol.md)

#### Inherited from

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[_messageBus](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#_messagebus)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L15)

___

### \_msgType

• `Protected` **\_msgType**: [`ConstructableMessage`](../interfaces/common_web_core_messaging_Message.ConstructableMessage.md)<`MsgType`\>

#### Inherited from

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[_msgType](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#_msgtype)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L17)

___

### \_originID

• `Protected` **\_originID**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Inherited from

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[_originID](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#_originid)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L14)

___

### \_params

• `Protected` **\_params**: `Record`<`string`, `any`\>

#### Inherited from

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[_params](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#_params)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L18)

___

### \_payload

• `Protected` **\_payload**: [`Payload`](../modules/common_web_core_messaging_MessagePayload.md#payload) = `{}`

#### Inherited from

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[_payload](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#_payload)

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

#### Inherited from

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[addPayload](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#addpayload)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L52)

___

### before

▸ **before**(`cb`): [`CommandReplyComposer`](common_web_core_messaging_composers_CommandReplyComposer.CommandReplyComposer.md)<`MsgType`\>

Adds a callback that will be called immediately before the message is dispatched.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`BeforeDispatchCallback`](../modules/common_web_core_messaging_composers_MessageComposer.md#beforedispatchcallback) | The callback to add. |

#### Returns

[`CommandReplyComposer`](common_web_core_messaging_composers_CommandReplyComposer.CommandReplyComposer.md)<`MsgType`\>

- This composer instance to allow call chaining.

#### Inherited from

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[before](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#before)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L63)

___

### compose

▸ **compose**(): `void`

#### Returns

`void`

#### Inherited from

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[compose](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#compose)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L89)

___

### createMetaInformation

▸ **createMetaInformation**(): [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

#### Returns

[`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

#### Overrides

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[createMetaInformation](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#createmetainformation)

#### Defined in

[src/common/web/core/messaging/composers/CommandReplyComposer.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/CommandReplyComposer.ts#L32)

___

### emit

▸ **emit**(): `void`

Sends the built message through the message bus.

#### Returns

`void`

#### Overrides

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[emit](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#emit)

#### Defined in

[src/common/web/core/messaging/composers/CommandReplyComposer.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/CommandReplyComposer.ts#L27)

___

### verify

▸ **verify**(): `void`

#### Returns

`void`

#### Inherited from

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[verify](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#verify)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:87](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L87)
