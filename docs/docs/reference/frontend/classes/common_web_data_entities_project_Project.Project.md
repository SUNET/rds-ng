---
id: "common_web_data_entities_project_Project.Project"
title: "Class: Project"
sidebar_label: "Project"
custom_edit_url: null
---

[common/web/data/entities/project/Project](../modules/common_web_data_entities_project_Project.md).Project

Data for a single **Project**.

**`Param`**

The unique project identifier.

**`Param`**

The ID of the user.

**`Param`**

A UNIX timestamp of the project creation time.

**`Param`**

The resources path of the project.

**`Param`**

The title of the project.

**`Param`**

An optional project description.

**`Param`**

The project status.

**`Param`**

All project features.

**`Param`**

All project options.

**`Param`**

The project's logbook.

## Constructors

### constructor

• **new Project**(`projectID`, `creationTime`, `resourcesPath`, `title`, `description?`, `features?`, `options?`, `logbook?`): [`Project`](common_web_data_entities_project_Project.Project.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `projectID` | `number` | `undefined` |
| `creationTime` | `number` | `undefined` |
| `resourcesPath` | `string` | `undefined` |
| `title` | `string` | `undefined` |
| `description` | `string` | `""` |
| `features` | [`ProjectFeatures`](common_web_data_entities_project_features_ProjectFeatures.ProjectFeatures.md) | `undefined` |
| `options` | [`ProjectOptions`](common_web_data_entities_project_ProjectOptions.ProjectOptions.md) | `undefined` |
| `logbook` | [`ProjectLogbook`](common_web_data_entities_project_logbook_ProjectLogbook.ProjectLogbook.md) | `undefined` |

#### Returns

[`Project`](common_web_data_entities_project_Project.Project.md)

#### Defined in

[src/common/web/data/entities/project/Project.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/Project.ts#L59)

## Properties

### creation\_time

• `Readonly` **creation\_time**: `number`

#### Defined in

[src/common/web/data/entities/project/Project.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/Project.ts#L39)

___

### description

• `Readonly` **description**: `string`

#### Defined in

[src/common/web/data/entities/project/Project.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/Project.ts#L44)

___

### features

• `Readonly` **features**: [`ProjectFeatures`](common_web_data_entities_project_features_ProjectFeatures.ProjectFeatures.md)

#### Defined in

[src/common/web/data/entities/project/Project.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/Project.ts#L50)

___

### logbook

• `Readonly` **logbook**: [`ProjectLogbook`](common_web_data_entities_project_logbook_ProjectLogbook.ProjectLogbook.md)

#### Defined in

[src/common/web/data/entities/project/Project.ts:57](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/Project.ts#L57)

___

### options

• `Readonly` **options**: [`ProjectOptions`](common_web_data_entities_project_ProjectOptions.ProjectOptions.md)

#### Defined in

[src/common/web/data/entities/project/Project.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/Project.ts#L53)

___

### project\_id

• `Readonly` **project\_id**: `number`

#### Defined in

[src/common/web/data/entities/project/Project.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/Project.ts#L36)

___

### resources\_path

• `Readonly` **resources\_path**: `string`

#### Defined in

[src/common/web/data/entities/project/Project.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/Project.ts#L41)

___

### status

• `Readonly` **status**: [`ProjectStatus`](../enums/common_web_data_entities_project_Project.ProjectStatus.md) = `ProjectStatus.Active`

#### Defined in

[src/common/web/data/entities/project/Project.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/Project.ts#L46)

___

### title

• `Readonly` **title**: `string`

#### Defined in

[src/common/web/data/entities/project/Project.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/Project.ts#L43)

___

### user\_id

• `Readonly` **user\_id**: `string`

#### Defined in

[src/common/web/data/entities/project/Project.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/Project.ts#L37)
