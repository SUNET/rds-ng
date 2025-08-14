---
id: "common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier"
title: "Class: ActionNotifier"
sidebar_label: "ActionNotifier"
custom_edit_url: null
---

[common/web/ui/actions/notifiers/ActionNotifier](../modules/common_web_ui_actions_notifiers_ActionNotifier.md).ActionNotifier

A snap-in for actions to display arbitrary notifications about the action execution.

## Hierarchy

- **`ActionNotifier`**

  ↳ [`CallbackNotifier`](common_web_ui_actions_notifiers_CallbackNotifier.CallbackNotifier.md)

  ↳ [`OverlayNotifier`](common_web_ui_actions_notifiers_OverlayNotifier.OverlayNotifier.md)

  ↳ [`StatusNotifier`](common_web_ui_actions_notifiers_StatusNotifier.StatusNotifier.md)

## Constructors

### constructor

• **new ActionNotifier**(): [`ActionNotifier`](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md)

#### Returns

[`ActionNotifier`](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md)

## Properties

### MessagePlaceholder

▪ `Static` `Readonly` **MessagePlaceholder**: ``"$MSG$"``

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

#### Defined in

[src/common/web/ui/actions/notifiers/ActionNotifier.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L21)

___

### onFinished

▸ **onFinished**(): `void`

Called when the action has finished (independent of its success).

#### Returns

`void`

#### Defined in

[src/common/web/ui/actions/notifiers/ActionNotifier.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L18)

___

### onNotify

▸ **onNotify**(`message?`): `void`

Called when the action triggers its notification.

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `message` | `string` | `""` |

#### Returns

`void`

#### Defined in

[src/common/web/ui/actions/notifiers/ActionNotifier.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L12)
