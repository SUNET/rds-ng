---
id: "common_web_data_entities_project_ProjectJob.ProjectJob"
title: "Class: ProjectJob"
sidebar_label: "ProjectJob"
custom_edit_url: null
---

[common/web/data/entities/project/ProjectJob](../modules/common_web_data_entities_project_ProjectJob.md).ProjectJob

A project job that is currently active.

**`Param`**

The ID of the user the job belongs to.

**`Param`**

The project ID.

**`Param`**

The connector instance ID.

**`Param`**

The starting time.

**`Param`**

The total progress (0.0 - 1.0).

**`Param`**

The current activity message.

## Constructors

### constructor

• **new ProjectJob**(`userID`, `projectID`, `connectorInstance`, `timestamp`, `progress?`, `message?`): [`ProjectJob`](common_web_data_entities_project_ProjectJob.ProjectJob.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `userID` | `string` | `undefined` |
| `projectID` | `number` | `undefined` |
| `connectorInstance` | `string` | `undefined` |
| `timestamp` | `number` | `undefined` |
| `progress` | `number` | `0.0` |
| `message` | `string` | `""` |

#### Returns

[`ProjectJob`](common_web_data_entities_project_ProjectJob.ProjectJob.md)

#### Defined in

[src/common/web/data/entities/project/ProjectJob.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectJob.ts#L25)

## Properties

### connector\_instance

• `Readonly` **connector\_instance**: `string`

#### Defined in

[src/common/web/data/entities/project/ProjectJob.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectJob.ts#L18)

___

### message

• `Readonly` **message**: `string`

#### Defined in

[src/common/web/data/entities/project/ProjectJob.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectJob.ts#L23)

___

### progress

• `Readonly` **progress**: `number`

#### Defined in

[src/common/web/data/entities/project/ProjectJob.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectJob.ts#L22)

___

### project\_id

• `Readonly` **project\_id**: `number`

#### Defined in

[src/common/web/data/entities/project/ProjectJob.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectJob.ts#L17)

___

### timestamp

• `Readonly` **timestamp**: `number`

#### Defined in

[src/common/web/data/entities/project/ProjectJob.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectJob.ts#L20)

___

### user\_id

• `Readonly` **user\_id**: `string`

#### Defined in

[src/common/web/data/entities/project/ProjectJob.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/ProjectJob.ts#L16)
