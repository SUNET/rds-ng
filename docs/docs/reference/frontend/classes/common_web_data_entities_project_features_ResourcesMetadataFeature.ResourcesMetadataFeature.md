---
id: "common_web_data_entities_project_features_ResourcesMetadataFeature.ResourcesMetadataFeature"
title: "Class: ResourcesMetadataFeature"
sidebar_label: "ResourcesMetadataFeature"
custom_edit_url: null
---

[common/web/data/entities/project/features/ResourcesMetadataFeature](../modules/common_web_data_entities_project_features_ResourcesMetadataFeature.md).ResourcesMetadataFeature

Data class for the files project feature.

## Hierarchy

- [`ProjectFeature`](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md)

  ↳ **`ResourcesMetadataFeature`**

## Constructors

### constructor

• **new ResourcesMetadataFeature**(`resourcesMetadata?`, `enabledProfiles?`): [`ResourcesMetadataFeature`](common_web_data_entities_project_features_ResourcesMetadataFeature.ResourcesMetadataFeature.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `resourcesMetadata` | [`ResourcesMetadata`](common_web_data_entities_project_features_ResourcesMetadataFeature.ResourcesMetadata.md) | `{}` |
| `enabledProfiles` | [`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)[] | `[]` |

#### Returns

[`ResourcesMetadataFeature`](common_web_data_entities_project_features_ResourcesMetadataFeature.ResourcesMetadataFeature.md)

#### Overrides

[ProjectFeature](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md).[constructor](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md#constructor)

#### Defined in

[src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts#L41)

## Properties

### enabled\_metadata\_profiles

• `Readonly` **enabled\_metadata\_profiles**: [`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)[] = `[]`

#### Inherited from

[ProjectFeature](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md).[enabled_metadata_profiles](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md#enabled_metadata_profiles)

#### Defined in

[src/common/web/data/entities/project/features/ProjectFeature.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectFeature.ts#L16)

___

### metadata

• `Readonly` **metadata**: [`ResourcesMetadata`](common_web_data_entities_project_features_ResourcesMetadataFeature.ResourcesMetadata.md)

#### Defined in

[src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts#L39)

___

### FeatureID

▪ `Static` `Readonly` **FeatureID**: `string` = `"resources_metadata"`

#### Defined in

[src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts#L33)

## Accessors

### featureID

• `get` **featureID**(): `string`

The ID of this feature.

#### Returns

`string`

#### Overrides

ProjectFeature.featureID

#### Defined in

[src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts:47](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts#L47)
