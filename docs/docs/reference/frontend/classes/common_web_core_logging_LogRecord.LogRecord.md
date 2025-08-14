---
id: "common_web_core_logging_LogRecord.LogRecord"
title: "Class: LogRecord"
sidebar_label: "LogRecord"
custom_edit_url: null
---

[common/web/core/logging/LogRecord](../modules/common_web_core_logging_LogRecord.md).LogRecord

## Constructors

### constructor

• **new LogRecord**(`msg`, `timestamp`, `level`, `scope`, `params`): [`LogRecord`](common_web_core_logging_LogRecord.LogRecord.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `msg` | `string` |
| `timestamp` | `Date` |
| `level` | [`LogLevel`](../enums/common_web_core_logging_LogRecord.LogLevel.md) |
| `scope` | `string` |
| `params` | `Record`<`string`, `any`\> |

#### Returns

[`LogRecord`](common_web_core_logging_LogRecord.LogRecord.md)

#### Defined in

[src/common/web/core/logging/LogRecord.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LogRecord.ts#L9)

## Properties

### level

• `Readonly` **level**: [`LogLevel`](../enums/common_web_core_logging_LogRecord.LogLevel.md)

#### Defined in

[src/common/web/core/logging/LogRecord.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LogRecord.ts#L9)

___

### msg

• `Readonly` **msg**: `string`

#### Defined in

[src/common/web/core/logging/LogRecord.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LogRecord.ts#L9)

___

### params

• `Readonly` **params**: `Record`<`string`, `any`\>

#### Defined in

[src/common/web/core/logging/LogRecord.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LogRecord.ts#L10)

___

### scope

• `Readonly` **scope**: `string`

#### Defined in

[src/common/web/core/logging/LogRecord.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LogRecord.ts#L9)

___

### timestamp

• `Readonly` **timestamp**: `Date`

#### Defined in

[src/common/web/core/logging/LogRecord.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LogRecord.ts#L9)

## Accessors

### levelName

• `get` **levelName**(): `string`

#### Returns

`string`

#### Defined in

[src/common/web/core/logging/LogRecord.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/LogRecord.ts#L13)
