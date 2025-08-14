# Class: ListResourcesCommand

Defined in: [src/common/web/api/resource/ResourceCommands.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/api/resource/ResourceCommands.ts#L63)

Command to fetch all available resources.

## Param

The root path (or empty if the system root should be used).

## Param

Whether to list folders (if this is set to false, no recursion will occur independent of `recursive`).

## Param

Whether to list files.

## Param

Whether to recursively process all sub-folders as well.

## Extends

- [`Command`](../../../../core/messaging/Command/classes/Command.md)

## Constructors

### Constructor

> **new ListResourcesCommand**(`name`, `origin`, `sender`, `target`, `hops`, `trace`, `apiKey`): `ListResourcesCommand`

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

[`Channel`](../../../../core/messaging/Channel/classes/Channel.md)

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

`ListResourcesCommand`

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`constructor`](../../../../core/messaging/Command/classes/Command.md#constructor)

## Properties

### api\_key

> `readonly` **api\_key**: `string` = `""`

Defined in: [src/common/web/core/messaging/Message.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L50)

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`api_key`](../../../../core/messaging/Command/classes/Command.md#api_key)

***

### hops

> `readonly` **hops**: [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)[] = `[]`

Defined in: [src/common/web/core/messaging/Message.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L46)

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`hops`](../../../../core/messaging/Command/classes/Command.md#hops)

***

### include\_files

> `readonly` **include\_files**: `boolean` = `true`

Defined in: [src/common/web/api/resource/ResourceCommands.ts:67](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/api/resource/ResourceCommands.ts#L67)

***

### include\_folders

> `readonly` **include\_folders**: `boolean` = `true`

Defined in: [src/common/web/api/resource/ResourceCommands.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/api/resource/ResourceCommands.ts#L66)

***

### name

> `readonly` **name**: `string`

Defined in: [src/common/web/core/messaging/Message.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L33)

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`name`](../../../../core/messaging/Command/classes/Command.md#name)

***

### origin

> `readonly` **origin**: [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/Message.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L36)

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`origin`](../../../../core/messaging/Command/classes/Command.md#origin)

***

### payload

> `readonly` **payload**: [`MessagePayload`](../../../../core/messaging/MessagePayload/classes/MessagePayload.md)

Defined in: [src/common/web/core/messaging/Message.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L52)

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`payload`](../../../../core/messaging/Command/classes/Command.md#payload)

***

### recursive

> `readonly` **recursive**: `boolean` = `true`

Defined in: [src/common/web/api/resource/ResourceCommands.ts:69](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/api/resource/ResourceCommands.ts#L69)

***

### root

> `readonly` **root**: `string` = `""`

Defined in: [src/common/web/api/resource/ResourceCommands.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/api/resource/ResourceCommands.ts#L64)

***

### sender

> `readonly` **sender**: [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/Message.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L39)

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`sender`](../../../../core/messaging/Command/classes/Command.md#sender)

***

### target

> `readonly` **target**: [`Channel`](../../../../core/messaging/Channel/classes/Channel.md)

Defined in: [src/common/web/core/messaging/Message.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L42)

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`target`](../../../../core/messaging/Command/classes/Command.md#target)

***

### trace

> `readonly` **trace**: `string` = `""`

Defined in: [src/common/web/core/messaging/Message.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L48)

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`trace`](../../../../core/messaging/Command/classes/Command.md#trace)

***

### unique

> `readonly` **unique**: `string`

Defined in: [src/common/web/core/messaging/Command.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Command.ts#L17)

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`unique`](../../../../core/messaging/Command/classes/Command.md#unique)

***

### Category

> `readonly` `static` **Category**: `string` = `"Command"`

Defined in: [src/common/web/core/messaging/Command.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Command.ts#L15)

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`Category`](../../../../core/messaging/Command/classes/Command.md#category)

## Accessors

### messageCategory

#### Get Signature

> **get** **messageCategory**(): `string`

Defined in: [src/common/web/core/messaging/Command.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Command.ts#L22)

Gets the global message category.

##### Returns

`string`

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`messageCategory`](../../../../core/messaging/Command/classes/Command.md#messagecategory)

## Methods

### convertToJSON()

> **convertToJSON**(): `string`

Defined in: [src/common/web/core/messaging/Message.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L76)

Converts this message to JSON.

#### Returns

`string`

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`convertToJSON`](../../../../core/messaging/Command/classes/Command.md#converttojson)

***

### toString()

> **toString**(): `string`

Defined in: [src/common/web/core/messaging/Message.ts:154](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L154)

Gets the string representation of this message.

#### Returns

`string`

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`toString`](../../../../core/messaging/Command/classes/Command.md#tostring)

***

### build()

> `static` **build**(`messageBuilder`, `root`, `includeFolders`, `includeFiles`, `recursive`, `chain`): [`CommandComposer`](../../../../core/messaging/composers/CommandComposer/classes/CommandComposer.md)\<`ListResourcesCommand`\>

Defined in: [src/common/web/api/resource/ResourceCommands.ts:74](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/api/resource/ResourceCommands.ts#L74)

Helper function to easily build this message.

#### Parameters

##### messageBuilder

[`MessageBuilder`](../../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

##### root

`string` = `""`

##### includeFolders

`boolean` = `true`

##### includeFiles

`boolean` = `true`

##### recursive

`boolean` = `true`

##### chain

`null` | [`Message`](../../../../core/messaging/Message/classes/Message.md)

#### Returns

[`CommandComposer`](../../../../core/messaging/composers/CommandComposer/classes/CommandComposer.md)\<`ListResourcesCommand`\>

***

### convertFromJSON()

> `static` **convertFromJSON**(`msgType`, `data`): [`Message`](../../../../core/messaging/Message/classes/Message.md)

Defined in: [src/common/web/core/messaging/Message.ts:93](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L93)

Creates a message from JSON data.

#### Parameters

##### msgType

[`ConstructableMessage`](../../../../core/messaging/Message/interfaces/ConstructableMessage.md)

The message type to construct.

##### data

`string`

The JSON data string.

#### Returns

[`Message`](../../../../core/messaging/Message/classes/Message.md)

- The created message.

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`convertFromJSON`](../../../../core/messaging/Command/classes/Command.md#convertfromjson)

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

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`define`](../../../../core/messaging/Command/classes/Command.md#define)

***

### isProtected()

> `static` **isProtected**(): `boolean`

Defined in: [src/common/web/core/messaging/Message.ts:108](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L108)

The frontend never receives or issues protected messages.

#### Returns

`boolean`

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`isProtected`](../../../../core/messaging/Command/classes/Command.md#isprotected)

***

### messageName()

> `static` **messageName**(): `string`

Defined in: [src/common/web/core/messaging/Message.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L101)

Retrieves the name of the message type on a message class basis.

#### Returns

`string`

#### Inherited from

[`Command`](../../../../core/messaging/Command/classes/Command.md).[`messageName`](../../../../core/messaging/Command/classes/Command.md#messagename)
