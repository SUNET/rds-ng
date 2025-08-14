---
id: "common_web_ui_actions_notifiers_CallbackNotifier.CallbackNotifier"
title: "Class: CallbackNotifier"
sidebar_label: "CallbackNotifier"
custom_edit_url: null
---

[common/web/ui/actions/notifiers/CallbackNotifier](../modules/common_web_ui_actions_notifiers_CallbackNotifier.md).CallbackNotifier

A simple action notifier that calls a callback function on notification.

## Hierarchy

- [`ActionNotifier`](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md)

  ↳ **`CallbackNotifier`**

## Constructors

### constructor

• **new CallbackNotifier**(`callback`): [`CallbackNotifier`](common_web_ui_actions_notifiers_CallbackNotifier.CallbackNotifier.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `callback` | [`NotifierCallback`](../modules/common_web_ui_actions_notifiers_CallbackNotifier.md#notifiercallback) |

#### Returns

[`CallbackNotifier`](common_web_ui_actions_notifiers_CallbackNotifier.CallbackNotifier.md)

#### Overrides

[ActionNotifier](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md).[constructor](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md#constructor)

#### Defined in

[src/common/web/ui/actions/notifiers/CallbackNotifier.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/CallbackNotifier.ts#L11)

## Properties

### \_callback

• `Private` `Readonly` **\_callback**: [`NotifierCallback`](../modules/common_web_ui_actions_notifiers_CallbackNotifier.md#notifiercallback)

#### Defined in

[src/common/web/ui/actions/notifiers/CallbackNotifier.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/CallbackNotifier.ts#L9)

___

### MessagePlaceholder

▪ `Static` `Readonly` **MessagePlaceholder**: ``"$MSG$"``

#### Inherited from

[ActionNotifier](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md).[MessagePlaceholder](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md#messageplaceholder)

#### Defined in

[src/common/web/ui/actions/notifiers/ActionNotifier.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L7)

## Methods

### formatMessage

▸ **formatMessage**(`displayMessage`, `message`): `string`

#### Parameters

| Name | Type |
| :------ | :------ |
| `displayMessage` | `string` |
| `message` | `string` |

#### Returns

`string`

#### Inherited from

[ActionNotifier](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md).[formatMessage](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md#formatmessage)

#### Defined in

[src/common/web/ui/actions/notifiers/ActionNotifier.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L21)

___

### onFinished

▸ **onFinished**(): `void`

Called when the action has finished (independent of its success).

#### Returns

`void`

#### Inherited from

[ActionNotifier](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md).[onFinished](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md#onfinished)

#### Defined in

[src/common/web/ui/actions/notifiers/ActionNotifier.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L18)

___

### onNotify

▸ **onNotify**(`message`): `void`

Called when the action triggers its notification.

#### Parameters

| Name | Type |
| :------ | :------ |
| `message` | `string` |

#### Returns

`void`

#### Overrides

[ActionNotifier](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md).[onNotify](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md#onnotify)

#### Defined in

[src/common/web/ui/actions/notifiers/CallbackNotifier.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/CallbackNotifier.ts#L17)
