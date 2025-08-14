---
id: "common_web_data_entities_project_ProjectOptions.ProjectOptions"
title: "Class: ProjectOptions"
sidebar_label: "ProjectOptions"
custom_edit_url: null
---

[common/web/data/entities/project/ProjectOptions](../modules/common_web_data_entities_project_ProjectOptions.md).ProjectOptions

Class holding all options of a **Project**.

**`Param`**

A list of all user-enabled optional features.

**`Param`**

Whether all available connector instances should be used.

**`Param`**

List of connector instances to use for the project (if *use_all_connector_instances* is false).

**`Param`**

Arbitrary UI options.

## Constructors

### constructor

• **new ProjectOptions**(`optionalFeatures?`, `useAllConnectors?`, `activeConnectorInstances?`, `uiOptions?`): [`ProjectOptions`](common_web_data_entities_project_ProjectOptions.ProjectOptions.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `optionalFeatures` | `string`[] | `[]` |
| `useAllConnectors` | `boolean` | `true` |
| `activeConnectorInstances` | `string`[] | `[]` |
| `uiOptions` | [`UIOptions`](../modules/common_web_data_entities_project_ProjectOptions.md#uioptions) | `{}` |

#### Returns

[`ProjectOptions`](common_web_data_entities_project_ProjectOptions.ProjectOptions.md)

#### Defined in

[src/common/web/data/entities/project/ProjectOptions.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectOptions.ts#L31)

## Properties

### active\_connector\_instances

• **active\_connector\_instances**: `string`[]

#### Defined in

[src/common/web/data/entities/project/ProjectOptions.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectOptions.ts#L27)

___

### optional\_features

• `Readonly` **optional\_features**: `string`[]

#### Defined in

[src/common/web/data/entities/project/ProjectOptions.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectOptions.ts#L22)

___

### ui

• `Readonly` **ui**: [`UIOptions`](../modules/common_web_data_entities_project_ProjectOptions.md#uioptions)

#### Defined in

[src/common/web/data/entities/project/ProjectOptions.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectOptions.ts#L29)

___

### use\_all\_connector\_instances

• **use\_all\_connector\_instances**: `boolean`

#### Defined in

[src/common/web/data/entities/project/ProjectOptions.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectOptions.ts#L24)
