---
id: "common_web_data_entities_project_ProjectUtils"
title: "Module: common/web/data/entities/project/ProjectUtils"
sidebar_label: "common/web/data/entities/project/ProjectUtils"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### findProjectByID

▸ **findProjectByID**(`projects`, `projectID`): [`Project`](../classes/common_web_data_entities_project_Project.Project.md) \| `undefined`

Searches for a project by its ID within a list of projects.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `projects` | [`Project`](../classes/common_web_data_entities_project_Project.Project.md)[] | The list of projects. |
| `projectID` | `number` | The project to search for. |

#### Returns

[`Project`](../classes/common_web_data_entities_project_Project.Project.md) \| `undefined`

- The found project or **undefined** otherwise.

#### Defined in

[src/common/web/data/entities/project/ProjectUtils.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectUtils.ts#L16)

___

### getOptionalMetadataProfiles

▸ **getOptionalMetadataProfiles**(`project`, `userSettings`, `connectors`, `profiles`, `featureID`): [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)

Gets all optional profiles for a specific feature of a project.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `project` | [`Project`](../classes/common_web_data_entities_project_Project.Project.md) | The project. |
| `userSettings` | [`UserSettings`](../classes/common_web_data_entities_user_UserSettings.UserSettings.md) | The user settings. |
| `connectors` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[] | A list of all known connectors. |
| `profiles` | [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist) | A list of all metadata profiles. |
| `featureID` | `string` | The project feature ID. |

#### Returns

[`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)

#### Defined in

[src/common/web/data/entities/project/ProjectUtils.ts:49](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectUtils.ts#L49)

___

### isConnectorActivated

▸ **isConnectorActivated**(`project`, `userSettings`, `connector`, `connectors`): `boolean`

Checks if a connector is activated and valid for a given project.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `project` | [`Project`](../classes/common_web_data_entities_project_Project.Project.md) | The project. |
| `userSettings` | [`UserSettings`](../classes/common_web_data_entities_user_UserSettings.UserSettings.md) | The user settings. |
| `connector` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md) | The connector to check. |
| `connectors` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[] | A list of all known connectors. |

#### Returns

`boolean`

#### Defined in

[src/common/web/data/entities/project/ProjectUtils.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectUtils.ts#L28)
