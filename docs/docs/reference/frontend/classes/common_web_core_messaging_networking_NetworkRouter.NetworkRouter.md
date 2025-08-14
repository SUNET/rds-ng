---
id: "common_web_core_messaging_networking_NetworkRouter.NetworkRouter"
title: "Class: NetworkRouter"
sidebar_label: "NetworkRouter"
custom_edit_url: null
---

[common/web/core/messaging/networking/NetworkRouter](../modules/common_web_core_messaging_networking_NetworkRouter.md).NetworkRouter

Network routing rules and logic.

When a message enters the network engine in order to be sent to remote targets, it is first checked for its
validity. Afterwards, the router decides through which channels (local, client) it needs to be sent.

## Constructors

### constructor

• **new NetworkRouter**(`compID`): [`NetworkRouter`](common_web_core_messaging_networking_NetworkRouter.NetworkRouter.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `compID` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | The component id (required to decide whether we match a given direct target). |

#### Returns

[`NetworkRouter`](common_web_core_messaging_networking_NetworkRouter.NetworkRouter.md)

#### Defined in

[src/common/web/core/messaging/networking/NetworkRouter.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/NetworkRouter.ts#L25)

## Properties

### \_compID

• `Private` `Readonly` **\_compID**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Defined in

[src/common/web/core/messaging/networking/NetworkRouter.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/NetworkRouter.ts#L20)

## Methods

### checkClientRouting

▸ **checkClientRouting**(`direction`, `msg`, `msgMeta`): `boolean`

Checks if the message should be routed through the client.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `direction` | [`NetworkRouterDirection`](../enums/common_web_core_messaging_networking_NetworkRouter.NetworkRouterDirection.md) | The direction (*IN* or *OUT*) of the message. |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) | The actual message. |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) | The message meta information. |

#### Returns

`boolean`

Whether client routing should happen.

#### Defined in

[src/common/web/core/messaging/networking/NetworkRouter.ts:75](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/NetworkRouter.ts#L75)

___

### checkLocalRouting

▸ **checkLocalRouting**(`direction`, `msg`, `msgMeta`): `boolean`

Checks if the message should be routed locally (dispatched via the message bus).

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `direction` | [`NetworkRouterDirection`](../enums/common_web_core_messaging_networking_NetworkRouter.NetworkRouterDirection.md) | The direction (*IN* or *OUT*) of the message. |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) | The actual message. |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) | The message meta information. |

#### Returns

`boolean`

Whether local routing should happen.

#### Defined in

[src/common/web/core/messaging/networking/NetworkRouter.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/NetworkRouter.ts#L54)

___

### verifyDirectMessage

▸ **verifyDirectMessage**(`direction`, `msg`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `direction` | [`NetworkRouterDirection`](../enums/common_web_core_messaging_networking_NetworkRouter.NetworkRouterDirection.md) |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/networking/NetworkRouter.ts:85](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/NetworkRouter.ts#L85)

___

### verifyLocalMessage

▸ **verifyLocalMessage**(`direction`, `msg`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `direction` | [`NetworkRouterDirection`](../enums/common_web_core_messaging_networking_NetworkRouter.NetworkRouterDirection.md) |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/networking/NetworkRouter.ts:80](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/NetworkRouter.ts#L80)

___

### verifyMessage

▸ **verifyMessage**(`direction`, `msg`): `void`

Verifies whether a message may enter the network engine.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `direction` | [`NetworkRouterDirection`](../enums/common_web_core_messaging_networking_NetworkRouter.NetworkRouterDirection.md) | The direction (*IN* or *OUT*) of the message. |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) | The message that wants to enter the network engine. |

#### Returns

`void`

**`Throws`**

Error - In case the message is not valid to enter the network engine.

#### Defined in

[src/common/web/core/messaging/networking/NetworkRouter.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/NetworkRouter.ts#L37)
