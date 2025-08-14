---
id: "common_web_core_messaging_networking_Client.Client"
title: "Class: Client"
sidebar_label: "Client"
custom_edit_url: null
---

[common/web/core/messaging/networking/Client](../modules/common_web_core_messaging_networking_Client.md).Client

The client connection, based on ``socketio``.

## Constructors

### constructor

• **new Client**(`compID`, `config`, `messageBuilder`): [`Client`](common_web_core_messaging_networking_Client.Client.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `compID` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | The component identifier. |
| `config` | [`Configuration`](common_web_utils_config_Configuration.Configuration.md) | The global configuration. |
| `messageBuilder` | [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md) | A message builder instance. |

#### Returns

[`Client`](common_web_core_messaging_networking_Client.Client.md)

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L35)

## Properties

### \_compID

• `Private` `Readonly` **\_compID**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L19)

___

### \_config

• `Private` `Readonly` **\_config**: [`Configuration`](common_web_utils_config_Configuration.Configuration.md)

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L20)

___

### \_connectionTimeout

• `Private` `Readonly` **\_connectionTimeout**: `number`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L26)

___

### \_messageBuilder

• `Private` `Readonly` **\_messageBuilder**: [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L23)

___

### \_messageHandler

• `Private` **\_messageHandler**: ``null`` \| `ClientMessageHandler` = `null`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L28)

___

### \_serverAddress

• `Private` `Readonly` **\_serverAddress**: `string`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L25)

___

### \_socket

• `Private` `Readonly` **\_socket**: `Socket`<`DefaultEventsMap`, `DefaultEventsMap`\>

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L22)

## Methods

### connectEvents

▸ **connectEvents**(): `void`

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L63)

___

### connectToServer

▸ **connectToServer**(): `void`

Establishes the connection to the server.

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:85](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L85)

___

### createSocket

▸ **createSocket**(): `Socket`<`DefaultEventsMap`, `DefaultEventsMap`\>

#### Returns

`Socket`<`DefaultEventsMap`, `DefaultEventsMap`\>

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L48)

___

### getAuthentication

▸ **getAuthentication**(): `Record`<`string`, `any`\>

#### Returns

`Record`<`string`, `any`\>

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:143](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L143)

___

### onConnect

▸ **onConnect**(): `void`

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:119](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L119)

___

### onConnectError

▸ **onConnectError**(`reason`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `reason` | `any` |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:125](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L125)

___

### onDisconnect

▸ **onDisconnect**(): `void`

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:131](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L131)

___

### onMessage

▸ **onMessage**(`msgName`, `data`, `payload`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `msgName` | `string` |
| `data` | `string` |
| `payload` | [`Payload`](../modules/common_web_core_messaging_MessagePayload.md#payload) |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:137](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L137)

___

### process

▸ **process**(): `void`

Periodically performs certain tasks.

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:80](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L80)

___

### run

▸ **run**(): `void`

Automatically connects to a server.

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:73](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L73)

___

### sendMessage

▸ **sendMessage**(`msg`): `void`

Sends a message to the server (if connected).

For this, the message will be encoded as *JSON* first.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msg` | [`Message`](common_web_core_messaging_Message.Message.md) | The message to send. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:113](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L113)

___

### setMessageHandler

▸ **setMessageHandler**(`msgHandler`): `void`

Sets a handler that gets called when a message arrives.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msgHandler` | `ClientMessageHandler` | The message handler to be called. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/networking/Client.ts:102](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/networking/Client.ts#L102)
