# Class: ProjectLogbookRecord

Defined in: [src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L13)

A single record of a project's logbook.

## Param

The record entry ID.

## Param

The timestamp of the record.

## Param

Whether the record has been seen by the user.

## Extended by

- [`ProjectJobHistoryRecord`](../../ProjectJobHistoryRecord/classes/ProjectJobHistoryRecord.md)

## Constructors

### Constructor

> **new ProjectLogbookRecord**(`record`, `timestamp`, `seen`): `ProjectLogbookRecord`

Defined in: [src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L19)

#### Parameters

##### record

`number`

##### timestamp

`number`

##### seen

`boolean` = `false`

#### Returns

`ProjectLogbookRecord`

## Properties

### record

> `readonly` **record**: `number`

Defined in: [src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L14)

***

### seen

> `readonly` **seen**: `boolean`

Defined in: [src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L17)

***

### timestamp

> `readonly` **timestamp**: `number`

Defined in: [src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L15)
