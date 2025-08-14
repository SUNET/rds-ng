---
id: "common_web_core_messaging_MessageRouter.MessageRouter"
title: "Class: MessageRouter"
sidebar_label: "MessageRouter"
custom_edit_url: null
---

[common/web/core/messaging/MessageRouter](../modules/common_web_core_messaging_MessageRouter.md).MessageRouter

Message routing rules and logic.

When a message enters the message bus, it is first checked for its validity.
Afterwards, the router decides through which channels (local, remote) it needs to be sent.

## Constructors

### constructor

• **new MessageRouter**(`compID`): [`MessageRouter`](common_web_core_messaging_MessageRouter.MessageRouter.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `compID` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | The component id (required to decide whether we match a given direct target). |

#### Returns

[`MessageRouter`](common_web_core_messaging_MessageRouter.MessageRouter.md)

#### Defined in

[src/common/web/core/messaging/MessageRouter.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageRouter.ts#L17)

## Properties

### \_compID

• `Private` `Readonly` **\_compID**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Defined in

[src/common/web/core/messaging/MessageRouter.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageRouter.ts#L12)

## Methods

### checkLocalRouting

▸ **checkLocalRouting**(`msg`, `msgMeta`): `boolean`

Checks if the message should be routed locally.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) | The message. |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) | The message meta information. |

#### Returns

`boolean`

#### Defined in

[src/common/web/core/messaging/MessageRouter.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageRouter.ts#L43)

___

### checkRemoteRouting

▸ **checkRemoteRouting**(`msg`, `msgMeta`): `boolean`

Checks if the message should be routed remotely.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) | The message. |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) | The message meta information. |

#### Returns

`boolean`

#### Defined in

[src/common/web/core/messaging/MessageRouter.ts:61](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageRouter.ts#L61)

___

### verifyDirectMessage

▸ **verifyDirectMessage**(`msg`, `msgMeta`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/MessageRouter.ts:71](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageRouter.ts#L71)

___

### verifyLocalMessage

▸ **verifyLocalMessage**(`msg`, `msgMeta`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/MessageRouter.ts:65](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageRouter.ts#L65)

___

### verifyMessage

▸ **verifyMessage**(`msg`, `msgMeta`): `void`

Verifies whether a message may enter the message bus.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) | The message that wants to enter the network engine. |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) | The message meta information. |

#### Returns

`void`

**`Throws`**

Error - In case the message is not valid to enter the message bus.

#### Defined in

[src/common/web/core/messaging/MessageRouter.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/MessageRouter.ts#L29)
