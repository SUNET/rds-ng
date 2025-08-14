---
id: "common_web_ui_actions_MultiAction.MultiAction"
title: "Class: MultiAction"
sidebar_label: "MultiAction"
custom_edit_url: null
---

[common/web/ui/actions/MultiAction](../modules/common_web_ui_actions_MultiAction.md).MultiAction

An action that encapsulates multiple other actions that are executed in order.

## Hierarchy

- [`ActionBase`](common_web_ui_actions_ActionBase.ActionBase.md)

  ↳ **`MultiAction`**

  ↳↳ [`GetAllDataAction`](frontend_src_ui_actions_multi_GetAllDataAction.GetAllDataAction.md)

## Constructors

### constructor

• **new MultiAction**(`suppressDefaultNotifiers?`): [`MultiAction`](common_web_ui_actions_MultiAction.MultiAction.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `suppressDefaultNotifiers` | `boolean` | `false` | Suppress default notifiers. |

#### Returns

[`MultiAction`](common_web_ui_actions_MultiAction.MultiAction.md)

#### Inherited from

[ActionBase](common_web_ui_actions_ActionBase.ActionBase.md).[constructor](common_web_ui_actions_ActionBase.ActionBase.md#constructor)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L33)

## Properties

### \_actions

• `Private` `Readonly` **\_actions**: [`ActionBase`](common_web_ui_actions_ActionBase.ActionBase.md)[]

#### Defined in

[src/common/web/ui/actions/MultiAction.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/MultiAction.ts#L8)

___

### \_currentAction

• `Private` **\_currentAction**: `number` = `-1`

#### Defined in

[src/common/web/ui/actions/MultiAction.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/MultiAction.ts#L9)

___

### \_state

• `Protected` **\_state**: [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Inherited from

[ActionBase](common_web_ui_actions_ActionBase.ActionBase.md).[_state](common_web_ui_actions_ActionBase.ActionBase.md#_state)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L23)

## Accessors

### state

• `get` **state**(): [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

The current state of the action.

#### Returns

[`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Inherited from

ActionBase.state

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

#### Defined in

[src/common/web/ui/actions/MultiAction.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/MultiAction.ts#L18)

___

### addDefaultNotifiers

▸ **addDefaultNotifiers**(`...args`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `...args` | `any`[] |

#### Returns

`void`

#### Inherited from

[ActionBase](common_web_ui_actions_ActionBase.ActionBase.md).[addDefaultNotifiers](common_web_ui_actions_ActionBase.ActionBase.md#adddefaultnotifiers)

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

[ActionBase](common_web_ui_actions_ActionBase.ActionBase.md).[addNotifier](common_web_ui_actions_ActionBase.ActionBase.md#addnotifier)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L66)

___

### completed

▸ **completed**(`cb`): [`MultiAction`](common_web_ui_actions_MultiAction.MultiAction.md)

Adds a callback for action completion.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionDoneCallback`](../modules/common_web_ui_actions_ActionBase.md#actiondonecallback) | The callback to add. |

#### Returns

[`MultiAction`](common_web_ui_actions_MultiAction.MultiAction.md)

#### Inherited from

[ActionBase](common_web_ui_actions_ActionBase.ActionBase.md).[completed](common_web_ui_actions_ActionBase.ActionBase.md#completed)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L44)

___

### execute

▸ **execute**(): `void`

Executes the action (i.e., all enqueued messages will be executed).

#### Returns

`void`

#### Overrides

[ActionBase](common_web_ui_actions_ActionBase.ActionBase.md).[execute](common_web_ui_actions_ActionBase.ActionBase.md#execute)

#### Defined in

[src/common/web/ui/actions/MultiAction.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/MultiAction.ts#L30)

___

### executeNextAction

▸ **executeNextAction**(): `void`

#### Returns

`void`

#### Defined in

[src/common/web/ui/actions/MultiAction.ts:45](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/MultiAction.ts#L45)

___

### failed

▸ **failed**(`cb`): [`MultiAction`](common_web_ui_actions_MultiAction.MultiAction.md)

Adds a callback for action failure.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionFailCallback`](../modules/common_web_ui_actions_ActionBase.md#actionfailcallback) | The callback to add. |

#### Returns

[`MultiAction`](common_web_ui_actions_MultiAction.MultiAction.md)

#### Inherited from

[ActionBase](common_web_ui_actions_ActionBase.ActionBase.md).[failed](common_web_ui_actions_ActionBase.ActionBase.md#failed)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L54)

___

### onActionDone

▸ **onActionDone**(`action`, `message`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `action` | [`ActionBase`](common_web_ui_actions_ActionBase.ActionBase.md) |
| `message` | `string` |

#### Returns

`void`

#### Defined in

[src/common/web/ui/actions/MultiAction.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/MultiAction.ts#L54)

___

### onActionFailed

▸ **onActionFailed**(`action`, `message`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `action` | [`ActionBase`](common_web_ui_actions_ActionBase.ActionBase.md) |
| `message` | `string` |

#### Returns

`void`

#### Defined in

[src/common/web/ui/actions/MultiAction.ts:58](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/MultiAction.ts#L58)

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

[ActionBase](common_web_ui_actions_ActionBase.ActionBase.md).[onStateChanged](common_web_ui_actions_ActionBase.ActionBase.md#onstatechanged)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:134](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L134)

___

### postExecution

▸ **postExecution**(): `void`

#### Returns

`void`

#### Inherited from

[ActionBase](common_web_ui_actions_ActionBase.ActionBase.md).[postExecution](common_web_ui_actions_ActionBase.ActionBase.md#postexecution)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:138](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L138)

___

### preExecution

▸ **preExecution**(): `void`

#### Returns

`void`

#### Inherited from

[ActionBase](common_web_ui_actions_ActionBase.ActionBase.md).[preExecution](common_web_ui_actions_ActionBase.ActionBase.md#preexecution)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:136](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L136)

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

[ActionBase](common_web_ui_actions_ActionBase.ActionBase.md).[prepareNotifiers](common_web_ui_actions_ActionBase.ActionBase.md#preparenotifiers)

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

[ActionBase](common_web_ui_actions_ActionBase.ActionBase.md).[setState](common_web_ui_actions_ActionBase.ActionBase.md#setstate)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:103](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L103)
