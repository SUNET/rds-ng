---
id: "common_web_api_metadata_MetadataCommands.GetMetadataProfilesReply"
title: "Class: GetMetadataProfilesReply"
sidebar_label: "GetMetadataProfilesReply"
custom_edit_url: null
---

[common/web/api/metadata/MetadataCommands](../modules/common_web_api_metadata_MetadataCommands.md).GetMetadataProfilesReply

Reply to ``GetMetadataProfilesCommand``.

**`Param`**

List of all global profiles.

## Hierarchy

- [`CommandReply`](common_web_core_messaging_CommandReply.CommandReply.md)

  ↳ **`GetMetadataProfilesReply`**

## Constructors

### constructor

• **new GetMetadataProfilesReply**(`name`, `origin`, `sender`, `target`, `hops?`, `trace?`, `apiKey?`): [`GetMetadataProfilesReply`](common_web_api_metadata_MetadataCommands.GetMetadataProfilesReply.md)

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

[`GetMetadataProfilesReply`](common_web_api_metadata_MetadataCommands.GetMetadataProfilesReply.md)

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[constructor](common_web_core_messaging_CommandReply.CommandReply.md#constructor)

#### Defined in

[src/common/web/core/messaging/Message.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L63)

## Properties

### api\_key

• `Readonly` **api\_key**: `string` = `""`

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[api_key](common_web_core_messaging_CommandReply.CommandReply.md#api_key)

#### Defined in

[src/common/web/core/messaging/Message.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L50)

___

### hops

• `Readonly` **hops**: [`UnitID`](common_web_utils_UnitID.UnitID.md)[] = `[]`

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[hops](common_web_core_messaging_CommandReply.CommandReply.md#hops)

#### Defined in

[src/common/web/core/messaging/Message.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L46)

___

### message

• `Readonly` **message**: `string` = `""`

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[message](common_web_core_messaging_CommandReply.CommandReply.md#message)

#### Defined in

[src/common/web/core/messaging/CommandReply.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/CommandReply.ts#L27)

___

### name

• `Readonly` **name**: `string`

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[name](common_web_core_messaging_CommandReply.CommandReply.md#name)

#### Defined in

[src/common/web/core/messaging/Message.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L33)

___

### origin

• `Readonly` **origin**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[origin](common_web_core_messaging_CommandReply.CommandReply.md#origin)

#### Defined in

[src/common/web/core/messaging/Message.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L36)

___

### payload

• `Readonly` **payload**: [`MessagePayload`](common_web_core_messaging_MessagePayload.MessagePayload.md)

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[payload](common_web_core_messaging_CommandReply.CommandReply.md#payload)

#### Defined in

[src/common/web/core/messaging/Message.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L52)

___

### profiles

• `Readonly` **profiles**: [`MetadataProfileContainerList`](../modules/common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist) = `[]`

#### Defined in

[src/common/web/api/metadata/MetadataCommands.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/metadata/MetadataCommands.ts#L33)

___

### sender

• `Readonly` **sender**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[sender](common_web_core_messaging_CommandReply.CommandReply.md#sender)

#### Defined in

[src/common/web/core/messaging/Message.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L39)

___

### success

• `Readonly` **success**: `boolean` = `true`

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[success](common_web_core_messaging_CommandReply.CommandReply.md#success)

#### Defined in

[src/common/web/core/messaging/CommandReply.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/CommandReply.ts#L26)

___

### target

• `Readonly` **target**: [`Channel`](common_web_core_messaging_Channel.Channel.md)

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[target](common_web_core_messaging_CommandReply.CommandReply.md#target)

#### Defined in

[src/common/web/core/messaging/Message.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L42)

___

### trace

• `Readonly` **trace**: `string` = `""`

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[trace](common_web_core_messaging_CommandReply.CommandReply.md#trace)

#### Defined in

[src/common/web/core/messaging/Message.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L48)

___

### unique

• `Readonly` **unique**: `string`

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[unique](common_web_core_messaging_CommandReply.CommandReply.md#unique)

#### Defined in

[src/common/web/core/messaging/CommandReply.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/CommandReply.ts#L29)

___

### Category

▪ `Static` `Readonly` **Category**: `string` = `"CommandReply"`

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[Category](common_web_core_messaging_CommandReply.CommandReply.md#category)

#### Defined in

[src/common/web/core/messaging/CommandReply.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/CommandReply.ts#L24)

## Accessors

### messageCategory

• `get` **messageCategory**(): `string`

Gets the global message category.

#### Returns

`string`

#### Inherited from

CommandReply.messageCategory

#### Defined in

[src/common/web/core/messaging/CommandReply.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/CommandReply.ts#L34)

## Methods

### convertToJSON

▸ **convertToJSON**(): `string`

Converts this message to JSON.

#### Returns

`string`

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[convertToJSON](common_web_core_messaging_CommandReply.CommandReply.md#converttojson)

#### Defined in

[src/common/web/core/messaging/Message.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L76)

___

### toString

▸ **toString**(): `string`

Gets the string representation of this message.

#### Returns

`string`

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[toString](common_web_core_messaging_CommandReply.CommandReply.md#tostring)

#### Defined in

[src/common/web/core/messaging/Message.ts:154](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L154)

___

### build

▸ **build**(`messageBuilder`, `cmd`, `profiles`, `success?`, `message?`): [`CommandReplyComposer`](common_web_core_messaging_composers_CommandReplyComposer.CommandReplyComposer.md)<[`GetMetadataProfilesReply`](common_web_api_metadata_MetadataCommands.GetMetadataProfilesReply.md)\>

Helper function to easily build this message.

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `messageBuilder` | [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md) | `undefined` |
| `cmd` | [`GetMetadataProfilesCommand`](common_web_api_metadata_MetadataCommands.GetMetadataProfilesCommand.md) | `undefined` |
| `profiles` | [`MetadataProfileContainerList`](../modules/common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist) | `undefined` |
| `success` | `boolean` | `true` |
| `message` | `string` | `""` |

#### Returns

[`CommandReplyComposer`](common_web_core_messaging_composers_CommandReplyComposer.CommandReplyComposer.md)<[`GetMetadataProfilesReply`](common_web_api_metadata_MetadataCommands.GetMetadataProfilesReply.md)\>

#### Defined in

[src/common/web/api/metadata/MetadataCommands.ts:38](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/metadata/MetadataCommands.ts#L38)

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

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[convertFromJSON](common_web_core_messaging_CommandReply.CommandReply.md#convertfromjson)

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

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[define](common_web_core_messaging_CommandReply.CommandReply.md#define)

#### Defined in

[src/common/web/core/messaging/Message.ts:128](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L128)

___

### isProtected

▸ **isProtected**(): `boolean`

The frontend never receives or issues protected messages.

#### Returns

`boolean`

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[isProtected](common_web_core_messaging_CommandReply.CommandReply.md#isprotected)

#### Defined in

[src/common/web/core/messaging/Message.ts:108](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L108)

___

### messageName

▸ **messageName**(): `string`

Retrieves the name of the message type on a message class basis.

#### Returns

`string`

#### Inherited from

[CommandReply](common_web_core_messaging_CommandReply.CommandReply.md).[messageName](common_web_core_messaging_CommandReply.CommandReply.md#messagename)

#### Defined in

[src/common/web/core/messaging/Message.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L101)
