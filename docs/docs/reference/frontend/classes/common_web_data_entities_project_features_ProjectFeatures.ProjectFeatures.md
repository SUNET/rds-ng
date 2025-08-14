---
id: "common_web_data_entities_project_features_ProjectFeatures.ProjectFeatures"
title: "Class: ProjectFeatures"
sidebar_label: "ProjectFeatures"
custom_edit_url: null
---

[common/web/data/entities/project/features/ProjectFeatures](../modules/common_web_data_entities_project_features_ProjectFeatures.md).ProjectFeatures

Superordinate data for all **Project** features.

**`Param`**

The metadata project feature.

**`Param`**

The resources metadata project feature.

**`Param`**

The data management plan feature.

**`Param`**

Project-wide shared metadata objects.

## Constructors

### constructor

• **new ProjectFeatures**(`projectMetadata?`, `resourceMetadata?`, `dmp?`, `sharedPropertyObjects?`): [`ProjectFeatures`](common_web_data_entities_project_features_ProjectFeatures.ProjectFeatures.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `projectMetadata?` | [`ProjectMetadataFeature`](common_web_data_entities_project_features_ProjectMetadataFeature.ProjectMetadataFeature.md) |
| `resourceMetadata?` | [`ResourcesMetadataFeature`](common_web_data_entities_project_features_ResourcesMetadataFeature.ResourcesMetadataFeature.md) |
| `dmp?` | [`DataManagementPlanFeature`](common_web_data_entities_project_features_DataManagementPlanFeature.DataManagementPlanFeature.md) |
| `sharedPropertyObjects?` | [`MetadataObjects`](../modules/common_web_data_entities_metadata_Types.md#metadataobjects) |

#### Returns

[`ProjectFeatures`](common_web_data_entities_project_features_ProjectFeatures.ProjectFeatures.md)

#### Defined in

[src/common/web/data/entities/project/features/ProjectFeatures.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectFeatures.ts#L32)

## Properties

### dmp

• `Readonly` **dmp**: [`DataManagementPlanFeature`](common_web_data_entities_project_features_DataManagementPlanFeature.DataManagementPlanFeature.md)

#### Defined in

[src/common/web/data/entities/project/features/ProjectFeatures.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectFeatures.ts#L26)

___

### project\_metadata

• `Readonly` **project\_metadata**: [`ProjectMetadataFeature`](common_web_data_entities_project_features_ProjectMetadataFeature.ProjectMetadataFeature.md)

#### Defined in

[src/common/web/data/entities/project/features/ProjectFeatures.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectFeatures.ts#L20)

___

### resources\_metadata

• `Readonly` **resources\_metadata**: [`ResourcesMetadataFeature`](common_web_data_entities_project_features_ResourcesMetadataFeature.ResourcesMetadataFeature.md)

#### Defined in

[src/common/web/data/entities/project/features/ProjectFeatures.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectFeatures.ts#L23)

___

### shared\_objects

• `Readonly` **shared\_objects**: [`MetadataObjects`](../modules/common_web_data_entities_metadata_Types.md#metadataobjects)

#### Defined in

[src/common/web/data/entities/project/features/ProjectFeatures.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectFeatures.ts#L30)
