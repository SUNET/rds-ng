# Class: MessageContext

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L21)

An execution context for messages dispatched by the message bus.

When a message handler gets executed (i.e., called by the message bus dispatchers), an instance of ``MessageContext`` (or a subclass)
is passed to the handler. This context can be seen as a *unit of work* that exists during the execution of the handler. Its main task is to
hold data that is specific to this single execution.

A message context is used as a context manager. In its ``__exit__`` method, any exceptions will be catched, printed and passed on. This
makes tracing of errors that occur during message handling easier.

It is also possible to have message handlers receive custom subtypes of this class. See ``WebComponent`` and its ``create_service`` method for
details.

## Extended by

- [`ServiceContext`](../../../../../services/ServiceContext/classes/ServiceContext.md)

## Constructors

### Constructor

> **new MessageContext**(`msgMeta`, `msgOrigin`, `msgBuilder`, `logger`, `config`): `MessageContext`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:38](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L38)

#### Parameters

##### msgMeta

[`MessageMetaInformation`](../../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

The meta information of the message.

##### msgOrigin

[`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

The origin of the message.

##### msgBuilder

[`MessageBuilder`](../../../composers/MessageBuilder/classes/MessageBuilder.md)

A ``MessageBuilder`` to be assigned to this context.

##### logger

[`LoggerProxy`](../../../../logging/LoggerProxy/classes/LoggerProxy.md)

A logger that is configured to automatically print the trace belonging to the message that caused the handler to be executed.

##### config

[`Configuration`](../../../../../utils/config/Configuration/classes/Configuration.md)

The global component configuration.

#### Returns

`MessageContext`

## Properties

### \_config

> `protected` `readonly` **\_config**: [`Configuration`](../../../../../utils/config/Configuration/classes/Configuration.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L27)

***

### \_logger

> `protected` `readonly` **\_logger**: [`LoggerProxy`](../../../../logging/LoggerProxy/classes/LoggerProxy.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L26)

***

### \_msgBuilder

> `protected` `readonly` **\_msgBuilder**: [`MessageBuilder`](../../../composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L24)

***

### \_msgMeta

> `protected` `readonly` **\_msgMeta**: [`MessageMetaInformation`](../../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L22)

***

### \_msgOrigin

> `protected` `readonly` **\_msgOrigin**: [`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L23)

***

### \_requiresReply

> `protected` **\_requiresReply**: `boolean` = `false`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L29)

## Accessors

### config

#### Get Signature

> **get** **config**(): [`Configuration`](../../../../../utils/config/Configuration/classes/Configuration.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:123](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L123)

The global component configuration.

##### Returns

[`Configuration`](../../../../../utils/config/Configuration/classes/Configuration.md)

***

### isEntrypointClient

#### Get Signature

> **get** **isEntrypointClient**(): `boolean`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:95](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L95)

Whether the message entered through the client.

##### Returns

`boolean`

***

### isEntrypointLocal

#### Get Signature

> **get** **isEntrypointLocal**(): `boolean`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:81](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L81)

Whether the message entered locally.

##### Returns

`boolean`

***

### isEntrypointServer

#### Get Signature

> **get** **isEntrypointServer**(): `boolean`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:88](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L88)

Whether the message entered through the server.

##### Returns

`boolean`

***

### logger

#### Get Signature

> **get** **logger**(): [`LoggerProxy`](../../../../logging/LoggerProxy/classes/LoggerProxy.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:116](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L116)

The logger to be used within this context.

##### Returns

[`LoggerProxy`](../../../../logging/LoggerProxy/classes/LoggerProxy.md)

***

### messageBuilder

#### Get Signature

> **get** **messageBuilder**(): [`MessageBuilder`](../../../composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:109](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L109)

The message builder to be used within this context.

##### Returns

[`MessageBuilder`](../../../composers/MessageBuilder/classes/MessageBuilder.md)

***

### origin

#### Get Signature

> **get** **origin**(): [`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:102](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L102)

The origin of the message.

##### Returns

[`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

## Methods

### begin()

> **begin**(`requiresReply`): `void`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L52)

Initiates execution within this context.

#### Parameters

##### requiresReply

`boolean`

Whether a reply is required.

#### Returns

`void`

***

### end()

> **end**(): `void`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L59)

Finishes execution within this context.

#### Returns

`void`

***

### reportError()

> **reportError**(`err`): `void`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:68](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L68)

Reports an error occurred during context execution.

#### Parameters

##### err

`any`

The error to report.

#### Returns

`void`
