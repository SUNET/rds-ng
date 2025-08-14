---
id: "common_web_core_messaging_Event.Event"
title: "Class: Event"
sidebar_label: "Event"
custom_edit_url: null
---

[common/web/core/messaging/Event](../modules/common_web_core_messaging_Event.md).Event

An event message.

Events are simple notifications that do not require a reply nor will *execute* anything.

## Hierarchy

- [`Message`](common_web_core_messaging_Message.Message.md)

  ↳ **`Event`**

  ↳↳ [`ComponentInformationEvent`](common_web_api_component_ComponentEvents.ComponentInformationEvent.md)

  ↳↳ [`ConnectorsListEvent`](common_web_api_connector_ConnectorEvents.ConnectorsListEvent.md)

  ↳↳ [`ConnectorAnnounceEvent`](common_web_api_connector_ConnectorEvents.ConnectorAnnounceEvent.md)

  ↳↳ [`ClientConnectedEvent`](common_web_api_network_NetworkEvents.ClientConnectedEvent.md)

  ↳↳ [`ClientDisconnectedEvent`](common_web_api_network_NetworkEvents.ClientDisconnectedEvent.md)

  ↳↳ [`ClientConnectionErrorEvent`](common_web_api_network_NetworkEvents.ClientConnectionErrorEvent.md)

  ↳↳ [`ServerDisconnectedEvent`](common_web_api_network_NetworkEvents.ServerDisconnectedEvent.md)

  ↳↳ [`ProjectsListEvent`](common_web_api_project_ProjectEvents.ProjectsListEvent.md)

  ↳↳ [`ProjectTouchEvent`](common_web_api_project_ProjectEvents.ProjectTouchEvent.md)

  ↳↳ [`ProjectLogbookEvent`](common_web_api_project_ProjectEvents.ProjectLogbookEvent.md)

  ↳↳ [`ProjectExternalStateEvent`](common_web_api_project_ProjectEvents.ProjectExternalStateEvent.md)

  ↳↳ [`ProjectJobsListEvent`](common_web_api_project_ProjectJobEvents.ProjectJobsListEvent.md)

  ↳↳ [`ProjectJobProgressEvent`](common_web_api_project_ProjectJobEvents.ProjectJobProgressEvent.md)

  ↳↳ [`ProjectJobCompletionEvent`](common_web_api_project_ProjectJobEvents.ProjectJobCompletionEvent.md)

  ↳↳ [`UserAuthorizationsListEvent`](common_web_api_user_UserEvents.UserAuthorizationsListEvent.md)

## Constructors

### constructor

• **new Event**(`name`, `origin`, `sender`, `target`, `hops?`, `trace?`, `apiKey?`): [`Event`](common_web_core_messaging_Event.Event.md)

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

[`Event`](common_web_core_messaging_Event.Event.md)

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[constructor](common_web_core_messaging_Message.Message.md#constructor)

#### Defined in

[src/common/web/core/messaging/Message.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L63)

## Properties

### api\_key

• `Readonly` **api\_key**: `string` = `""`

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[api_key](common_web_core_messaging_Message.Message.md#api_key)

#### Defined in

[src/common/web/core/messaging/Message.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L50)

___

### hops

• `Readonly` **hops**: [`UnitID`](common_web_utils_UnitID.UnitID.md)[] = `[]`

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[hops](common_web_core_messaging_Message.Message.md#hops)

#### Defined in

[src/common/web/core/messaging/Message.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L46)

___

### name

• `Readonly` **name**: `string`

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[name](common_web_core_messaging_Message.Message.md#name)

#### Defined in

[src/common/web/core/messaging/Message.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L33)

___

### origin

• `Readonly` **origin**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[origin](common_web_core_messaging_Message.Message.md#origin)

#### Defined in

[src/common/web/core/messaging/Message.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L36)

___

### payload

• `Readonly` **payload**: [`MessagePayload`](common_web_core_messaging_MessagePayload.MessagePayload.md)

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[payload](common_web_core_messaging_Message.Message.md#payload)

#### Defined in

[src/common/web/core/messaging/Message.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L52)

___

### sender

• `Readonly` **sender**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[sender](common_web_core_messaging_Message.Message.md#sender)

#### Defined in

[src/common/web/core/messaging/Message.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L39)

___

### target

• `Readonly` **target**: [`Channel`](common_web_core_messaging_Channel.Channel.md)

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[target](common_web_core_messaging_Message.Message.md#target)

#### Defined in

[src/common/web/core/messaging/Message.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L42)

___

### trace

• `Readonly` **trace**: `string` = `""`

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[trace](common_web_core_messaging_Message.Message.md#trace)

#### Defined in

[src/common/web/core/messaging/Message.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L48)

___

### Category

▪ `Static` `Readonly` **Category**: `string` = `"Event"`

#### Overrides

[Message](common_web_core_messaging_Message.Message.md).[Category](common_web_core_messaging_Message.Message.md#category)

#### Defined in

[src/common/web/core/messaging/Event.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Event.ts#L9)

## Accessors

### messageCategory

• `get` **messageCategory**(): `string`

Gets the global message category.

#### Returns

`string`

#### Overrides

Message.messageCategory

#### Defined in

[src/common/web/core/messaging/Event.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Event.ts#L14)

## Methods

### convertToJSON

▸ **convertToJSON**(): `string`

Converts this message to JSON.

#### Returns

`string`

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[convertToJSON](common_web_core_messaging_Message.Message.md#converttojson)

#### Defined in

[src/common/web/core/messaging/Message.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L76)

___

### toString

▸ **toString**(): `string`

Gets the string representation of this message.

#### Returns

`string`

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[toString](common_web_core_messaging_Message.Message.md#tostring)

#### Defined in

[src/common/web/core/messaging/Message.ts:154](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L154)

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

[Message](common_web_core_messaging_Message.Message.md).[convertFromJSON](common_web_core_messaging_Message.Message.md#convertfromjson)

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

[Message](common_web_core_messaging_Message.Message.md).[define](common_web_core_messaging_Message.Message.md#define)

#### Defined in

[src/common/web/core/messaging/Message.ts:128](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L128)

___

### isProtected

▸ **isProtected**(): `boolean`

The frontend never receives or issues protected messages.

#### Returns

`boolean`

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[isProtected](common_web_core_messaging_Message.Message.md#isprotected)

#### Defined in

[src/common/web/core/messaging/Message.ts:108](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L108)

___

### messageName

▸ **messageName**(): `string`

Retrieves the name of the message type on a message class basis.

#### Returns

`string`

#### Inherited from

[Message](common_web_core_messaging_Message.Message.md).[messageName](common_web_core_messaging_Message.Message.md#messagename)

#### Defined in

[src/common/web/core/messaging/Message.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/Message.ts#L101)
