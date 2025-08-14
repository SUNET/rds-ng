---
id: "frontend_src_ui_tools_project_ProjectTools"
title: "Module: frontend/src/ui/tools/project/ProjectTools"
sidebar_label: "frontend/src/ui/tools/project/ProjectTools"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### useProjectTools

▸ **useProjectTools**(`comp`): `Object`

Tools for working with projects.

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](../classes/frontend_src_component_FrontendComponent.FrontendComponent.md) |

#### Returns

`Object`

| Name | Type |
| :------ | :------ |
| `deleteProject` | (`project`: [`Project`](../classes/common_web_data_entities_project_Project.Project.md)) => `void` |
| `editProject` | (`project`: [`Project`](../classes/common_web_data_entities_project_Project.Project.md)) => `Promise`<`void`\> |
| `newProject` | () => `Promise`<`void`\> |
| `uploadProject` | (`project`: [`Project`](../classes/common_web_data_entities_project_Project.Project.md)) => `Promise`<[`UploadProjectDialogData`](../interfaces/frontend_src_ui_dialogs_project_upload_UploadProjectDialog.UploadProjectDialogData.md)\> |

#### Defined in

[src/frontend/src/ui/tools/project/ProjectTools.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/tools/project/ProjectTools.ts#L12)
