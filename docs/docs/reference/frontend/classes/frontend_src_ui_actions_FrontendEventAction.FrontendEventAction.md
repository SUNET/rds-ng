---
id: "frontend_src_ui_actions_FrontendEventAction.FrontendEventAction"
title: "Class: FrontendEventAction<EventType, CompType>"
sidebar_label: "FrontendEventAction"
custom_edit_url: null
---

[frontend/src/ui/actions/FrontendEventAction](../modules/frontend_src_ui_actions_FrontendEventAction.md).FrontendEventAction

Event actions specific to the frontend.

## Type parameters

| Name | Type |
| :------ | :------ |
| `EventType` | extends [`Event`](common_web_core_messaging_Event.Event.md) |
| `CompType` | extends [`EventComposer`](common_web_core_messaging_composers_EventComposer.EventComposer.md)<`EventType`\> |

## Hierarchy

- [`EventAction`](common_web_ui_actions_EventAction.EventAction.md)<`EventType`, `CompType`\>

  ↳ **`FrontendEventAction`**

  ↳↳ [`TouchProjectAction`](frontend_src_ui_actions_project_TouchProjectAction.TouchProjectAction.md)

## Constructors

### constructor

• **new FrontendEventAction**<`EventType`, `CompType`\>(`comp`, `suppressDefaultNotifiers?`): [`FrontendEventAction`](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md)<`EventType`, `CompType`\>

#### Type parameters

| Name | Type |
| :------ | :------ |
| `EventType` | extends [`Event`](common_web_core_messaging_Event.Event.md) |
| `CompType` | extends [`EventComposer`](common_web_core_messaging_composers_EventComposer.EventComposer.md)<`EventType`\> |

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) | `undefined` | The main frontend component. |
| `suppressDefaultNotifiers` | `boolean` | `false` | Suppress default notifiers. |

#### Returns

[`FrontendEventAction`](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md)<`EventType`, `CompType`\>

#### Overrides

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[constructor](common_web_ui_actions_EventAction.EventAction.md#constructor)

#### Defined in

[src/frontend/src/ui/actions/FrontendEventAction.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/actions/FrontendEventAction.ts#L15)

## Properties

### \_composer

• `Protected` **\_composer**: ``null`` \| `CompType` = `null`

#### Inherited from

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[_composer](common_web_ui_actions_EventAction.EventAction.md#_composer)

#### Defined in

[src/common/web/ui/actions/Action.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L19)

___

### \_state

• `Protected` **\_state**: [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Inherited from

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[_state](common_web_ui_actions_EventAction.EventAction.md#_state)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L23)

## Accessors

### messageBuilder

• `get` **messageBuilder**(): [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Returns

[`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Inherited from

EventAction.messageBuilder

#### Defined in

[src/common/web/ui/actions/Action.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L59)

___

### state

• `get` **state**(): [`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

The current state of the action.

#### Returns

[`ActionState`](../enums/common_web_ui_actions_ActionBase.ActionState.md)

#### Inherited from

EventAction.state

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

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[addDefaultNotifiers](common_web_ui_actions_EventAction.EventAction.md#adddefaultnotifiers)

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

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[addNotifier](common_web_ui_actions_EventAction.EventAction.md#addnotifier)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L66)

___

### completed

▸ **completed**(`cb`): [`FrontendEventAction`](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md)<`EventType`, `CompType`\>

Adds a callback for action completion.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionDoneCallback`](../modules/common_web_ui_actions_ActionBase.md#actiondonecallback) | The callback to add. |

#### Returns

[`FrontendEventAction`](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md)<`EventType`, `CompType`\>

#### Inherited from

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[completed](common_web_ui_actions_EventAction.EventAction.md#completed)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L44)

___

### execute

▸ **execute**(): `void`

Executes the action (i.e., the message will be emitted).

#### Returns

`void`

#### Inherited from

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[execute](common_web_ui_actions_EventAction.EventAction.md#execute)

#### Defined in

[src/common/web/ui/actions/Action.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/Action.ts#L44)

___

### failed

▸ **failed**(`cb`): [`FrontendEventAction`](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md)<`EventType`, `CompType`\>

Adds a callback for action failure.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ActionFailCallback`](../modules/common_web_ui_actions_ActionBase.md#actionfailcallback) | The callback to add. |

#### Returns

[`FrontendEventAction`](frontend_src_ui_actions_FrontendEventAction.FrontendEventAction.md)<`EventType`, `CompType`\>

#### Inherited from

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[failed](common_web_ui_actions_EventAction.EventAction.md#failed)

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

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[onStateChanged](common_web_ui_actions_EventAction.EventAction.md#onstatechanged)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:134](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L134)

___

### postExecution

▸ **postExecution**(): `void`

#### Returns

`void`

#### Inherited from

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[postExecution](common_web_ui_actions_EventAction.EventAction.md#postexecution)

#### Defined in

[src/common/web/ui/actions/EventAction.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/EventAction.ts#L10)

___

### preExecution

▸ **preExecution**(): `void`

#### Returns

`void`

#### Inherited from

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[preExecution](common_web_ui_actions_EventAction.EventAction.md#preexecution)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:136](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L136)

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

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[prepare](common_web_ui_actions_EventAction.EventAction.md#prepare)

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

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[prepareNotifiers](common_web_ui_actions_EventAction.EventAction.md#preparenotifiers)

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

[EventAction](common_web_ui_actions_EventAction.EventAction.md).[setState](common_web_ui_actions_EventAction.EventAction.md#setstate)

#### Defined in

[src/common/web/ui/actions/ActionBase.ts:103](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/ActionBase.ts#L103)
