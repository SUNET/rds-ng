---
id: "frontend_src_data_entities_project_ProjectJobUtils"
title: "Module: frontend/src/data/entities/project/ProjectJobUtils"
sidebar_label: "frontend/src/data/entities/project/ProjectJobUtils"
sidebar_position: 0
custom_edit_url: null
---

## Interfaces

- [ProjectJobDetails](../interfaces/frontend_src_data_entities_project_ProjectJobUtils.ProjectJobDetails.md)

## Functions

### getActiveProjectJob

▸ **getActiveProjectJob**(`project`, `instance`): [`ProjectJob`](../classes/common_web_data_entities_project_ProjectJob.ProjectJob.md) \| `undefined`

Gets the active job for a specific project and connector instance, if any.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `project` | [`Project`](../classes/common_web_data_entities_project_Project.Project.md) | The project. |
| `instance` | [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md) | The connector instance. |

#### Returns

[`ProjectJob`](../classes/common_web_data_entities_project_ProjectJob.ProjectJob.md) \| `undefined`

- The active job, if any.

#### Defined in

[src/frontend/src/data/entities/project/ProjectJobUtils.ts:73](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/project/ProjectJobUtils.ts#L73)

___

### getAllProjectJobDetails

▸ **getAllProjectJobDetails**(`projects`, `jobs`, `connectors`, `connectorInstances`): [`ProjectJobDetails`](../interfaces/frontend_src_data_entities_project_ProjectJobUtils.ProjectJobDetails.md)[]

Bundles information about all project jobs.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `projects` | [`Project`](../classes/common_web_data_entities_project_Project.Project.md)[] | All projects. |
| `jobs` | [`ProjectJob`](../classes/common_web_data_entities_project_ProjectJob.ProjectJob.md)[] | All project jobs. |
| `connectors` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[] | All connectors. |
| `connectorInstances` | [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)[] | All connector instances. |

#### Returns

[`ProjectJobDetails`](../interfaces/frontend_src_data_entities_project_ProjectJobUtils.ProjectJobDetails.md)[]

#### Defined in

[src/frontend/src/data/entities/project/ProjectJobUtils.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/project/ProjectJobUtils.ts#L52)

___

### getProjectJobDetails

▸ **getProjectJobDetails**(`job`, `project`, `connectors`, `connectorInstances`): [`ProjectJobDetails`](../interfaces/frontend_src_data_entities_project_ProjectJobUtils.ProjectJobDetails.md)

Bundles information about a project job.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `job` | [`ProjectJob`](../classes/common_web_data_entities_project_ProjectJob.ProjectJob.md) | The project job. |
| `project` | `undefined` \| [`Project`](../classes/common_web_data_entities_project_Project.Project.md) | The project. |
| `connectors` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[] | All connectors. |
| `connectorInstances` | [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)[] | All connector instances. |

#### Returns

[`ProjectJobDetails`](../interfaces/frontend_src_data_entities_project_ProjectJobUtils.ProjectJobDetails.md)

#### Defined in

[src/frontend/src/data/entities/project/ProjectJobUtils.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/project/ProjectJobUtils.ts#L30)
