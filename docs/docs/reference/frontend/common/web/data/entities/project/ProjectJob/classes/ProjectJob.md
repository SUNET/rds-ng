# Class: ProjectJob

Defined in: [src/common/web/data/entities/project/ProjectJob.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectJob.ts#L15)

A project job that is currently active.

## Param

The ID of the user the job belongs to.

## Param

The project ID.

## Param

The connector instance ID.

## Param

The starting time.

## Param

The total progress (0.0 - 1.0).

## Param

The current activity message.

## Constructors

### Constructor

> **new ProjectJob**(`userID`, `projectID`, `connectorInstance`, `timestamp`, `progress`, `message`): `ProjectJob`

Defined in: [src/common/web/data/entities/project/ProjectJob.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectJob.ts#L25)

#### Parameters

##### userID

`string`

##### projectID

`number`

##### connectorInstance

`string`

##### timestamp

`number`

##### progress

`number` = `0.0`

##### message

`string` = `""`

#### Returns

`ProjectJob`

## Properties

### connector\_instance

> `readonly` **connector\_instance**: `string`

Defined in: [src/common/web/data/entities/project/ProjectJob.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectJob.ts#L18)

***

### message

> `readonly` **message**: `string`

Defined in: [src/common/web/data/entities/project/ProjectJob.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectJob.ts#L23)

***

### progress

> `readonly` **progress**: `number`

Defined in: [src/common/web/data/entities/project/ProjectJob.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectJob.ts#L22)

***

### project\_id

> `readonly` **project\_id**: `number`

Defined in: [src/common/web/data/entities/project/ProjectJob.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectJob.ts#L17)

***

### timestamp

> `readonly` **timestamp**: `number`

Defined in: [src/common/web/data/entities/project/ProjectJob.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectJob.ts#L20)

***

### user\_id

> `readonly` **user\_id**: `string`

Defined in: [src/common/web/data/entities/project/ProjectJob.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectJob.ts#L16)
