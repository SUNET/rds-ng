# Function: getActiveProjectJob()

> **getActiveProjectJob**(`project`, `instance`): `undefined` \| [`ProjectJob`](../../../../../../../common/web/data/entities/project/ProjectJob/classes/ProjectJob.md)

Defined in: [src/frontend/src/data/entities/project/ProjectJobUtils.ts:73](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/project/ProjectJobUtils.ts#L73)

Gets the active job for a specific project and connector instance, if any.

## Parameters

### project

[`Project`](../../../../../../../common/web/data/entities/project/Project/classes/Project.md)

The project.

### instance

[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)

The connector instance.

## Returns

`undefined` \| [`ProjectJob`](../../../../../../../common/web/data/entities/project/ProjectJob/classes/ProjectJob.md)

- The active job, if any.
