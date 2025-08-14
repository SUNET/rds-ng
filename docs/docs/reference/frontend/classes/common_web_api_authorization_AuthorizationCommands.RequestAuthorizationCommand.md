---
id: "common_web_api_authorization_AuthorizationCommands.RequestAuthorizationCommand"
title: "Class: RequestAuthorizationCommand"
sidebar_label: "RequestAuthorizationCommand"
custom_edit_url: null
---

[common/web/api/authorization/AuthorizationCommands](../modules/common_web_api_authorization_AuthorizationCommands.md).RequestAuthorizationCommand

Command to perform an authorization request. Requires a ``RequestAuthorizationReply`` reply.

**`Param`**

The authorization request information.

**`Param`**

The token strategy (e.g., OAuth2).

**`Param`**

The actual token request data.

## Hierarchy

- [`Command`](common_web_core_messaging_Command.Command.md)

  ↳ **`RequestAuthorizationCommand`**

## Constructors

### constructor

• **new RequestAuthorizationCommand**(`name`, `origin`, `sender`, `target`, `hops?`, `trace?`, `apiKey?`): [`RequestAuthorizationCommand`](common_web_api_authorization_AuthorizationCommands.RequestAuthorizationCommand.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `name` | `string` | `undefined` | The name of the message. |
| `origin` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | `undefined` | The initial source component of the message. |
| `sender` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | `undefined` | The component from where the message came from. |
| `target` | [`Channel`](common_web_core_messaging_Channel.Channel.md) | `undefined` | Where the message should go to. |
| `hops` | [`UnitID`](common_web_utils_UnitID.UnitID.md)[] | `[]` | A list of components the message was sent through. |
| `trace` | `string` | `undefined` | A unique trace identifying messages that logically belong together. |
| `apiKey` | `string` | `""` | An optional API key to access protected resources. |

#### Returns

[`RequestAuthorizationCommand`](common_web_api_authorization_AuthorizationCommands.RequestAuthorizationCommand.md)

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[constructor](common_web_core_messaging_Command.Command.md#constructor)

#### Defined in

[src/common/web/core/messaging/Message.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L63)

## Properties

### api\_key

• `Readonly` **api\_key**: `string` = `""`

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[api_key](common_web_core_messaging_Command.Command.md#api_key)

#### Defined in

[src/common/web/core/messaging/Message.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L50)

___

### data

• `Readonly` **data**: `any` = `null`

#### Defined in

[src/common/web/api/authorization/AuthorizationCommands.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/authorization/AuthorizationCommands.ts#L28)

___

### hops

• `Readonly` **hops**: [`UnitID`](common_web_utils_UnitID.UnitID.md)[] = `[]`

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[hops](common_web_core_messaging_Command.Command.md#hops)

#### Defined in

[src/common/web/core/messaging/Message.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L46)

___

### name

• `Readonly` **name**: `string`

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[name](common_web_core_messaging_Command.Command.md#name)

#### Defined in

[src/common/web/core/messaging/Message.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L33)

___

### origin

• `Readonly` **origin**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[origin](common_web_core_messaging_Command.Command.md#origin)

#### Defined in

[src/common/web/core/messaging/Message.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L36)

___

### payload

• `Readonly` **payload**: [`MessagePayload`](common_web_core_messaging_MessagePayload.MessagePayload.md)

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[payload](common_web_core_messaging_Command.Command.md#payload)

#### Defined in

[src/common/web/core/messaging/Message.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L52)

___

### request\_payload

• `Readonly` **request\_payload**: [`AuthorizationRequestPayload`](../interfaces/common_web_integration_authorization_AuthorizationRequest.AuthorizationRequestPayload.md)

#### Defined in

[src/common/web/api/authorization/AuthorizationCommands.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/authorization/AuthorizationCommands.ts#L20)

___

### sender

• `Readonly` **sender**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[sender](common_web_core_messaging_Command.Command.md#sender)

#### Defined in

[src/common/web/core/messaging/Message.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L39)

___

### strategy

• `Readonly` **strategy**: `string` = `""`

#### Defined in

[src/common/web/api/authorization/AuthorizationCommands.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/authorization/AuthorizationCommands.ts#L27)

___

### target

• `Readonly` **target**: [`Channel`](common_web_core_messaging_Channel.Channel.md)

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[target](common_web_core_messaging_Command.Command.md#target)

#### Defined in

[src/common/web/core/messaging/Message.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L42)

___

### trace

• `Readonly` **trace**: `string` = `""`

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[trace](common_web_core_messaging_Command.Command.md#trace)

#### Defined in

[src/common/web/core/messaging/Message.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L48)

___

### unique

• `Readonly` **unique**: `string`

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[unique](common_web_core_messaging_Command.Command.md#unique)

#### Defined in

[src/common/web/core/messaging/Command.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Command.ts#L17)

___

### Category

▪ `Static` `Readonly` **Category**: `string` = `"Command"`

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[Category](common_web_core_messaging_Command.Command.md#category)

#### Defined in

[src/common/web/core/messaging/Command.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Command.ts#L15)

## Accessors

### messageCategory

• `get` **messageCategory**(): `string`

Gets the global message category.

#### Returns

`string`

#### Inherited from

Command.messageCategory

#### Defined in

[src/common/web/core/messaging/Command.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Command.ts#L22)

## Methods

### convertToJSON

▸ **convertToJSON**(): `string`

Converts this message to JSON.

#### Returns

`string`

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[convertToJSON](common_web_core_messaging_Command.Command.md#converttojson)

#### Defined in

[src/common/web/core/messaging/Message.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L76)

___

### toString

▸ **toString**(): `string`

Gets the string representation of this message.

#### Returns

`string`

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[toString](common_web_core_messaging_Command.Command.md#tostring)

#### Defined in

[src/common/web/core/messaging/Message.ts:154](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L154)

___

### build

▸ **build**(`messageBuilder`, `request_payload`, `strategy`, `data`, `chain?`): [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<[`RequestAuthorizationCommand`](common_web_api_authorization_AuthorizationCommands.RequestAuthorizationCommand.md)\>

Helper function to easily build this message.

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `messageBuilder` | [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md) | `undefined` |
| `request_payload` | [`AuthorizationRequestPayload`](../interfaces/common_web_integration_authorization_AuthorizationRequest.AuthorizationRequestPayload.md) | `undefined` |
| `strategy` | `string` | `undefined` |
| `data` | `any` | `undefined` |
| `chain` | ``null`` \| [`Message`](common_web_core_messaging_Message.Message.md) | `null` |

#### Returns

[`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<[`RequestAuthorizationCommand`](common_web_api_authorization_AuthorizationCommands.RequestAuthorizationCommand.md)\>

#### Defined in

[src/common/web/api/authorization/AuthorizationCommands.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/authorization/AuthorizationCommands.ts#L33)

___

### convertFromJSON

▸ **convertFromJSON**(`msgType`, `data`): [`Message`](common_web_core_messaging_Message.Message.md)

Creates a message from JSON data.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msgType` | [`ConstructableMessage`](../interfaces/common_web_core_messaging_Message.ConstructableMessage.md)<[`Message`](common_web_core_messaging_Message.Message.md)\> | The message type to construct. |
| `data` | `string` | The JSON data string. |

#### Returns

[`Message`](common_web_core_messaging_Message.Message.md)

- The created message.

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[convertFromJSON](common_web_core_messaging_Command.Command.md#convertfromjson)

#### Defined in

[src/common/web/core/messaging/Message.ts:93](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L93)

___

### define

▸ **define**(`name`): `Function`

Defines a new message.

The decorator takes care of wrapping the new class as a dataclass, passing the correct message
name to its constructor. It also registers the new message type in the global ``MessageTypesCatalog``.

Examples:
```
    @Message.define("msg/command")
    class MyCommand extends Command {
        ...
    }
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | The name of the message. |

#### Returns

`Function`

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[define](common_web_core_messaging_Command.Command.md#define)

#### Defined in

[src/common/web/core/messaging/Message.ts:128](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L128)

___

### isProtected

▸ **isProtected**(): `boolean`

The frontend never receives or issues protected messages.

#### Returns

`boolean`

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[isProtected](common_web_core_messaging_Command.Command.md#isprotected)

#### Defined in

[src/common/web/core/messaging/Message.ts:108](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L108)

___

### messageName

▸ **messageName**(): `string`

Retrieves the name of the message type on a message class basis.

#### Returns

`string`

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[messageName](common_web_core_messaging_Command.Command.md#messagename)

#### Defined in

[src/common/web/core/messaging/Message.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L101)
