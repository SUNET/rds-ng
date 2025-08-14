---
id: "common_web_core_logging_Logger.Logger"
title: "Class: Logger"
sidebar_label: "Logger"
custom_edit_url: null
---

[common/web/core/logging/Logger](../modules/common_web_core_logging_Logger.md).Logger

A customized logger offering advanced formatting and parameters listing.

This logger and its corresponding ``Formatter`` display the log level, scope, as well as a parameters listing
in a color-rich format for easy readability.

## Constructors

### constructor

• **new Logger**(`level?`): [`Logger`](common_web_core_logging_Logger.Logger.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `level` | [`LogLevel`](../enums/common_web_core_logging_LogRecord.LogLevel.md) | `LogLevel.Info` | The maximum level for log entries to be displayed. |

#### Returns

[`Logger`](common_web_core_logging_Logger.Logger.md)

#### Defined in

[src/common/web/core/logging/Logger.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logger.ts#L16)

## Properties

### \_level

• `Private` **\_level**: [`LogLevel`](../enums/common_web_core_logging_LogRecord.LogLevel.md)

#### Defined in

[src/common/web/core/logging/Logger.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logger.ts#L11)

## Methods

### createLogRecord

▸ **createLogRecord**(`level`, `msg`, `scope`, `params`): [`LogRecord`](common_web_core_logging_LogRecord.LogRecord.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `level` | [`LogLevel`](../enums/common_web_core_logging_LogRecord.LogLevel.md) |
| `msg` | `string` |
| `scope` | `string` |
| `params` | `Record`<`string`, `any`\> |

#### Returns

[`LogRecord`](common_web_core_logging_LogRecord.LogRecord.md)

#### Defined in

[src/common/web/core/logging/Logger.ts:77](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logger.ts#L77)

___

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

[src/common/web/core/logging/Logger.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logger.ts#L36)

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

[src/common/web/core/logging/Logger.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logger.ts#L72)

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

[src/common/web/core/logging/Logger.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logger.ts#L48)

___

### log

▸ **log**(`record`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `record` | [`LogRecord`](common_web_core_logging_LogRecord.LogRecord.md) |

#### Returns

`void`

#### Defined in

[src/common/web/core/logging/Logger.ts:81](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logger.ts#L81)

___

### setLevel

▸ **setLevel**(`level`): `void`

Sets the maximum logging level.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `level` | [`LogLevel`](../enums/common_web_core_logging_LogRecord.LogLevel.md) | The logging level. |

#### Returns

`void`

#### Defined in

[src/common/web/core/logging/Logger.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logger.ts#L25)

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

[src/common/web/core/logging/Logger.ts:60](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Logger.ts#L60)
