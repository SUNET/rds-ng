---
id: "frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction"
title: "Class: FrontendCommandAction<CmdType, CompType>"
sidebar_label: "FrontendCommandAction"
custom_edit_url: null
---

[frontend/src/ui/actions/FrontendCommandAction](../modules/frontend_src_ui_actions_FrontendCommandAction.md).FrontendCommandAction

Command actions specific to the frontend.

## Type parameters

| Name | Type |
| :------ | :------ |
| `CmdType` | extends [`Command`](common_web_core_messaging_Command.Command.md) |
| `CompType` | extends [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`CmdType`\> |

## Hierarchy

- [`CommandAction`](common_web_ui_actions_CommandAction.CommandAction.md)<`CmdType`, `CompType`\>

  ↳ **`FrontendCommandAction`**

  ↳↳ [`ListUserAuthorizationsAction`](frontend_src_ui_actions_authorization_ListUserAuthorizationsAction.ListUserAuthorizationsAction.md)

  ↳↳ [`RevokeAuthorizationAction`](frontend_src_ui_actions_authorization_RevokeAuthorizationAction.RevokeAuthorizationAction.md)

  ↳↳ [`ListConnectorsAction`](frontend_src_ui_actions_connector_ListConnectorsAction.ListConnectorsAction.md)

  ↳↳ [`GetMetadataProfilesAction`](frontend_src_ui_actions_metadata_GetMetadataProfilesAction.GetMetadataProfilesAction.md)

  ↳↳ [`CreateProjectAction`](frontend_src_ui_actions_project_CreateProjectAction.CreateProjectAction.md)

  ↳↳ [`DeleteProjectAction`](frontend_src_ui_actions_project_DeleteProjectAction.DeleteProjectAction.md)

  ↳↳ [`ExportProjectAction`](frontend_src_ui_actions_project_ExportProjectAction.ExportProjectAction.md)

  ↳↳ [`InitiateProjectJobAction`](frontend_src_ui_actions_project_InitiateProjectJobAction.InitiateProjectJobAction.md)

  ↳↳ [`ListProjectJobsAction`](frontend_src_ui_actions_project_ListProjectJobsAction.ListProjectJobsAction.md)

  ↳↳ [`ListProjectgExportersAction`](frontend_src_ui_actions_project_ListProjectgExportersAction.ListProjectgExportersAction.md)

  ↳↳ [`ListProjectsAction`](frontend_src_ui_actions_project_ListProjectsAction.ListProjectsAction.md)

  ↳↳ [`MarkProjectLogbookSeenAction`](frontend_src_ui_actions_project_MarkProjectLogbookSeenAction.MarkProjectLogbookSeenAction.md)

  ↳↳ [`UpdateProjectAction`](frontend_src_ui_actions_project_UpdateProjectAction.UpdateProjectAction.md)

  ↳↳ [`UpdateProjectFeaturesAction`](frontend_src_ui_actions_project_UpdateProjectFeaturesAction.UpdateProjectFeaturesAction.md)

  ↳↳ [`GetResourceAction`](frontend_src_ui_actions_resource_GetResourceAction.GetResourceAction.md)

  ↳↳ [`ListResourcesAction`](frontend_src_ui_actions_resource_ListResourcesAction.ListResourcesAction.md)

  ↳↳ [`GetSessionValueAction`](frontend_src_ui_actions_session_GetSessionValueAction.GetSessionValueAction.md)

  ↳↳ [`SetSessionValueAction`](frontend_src_ui_actions_session_SetSessionValueAction.SetSessionValueAction.md)

  ↳↳ [`GetUserSettingsAction`](frontend_src_ui_actions_user_GetUserSettingsAction.GetUserSettingsAction.md)

  ↳↳ [`SetUserSettingsAction`](frontend_src_ui_actions_user_SetUserSettingsAction.SetUserSettingsAction.md)

## Constructors

### constructor

• **new FrontendCommandAction**<`CmdType`, `CompType`\>(`comp`, `suppressDefaultNotifiers?`): [`FrontendCommandAction`](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md)<`CmdType`, `CompType`\>

#### Type parameters

| Name | Type |
| :------ | :------ |
| `CmdType` | extends [`Command`](common_web_core_messaging_Command.Command.md) |
| `CompType` | extends [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<`CmdType`\> |

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) | `undefined` | The main frontend component. |
| `suppressDefaultNotifiers` | `boolean` | `false` | Suppress default notifiers. |

#### Returns

[`FrontendCommandAction`](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md)<`CmdType`, `CompType`\>

#### Overrides

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[constructor](common_web_ui_actions_CommandAction.CommandAction.md#constructor)

#### Defined in

[src/frontend/src/ui/actions/FrontendCommandAction.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/actions/FrontendCommandAction.ts#L17)

## Properties

### \_component

• `Protected` **\_component**: [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

#### Defined in

[src/frontend/src/ui/actions/FrontendCommandAction.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/actions/FrontendCommandAction.ts#L11)

___

### \_composer

• `Protected` **\_composer**: ``null`` \| `CompType` = `null`

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[_composer](common_web_ui_actions_CommandAction.CommandAction.md#_composer)

#### Defined in

[src/common/web/ui/actions/Action.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L19)

___

### \_state

• `Protected` **\_state**: [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[_state](common_web_ui_actions_CommandAction.CommandAction.md#_state)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L23)

## Accessors

### messageBuilder

• `get` **messageBuilder**(): [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Returns

[`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Inherited from

CommandAction.messageBuilder

#### Defined in

[src/common/web/ui/actions/Action.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L59)

___

### state

• `get` **state**(): [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

The current state of the action.

#### Returns

[`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Inherited from

CommandAction.state

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:143](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L143)

## Methods

### addDefaultNotifiers

▸ **addDefaultNotifiers**(`...args`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `...args` | `any`[] |

#### Returns

`void`

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[addDefaultNotifiers](common_web_ui_actions_CommandAction.CommandAction.md#adddefaultnotifiers)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:90](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L90)

___

### addNotifier

▸ **addNotifier**(`state`, `notifier`, `verboseOnly?`): `void`

Adds a new notifier for the specified state.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `state` | [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md) | `undefined` | The state the notifier should react to. |
| `notifier` | [`ActionNotifier`](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md) \| [`ActionNotifier`](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md)[] | `undefined` | The notifier. |
| `verboseOnly` | `boolean` | `false` | If true, the notification will only be added in verbose mode. |

#### Returns

`void`

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[addNotifier](common_web_ui_actions_CommandAction.CommandAction.md#addnotifier)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L66)

___

### completed

▸ **completed**(`cb`): [`FrontendCommandAction`](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md)<`CmdType`, `CompType`\>

Adds a callback for action completion.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionDoneCallback`](../modules/common_web_ui_actions_ActionBase.md#actiondonecallback) | The callback to add. |

#### Returns

[`FrontendCommandAction`](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md)<`CmdType`, `CompType`\>

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[completed](common_web_ui_actions_CommandAction.CommandAction.md#completed)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L44)

___

### execute

▸ **execute**(): `void`

Executes the action (i.e., the message will be emitted).

#### Returns

`void`

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[execute](common_web_ui_actions_CommandAction.CommandAction.md#execute)

#### Defined in

[src/common/web/ui/actions/Action.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L44)

___

### failed

▸ **failed**(`cb`): [`FrontendCommandAction`](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md)<`CmdType`, `CompType`\>

Adds a callback for action failure.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionFailCallback`](../modules/common_web_ui_actions_ActionBase.md#actionfailcallback) | The callback to add. |

#### Returns

[`FrontendCommandAction`](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md)<`CmdType`, `CompType`\>

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[failed](common_web_ui_actions_CommandAction.CommandAction.md#failed)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L54)

___

### onStateChanged

▸ **onStateChanged**(`newState`, `oldState`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `newState` | [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md) |
| `oldState` | [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md) |

#### Returns

`void`

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[onStateChanged](common_web_ui_actions_CommandAction.CommandAction.md#onstatechanged)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:134](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L134)

___

### postExecution

▸ **postExecution**(): `void`

#### Returns

`void`

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[postExecution](common_web_ui_actions_CommandAction.CommandAction.md#postexecution)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:138](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L138)

___

### preExecution

▸ **preExecution**(): `void`

#### Returns

`void`

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[preExecution](common_web_ui_actions_CommandAction.CommandAction.md#preexecution)

#### Defined in

[src/common/web/ui/actions/CommandAction.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/CommandAction.ts#L11)

___

### prepare

▸ **prepare**(`...args`): `CompType`

Prepares this action.

#### Parameters

| Name | Type |
| :------ | :------ |
| `...args` | `any`[] |

#### Returns

`CompType`

- A message composer that can be further modified.

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[prepare](common_web_ui_actions_CommandAction.CommandAction.md#prepare)

#### Defined in

[src/common/web/ui/actions/Action.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L39)

___

### prepareNotifiers

▸ **prepareNotifiers**(`...args`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `...args` | `any`[] |

#### Returns

`void`

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[prepareNotifiers](common_web_ui_actions_CommandAction.CommandAction.md#preparenotifiers)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:84](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L84)

___

### setState

▸ **setState**(`state`, `message?`): `void`

Sets the active state of this action.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `state` | [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md) | `undefined` | The state to apply |
| `message` | `string` | `""` | An optional notification message. |

#### Returns

`void`

#### Inherited from

[CommandAction](common_web_ui_actions_CommandAction.CommandAction.md).[setState](common_web_ui_actions_CommandAction.CommandAction.md#setstate)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:103](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L103)
