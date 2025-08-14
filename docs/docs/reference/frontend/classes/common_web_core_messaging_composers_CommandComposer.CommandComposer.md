---
id: "common_web_core_messaging_composers_CommandComposer.CommandComposer"
title: "Class: CommandComposer<MsgType>"
sidebar_label: "CommandComposer"
custom_edit_url: null
---

[common/web/core/messaging/composers/CommandComposer](../modules/common_web_core_messaging_composers_CommandComposer.md).CommandComposer

Composer for ``Command`` messages.

## Type parameters

| Name | Type |
| :------ | :------ |
| `MsgType` | extends [`Command`](common_web_core_messaging_Command.Command.md) |

## Hierarchy

- [`MessageComposer`](common_web_core_messaging_composers_MessageComposer.MessageComposer.md)<`MsgType`\>

  ↳ **`CommandComposer`**

## Constructors

### constructor

• **new CommandComposer**<`MsgType`\>(`originID`, `messageBus`, `msgType`, `params?`, `chain?`): [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`MsgType`\>

#### Type parameters

| Name | Type |
| :------ | :------ |
| `MsgType` | extends [`Command`](common_web_core_messaging_Command.Command.md) |

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `originID` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | `undefined` |
| `messageBus` | [`MessageBusProtocol`](../interfaces/common_web_core_messaging_MessageBusProtocol.MessageBusProtocol.md) | `undefined` |
| `msgType` | [`ConstructableMessage`](../interfaces/common_web_core_messaging_Message.ConstructableMessage.md)<`MsgType`\> | `undefined` |
| `params` | `Record`<`string`, `any`\> | `{}` |
| `chain` | ``null`` \| [`Message`](common_web_core_messaging_Message.Message.md) | `null` |

#### Returns

[`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`MsgType`\>

#### Overrides

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[constructor](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#constructor)

#### Defined in

[src/common/web/core/messaging/composers/CommandComposer.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/CommandComposer.ts#L22)

## Properties

### \_callbacks

• `Private` **\_callbacks**: [`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<[`CommandDoneCallback`](../modules/common_web_core_messaging_CommandReply.md#commanddonecallback), [`CommandFailCallback`](../modules/common_web_core_messaging_CommandReply.md#commandfailcallback)\>

#### Defined in

[src/common/web/core/messaging/composers/CommandComposer.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/CommandComposer.ts#L18)

___

### \_chain

• `Protected` **\_chain**: ``null`` \| [`Message`](common_web_core_messaging_Message.Message.md)

#### Inherited from

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[_chain](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#_chain)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L20)

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

___

### \_timeout

• `Private` **\_timeout**: `number` = `0.0`

#### Defined in

[src/common/web/core/messaging/composers/CommandComposer.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/CommandComposer.ts#L20)

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

▸ **before**(`cb`): [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`MsgType`\>

Adds a callback that will be called immediately before the message is dispatched.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`BeforeDispatchCallback`](../modules/common_web_core_messaging_composers_MessageComposer.md#beforedispatchcallback) | The callback to add. |

#### Returns

[`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`MsgType`\>

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

[src/common/web/core/messaging/composers/CommandComposer.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/CommandComposer.ts#L76)

___

### done

▸ **done**(`cb`): [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`MsgType`\>

Adds a *Done* callback.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`CommandDoneCallback`](../modules/common_web_core_messaging_CommandReply.md#commanddonecallback) | The callback to add. |

#### Returns

[`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`MsgType`\>

- This composer instance to allow call chaining.

#### Defined in

[src/common/web/core/messaging/composers/CommandComposer.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/CommandComposer.ts#L41)

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

#### Inherited from

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[emit](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#emit)

#### Defined in

[src/common/web/core/messaging/composers/MessageComposer.ts:73](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/MessageComposer.ts#L73)

___

### failed

▸ **failed**(`cb`): [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`MsgType`\>

Adds a *Fail* callback.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`CommandFailCallback`](../modules/common_web_core_messaging_CommandReply.md#commandfailcallback) | The callback to add. |

#### Returns

[`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`MsgType`\>

- This composer instance to allow call chaining.

#### Defined in

[src/common/web/core/messaging/composers/CommandComposer.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/CommandComposer.ts#L53)

___

### timeout

▸ **timeout**(`timeout`): [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`MsgType`\>

Assigns a *Done* callback.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `timeout` | `number` | The timeout (in seconds). |

#### Returns

[`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`MsgType`\>

- This composer instance to allow call chaining.

#### Defined in

[src/common/web/core/messaging/composers/CommandComposer.ts:65](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/CommandComposer.ts#L65)

___

### verify

▸ **verify**(): `void`

#### Returns

`void`

#### Overrides

[MessageComposer](common_web_core_messaging_composers_MessageComposer.MessageComposer.md).[verify](common_web_core_messaging_composers_MessageComposer.MessageComposer.md#verify)

#### Defined in

[src/common/web/core/messaging/composers/CommandComposer.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/composers/CommandComposer.ts#L70)
