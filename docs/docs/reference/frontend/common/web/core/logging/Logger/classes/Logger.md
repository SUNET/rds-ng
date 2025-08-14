# Class: Logger

Defined in: [src/common/web/core/logging/Logger.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/Logger.ts#L10)

A customized logger offering advanced formatting and parameters listing.

This logger and its corresponding ``Formatter`` display the log level, scope, as well as a parameters listing
in a color-rich format for easy readability.

## Constructors

### Constructor

> **new Logger**(`level`): `Logger`

Defined in: [src/common/web/core/logging/Logger.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/Logger.ts#L16)

#### Parameters

##### level

[`LogLevel`](../../LogRecord/enumerations/LogLevel.md) = `LogLevel.Info`

The maximum level for log entries to be displayed.

#### Returns

`Logger`

## Methods

### debug()

> **debug**(`msg`, `scope`, `params`): `void`

Defined in: [src/common/web/core/logging/Logger.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/Logger.ts#L36)

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

Defined in: [src/common/web/core/logging/Logger.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/Logger.ts#L72)

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

Defined in: [src/common/web/core/logging/Logger.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/Logger.ts#L48)

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

### setLevel()

> **setLevel**(`level`): `void`

Defined in: [src/common/web/core/logging/Logger.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/Logger.ts#L25)

Sets the maximum logging level.

#### Parameters

##### level

[`LogLevel`](../../LogRecord/enumerations/LogLevel.md)

The logging level.

#### Returns

`void`

***

### warning()

> **warning**(`msg`, `scope`, `params`): `void`

Defined in: [src/common/web/core/logging/Logger.ts:60](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/Logger.ts#L60)

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
