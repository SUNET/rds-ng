---
id: "common_web_ui_actions_notifiers_StatusNotifier.StatusNotifier"
title: "Class: StatusNotifier"
sidebar_label: "StatusNotifier"
custom_edit_url: null
---

[common/web/ui/actions/notifiers/StatusNotifier](../modules/common_web_ui_actions_notifiers_StatusNotifier.md).StatusNotifier

Notifications displayed via status messages.

## Hierarchy

- [`ActionNotifier`](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md)

  ↳ **`StatusNotifier`**

## Constructors

### constructor

• **new StatusNotifier**(`type`, `message`, `icon`, `sticky?`): [`StatusNotifier`](common_web_ui_actions_notifiers_StatusNotifier.StatusNotifier.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `type` | [`OverlayNotificationType`](../enums/common_web_ui_notifications_OverlayNotifications.OverlayNotificationType.md) | `undefined` | The notification type. |
| `message` | `string` | `undefined` | The message. |
| `icon` | `string` | `undefined` | The message icon. |
| `sticky` | `boolean` | `false` | Whether the notification will be sticky. |

#### Returns

[`StatusNotifier`](common_web_ui_actions_notifiers_StatusNotifier.StatusNotifier.md)

#### Overrides

[ActionNotifier](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md).[constructor](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md#constructor)

#### Defined in

[src/common/web/ui/actions/notifiers/StatusNotifier.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/StatusNotifier.ts#L20)

## Properties

### \_icon

• `Private` `Readonly` **\_icon**: `string`

#### Defined in

[src/common/web/ui/actions/notifiers/StatusNotifier.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/StatusNotifier.ts#L11)

___

### \_message

• `Private` `Readonly` **\_message**: `string`

#### Defined in

[src/common/web/ui/actions/notifiers/StatusNotifier.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/StatusNotifier.ts#L10)

___

### \_sticky

• `Private` `Readonly` **\_sticky**: `boolean`

#### Defined in

[src/common/web/ui/actions/notifiers/StatusNotifier.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/StatusNotifier.ts#L12)

___

### \_type

• `Private` `Readonly` **\_type**: [`OverlayNotificationType`](../enums/common_web_ui_notifications_OverlayNotifications.OverlayNotificationType.md)

#### Defined in

[src/common/web/ui/actions/notifiers/StatusNotifier.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/StatusNotifier.ts#L9)

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

[src/common/web/ui/actions/notifiers/StatusNotifier.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/StatusNotifier.ts#L29)
