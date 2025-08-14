# Function: findProjectByID()

> **findProjectByID**(`projects`, `projectID`): `undefined` \| [`Project`](../../Project/classes/Project.md)

Defined in: [src/common/web/data/entities/project/ProjectUtils.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectUtils.ts#L16)

Searches for a project by its ID within a list of projects.

## Parameters

### projects

[`Project`](../../Project/classes/Project.md)[]

The list of projects.

### projectID

`number`

The project to search for.

## Returns

`undefined` \| [`Project`](../../Project/classes/Project.md)

- The found project or **undefined** otherwise.
