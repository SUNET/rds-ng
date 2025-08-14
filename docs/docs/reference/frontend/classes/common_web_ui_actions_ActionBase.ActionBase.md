---
id: "common_web_ui_actions_ActionBase.ActionBase"
title: "Class: ActionBase"
sidebar_label: "ActionBase"
custom_edit_url: null
---

[common/web/ui/actions/ActionBase](../modules/common_web_ui_actions_ActionBase.md).ActionBase

Abstract base class for general actions.

## Hierarchy

- **`ActionBase`**

  ↳ [`Action`](common_web_ui_actions_Action.Action.md)

  ↳ [`MultiAction`](common_web_ui_actions_MultiAction.MultiAction.md)

## Constructors

### constructor

• **new ActionBase**(`suppressDefaultNotifiers?`): [`ActionBase`](common_web_ui_actions_ActionBase.ActionBase.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `suppressDefaultNotifiers` | `boolean` | `false` | Suppress default notifiers. |

#### Returns

[`ActionBase`](common_web_ui_actions_ActionBase.ActionBase.md)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L33)

## Properties

### \_notifiers

• `Private` `Readonly` **\_notifiers**: [`ActionNotifiers`](../modules/common_web_ui_actions_notifiers_ActionNotifier.md#actionnotifiers)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L27)

___

### \_state

• `Protected` **\_state**: [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L23)

___

### \_stateCallbacks

• `Private` `Readonly` **\_stateCallbacks**: [`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<[`ActionDoneCallback`](../modules/common_web_ui_actions_ActionBase.md#actiondonecallback), [`ActionFailCallback`](../modules/common_web_ui_actions_ActionBase.md#actionfailcallback)\>

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L25)

___

### \_suppressDefaultNotifiers

• `Private` `Readonly` **\_suppressDefaultNotifiers**: `boolean`

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L28)

## Accessors

### state

• `get` **state**(): [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

The current state of the action.

#### Returns

[`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

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

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L66)

___

### completed

▸ **completed**(`cb`): [`ActionBase`](common_web_ui_actions_ActionBase.ActionBase.md)

Adds a callback for action completion.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionDoneCallback`](../modules/common_web_ui_actions_ActionBase.md#actiondonecallback) | The callback to add. |

#### Returns

[`ActionBase`](common_web_ui_actions_ActionBase.ActionBase.md)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L44)

___

### execute

▸ **execute**(): `void`

Executes the action.

#### Returns

`void`

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:95](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L95)

___

### failed

▸ **failed**(`cb`): [`ActionBase`](common_web_ui_actions_ActionBase.ActionBase.md)

Adds a callback for action failure.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionFailCallback`](../modules/common_web_ui_actions_ActionBase.md#actionfailcallback) | The callback to add. |

#### Returns

[`ActionBase`](common_web_ui_actions_ActionBase.ActionBase.md)

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

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:134](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L134)

___

### postExecution

▸ **postExecution**(): `void`

#### Returns

`void`

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:138](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L138)

___

### preExecution

▸ **preExecution**(): `void`

#### Returns

`void`

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

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:103](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L103)
