---
id: "common_web_api_project_ProjectCommands.UpdateProjectCommand"
title: "Class: UpdateProjectCommand"
sidebar_label: "UpdateProjectCommand"
custom_edit_url: null
---

[common/web/api/project/ProjectCommands](../modules/common_web_api_project_ProjectCommands.md).UpdateProjectCommand

Command to update a project. Requires an ``UpdateProjectReply`` reply.
Note that the project features are updated using a separate ``UpdateProjectFeaturesCommand`` message.

**`Param`**

The ID of the project to update.

**`Param`**

The title of the project.

**`Param`**

An optional project description.

**`Param`**

The project options.

## Hierarchy

- [`Command`](common_web_core_messaging_Command.Command.md)

  ↳ **`UpdateProjectCommand`**

## Constructors

### constructor

• **new UpdateProjectCommand**(`name`, `origin`, `sender`, `target`, `hops?`, `trace?`, `apiKey?`): [`UpdateProjectCommand`](common_web_api_project_ProjectCommands.UpdateProjectCommand.md)

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

[`UpdateProjectCommand`](common_web_api_project_ProjectCommands.UpdateProjectCommand.md)

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

### description

• `Readonly` **description**: `string` = `""`

#### Defined in

[src/common/web/api/project/ProjectCommands.ts:127](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/project/ProjectCommands.ts#L127)

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

### options

• `Readonly` **options**: [`ProjectOptions`](common_web_data_entities_project_ProjectOptions.ProjectOptions.md)

#### Defined in

[src/common/web/api/project/ProjectCommands.ts:131](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/project/ProjectCommands.ts#L131)

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

### project\_id

• `Readonly` **project\_id**: `number` = `0`

#### Defined in

[src/common/web/api/project/ProjectCommands.ts:124](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/project/ProjectCommands.ts#L124)

___

### sender

• `Readonly` **sender**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[sender](common_web_core_messaging_Command.Command.md#sender)

#### Defined in

[src/common/web/core/messaging/Message.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L39)

___

### target

• `Readonly` **target**: [`Channel`](common_web_core_messaging_Channel.Channel.md)

#### Inherited from

[Command](common_web_core_messaging_Command.Command.md).[target](common_web_core_messaging_Command.Command.md#target)

#### Defined in

[src/common/web/core/messaging/Message.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L42)

___

### title

• `Readonly` **title**: `string` = `""`

#### Defined in

[src/common/web/api/project/ProjectCommands.ts:126](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/project/ProjectCommands.ts#L126)

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

▸ **build**(`messageBuilder`, `project_id`, `title`, `description`, `options`, `chain?`): [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<[`UpdateProjectCommand`](common_web_api_project_ProjectCommands.UpdateProjectCommand.md)\>

Helper function to easily build this message.

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `messageBuilder` | [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md) | `undefined` |
| `project_id` | `number` | `undefined` |
| `title` | `string` | `undefined` |
| `description` | `string` | `undefined` |
| `options` | [`ProjectOptions`](common_web_data_entities_project_ProjectOptions.ProjectOptions.md) | `undefined` |
| `chain` | ``null`` \| [`Message`](common_web_core_messaging_Message.Message.md) | `null` |

#### Returns

[`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<[`UpdateProjectCommand`](common_web_api_project_ProjectCommands.UpdateProjectCommand.md)\>

#### Defined in

[src/common/web/api/project/ProjectCommands.ts:136](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/project/ProjectCommands.ts#L136)

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
