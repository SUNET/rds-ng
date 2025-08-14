# Class: LogRecord

Defined in: [src/common/web/core/logging/LogRecord.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LogRecord.ts#L8)

## Constructors

### Constructor

> **new LogRecord**(`msg`, `timestamp`, `level`, `scope`, `params`): `LogRecord`

Defined in: [src/common/web/core/logging/LogRecord.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LogRecord.ts#L9)

#### Parameters

##### msg

`string`

##### timestamp

`Date`

##### level

[`LogLevel`](../enumerations/LogLevel.md)

##### scope

`string`

##### params

`Record`\<`string`, `any`\>

#### Returns

`LogRecord`

## Properties

### level

> `readonly` **level**: [`LogLevel`](../enumerations/LogLevel.md)

Defined in: [src/common/web/core/logging/LogRecord.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LogRecord.ts#L9)

***

### msg

> `readonly` **msg**: `string`

Defined in: [src/common/web/core/logging/LogRecord.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LogRecord.ts#L9)

***

### params

> `readonly` **params**: `Record`\<`string`, `any`\>

Defined in: [src/common/web/core/logging/LogRecord.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LogRecord.ts#L10)

***

### scope

> `readonly` **scope**: `string`

Defined in: [src/common/web/core/logging/LogRecord.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LogRecord.ts#L9)

***

### timestamp

> `readonly` **timestamp**: `Date`

Defined in: [src/common/web/core/logging/LogRecord.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LogRecord.ts#L9)

## Accessors

### levelName

#### Get Signature

> **get** **levelName**(): `string`

Defined in: [src/common/web/core/logging/LogRecord.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/logging/LogRecord.ts#L13)

##### Returns

`string`
