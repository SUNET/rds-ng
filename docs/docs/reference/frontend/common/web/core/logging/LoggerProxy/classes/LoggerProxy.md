# Class: LoggerProxy

Defined in: [src/common/web/core/logging/LoggerProxy.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LoggerProxy.ts#L10)

A proxy to automatically pass extra parameters to a logger.

This class allows us to store additional, fixed parameters passed to an existing logger, avoiding the need to use
a new logger instance. It offers the same public interface as an actual ``Logger`` and can thus be used like a
*real* logger.

## Constructors

### Constructor

> **new LoggerProxy**(`logger`): `LoggerProxy`

Defined in: [src/common/web/core/logging/LoggerProxy.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LoggerProxy.ts#L18)

#### Parameters

##### logger

[`Logger`](../../Logger/classes/Logger.md)

The logger to use.

#### Returns

`LoggerProxy`

## Methods

### addParam()

> **addParam**(`name`, `value`): `void`

Defined in: [src/common/web/core/logging/LoggerProxy.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LoggerProxy.ts#L28)

Adds a new paramter that is always automatically passed to the logger.

#### Parameters

##### name

`string`

The name of the parameter.

##### value

`any`

Its value.

#### Returns

`void`

***

### clearParams()

> **clearParams**(): `void`

Defined in: [src/common/web/core/logging/LoggerProxy.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LoggerProxy.ts#L44)

Removes all stored parameters.

#### Returns

`void`

***

### debug()

> **debug**(`msg`, `scope`, `params`): `void`

Defined in: [src/common/web/core/logging/LoggerProxy.ts:55](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LoggerProxy.ts#L55)

Logs a debugging message.

#### Parameters

##### msg

`string`

The text to log.

##### scope

`string` = `""`

The scope of the entry.

##### params

`Record`\<`string`, `any`\> = `{}`

Any additional parameters.

#### Returns

`void`

***

### error()

> **error**(`msg`, `scope`, `params`): `void`

Defined in: [src/common/web/core/logging/LoggerProxy.ts:88](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LoggerProxy.ts#L88)

Logs an error message.

#### Parameters

##### msg

`string`

The text to log.

##### scope

`string` = `""`

The scope of the entry.

##### params

`Record`\<`string`, `any`\> = `{}`

Any additional parameters.

#### Returns

`void`

***

### info()

> **info**(`msg`, `scope`, `params`): `void`

Defined in: [src/common/web/core/logging/LoggerProxy.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LoggerProxy.ts#L66)

Logs an info message.

#### Parameters

##### msg

`string`

The text to log.

##### scope

`string` = `""`

The scope of the entry.

##### params

`Record`\<`string`, `any`\> = `{}`

Any additional parameters.

#### Returns

`void`

***

### removeParam()

> **removeParam**(`name`): `void`

Defined in: [src/common/web/core/logging/LoggerProxy.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LoggerProxy.ts#L37)

Removes a parameter that has been added previously.

#### Parameters

##### name

`string`

The name of the parameter.

#### Returns

`void`

***

### warning()

> **warning**(`msg`, `scope`, `params`): `void`

Defined in: [src/common/web/core/logging/LoggerProxy.ts:77](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LoggerProxy.ts#L77)

Logs a warning message.

#### Parameters

##### msg

`string`

The text to log.

##### scope

`string` = `""`

The scope of the entry.

##### params

`Record`\<`string`, `any`\> = `{}`

Any additional parameters.

#### Returns

`void`
