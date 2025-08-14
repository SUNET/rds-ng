---
id: "common_web_api_project_ProjectJobEvents.ProjectJobCompletionEvent"
title: "Class: ProjectJobCompletionEvent"
sidebar_label: "ProjectJobCompletionEvent"
custom_edit_url: null
---

[common/web/api/project/ProjectJobEvents](../modules/common_web_api_project_ProjectJobEvents.md).ProjectJobCompletionEvent

Emitted to inform about the completion (either succeeded or failed) of a job.

**`Param`**

The project ID.

**`Param`**

The connector instance ID.

**`Param`**

The success status (done or failed).

**`Param`**

An optional message (usually in case of an error).

## Hierarchy

- [`Event`](common_web_core_messaging_Event.Event.md)

  ↳ **`ProjectJobCompletionEvent`**

## Constructors

### constructor

• **new ProjectJobCompletionEvent**(`name`, `origin`, `sender`, `target`, `hops?`, `trace?`, `apiKey?`): [`ProjectJobCompletionEvent`](common_web_api_project_ProjectJobEvents.ProjectJobCompletionEvent.md)

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

[`ProjectJobCompletionEvent`](common_web_api_project_ProjectJobEvents.ProjectJobCompletionEvent.md)

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[constructor](common_web_core_messaging_Event.Event.md#constructor)

#### Defined in

[src/common/web/core/messaging/Message.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L63)

## Properties

### api\_key

• `Readonly` **api\_key**: `string` = `""`

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[api_key](common_web_core_messaging_Event.Event.md#api_key)

#### Defined in

[src/common/web/core/messaging/Message.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L50)

___

### connector\_instance

• `Readonly` **connector\_instance**: `string` = `""`

#### Defined in

[src/common/web/api/project/ProjectJobEvents.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/project/ProjectJobEvents.ts#L89)

___

### ext\_data

• `Readonly` **ext\_data**: [`ProjectJobHistoryRecordExtData`](../modules/common_web_data_entities_project_logbook_ProjectJobHistoryRecord.md#projectjobhistoryrecordextdata) = `{}`

#### Defined in

[src/common/web/api/project/ProjectJobEvents.ts:94](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/project/ProjectJobEvents.ts#L94)

___

### hops

• `Readonly` **hops**: [`UnitID`](common_web_utils_UnitID.UnitID.md)[] = `[]`

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[hops](common_web_core_messaging_Event.Event.md#hops)

#### Defined in

[src/common/web/core/messaging/Message.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L46)

___

### message

• `Readonly` **message**: `string` = `""`

#### Defined in

[src/common/web/api/project/ProjectJobEvents.ts:92](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/project/ProjectJobEvents.ts#L92)

___

### name

• `Readonly` **name**: `string`

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[name](common_web_core_messaging_Event.Event.md#name)

#### Defined in

[src/common/web/core/messaging/Message.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L33)

___

### origin

• `Readonly` **origin**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[origin](common_web_core_messaging_Event.Event.md#origin)

#### Defined in

[src/common/web/core/messaging/Message.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L36)

___

### payload

• `Readonly` **payload**: [`MessagePayload`](common_web_core_messaging_MessagePayload.MessagePayload.md)

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[payload](common_web_core_messaging_Event.Event.md#payload)

#### Defined in

[src/common/web/core/messaging/Message.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L52)

___

### project\_id

• `Readonly` **project\_id**: `number` = `0`

#### Defined in

[src/common/web/api/project/ProjectJobEvents.ts:88](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/project/ProjectJobEvents.ts#L88)

___

### sender

• `Readonly` **sender**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[sender](common_web_core_messaging_Event.Event.md#sender)

#### Defined in

[src/common/web/core/messaging/Message.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L39)

___

### success

• `Readonly` **success**: `boolean` = `true`

#### Defined in

[src/common/web/api/project/ProjectJobEvents.ts:91](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/project/ProjectJobEvents.ts#L91)

___

### target

• `Readonly` **target**: [`Channel`](common_web_core_messaging_Channel.Channel.md)

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[target](common_web_core_messaging_Event.Event.md#target)

#### Defined in

[src/common/web/core/messaging/Message.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L42)

___

### trace

• `Readonly` **trace**: `string` = `""`

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[trace](common_web_core_messaging_Event.Event.md#trace)

#### Defined in

[src/common/web/core/messaging/Message.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L48)

___

### Category

▪ `Static` `Readonly` **Category**: `string` = `"Event"`

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[Category](common_web_core_messaging_Event.Event.md#category)

#### Defined in

[src/common/web/core/messaging/Event.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Event.ts#L9)

## Accessors

### messageCategory

• `get` **messageCategory**(): `string`

Gets the global message category.

#### Returns

`string`

#### Inherited from

Event.messageCategory

#### Defined in

[src/common/web/core/messaging/Event.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Event.ts#L14)

## Methods

### convertToJSON

▸ **convertToJSON**(): `string`

Converts this message to JSON.

#### Returns

`string`

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[convertToJSON](common_web_core_messaging_Event.Event.md#converttojson)

#### Defined in

[src/common/web/core/messaging/Message.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L76)

___

### toString

▸ **toString**(): `string`

Gets the string representation of this message.

#### Returns

`string`

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[toString](common_web_core_messaging_Event.Event.md#tostring)

#### Defined in

[src/common/web/core/messaging/Message.ts:154](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L154)

___

### build

▸ **build**(`messageBuilder`, `projectID`, `connectorInstance`, `success`, `message?`, `extData?`, `chain?`): [`EventComposer`](common_web_core_messaging_composers_EventComposer.EventComposer.md)<[`ProjectJobCompletionEvent`](common_web_api_project_ProjectJobEvents.ProjectJobCompletionEvent.md)\>

Helper function to easily build this message.

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `messageBuilder` | [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md) | `undefined` |
| `projectID` | `number` | `undefined` |
| `connectorInstance` | `string` | `undefined` |
| `success` | `boolean` | `undefined` |
| `message` | `string` | `""` |
| `extData` | [`ProjectJobHistoryRecordExtData`](../modules/common_web_data_entities_project_logbook_ProjectJobHistoryRecord.md#projectjobhistoryrecordextdata) | `{}` |
| `chain` | ``null`` \| [`Message`](common_web_core_messaging_Message.Message.md) | `null` |

#### Returns

[`EventComposer`](common_web_core_messaging_composers_EventComposer.EventComposer.md)<[`ProjectJobCompletionEvent`](common_web_api_project_ProjectJobEvents.ProjectJobCompletionEvent.md)\>

#### Defined in

[src/common/web/api/project/ProjectJobEvents.ts:99](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/api/project/ProjectJobEvents.ts#L99)

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

[Event](common_web_core_messaging_Event.Event.md).[convertFromJSON](common_web_core_messaging_Event.Event.md#convertfromjson)

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

[Event](common_web_core_messaging_Event.Event.md).[define](common_web_core_messaging_Event.Event.md#define)

#### Defined in

[src/common/web/core/messaging/Message.ts:128](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L128)

___

### isProtected

▸ **isProtected**(): `boolean`

The frontend never receives or issues protected messages.

#### Returns

`boolean`

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[isProtected](common_web_core_messaging_Event.Event.md#isprotected)

#### Defined in

[src/common/web/core/messaging/Message.ts:108](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L108)

___

### messageName

▸ **messageName**(): `string`

Retrieves the name of the message type on a message class basis.

#### Returns

`string`

#### Inherited from

[Event](common_web_core_messaging_Event.Event.md).[messageName](common_web_core_messaging_Event.Event.md#messagename)

#### Defined in

[src/common/web/core/messaging/Message.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L101)
