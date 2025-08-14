# Class: ProjectOptions

Defined in: [src/common/web/data/entities/project/ProjectOptions.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectOptions.ts#L19)

Class holding all options of a **Project**.

## Param

A list of all user-enabled optional features.

## Param

Whether all available connector instances should be used.

## Param

List of connector instances to use for the project (if *use_all_connector_instances* is false).

## Param

Arbitrary UI options.

## Constructors

### Constructor

> **new ProjectOptions**(`optionalFeatures`, `useAllConnectors`, `activeConnectorInstances`, `uiOptions`): `ProjectOptions`

Defined in: [src/common/web/data/entities/project/ProjectOptions.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectOptions.ts#L31)

#### Parameters

##### optionalFeatures

`string`[] = `[]`

##### useAllConnectors

`boolean` = `true`

##### activeConnectorInstances

`string`[] = `[]`

##### uiOptions

[`UIOptions`](../type-aliases/UIOptions.md) = `{}`

#### Returns

`ProjectOptions`

## Properties

### active\_connector\_instances

> **active\_connector\_instances**: `string`[]

Defined in: [src/common/web/data/entities/project/ProjectOptions.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectOptions.ts#L27)

***

### optional\_features

> `readonly` **optional\_features**: `string`[]

Defined in: [src/common/web/data/entities/project/ProjectOptions.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectOptions.ts#L22)

***

### ui

> `readonly` **ui**: [`UIOptions`](../type-aliases/UIOptions.md)

Defined in: [src/common/web/data/entities/project/ProjectOptions.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectOptions.ts#L29)

***

### use\_all\_connector\_instances

> **use\_all\_connector\_instances**: `boolean`

Defined in: [src/common/web/data/entities/project/ProjectOptions.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectOptions.ts#L24)
