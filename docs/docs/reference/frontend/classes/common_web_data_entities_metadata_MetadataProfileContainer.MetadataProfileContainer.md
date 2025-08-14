---
id: "common_web_data_entities_metadata_MetadataProfileContainer.MetadataProfileContainer"
title: "Class: MetadataProfileContainer"
sidebar_label: "MetadataProfileContainer"
custom_edit_url: null
---

[common/web/data/entities/metadata/MetadataProfileContainer](../modules/common_web_data_entities_metadata_MetadataProfileContainer.md).MetadataProfileContainer

A container that holds a metadata profile along with various descriptive information.

**`Param`**

The overall category of the profile.

**`Param`**

The role of the profile within its category.

**`Param`**

The actual profile data.

## Constructors

### constructor

• **new MetadataProfileContainer**(`category`, `role`, `profile`): [`MetadataProfileContainer`](common_web_data_entities_metadata_MetadataProfileContainer.MetadataProfileContainer.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `category` | `string` |
| `role` | [`MetadataProfileContainerRole`](../enums/common_web_data_entities_metadata_MetadataProfileContainer.MetadataProfileContainerRole.md) |
| `profile` | [`PropertyProfile`](common_web_ui_components_propertyeditor_PropertyProfile.PropertyProfile.md) |

#### Returns

[`MetadataProfileContainer`](common_web_data_entities_metadata_MetadataProfileContainer.MetadataProfileContainer.md)

#### Defined in

[src/common/web/data/entities/metadata/MetadataProfileContainer.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/metadata/MetadataProfileContainer.ts#L31)

## Properties

### category

• `Readonly` **category**: `string`

#### Defined in

[src/common/web/data/entities/metadata/MetadataProfileContainer.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/metadata/MetadataProfileContainer.ts#L24)

___

### profile

• `Readonly` **profile**: [`PropertyProfile`](common_web_ui_components_propertyeditor_PropertyProfile.PropertyProfile.md)

#### Defined in

[src/common/web/data/entities/metadata/MetadataProfileContainer.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/metadata/MetadataProfileContainer.ts#L29)

___

### role

• `Readonly` **role**: [`MetadataProfileContainerRole`](../enums/common_web_data_entities_metadata_MetadataProfileContainer.MetadataProfileContainerRole.md)

#### Defined in

[src/common/web/data/entities/metadata/MetadataProfileContainer.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/metadata/MetadataProfileContainer.ts#L25)
