# Function: getUnseenProjectJobHistoryRecords()

> **getUnseenProjectJobHistoryRecords**(`project`): [`ProjectJobHistoryRecord`](../../../../../../../common/web/data/entities/project/logbook/ProjectJobHistoryRecord/classes/ProjectJobHistoryRecord.md)[]

Defined in: [src/frontend/src/data/entities/project/ProjectUtils.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/project/ProjectUtils.ts#L11)

Gets all unseen job history records of a project.

## Parameters

### project

[`Project`](../../../../../../../common/web/data/entities/project/Project/classes/Project.md)

The project.

## Returns

[`ProjectJobHistoryRecord`](../../../../../../../common/web/data/entities/project/logbook/ProjectJobHistoryRecord/classes/ProjectJobHistoryRecord.md)[]

A list of all matching jobs.
