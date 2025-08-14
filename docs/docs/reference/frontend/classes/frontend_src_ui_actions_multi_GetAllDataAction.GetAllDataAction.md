---
id: "frontend_src_ui_actions_multi_GetAllDataAction.GetAllDataAction"
title: "Class: GetAllDataAction"
sidebar_label: "GetAllDataAction"
custom_edit_url: null
---

[frontend/src/ui/actions/multi/GetAllDataAction](../modules/frontend_src_ui_actions_multi_GetAllDataAction.md).GetAllDataAction

Multi-action to fetch all data from the server.

## Hierarchy

- [`MultiAction`](common_web_ui_actions_MultiAction.MultiAction.md)

  ↳ **`GetAllDataAction`**

## Constructors

### constructor

• **new GetAllDataAction**(`suppressDefaultNotifiers?`): [`GetAllDataAction`](frontend_src_ui_actions_multi_GetAllDataAction.GetAllDataAction.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `suppressDefaultNotifiers` | `boolean` | `false` | Suppress default notifiers. |

#### Returns

[`GetAllDataAction`](frontend_src_ui_actions_multi_GetAllDataAction.GetAllDataAction.md)

#### Inherited from

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[constructor](common_web_ui_actions_MultiAction.MultiAction.md#constructor)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L33)

## Properties

### \_state

• `Protected` **\_state**: [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Inherited from

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[_state](common_web_ui_actions_MultiAction.MultiAction.md#_state)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L23)

## Accessors

### state

• `get` **state**(): [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

The current state of the action.

#### Returns

[`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Inherited from

MultiAction.state

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:143](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L143)

## Methods

### addActions

▸ **addActions**(`actions`): `void`

Enqueues new actions.

Note that actions are executed synchronously in the order in which they were added.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `actions` | [`ActionBase`](common_web_ui_actions_ActionBase.ActionBase.md)[] | The actions to add. |

#### Returns

`void`

#### Inherited from

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[addActions](common_web_ui_actions_MultiAction.MultiAction.md#addactions)

#### Defined in

[src/common/web/ui/actions/MultiAction.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/MultiAction.ts#L18)

___

### addDefaultNotifiers

▸ **addDefaultNotifiers**(): `void`

#### Returns

`void`

#### Overrides

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[addDefaultNotifiers](common_web_ui_actions_MultiAction.MultiAction.md#adddefaultnotifiers)

#### Defined in

[src/frontend/src/ui/actions/multi/GetAllDataAction.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/actions/multi/GetAllDataAction.ts#L50)

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

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[addNotifier](common_web_ui_actions_MultiAction.MultiAction.md#addnotifier)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L66)

___

### completed

▸ **completed**(`cb`): [`GetAllDataAction`](frontend_src_ui_actions_multi_GetAllDataAction.GetAllDataAction.md)

Adds a callback for action completion.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionDoneCallback`](../modules/common_web_ui_actions_ActionBase.md#actiondonecallback) | The callback to add. |

#### Returns

[`GetAllDataAction`](frontend_src_ui_actions_multi_GetAllDataAction.GetAllDataAction.md)

#### Inherited from

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[completed](common_web_ui_actions_MultiAction.MultiAction.md#completed)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L44)

___

### execute

▸ **execute**(): `void`

Executes the action (i.e., all enqueued messages will be executed).

#### Returns

`void`

#### Inherited from

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[execute](common_web_ui_actions_MultiAction.MultiAction.md#execute)

#### Defined in

[src/common/web/ui/actions/MultiAction.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/MultiAction.ts#L30)

___

### failed

▸ **failed**(`cb`): [`GetAllDataAction`](frontend_src_ui_actions_multi_GetAllDataAction.GetAllDataAction.md)

Adds a callback for action failure.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionFailCallback`](../modules/common_web_ui_actions_ActionBase.md#actionfailcallback) | The callback to add. |

#### Returns

[`GetAllDataAction`](frontend_src_ui_actions_multi_GetAllDataAction.GetAllDataAction.md)

#### Inherited from

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[failed](common_web_ui_actions_MultiAction.MultiAction.md#failed)

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

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[onStateChanged](common_web_ui_actions_MultiAction.MultiAction.md#onstatechanged)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:134](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L134)

___

### postExecution

▸ **postExecution**(): `void`

#### Returns

`void`

#### Inherited from

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[postExecution](common_web_ui_actions_MultiAction.MultiAction.md#postexecution)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:138](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L138)

___

### preExecution

▸ **preExecution**(): `void`

#### Returns

`void`

#### Inherited from

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[preExecution](common_web_ui_actions_MultiAction.MultiAction.md#preexecution)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:136](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L136)

___

### prepare

▸ **prepare**(`comp`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) |

#### Returns

`void`

#### Defined in

[src/frontend/src/ui/actions/multi/GetAllDataAction.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/actions/multi/GetAllDataAction.ts#L20)

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

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[prepareNotifiers](common_web_ui_actions_MultiAction.MultiAction.md#preparenotifiers)

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

[MultiAction](common_web_ui_actions_MultiAction.MultiAction.md).[setState](common_web_ui_actions_MultiAction.MultiAction.md#setstate)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:103](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L103)
