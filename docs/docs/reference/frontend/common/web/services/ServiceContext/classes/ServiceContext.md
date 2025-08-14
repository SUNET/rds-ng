# Class: ServiceContext

Defined in: [src/common/web/services/ServiceContext.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/services/ServiceContext.ts#L8)

An execution context for messages dispatched by the message bus to a service.

This class is an extension to the more general ``MessageContext`` specifically used by ``Service`` and its message handlers.

## Extends

- [`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md)

## Extended by

- [`FrontendServiceContext`](../../../../../frontend/src/services/FrontendServiceContext/classes/FrontendServiceContext.md)

## Constructors

### Constructor

> **new ServiceContext**(`msgMeta`, `msgOrigin`, `msgBuilder`, `logger`, `config`): `ServiceContext`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:38](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L38)

#### Parameters

##### msgMeta

[`MessageMetaInformation`](../../../core/messaging/meta/MessageMetaInformation/classes/MessageMetaInformation.md)

The meta information of the message.

##### msgOrigin

[`UnitID`](../../../utils/UnitID/classes/UnitID.md)

The origin of the message.

##### msgBuilder

[`MessageBuilder`](../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

A ``MessageBuilder`` to be assigned to this context.

##### logger

[`LoggerProxy`](../../../core/logging/LoggerProxy/classes/LoggerProxy.md)

A logger that is configured to automatically print the trace belonging to the message that caused the handler to be executed.

##### config

[`Configuration`](../../../utils/config/Configuration/classes/Configuration.md)

The global component configuration.

#### Returns

`ServiceContext`

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`constructor`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#constructor)

## Properties

### \_config

> `protected` `readonly` **\_config**: [`Configuration`](../../../utils/config/Configuration/classes/Configuration.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L27)

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`_config`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#_config)

***

### \_logger

> `protected` `readonly` **\_logger**: [`LoggerProxy`](../../../core/logging/LoggerProxy/classes/LoggerProxy.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L26)

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`_logger`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#_logger)

***

### \_msgBuilder

> `protected` `readonly` **\_msgBuilder**: [`MessageBuilder`](../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L24)

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`_msgBuilder`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#_msgbuilder)

***

### \_msgMeta

> `protected` `readonly` **\_msgMeta**: [`MessageMetaInformation`](../../../core/messaging/meta/MessageMetaInformation/classes/MessageMetaInformation.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L22)

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`_msgMeta`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#_msgmeta)

***

### \_msgOrigin

> `protected` `readonly` **\_msgOrigin**: [`UnitID`](../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L23)

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`_msgOrigin`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#_msgorigin)

***

### \_requiresReply

> `protected` **\_requiresReply**: `boolean` = `false`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L29)

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`_requiresReply`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#_requiresreply)

## Accessors

### config

#### Get Signature

> **get** **config**(): [`Configuration`](../../../utils/config/Configuration/classes/Configuration.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:123](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L123)

The global component configuration.

##### Returns

[`Configuration`](../../../utils/config/Configuration/classes/Configuration.md)

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`config`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#config)

***

### isEntrypointClient

#### Get Signature

> **get** **isEntrypointClient**(): `boolean`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:95](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L95)

Whether the message entered through the client.

##### Returns

`boolean`

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`isEntrypointClient`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#isentrypointclient)

***

### isEntrypointLocal

#### Get Signature

> **get** **isEntrypointLocal**(): `boolean`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:81](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L81)

Whether the message entered locally.

##### Returns

`boolean`

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`isEntrypointLocal`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#isentrypointlocal)

***

### isEntrypointServer

#### Get Signature

> **get** **isEntrypointServer**(): `boolean`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:88](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L88)

Whether the message entered through the server.

##### Returns

`boolean`

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`isEntrypointServer`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#isentrypointserver)

***

### logger

#### Get Signature

> **get** **logger**(): [`LoggerProxy`](../../../core/logging/LoggerProxy/classes/LoggerProxy.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:116](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L116)

The logger to be used within this context.

##### Returns

[`LoggerProxy`](../../../core/logging/LoggerProxy/classes/LoggerProxy.md)

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`logger`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#logger)

***

### messageBuilder

#### Get Signature

> **get** **messageBuilder**(): [`MessageBuilder`](../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:109](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L109)

The message builder to be used within this context.

##### Returns

[`MessageBuilder`](../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`messageBuilder`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#messagebuilder)

***

### origin

#### Get Signature

> **get** **origin**(): [`UnitID`](../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:102](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L102)

The origin of the message.

##### Returns

[`UnitID`](../../../utils/UnitID/classes/UnitID.md)

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`origin`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#origin)

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

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`begin`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#begin)

***

### end()

> **end**(): `void`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L59)

Finishes execution within this context.

#### Returns

`void`

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`end`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#end)

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

#### Inherited from

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md).[`reportError`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md#reporterror)
