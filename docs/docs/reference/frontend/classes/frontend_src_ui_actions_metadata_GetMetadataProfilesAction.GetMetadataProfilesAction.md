---
id: "frontend_src_ui_actions_metadata_GetMetadataProfilesAction.GetMetadataProfilesAction"
title: "Class: GetMetadataProfilesAction"
sidebar_label: "GetMetadataProfilesAction"
custom_edit_url: null
---

[frontend/src/ui/actions/metadata/GetMetadataProfilesAction](../modules/frontend_src_ui_actions_metadata_GetMetadataProfilesAction.md).GetMetadataProfilesAction

Action to retrieve all connectors.

## Hierarchy

- [`FrontendCommandAction`](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md)<[`GetMetadataProfilesCommand`](common_web_api_metadata_MetadataCommands.GetMetadataProfilesCommand.md), [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<[`GetMetadataProfilesCommand`](common_web_api_metadata_MetadataCommands.GetMetadataProfilesCommand.md)\>\>

  ↳ **`GetMetadataProfilesAction`**

## Constructors

### constructor

• **new GetMetadataProfilesAction**(`comp`, `suppressDefaultNotifiers?`): [`GetMetadataProfilesAction`](frontend_src_ui_actions_metadata_GetMetadataProfilesAction.GetMetadataProfilesAction.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) | `undefined` | The main frontend component. |
| `suppressDefaultNotifiers` | `boolean` | `false` | Suppress default notifiers. |

#### Returns

[`GetMetadataProfilesAction`](frontend_src_ui_actions_metadata_GetMetadataProfilesAction.GetMetadataProfilesAction.md)

#### Inherited from

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[constructor](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#constructor)

#### Defined in

[src/frontend/src/ui/actions/FrontendCommandAction.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/actions/FrontendCommandAction.ts#L17)

## Properties

### \_component

• `Protected` **\_component**: [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

#### Inherited from

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[_component](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#_component)

#### Defined in

[src/frontend/src/ui/actions/FrontendCommandAction.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/actions/FrontendCommandAction.ts#L11)

___

### \_composer

• `Protected` **\_composer**: ``null`` \| [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<[`GetMetadataProfilesCommand`](common_web_api_metadata_MetadataCommands.GetMetadataProfilesCommand.md)\> = `null`

#### Inherited from

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[_composer](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#_composer)

#### Defined in

[src/common/web/ui/actions/Action.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L19)

___

### \_state

• `Protected` **\_state**: [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Inherited from

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[_state](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#_state)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L23)

## Accessors

### messageBuilder

• `get` **messageBuilder**(): [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Returns

[`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Inherited from

FrontendCommandAction.messageBuilder

#### Defined in

[src/common/web/ui/actions/Action.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L59)

___

### state

• `get` **state**(): [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

The current state of the action.

#### Returns

[`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Inherited from

FrontendCommandAction.state

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:143](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L143)

## Methods

### addDefaultNotifiers

▸ **addDefaultNotifiers**(): `void`

#### Returns

`void`

#### Overrides

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[addDefaultNotifiers](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#adddefaultnotifiers)

#### Defined in

[src/frontend/src/ui/actions/metadata/GetMetadataProfilesAction.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/actions/metadata/GetMetadataProfilesAction.ts#L21)

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

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[addNotifier](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#addnotifier)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L66)

___

### completed

▸ **completed**(`cb`): [`GetMetadataProfilesAction`](frontend_src_ui_actions_metadata_GetMetadataProfilesAction.GetMetadataProfilesAction.md)

Adds a callback for action completion.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionDoneCallback`](../modules/common_web_ui_actions_ActionBase.md#actiondonecallback) | The callback to add. |

#### Returns

[`GetMetadataProfilesAction`](frontend_src_ui_actions_metadata_GetMetadataProfilesAction.GetMetadataProfilesAction.md)

#### Inherited from

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[completed](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#completed)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L44)

___

### execute

▸ **execute**(): `void`

Executes the action (i.e., the message will be emitted).

#### Returns

`void`

#### Inherited from

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[execute](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#execute)

#### Defined in

[src/common/web/ui/actions/Action.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L44)

___

### failed

▸ **failed**(`cb`): [`GetMetadataProfilesAction`](frontend_src_ui_actions_metadata_GetMetadataProfilesAction.GetMetadataProfilesAction.md)

Adds a callback for action failure.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionFailCallback`](../modules/common_web_ui_actions_ActionBase.md#actionfailcallback) | The callback to add. |

#### Returns

[`GetMetadataProfilesAction`](frontend_src_ui_actions_metadata_GetMetadataProfilesAction.GetMetadataProfilesAction.md)

#### Inherited from

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[failed](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#failed)

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

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[onStateChanged](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#onstatechanged)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:134](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L134)

___

### postExecution

▸ **postExecution**(): `void`

#### Returns

`void`

#### Inherited from

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[postExecution](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#postexecution)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:138](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L138)

___

### preExecution

▸ **preExecution**(): `void`

#### Returns

`void`

#### Inherited from

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[preExecution](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#preexecution)

#### Defined in

[src/common/web/ui/actions/CommandAction.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/CommandAction.ts#L11)

___

### prepare

▸ **prepare**(): [`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<[`GetMetadataProfilesCommand`](common_web_api_metadata_MetadataCommands.GetMetadataProfilesCommand.md)\>

Prepares this action.

#### Returns

[`CommandComposer`](common_web_core_messaging_composers_CommandComposer.CommandComposer.md)<[`GetMetadataProfilesCommand`](common_web_api_metadata_MetadataCommands.GetMetadataProfilesCommand.md)\>

- A message composer that can be further modified.

#### Overrides

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[prepare](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#prepare)

#### Defined in

[src/frontend/src/ui/actions/metadata/GetMetadataProfilesAction.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/actions/metadata/GetMetadataProfilesAction.ts#L14)

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

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[prepareNotifiers](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#preparenotifiers)

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

[FrontendCommandAction](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md).[setState](frontend_src_ui_actions_FrontendCommandAction.FrontendCommandAction.md#setstate)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:103](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L103)
