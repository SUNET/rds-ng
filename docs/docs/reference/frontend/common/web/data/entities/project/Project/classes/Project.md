# Class: Project

Defined in: [src/common/web/data/entities/project/Project.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/Project.ts#L35)

Data for a single **Project**.

## Param

The unique project identifier.

## Param

The ID of the user.

## Param

A UNIX timestamp of the project creation time.

## Param

The resources path of the project.

## Param

The title of the project.

## Param

An optional project description.

## Param

The project status.

## Param

All project features.

## Param

All project options.

## Param

The project's logbook.

## Constructors

### Constructor

> **new Project**(`projectID`, `creationTime`, `resourcesPath`, `title`, `description`, `features`, `options`, `logbook`): `Project`

Defined in: [src/common/web/data/entities/project/Project.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/Project.ts#L59)

#### Parameters

##### projectID

`number`

##### creationTime

`number`

##### resourcesPath

`string`

##### title

`string`

##### description

`string` = `""`

##### features

[`ProjectFeatures`](../../features/ProjectFeatures/classes/ProjectFeatures.md) = `...`

##### options

[`ProjectOptions`](../../ProjectOptions/classes/ProjectOptions.md) = `...`

##### logbook

[`ProjectLogbook`](../../logbook/ProjectLogbook/classes/ProjectLogbook.md) = `...`

#### Returns

`Project`

## Properties

### creation\_time

> `readonly` **creation\_time**: `number`

Defined in: [src/common/web/data/entities/project/Project.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/Project.ts#L39)

***

### description

> `readonly` **description**: `string`

Defined in: [src/common/web/data/entities/project/Project.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/Project.ts#L44)

***

### features

> `readonly` **features**: [`ProjectFeatures`](../../features/ProjectFeatures/classes/ProjectFeatures.md)

Defined in: [src/common/web/data/entities/project/Project.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/Project.ts#L50)

***

### logbook

> `readonly` **logbook**: [`ProjectLogbook`](../../logbook/ProjectLogbook/classes/ProjectLogbook.md)

Defined in: [src/common/web/data/entities/project/Project.ts:57](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/Project.ts#L57)

***

### options

> `readonly` **options**: [`ProjectOptions`](../../ProjectOptions/classes/ProjectOptions.md)

Defined in: [src/common/web/data/entities/project/Project.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/Project.ts#L53)

***

### project\_id

> `readonly` **project\_id**: `number`

Defined in: [src/common/web/data/entities/project/Project.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/Project.ts#L36)

***

### resources\_path

> `readonly` **resources\_path**: `string`

Defined in: [src/common/web/data/entities/project/Project.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/Project.ts#L41)

***

### status

> `readonly` **status**: [`ProjectStatus`](../enumerations/ProjectStatus.md) = `ProjectStatus.Active`

Defined in: [src/common/web/data/entities/project/Project.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/Project.ts#L46)

***

### title

> `readonly` **title**: `string`

Defined in: [src/common/web/data/entities/project/Project.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/Project.ts#L43)

***

### user\_id

> `readonly` **user\_id**: `string`

Defined in: [src/common/web/data/entities/project/Project.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/Project.ts#L37)
