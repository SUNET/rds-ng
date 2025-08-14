# Class: UserAuthorizationsListEvent

Defined in: [src/common/web/api/user/UserEvents.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/api/user/UserEvents.ts#L14)

Event sent when the user authorizations have changed.

## Param

The new list of all granted authorizations.

## Extends

- [`Event`](../../../../core/messaging/Event/classes/Event.md)

## Constructors

### Constructor

> **new UserAuthorizationsListEvent**(`name`, `origin`, `sender`, `target`, `hops`, `trace`, `apiKey`): `UserAuthorizationsListEvent`

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

`UserAuthorizationsListEvent`

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`constructor`](../../../../core/messaging/Event/classes/Event.md#constructor)

## Properties

### api\_key

> `readonly` **api\_key**: `string` = `""`

Defined in: [src/common/web/core/messaging/Message.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L50)

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`api_key`](../../../../core/messaging/Event/classes/Event.md#api_key)

***

### authorizations

> `readonly` **authorizations**: `string`[] = `[]`

Defined in: [src/common/web/api/user/UserEvents.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/api/user/UserEvents.ts#L17)

***

### hops

> `readonly` **hops**: [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)[] = `[]`

Defined in: [src/common/web/core/messaging/Message.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L46)

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`hops`](../../../../core/messaging/Event/classes/Event.md#hops)

***

### name

> `readonly` **name**: `string`

Defined in: [src/common/web/core/messaging/Message.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L33)

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`name`](../../../../core/messaging/Event/classes/Event.md#name)

***

### origin

> `readonly` **origin**: [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/Message.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L36)

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`origin`](../../../../core/messaging/Event/classes/Event.md#origin)

***

### payload

> `readonly` **payload**: [`MessagePayload`](../../../../core/messaging/MessagePayload/classes/MessagePayload.md)

Defined in: [src/common/web/core/messaging/Message.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L52)

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`payload`](../../../../core/messaging/Event/classes/Event.md#payload)

***

### sender

> `readonly` **sender**: [`UnitID`](../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/Message.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L39)

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`sender`](../../../../core/messaging/Event/classes/Event.md#sender)

***

### target

> `readonly` **target**: [`Channel`](../../../../core/messaging/Channel/classes/Channel.md)

Defined in: [src/common/web/core/messaging/Message.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L42)

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`target`](../../../../core/messaging/Event/classes/Event.md#target)

***

### trace

> `readonly` **trace**: `string` = `""`

Defined in: [src/common/web/core/messaging/Message.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L48)

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`trace`](../../../../core/messaging/Event/classes/Event.md#trace)

***

### Category

> `readonly` `static` **Category**: `string` = `"Event"`

Defined in: [src/common/web/core/messaging/Event.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Event.ts#L9)

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`Category`](../../../../core/messaging/Event/classes/Event.md#category)

## Accessors

### messageCategory

#### Get Signature

> **get** **messageCategory**(): `string`

Defined in: [src/common/web/core/messaging/Event.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Event.ts#L14)

Gets the global message category.

##### Returns

`string`

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`messageCategory`](../../../../core/messaging/Event/classes/Event.md#messagecategory)

## Methods

### convertToJSON()

> **convertToJSON**(): `string`

Defined in: [src/common/web/core/messaging/Message.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L76)

Converts this message to JSON.

#### Returns

`string`

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`convertToJSON`](../../../../core/messaging/Event/classes/Event.md#converttojson)

***

### toString()

> **toString**(): `string`

Defined in: [src/common/web/core/messaging/Message.ts:154](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L154)

Gets the string representation of this message.

#### Returns

`string`

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`toString`](../../../../core/messaging/Event/classes/Event.md#tostring)

***

### build()

> `static` **build**(`messageBuilder`, `authorizations`, `chain`): [`EventComposer`](../../../../core/messaging/composers/EventComposer/classes/EventComposer.md)\<`UserAuthorizationsListEvent`\>

Defined in: [src/common/web/api/user/UserEvents.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/api/user/UserEvents.ts#L22)

Helper function to easily build this message.

#### Parameters

##### messageBuilder

[`MessageBuilder`](../../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

##### authorizations

`string`[]

##### chain

`null` | [`Message`](../../../../core/messaging/Message/classes/Message.md)

#### Returns

[`EventComposer`](../../../../core/messaging/composers/EventComposer/classes/EventComposer.md)\<`UserAuthorizationsListEvent`\>

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

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`convertFromJSON`](../../../../core/messaging/Event/classes/Event.md#convertfromjson)

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

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`define`](../../../../core/messaging/Event/classes/Event.md#define)

***

### isProtected()

> `static` **isProtected**(): `boolean`

Defined in: [src/common/web/core/messaging/Message.ts:108](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L108)

The frontend never receives or issues protected messages.

#### Returns

`boolean`

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`isProtected`](../../../../core/messaging/Event/classes/Event.md#isprotected)

***

### messageName()

> `static` **messageName**(): `string`

Defined in: [src/common/web/core/messaging/Message.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/Message.ts#L101)

Retrieves the name of the message type on a message class basis.

#### Returns

`string`

#### Inherited from

[`Event`](../../../../core/messaging/Event/classes/Event.md).[`messageName`](../../../../core/messaging/Event/classes/Event.md#messagename)
