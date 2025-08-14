# Class: MarkProjectLogbookSeenReply

Defined in: [src/common/web/api/project/ProjectCommands.ts:211](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/api/project/ProjectCommands.ts#L211)

Reply to ``ProjectLogbookMarkSeenCommand``.

## Extends

- [`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md)

## Constructors

### Constructor

> **new MarkProjectLogbookSeenReply**(`name`, `origin`, `sender`, `target`, `hops`, `trace`, `apiKey`): `MarkProjectLogbookSeenReply`

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

`MarkProjectLogbookSeenReply`

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`constructor`](../../../../core/messaging/CommandReply/classes/CommandReply.md#constructor)

## Properties

### api\_key

> `readonly` **api\_key**: `string` = `""`

Defined in: [src/common/web/core/messaging/Message.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L50)

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`api_key`](../../../../core/messaging/CommandReply/classes/CommandReply.md#api_key)

***

### hops

> `readonly` **hops**: [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)[] = `[]`

Defined in: [src/common/web/core/messaging/Message.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L46)

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`hops`](../../../../core/messaging/CommandReply/classes/CommandReply.md#hops)

***

### message

> `readonly` **message**: `string` = `""`

Defined in: [src/common/web/core/messaging/CommandReply.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/CommandReply.ts#L27)

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`message`](../../../../core/messaging/CommandReply/classes/CommandReply.md#message)

***

### name

> `readonly` **name**: `string`

Defined in: [src/common/web/core/messaging/Message.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L33)

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`name`](../../../../core/messaging/CommandReply/classes/CommandReply.md#name)

***

### origin

> `readonly` **origin**: [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/Message.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L36)

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`origin`](../../../../core/messaging/CommandReply/classes/CommandReply.md#origin)

***

### payload

> `readonly` **payload**: [`MessagePayload`](../../../../core/messaging/MessagePayload/classes/MessagePayload.md)

Defined in: [src/common/web/core/messaging/Message.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L52)

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`payload`](../../../../core/messaging/CommandReply/classes/CommandReply.md#payload)

***

### sender

> `readonly` **sender**: [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/Message.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L39)

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`sender`](../../../../core/messaging/CommandReply/classes/CommandReply.md#sender)

***

### success

> `readonly` **success**: `boolean` = `true`

Defined in: [src/common/web/core/messaging/CommandReply.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/CommandReply.ts#L26)

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`success`](../../../../core/messaging/CommandReply/classes/CommandReply.md#success)

***

### target

> `readonly` **target**: [`Channel`](../../../../core/messaging/Channel/classes/Channel.md)

Defined in: [src/common/web/core/messaging/Message.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L42)

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`target`](../../../../core/messaging/CommandReply/classes/CommandReply.md#target)

***

### trace

> `readonly` **trace**: `string` = `""`

Defined in: [src/common/web/core/messaging/Message.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L48)

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`trace`](../../../../core/messaging/CommandReply/classes/CommandReply.md#trace)

***

### unique

> `readonly` **unique**: `string`

Defined in: [src/common/web/core/messaging/CommandReply.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/CommandReply.ts#L29)

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`unique`](../../../../core/messaging/CommandReply/classes/CommandReply.md#unique)

***

### Category

> `readonly` `static` **Category**: `string` = `"CommandReply"`

Defined in: [src/common/web/core/messaging/CommandReply.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/CommandReply.ts#L24)

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`Category`](../../../../core/messaging/CommandReply/classes/CommandReply.md#category)

## Accessors

### messageCategory

#### Get Signature

> **get** **messageCategory**(): `string`

Defined in: [src/common/web/core/messaging/CommandReply.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/CommandReply.ts#L34)

Gets the global message category.

##### Returns

`string`

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`messageCategory`](../../../../core/messaging/CommandReply/classes/CommandReply.md#messagecategory)

## Methods

### convertToJSON()

> **convertToJSON**(): `string`

Defined in: [src/common/web/core/messaging/Message.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L76)

Converts this message to JSON.

#### Returns

`string`

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`convertToJSON`](../../../../core/messaging/CommandReply/classes/CommandReply.md#converttojson)

***

### toString()

> **toString**(): `string`

Defined in: [src/common/web/core/messaging/Message.ts:154](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L154)

Gets the string representation of this message.

#### Returns

`string`

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`toString`](../../../../core/messaging/CommandReply/classes/CommandReply.md#tostring)

***

### build()

> `static` **build**(`messageBuilder`, `cmd`, `success`, `message`): [`CommandReplyComposer`](../../../../core/messaging/composers/CommandReplyComposer/classes/CommandReplyComposer.md)\<`MarkProjectLogbookSeenReply`\>

Defined in: [src/common/web/api/project/ProjectCommands.ts:215](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/api/project/ProjectCommands.ts#L215)

Helper function to easily build this message.

#### Parameters

##### messageBuilder

[`MessageBuilder`](../../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

##### cmd

[`MarkProjectLogbookSeenCommand`](MarkProjectLogbookSeenCommand.md)

##### success

`boolean` = `true`

##### message

`string` = `""`

#### Returns

[`CommandReplyComposer`](../../../../core/messaging/composers/CommandReplyComposer/classes/CommandReplyComposer.md)\<`MarkProjectLogbookSeenReply`\>

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

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`convertFromJSON`](../../../../core/messaging/CommandReply/classes/CommandReply.md#convertfromjson)

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

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`define`](../../../../core/messaging/CommandReply/classes/CommandReply.md#define)

***

### isProtected()

> `static` **isProtected**(): `boolean`

Defined in: [src/common/web/core/messaging/Message.ts:108](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L108)

The frontend never receives or issues protected messages.

#### Returns

`boolean`

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`isProtected`](../../../../core/messaging/CommandReply/classes/CommandReply.md#isprotected)

***

### messageName()

> `static` **messageName**(): `string`

Defined in: [src/common/web/core/messaging/Message.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L101)

Retrieves the name of the message type on a message class basis.

#### Returns

`string`

#### Inherited from

[`CommandReply`](../../../../core/messaging/CommandReply/classes/CommandReply.md).[`messageName`](../../../../core/messaging/CommandReply/classes/CommandReply.md#messagename)
