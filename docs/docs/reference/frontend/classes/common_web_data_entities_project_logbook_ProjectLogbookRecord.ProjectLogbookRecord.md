---
id: "common_web_data_entities_project_logbook_ProjectLogbookRecord.ProjectLogbookRecord"
title: "Class: ProjectLogbookRecord"
sidebar_label: "ProjectLogbookRecord"
custom_edit_url: null
---

[common/web/data/entities/project/logbook/ProjectLogbookRecord](../modules/common_web_data_entities_project_logbook_ProjectLogbookRecord.md).ProjectLogbookRecord

A single record of a project's logbook.

**`Param`**

The record entry ID.

**`Param`**

The timestamp of the record.

**`Param`**

Whether the record has been seen by the user.

## Hierarchy

- **`ProjectLogbookRecord`**

  ↳ [`ProjectJobHistoryRecord`](common_web_data_entities_project_logbook_ProjectJobHistoryRecord.ProjectJobHistoryRecord.md)

## Constructors

### constructor

• **new ProjectLogbookRecord**(`record`, `timestamp`, `seen?`): [`ProjectLogbookRecord`](common_web_data_entities_project_logbook_ProjectLogbookRecord.ProjectLogbookRecord.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `record` | `number` | `undefined` |
| `timestamp` | `number` | `undefined` |
| `seen` | `boolean` | `false` |

#### Returns

[`ProjectLogbookRecord`](common_web_data_entities_project_logbook_ProjectLogbookRecord.ProjectLogbookRecord.md)

#### Defined in

[src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L19)

## Properties

### record

• `Readonly` **record**: `number`

#### Defined in

[src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L14)

___

### seen

• `Readonly` **seen**: `boolean`

#### Defined in

[src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L17)

___

### timestamp

• `Readonly` **timestamp**: `number`

#### Defined in

[src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/project/logbook/ProjectLogbookRecord.ts#L15)
