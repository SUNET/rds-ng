# Variable: default

> **default**: `object`

Defined in: [src/common/web/core/logging/Logging.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/Logging.ts#L66)

## Type declaration

### debug()

> **debug**: (`msg`, `scope`, `params`) => `void`

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

### error()

> **error**: (`msg`, `scope`, `params`) => `void`

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

### getDefaultLogger()

> **getDefaultLogger**: () => [`Logger`](../../Logger/classes/Logger.md)

Retrieves the global default logger.

#### Returns

[`Logger`](../../Logger/classes/Logger.md)

### info()

> **info**: (`msg`, `scope`, `params`) => `void`

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

### setLevel()

> **setLevel**: (`level`) => `void`

Sets the default log level.

#### Parameters

##### level

[`LogLevel`](../../LogRecord/enumerations/LogLevel.md)

The maximum level for log entries to be displayed.

#### Returns

`void`

### warning()

> **warning**: (`msg`, `scope`, `params`) => `void`

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
