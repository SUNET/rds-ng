---
id: "common_web_data_entities_project_features_DataManagementPlanFeature.DataManagementPlanFeature"
title: "Class: DataManagementPlanFeature"
sidebar_label: "DataManagementPlanFeature"
custom_edit_url: null
---

[common/web/data/entities/project/features/DataManagementPlanFeature](../modules/common_web_data_entities_project_features_DataManagementPlanFeature.md).DataManagementPlanFeature

Data class for the data management plan project feature.

## Hierarchy

- [`ProjectFeature`](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md)

  ↳ **`DataManagementPlanFeature`**

## Constructors

### constructor

• **new DataManagementPlanFeature**(`plan?`, `enabledProfiles?`): [`DataManagementPlanFeature`](common_web_data_entities_project_features_DataManagementPlanFeature.DataManagementPlanFeature.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `plan` | [`DataManagementPlan`](../modules/common_web_data_entities_project_features_DataManagementPlanFeature.md#datamanagementplan) | `[]` |
| `enabledProfiles` | [`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)[] | `[]` |

#### Returns

[`DataManagementPlanFeature`](common_web_data_entities_project_features_DataManagementPlanFeature.DataManagementPlanFeature.md)

#### Overrides

[ProjectFeature](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md).[constructor](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md#constructor)

#### Defined in

[src/common/web/data/entities/project/features/DataManagementPlanFeature.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/DataManagementPlanFeature.ts#L25)

## Properties

### enabled\_metadata\_profiles

• `Readonly` **enabled\_metadata\_profiles**: [`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)[] = `[]`

#### Inherited from

[ProjectFeature](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md).[enabled_metadata_profiles](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md#enabled_metadata_profiles)

#### Defined in

[src/common/web/data/entities/project/features/ProjectFeature.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectFeature.ts#L16)

___

### plan

• `Readonly` **plan**: [`DataManagementPlan`](../modules/common_web_data_entities_project_features_DataManagementPlanFeature.md#datamanagementplan)

#### Defined in

[src/common/web/data/entities/project/features/DataManagementPlanFeature.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/DataManagementPlanFeature.ts#L23)

___

### FeatureID

▪ `Static` `Readonly` **FeatureID**: `string` = `"dmp"`

#### Defined in

[src/common/web/data/entities/project/features/DataManagementPlanFeature.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/DataManagementPlanFeature.ts#L19)

## Accessors

### featureID

• `get` **featureID**(): `string`

The ID of this feature.

#### Returns

`string`

#### Overrides

ProjectFeature.featureID

#### Defined in

[src/common/web/data/entities/project/features/DataManagementPlanFeature.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/DataManagementPlanFeature.ts#L31)
