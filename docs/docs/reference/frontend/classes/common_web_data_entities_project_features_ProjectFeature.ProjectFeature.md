---
id: "common_web_data_entities_project_features_ProjectFeature.ProjectFeature"
title: "Class: ProjectFeature"
sidebar_label: "ProjectFeature"
custom_edit_url: null
---

[common/web/data/entities/project/features/ProjectFeature](../modules/common_web_data_entities_project_features_ProjectFeature.md).ProjectFeature

Base data class for a project feature.

## Hierarchy

- **`ProjectFeature`**

  ↳ [`DataManagementPlanFeature`](common_web_data_entities_project_features_DataManagementPlanFeature.DataManagementPlanFeature.md)

  ↳ [`ProjectMetadataFeature`](common_web_data_entities_project_features_ProjectMetadataFeature.ProjectMetadataFeature.md)

  ↳ [`ResourcesMetadataFeature`](common_web_data_entities_project_features_ResourcesMetadataFeature.ResourcesMetadataFeature.md)

## Constructors

### constructor

• **new ProjectFeature**(`enabledProfiles?`): [`ProjectFeature`](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `enabledProfiles` | [`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)[] | `[]` |

#### Returns

[`ProjectFeature`](common_web_data_entities_project_features_ProjectFeature.ProjectFeature.md)

#### Defined in

[src/common/web/data/entities/project/features/ProjectFeature.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectFeature.ts#L23)

## Properties

### enabled\_metadata\_profiles

• `Readonly` **enabled\_metadata\_profiles**: [`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)[] = `[]`

#### Defined in

[src/common/web/data/entities/project/features/ProjectFeature.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectFeature.ts#L16)

## Accessors

### featureID

• `get` **featureID**(): `string`

The ID of this feature.

#### Returns

`string`

#### Defined in

[src/common/web/data/entities/project/features/ProjectFeature.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/features/ProjectFeature.ts#L21)
