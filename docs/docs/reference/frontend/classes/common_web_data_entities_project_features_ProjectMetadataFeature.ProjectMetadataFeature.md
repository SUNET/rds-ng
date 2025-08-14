---
id: "common_web_data_entities_project_features_ProjectMetadataFeature.ProjectMetadataFeature"
title: "Class: ProjectMetadataFeature"
sidebar_label: "ProjectMetadataFeature"
custom_edit_url: null
---

[common/web/data/entities/project/features/ProjectMetadataFeature](../modules/common_web_data_entities_project_features_ProjectMetadataFeature.md).ProjectMetadataFeature

Data class for the metadata project feature.

## Hierarchy

- [`ProjectFeature`](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md)

  ↳ **`ProjectMetadataFeature`**

## Constructors

### constructor

• **new ProjectMetadataFeature**(`metadata?`, `enabledProfiles?`): [`ProjectMetadataFeature`](common_web_data_entities_project_features_ProjectMetadataFeature.ProjectMetadataFeature.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `metadata` | [`ProjectMetadata`](../modules/common_web_data_entities_project_features_ProjectMetadataFeature.md#projectmetadata) | `[]` |
| `enabledProfiles` | [`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)[] | `[]` |

#### Returns

[`ProjectMetadataFeature`](common_web_data_entities_project_features_ProjectMetadataFeature.ProjectMetadataFeature.md)

#### Overrides

[ProjectFeature](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md).[constructor](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md#constructor)

#### Defined in

[src/common/web/data/entities/project/features/ProjectMetadataFeature.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectMetadataFeature.ts#L24)

## Properties

### enabled\_metadata\_profiles

• `Readonly` **enabled\_metadata\_profiles**: [`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)[] = `[]`

#### Inherited from

[ProjectFeature](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md).[enabled_metadata_profiles](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md#enabled_metadata_profiles)

#### Defined in

[src/common/web/data/entities/project/features/ProjectFeature.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectFeature.ts#L16)

___

### metadata

• `Readonly` **metadata**: [`ProjectMetadata`](../modules/common_web_data_entities_project_features_ProjectMetadataFeature.md#projectmetadata)

#### Defined in

[src/common/web/data/entities/project/features/ProjectMetadataFeature.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectMetadataFeature.ts#L22)

___

### FeatureID

▪ `Static` `Readonly` **FeatureID**: `string` = `"project_metadata"`

#### Defined in

[src/common/web/data/entities/project/features/ProjectMetadataFeature.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectMetadataFeature.ts#L18)

## Accessors

### featureID

• `get` **featureID**(): `string`

The ID of this feature.

#### Returns

`string`

#### Overrides

ProjectFeature.featureID

#### Defined in

[src/common/web/data/entities/project/features/ProjectMetadataFeature.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectMetadataFeature.ts#L30)
