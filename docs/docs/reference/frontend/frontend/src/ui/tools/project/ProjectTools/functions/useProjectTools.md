# Function: useProjectTools()

> **useProjectTools**(`comp`): `object`

Defined in: [src/frontend/src/ui/tools/project/ProjectTools.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/tools/project/ProjectTools.ts#L12)

Tools for working with projects.

## Parameters

### comp

[`FrontendComponent`](../../../../../component/FrontendComponent/classes/FrontendComponent.md)

## Returns

`object`

### deleteProject()

> **deleteProject**: (`project`) => `void`

#### Parameters

##### project

[`Project`](../../../../../../../common/web/data/entities/project/Project/classes/Project.md)

#### Returns

`void`

### editProject()

> **editProject**: (`project`) => `Promise`\<`void`\>

#### Parameters

##### project

[`Project`](../../../../../../../common/web/data/entities/project/Project/classes/Project.md)

#### Returns

`Promise`\<`void`\>

### newProject()

> **newProject**: () => `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

### uploadProject()

> **uploadProject**: (`project`) => `Promise`\<[`UploadProjectDialogData`](../../../../dialogs/project/upload/UploadProjectDialog/interfaces/UploadProjectDialogData.md)\>

#### Parameters

##### project

[`Project`](../../../../../../../common/web/data/entities/project/Project/classes/Project.md)

#### Returns

`Promise`\<[`UploadProjectDialogData`](../../../../dialogs/project/upload/UploadProjectDialog/interfaces/UploadProjectDialogData.md)\>
