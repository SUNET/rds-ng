---
id: "common_web_data_entities_metadata_MetadataProfileContainerUtils"
title: "Module: common/web/data/entities/metadata/MetadataProfileContainerUtils"
sidebar_label: "common/web/data/entities/metadata/MetadataProfileContainerUtils"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### filterContainers

▸ **filterContainers**(`containers`, `category`, `roles`): [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)

Gets all containers from a list matching the specified category and role.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `containers` | [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist) | The list of containers. |
| `category` | `string` | The category to match. |
| `roles` | [`MetadataProfileContainerRole`](../enums/common_web_data_entities_metadata_MetadataProfileContainer.MetadataProfileContainerRole.md)[] | The roles to match. |

#### Returns

[`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)

- List of all matching containers.

#### Defined in

[src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts#L37)

___

### filterContainersByCategory

▸ **filterContainersByCategory**(`containers`, `category`): [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)

Gets all containers from a list matching the specified category.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `containers` | [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist) | The list of containers. |
| `category` | `string` | The category to match. |

#### Returns

[`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)

- List of all matching containers.

#### Defined in

[src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts#L12)

___

### filterContainersByRoles

▸ **filterContainersByRoles**(`containers`, `roles`): [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)

Gets all containers from a list matching the specified role.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `containers` | [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist) | The list of containers. |
| `roles` | [`MetadataProfileContainerRole`](../enums/common_web_data_entities_metadata_MetadataProfileContainer.MetadataProfileContainerRole.md)[] | The roles to match. |

#### Returns

[`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)

- List of all matching containers.

#### Defined in

[src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts#L24)

___

### isContainerSelected

▸ **isContainerSelected**(`container`, `enabledProfiles`): `boolean`

Checks whether a profile (container) is selected - either since it is a default one or the user has enabled it.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `container` | [`MetadataProfileContainer`](../classes/common_web_data_entities_metadata_MetadataProfileContainer.MetadataProfileContainer.md) | The container to check. |
| `enabledProfiles` | [`ProfileID`](common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)[] | All user-enabled profiles. |

#### Returns

`boolean`

#### Defined in

[src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts:51](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts#L51)
