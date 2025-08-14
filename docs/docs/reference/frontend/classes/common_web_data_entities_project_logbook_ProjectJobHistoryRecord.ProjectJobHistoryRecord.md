---
id: "common_web_data_entities_project_logbook_ProjectJobHistoryRecord.ProjectJobHistoryRecord"
title: "Class: ProjectJobHistoryRecord"
sidebar_label: "ProjectJobHistoryRecord"
custom_edit_url: null
---

[common/web/data/entities/project/logbook/ProjectJobHistoryRecord](../modules/common_web_data_entities_project_logbook_ProjectJobHistoryRecord.md).ProjectJobHistoryRecord

A single record of a project's job history.

**`Param`**

The connector instance ID.

**`Param`**

The success status (done or failed).

**`Param`**

An optional message (usually in case of an error).

## Hierarchy

- [`ProjectLogbookRecord`](common_web_data_entities_project_logbook_ProjectLogbookRecord.ProjectLogbookRecord.md)

  ↳ **`ProjectJobHistoryRecord`**

## Constructors

### constructor

• **new ProjectJobHistoryRecord**(`record`, `timestamp`, `connectorInstance`, `success`, `message`, `extData?`): [`ProjectJobHistoryRecord`](common_web_data_entities_project_logbook_ProjectJobHistoryRecord.ProjectJobHistoryRecord.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `record` | `number` |
| `timestamp` | `number` |
| `connectorInstance` | `string` |
| `success` | `boolean` |
| `message` | `string` |
| `extData` | [`ProjectJobHistoryRecordExtData`](../modules/common_web_data_entities_project_logbook_ProjectJobHistoryRecord.md#projectjobhistoryrecordextdata) |

#### Returns

[`ProjectJobHistoryRecord`](common_web_data_entities_project_logbook_ProjectJobHistoryRecord.ProjectJobHistoryRecord.md)

#### Overrides

[ProjectLogbookRecord](common_web_data_entities_project_logbook_ProjectLogbookRecord.ProjectLogbookRecord.md).[constructor](common_web_data_entities_project_logbook_ProjectLogbookRecord.ProjectLogbookRecord.md#constructor)

#### Defined in

[src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts#L33)

## Properties

### connector\_instance

• `Readonly` **connector\_instance**: `string`

#### Defined in

[src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts#L26)

___

### ext\_data

• `Readonly` **ext\_data**: [`ProjectJobHistoryRecordExtData`](../modules/common_web_data_entities_project_logbook_ProjectJobHistoryRecord.md#projectjobhistoryrecordextdata)

#### Defined in

[src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts#L31)

___

### message

• `Readonly` **message**: `string`

#### Defined in

[src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts#L29)

___

### record

• `Readonly` **record**: `number`

#### Inherited from

[ProjectLogbookRecord](common_web_data_entities_project_logbook_ProjectLogbookRecord.ProjectLogbookRecord.md).[record](common_web_data_entities_project_logbook_ProjectLogbookRecord.ProjectLogbookRecord.md#record)

#### Defined in

[src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L14)

___

### seen

• `Readonly` **seen**: `boolean`

#### Inherited from

[ProjectLogbookRecord](common_web_data_entities_project_logbook_ProjectLogbookRecord.ProjectLogbookRecord.md).[seen](common_web_data_entities_project_logbook_ProjectLogbookRecord.ProjectLogbookRecord.md#seen)

#### Defined in

[src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L17)

___

### success

• `Readonly` **success**: `boolean`

#### Defined in

[src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/logbook/ProjectJobHistoryRecord.ts#L28)

___

### timestamp

• `Readonly` **timestamp**: `number`

#### Inherited from

[ProjectLogbookRecord](common_web_data_entities_project_logbook_ProjectLogbookRecord.ProjectLogbookRecord.md).[timestamp](common_web_data_entities_project_logbook_ProjectLogbookRecord.ProjectLogbookRecord.md#timestamp)

#### Defined in

[src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L15)
