# Class: ProjectJobHistoryRecord

Defined in: [src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts#L25)

A single record of a project's job history.

## Param

The connector instance ID.

## Param

The success status (done or failed).

## Param

An optional message (usually in case of an error).

## Extends

- [`ProjectLogbookRecord`](../../ProjectLogbookRecord/classes/ProjectLogbookRecord.md)

## Constructors

### Constructor

> **new ProjectJobHistoryRecord**(`record`, `timestamp`, `connectorInstance`, `success`, `message`, `extData`): `ProjectJobHistoryRecord`

Defined in: [src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts#L33)

#### Parameters

##### record

`number`

##### timestamp

`number`

##### connectorInstance

`string`

##### success

`boolean`

##### message

`string`

##### extData

[`ProjectJobHistoryRecordExtData`](../type-aliases/ProjectJobHistoryRecordExtData.md) = `{}`

#### Returns

`ProjectJobHistoryRecord`

#### Overrides

[`ProjectLogbookRecord`](../../ProjectLogbookRecord/classes/ProjectLogbookRecord.md).[`constructor`](../../ProjectLogbookRecord/classes/ProjectLogbookRecord.md#constructor)

## Properties

### connector\_instance

> `readonly` **connector\_instance**: `string`

Defined in: [src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts#L26)

***

### ext\_data

> `readonly` **ext\_data**: [`ProjectJobHistoryRecordExtData`](../type-aliases/ProjectJobHistoryRecordExtData.md)

Defined in: [src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts#L31)

***

### message

> `readonly` **message**: `string`

Defined in: [src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts#L29)

***

### record

> `readonly` **record**: `number`

Defined in: [src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L14)

#### Inherited from

[`ProjectLogbookRecord`](../../ProjectLogbookRecord/classes/ProjectLogbookRecord.md).[`record`](../../ProjectLogbookRecord/classes/ProjectLogbookRecord.md#record)

***

### seen

> `readonly` **seen**: `boolean`

Defined in: [src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L17)

#### Inherited from

[`ProjectLogbookRecord`](../../ProjectLogbookRecord/classes/ProjectLogbookRecord.md).[`seen`](../../ProjectLogbookRecord/classes/ProjectLogbookRecord.md#seen)

***

### success

> `readonly` **success**: `boolean`

Defined in: [src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts#L28)

***

### timestamp

> `readonly` **timestamp**: `number`

Defined in: [src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L15)

#### Inherited from

[`ProjectLogbookRecord`](../../ProjectLogbookRecord/classes/ProjectLogbookRecord.md).[`timestamp`](../../ProjectLogbookRecord/classes/ProjectLogbookRecord.md#timestamp)
