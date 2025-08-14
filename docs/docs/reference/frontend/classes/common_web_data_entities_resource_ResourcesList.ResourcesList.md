---
id: "common_web_data_entities_resource_ResourcesList.ResourcesList"
title: "Class: ResourcesList"
sidebar_label: "ResourcesList"
custom_edit_url: null
---

[common/web/data/entities/resource/ResourcesList](../modules/common_web_data_entities_resource_ResourcesList.md).ResourcesList

A recursive list of resources.

Resources are always given in absolute form.

**`Param`**

The current resource path.

**`Param`**

A list of all folders.

**`Param`**

A list of all files.

## Constructors

### constructor

• **new ResourcesList**(`resource`, `folders?`, `files?`): [`ResourcesList`](common_web_data_entities_resource_ResourcesList.ResourcesList.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `resource` | [`Resource`](common_web_data_entities_resource_Resource.Resource.md) | `undefined` |
| `folders` | [`ResourceFolders`](../modules/common_web_data_entities_resource_ResourcesList.md#resourcefolders) | `[]` |
| `files` | [`ResourceFiles`](../modules/common_web_data_entities_resource_ResourcesList.md#resourcefiles) | `[]` |

#### Returns

[`ResourcesList`](common_web_data_entities_resource_ResourcesList.ResourcesList.md)

#### Defined in

[src/common/web/data/entities/resource/ResourcesList.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/ResourcesList.ts#L34)

## Properties

### files

• `Readonly` **files**: [`ResourceFiles`](../modules/common_web_data_entities_resource_ResourcesList.md#resourcefiles)

#### Defined in

[src/common/web/data/entities/resource/ResourcesList.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/ResourcesList.ts#L32)

___

### folders

• `Readonly` **folders**: [`ResourceFolders`](../modules/common_web_data_entities_resource_ResourcesList.md#resourcefolders)

#### Defined in

[src/common/web/data/entities/resource/ResourcesList.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/ResourcesList.ts#L29)

___

### resource

• `Readonly` **resource**: [`Resource`](common_web_data_entities_resource_Resource.Resource.md)

#### Defined in

[src/common/web/data/entities/resource/ResourcesList.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/ResourcesList.ts#L25)
