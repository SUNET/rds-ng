# Class: CommandReply

Defined in: [src/common/web/core/messaging/CommandReply.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/CommandReply.ts#L23)

A command reply message.

Every command needs to receive a reply in the form of a ``CommandReply`` message. The reply contains
information about its ``success``, as well as a text message which is usually used to describe reasons for
failures.

## Extends

- [`Message`](../../Message/classes/Message.md)

## Extended by

- [`RequestAuthorizationReply`](../../../../api/authorization/AuthorizationCommands/classes/RequestAuthorizationReply.md)
- [`RevokeAuthorizationReply`](../../../../api/authorization/AuthorizationCommands/classes/RevokeAuthorizationReply.md)
- [`ListConnectorsReply`](../../../../api/connector/ConnectorCommands/classes/ListConnectorsReply.md)
- [`GetMetadataProfilesReply`](../../../../api/metadata/MetadataCommands/classes/GetMetadataProfilesReply.md)
- [`PingReply`](../../../../api/network/NetworkCommands/classes/PingReply.md)
- [`ListProjectsReply`](../../../../api/project/ProjectCommands/classes/ListProjectsReply.md)
- [`CreateProjectReply`](../../../../api/project/ProjectCommands/classes/CreateProjectReply.md)
- [`UpdateProjectReply`](../../../../api/project/ProjectCommands/classes/UpdateProjectReply.md)
- [`MarkProjectLogbookSeenReply`](../../../../api/project/ProjectCommands/classes/MarkProjectLogbookSeenReply.md)
- [`DeleteProjectReply`](../../../../api/project/ProjectCommands/classes/DeleteProjectReply.md)
- [`ListProjectExportersReply`](../../../../api/project/ProjectExportersCommands/classes/ListProjectExportersReply.md)
- [`ExportProjectReply`](../../../../api/project/ProjectExportersCommands/classes/ExportProjectReply.md)
- [`UpdateProjectFeaturesReply`](../../../../api/project/ProjectFeaturesCommands/classes/UpdateProjectFeaturesReply.md)
- [`ListProjectJobsReply`](../../../../api/project/ProjectJobCommands/classes/ListProjectJobsReply.md)
- [`InitiateProjectJobReply`](../../../../api/project/ProjectJobCommands/classes/InitiateProjectJobReply.md)
- [`AssignResourcesBrokerReply`](../../../../api/resource/ResourceCommands/classes/AssignResourcesBrokerReply.md)
- [`ListResourcesReply`](../../../../api/resource/ResourceCommands/classes/ListResourcesReply.md)
- [`GetResourceReply`](../../../../api/resource/ResourceCommands/classes/GetResourceReply.md)
- [`GetSessionValueReply`](../../../../api/session/SessionCommands/classes/GetSessionValueReply.md)
- [`SetSessionValueReply`](../../../../api/session/SessionCommands/classes/SetSessionValueReply.md)
- [`AuthenticateUserReply`](../../../../api/user/UserCommands/classes/AuthenticateUserReply.md)
- [`GetUserSettingsReply`](../../../../api/user/UserCommands/classes/GetUserSettingsReply.md)
- [`SetUserSettingsReply`](../../../../api/user/UserCommands/classes/SetUserSettingsReply.md)
- [`ListUserAuthorizationsReply`](../../../../api/user/UserCommands/classes/ListUserAuthorizationsReply.md)

## Constructors

### Constructor

> **new CommandReply**(`name`, `origin`, `sender`, `target`, `hops`, `trace`, `apiKey`): `CommandReply`

Defined in: [src/common/web/core/messaging/Message.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L63)

#### Parameters

##### name

`string`

The name of the message.

##### origin

[`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

The initial source component of the message.

##### sender

[`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

The component from where the message came from.

##### target

[`Channel`](../../Channel/classes/Channel.md)

Where the message should go to.

##### hops

[`UnitID`](../../../../utils/UnitID/classes/UnitID.md)[] = `[]`

A list of components the message was sent through.

##### trace

`string` = `...`

A unique trace identifying messages that logically belong together.

##### apiKey

`string` = `""`

An optional API key to access protected resources.

#### Returns

`CommandReply`

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`constructor`](../../Message/classes/Message.md#constructor)

## Properties

### api\_key

> `readonly` **api\_key**: `string` = `""`

Defined in: [src/common/web/core/messaging/Message.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L50)

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`api_key`](../../Message/classes/Message.md#api_key)

***

### hops

> `readonly` **hops**: [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)[] = `[]`

Defined in: [src/common/web/core/messaging/Message.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L46)

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`hops`](../../Message/classes/Message.md#hops)

***

### message

> `readonly` **message**: `string` = `""`

Defined in: [src/common/web/core/messaging/CommandReply.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/CommandReply.ts#L27)

***

### name

> `readonly` **name**: `string`

Defined in: [src/common/web/core/messaging/Message.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L33)

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`name`](../../Message/classes/Message.md#name)

***

### origin

> `readonly` **origin**: [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/Message.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L36)

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`origin`](../../Message/classes/Message.md#origin)

***

### payload

> `readonly` **payload**: [`MessagePayload`](../../MessagePayload/classes/MessagePayload.md)

Defined in: [src/common/web/core/messaging/Message.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L52)

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`payload`](../../Message/classes/Message.md#payload)

***

### sender

> `readonly` **sender**: [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/Message.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L39)

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`sender`](../../Message/classes/Message.md#sender)

***

### success

> `readonly` **success**: `boolean` = `true`

Defined in: [src/common/web/core/messaging/CommandReply.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/CommandReply.ts#L26)

***

### target

> `readonly` **target**: [`Channel`](../../Channel/classes/Channel.md)

Defined in: [src/common/web/core/messaging/Message.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L42)

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`target`](../../Message/classes/Message.md#target)

***

### trace

> `readonly` **trace**: `string` = `""`

Defined in: [src/common/web/core/messaging/Message.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L48)

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`trace`](../../Message/classes/Message.md#trace)

***

### unique

> `readonly` **unique**: `string`

Defined in: [src/common/web/core/messaging/CommandReply.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/CommandReply.ts#L29)

***

### Category

> `readonly` `static` **Category**: `string` = `"CommandReply"`

Defined in: [src/common/web/core/messaging/CommandReply.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/CommandReply.ts#L24)

#### Overrides

[`Message`](../../Message/classes/Message.md).[`Category`](../../Message/classes/Message.md#category)

## Accessors

### messageCategory

#### Get Signature

> **get** **messageCategory**(): `string`

Defined in: [src/common/web/core/messaging/CommandReply.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/CommandReply.ts#L34)

Gets the global message category.

##### Returns

`string`

#### Overrides

[`Message`](../../Message/classes/Message.md).[`messageCategory`](../../Message/classes/Message.md#messagecategory)

## Methods

### convertToJSON()

> **convertToJSON**(): `string`

Defined in: [src/common/web/core/messaging/Message.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L76)

Converts this message to JSON.

#### Returns

`string`

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`convertToJSON`](../../Message/classes/Message.md#converttojson)

***

### toString()

> **toString**(): `string`

Defined in: [src/common/web/core/messaging/Message.ts:154](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L154)

Gets the string representation of this message.

#### Returns

`string`

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`toString`](../../Message/classes/Message.md#tostring)

***

### convertFromJSON()

> `static` **convertFromJSON**(`msgType`, `data`): [`Message`](../../Message/classes/Message.md)

Defined in: [src/common/web/core/messaging/Message.ts:93](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L93)

Creates a message from JSON data.

#### Parameters

##### msgType

[`ConstructableMessage`](../../Message/interfaces/ConstructableMessage.md)

The message type to construct.

##### data

`string`

The JSON data string.

#### Returns

[`Message`](../../Message/classes/Message.md)

- The created message.

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`convertFromJSON`](../../Message/classes/Message.md#convertfromjson)

***

### define()

> `static` **define**(`name`): `Function`

Defined in: [src/common/web/core/messaging/Message.ts:128](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L128)

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

##### name

`string`

The name of the message.

#### Returns

`Function`

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`define`](../../Message/classes/Message.md#define)

***

### isProtected()

> `static` **isProtected**(): `boolean`

Defined in: [src/common/web/core/messaging/Message.ts:108](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L108)

The frontend never receives or issues protected messages.

#### Returns

`boolean`

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`isProtected`](../../Message/classes/Message.md#isprotected)

***

### messageName()

> `static` **messageName**(): `string`

Defined in: [src/common/web/core/messaging/Message.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L101)

Retrieves the name of the message type on a message class basis.

#### Returns

`string`

#### Inherited from

[`Message`](../../Message/classes/Message.md).[`messageName`](../../Message/classes/Message.md#messagename)
