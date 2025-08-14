---
id: "common_web_core_logging_LoggerProxy.LoggerProxy"
title: "Class: LoggerProxy"
sidebar_label: "LoggerProxy"
custom_edit_url: null
---

[common/web/core/logging/LoggerProxy](../modules/common_web_core_logging_LoggerProxy.md).LoggerProxy

A proxy to automatically pass extra parameters to a logger.

This class allows us to store additional, fixed parameters passed to an existing logger, avoiding the need to use
a new logger instance. It offers the same public interface as an actual ``Logger`` and can thus be used like a
*real* logger.

## Constructors

### constructor

• **new LoggerProxy**(`logger`): [`LoggerProxy`](common_web_core_logging_LoggerProxy.LoggerProxy.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `logger` | [`Logger`](common_web_core_logging_Logger.Logger.md) | The logger to use. |

#### Returns

[`LoggerProxy`](common_web_core_logging_LoggerProxy.LoggerProxy.md)

#### Defined in

[src/common/web/core/logging/LoggerProxy.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LoggerProxy.ts#L18)

## Properties

### \_autoParams

• `Private` **\_autoParams**: `Record`<`string`, `any`\> = `{}`

#### Defined in

[src/common/web/core/logging/LoggerProxy.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LoggerProxy.ts#L13)

___

### \_logger

• `Private` `Readonly` **\_logger**: [`Logger`](common_web_core_logging_Logger.Logger.md)

#### Defined in

[src/common/web/core/logging/LoggerProxy.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LoggerProxy.ts#L11)

## Methods

### addParam

▸ **addParam**(`name`, `value`): `void`

Adds a new paramter that is always automatically passed to the logger.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | The name of the parameter. |
| `value` | `any` | Its value. |

#### Returns

`void`

#### Defined in

[src/common/web/core/logging/LoggerProxy.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LoggerProxy.ts#L28)

___

### clearParams

▸ **clearParams**(): `void`

Removes all stored parameters.

#### Returns

`void`

#### Defined in

[src/common/web/core/logging/LoggerProxy.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LoggerProxy.ts#L44)

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

[src/common/web/core/logging/LoggerProxy.ts:55](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LoggerProxy.ts#L55)

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

[src/common/web/core/logging/LoggerProxy.ts:88](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LoggerProxy.ts#L88)

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

[src/common/web/core/logging/LoggerProxy.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LoggerProxy.ts#L66)

___

### removeParam

▸ **removeParam**(`name`): `void`

Removes a parameter that has been added previously.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | The name of the parameter. |

#### Returns

`void`

#### Defined in

[src/common/web/core/logging/LoggerProxy.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LoggerProxy.ts#L37)

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

[src/common/web/core/logging/LoggerProxy.ts:77](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LoggerProxy.ts#L77)
