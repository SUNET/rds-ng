# Function: getProjectJobDetails()

> **getProjectJobDetails**(`job`, `project`, `connectors`, `connectorInstances`): [`ProjectJobDetails`](../interfaces/ProjectJobDetails.md)

Defined in: [src/frontend/src/data/entities/project/ProjectJobUtils.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/project/ProjectJobUtils.ts#L30)

Bundles information about a project job.

## Parameters

### job

[`ProjectJob`](../../../../../../../common/web/data/entities/project/ProjectJob/classes/ProjectJob.md)

The project job.

### project

The project.

`undefined` | [`Project`](../../../../../../../common/web/data/entities/project/Project/classes/Project.md)

### connectors

[`Connector`](../../../../../../../common/web/data/entities/connector/Connector/classes/Connector.md)[]

All connectors.

### connectorInstances

[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)[]

All connector instances.

## Returns

[`ProjectJobDetails`](../interfaces/ProjectJobDetails.md)
