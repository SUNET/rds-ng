---
id: "common_web_core_logging_Logging"
title: "Module: common/web/core/logging/Logging"
sidebar_label: "common/web/core/logging/Logging"
sidebar_position: 0
custom_edit_url: null
---

## Variables

### default

• **default**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `debug` | (`msg`: `string`, `scope`: `string`, `params`: `Record`<`string`, `any`\>) => `void` |
| `error` | (`msg`: `string`, `scope`: `string`, `params`: `Record`<`string`, `any`\>) => `void` |
| `getDefaultLogger` | () => [`Logger`](../classes/common_web_core_logging_Logger.Logger.md) |
| `info` | (`msg`: `string`, `scope`: `string`, `params`: `Record`<`string`, `any`\>) => `void` |
| `setLevel` | (`level`: [`LogLevel`](../enums/common_web_core_logging_LogRecord.LogLevel.md)) => `void` |
| `warning` | (`msg`: `string`, `scope`: `string`, `params`: `Record`<`string`, `any`\>) => `void` |

#### Defined in

[src/common/web/core/logging/Logging.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logging.ts#L66)

## Functions

### debug

▸ **debug**(`msg`, `scope?`, `params?`): `void`

Logs a debugging message.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `msg` | `string` | `undefined` | The text to log. |
| `scope` | `string` | `""` | The scope of the entry. |
| `params` | `Record`<`string`, `any`\> | `{}` | Any additional parameters. |

#### Returns

`void`

#### Defined in

[src/common/web/core/logging/Logging.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logging.ts#L22)

___

### error

▸ **error**(`msg`, `scope?`, `params?`): `void`

Logs an error message.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `msg` | `string` | `undefined` | The text to log. |
| `scope` | `string` | `""` | The scope of the entry. |
| `params` | `Record`<`string`, `any`\> | `{}` | Any additional parameters. |

#### Returns

`void`

#### Defined in

[src/common/web/core/logging/Logging.ts:55](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logging.ts#L55)

___

### getDefaultLogger

▸ **getDefaultLogger**(): [`Logger`](../classes/common_web_core_logging_Logger.Logger.md)

Retrieves the global default logger.

#### Returns

[`Logger`](../classes/common_web_core_logging_Logger.Logger.md)

#### Defined in

[src/common/web/core/logging/Logging.ts:62](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logging.ts#L62)

___

### info

▸ **info**(`msg`, `scope?`, `params?`): `void`

Logs an info message.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `msg` | `string` | `undefined` | The text to log. |
| `scope` | `string` | `""` | The scope of the entry. |
| `params` | `Record`<`string`, `any`\> | `{}` | Any additional parameters. |

#### Returns

`void`

#### Defined in

[src/common/web/core/logging/Logging.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logging.ts#L33)

___

### setLevel

▸ **setLevel**(`level`): `void`

Sets the default log level.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `level` | [`LogLevel`](../enums/common_web_core_logging_LogRecord.LogLevel.md) | The maximum level for log entries to be displayed. |

#### Returns

`void`

#### Defined in

[src/common/web/core/logging/Logging.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logging.ts#L11)

___

### warning

▸ **warning**(`msg`, `scope?`, `params?`): `void`

Logs a warning message.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `msg` | `string` | `undefined` | The text to log. |
| `scope` | `string` | `""` | The scope of the entry. |
| `params` | `Record`<`string`, `any`\> | `{}` | Any additional parameters. |

#### Returns

`void`

#### Defined in

[src/common/web/core/logging/Logging.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logging.ts#L44)
