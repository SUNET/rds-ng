---
id: "frontend_src_ui_actions_project_TouchProjectAction.TouchProjectAction"
title: "Class: TouchProjectAction"
sidebar_label: "TouchProjectAction"
custom_edit_url: null
---

[frontend/src/ui/actions/project/TouchProjectAction](../modules/frontend_src_ui_actions_project_TouchProjectAction.md).TouchProjectAction

Action to touch a project.

## Hierarchy

- [`FrontendEventAction`](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md)<[`ProjectTouchEvent`](common_web_api_project_ProjectEvents.ProjectTouchEvent.md), [`EventComposer`](common_web_core_messaging_composers_EventComposer.EventComposer.md)<[`ProjectTouchEvent`](common_web_api_project_ProjectEvents.ProjectTouchEvent.md)\>\>

  ↳ **`TouchProjectAction`**

## Constructors

### constructor

• **new TouchProjectAction**(`comp`, `suppressDefaultNotifiers?`): [`TouchProjectAction`](frontend_src_ui_actions_project_TouchProjectAction.TouchProjectAction.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) | `undefined` | The main frontend component. |
| `suppressDefaultNotifiers` | `boolean` | `false` | Suppress default notifiers. |

#### Returns

[`TouchProjectAction`](frontend_src_ui_actions_project_TouchProjectAction.TouchProjectAction.md)

#### Inherited from

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[constructor](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#constructor)

#### Defined in

[src/frontend/src/ui/actions/FrontendEventAction.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/actions/FrontendEventAction.ts#L15)

## Properties

### \_composer

• `Protected` **\_composer**: ``null`` \| [`EventComposer`](common_web_core_messaging_composers_EventComposer.EventComposer.md)<[`ProjectTouchEvent`](common_web_api_project_ProjectEvents.ProjectTouchEvent.md)\> = `null`

#### Inherited from

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[_composer](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#_composer)

#### Defined in

[src/common/web/ui/actions/Action.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L19)

___

### \_state

• `Protected` **\_state**: [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Inherited from

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[_state](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#_state)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L23)

## Accessors

### messageBuilder

• `get` **messageBuilder**(): [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Returns

[`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Inherited from

FrontendEventAction.messageBuilder

#### Defined in

[src/common/web/ui/actions/Action.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L59)

___

### state

• `get` **state**(): [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

The current state of the action.

#### Returns

[`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Inherited from

FrontendEventAction.state

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

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[addDefaultNotifiers](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#adddefaultnotifiers)

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

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[addNotifier](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#addnotifier)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L66)

___

### completed

▸ **completed**(`cb`): [`TouchProjectAction`](frontend_src_ui_actions_project_TouchProjectAction.TouchProjectAction.md)

Adds a callback for action completion.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionDoneCallback`](../modules/common_web_ui_actions_ActionBase.md#actiondonecallback) | The callback to add. |

#### Returns

[`TouchProjectAction`](frontend_src_ui_actions_project_TouchProjectAction.TouchProjectAction.md)

#### Inherited from

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[completed](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#completed)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L44)

___

### execute

▸ **execute**(): `void`

Executes the action (i.e., the message will be emitted).

#### Returns

`void`

#### Inherited from

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[execute](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#execute)

#### Defined in

[src/common/web/ui/actions/Action.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L44)

___

### failed

▸ **failed**(`cb`): [`TouchProjectAction`](frontend_src_ui_actions_project_TouchProjectAction.TouchProjectAction.md)

Adds a callback for action failure.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionFailCallback`](../modules/common_web_ui_actions_ActionBase.md#actionfailcallback) | The callback to add. |

#### Returns

[`TouchProjectAction`](frontend_src_ui_actions_project_TouchProjectAction.TouchProjectAction.md)

#### Inherited from

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[failed](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#failed)

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

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[onStateChanged](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#onstatechanged)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:134](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L134)

___

### postExecution

▸ **postExecution**(): `void`

#### Returns

`void`

#### Inherited from

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[postExecution](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#postexecution)

#### Defined in

[src/common/web/ui/actions/EventAction.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/EventAction.ts#L10)

___

### preExecution

▸ **preExecution**(): `void`

#### Returns

`void`

#### Inherited from

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[preExecution](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#preexecution)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:136](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L136)

___

### prepare

▸ **prepare**(`projectID`): [`EventComposer`](common_web_core_messaging_composers_EventComposer.EventComposer.md)<[`ProjectTouchEvent`](common_web_api_project_ProjectEvents.ProjectTouchEvent.md)\>

Prepares this action.

#### Parameters

| Name | Type |
| :------ | :------ |
| `projectID` | `number` |

#### Returns

[`EventComposer`](common_web_core_messaging_composers_EventComposer.EventComposer.md)<[`ProjectTouchEvent`](common_web_api_project_ProjectEvents.ProjectTouchEvent.md)\>

- A message composer that can be further modified.

#### Overrides

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[prepare](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#prepare)

#### Defined in

[src/frontend/src/ui/actions/project/TouchProjectAction.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/actions/project/TouchProjectAction.ts#L11)

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

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[prepareNotifiers](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#preparenotifiers)

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

[FrontendEventAction](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md).[setState](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md#setstate)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:103](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L103)
