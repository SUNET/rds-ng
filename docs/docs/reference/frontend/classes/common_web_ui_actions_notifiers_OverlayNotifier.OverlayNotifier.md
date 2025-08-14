---
id: "common_web_ui_actions_notifiers_OverlayNotifier.OverlayNotifier"
title: "Class: OverlayNotifier"
sidebar_label: "OverlayNotifier"
custom_edit_url: null
---

[common/web/ui/actions/notifiers/OverlayNotifier](../modules/common_web_ui_actions_notifiers_OverlayNotifier.md).OverlayNotifier

Notifications displayed via overlay messages.

## Hierarchy

- [`ActionNotifier`](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md)

  ↳ **`OverlayNotifier`**

## Constructors

### constructor

• **new OverlayNotifier**(`type`, `caption`, `message`, `sticky?`): [`OverlayNotifier`](common_web_ui_actions_notifiers_OverlayNotifier.OverlayNotifier.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `type` | [`OverlayNotificationType`](../enums/common_web_ui_notifications_OverlayNotifications.OverlayNotificationType.md) | `undefined` | The notification type. |
| `caption` | `string` | `undefined` | The caption. |
| `message` | `string` | `undefined` | The message. |
| `sticky` | `boolean` | `false` | Whether the notification will be sticky. |

#### Returns

[`OverlayNotifier`](common_web_ui_actions_notifiers_OverlayNotifier.OverlayNotifier.md)

#### Overrides

[ActionNotifier](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md).[constructor](common_web_ui_actions_notifiers_ActionNotifier.ActionNotifier.md#constructor)

#### Defined in

[src/common/web/ui/actions/notifiers/OverlayNotifier.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/OverlayNotifier.ts#L20)

## Properties

### \_caption

• `Private` `Readonly` **\_caption**: `string`

#### Defined in

[src/common/web/ui/actions/notifiers/OverlayNotifier.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/OverlayNotifier.ts#L10)

___

### \_message

• `Private` `Readonly` **\_message**: `string`

#### Defined in

[src/common/web/ui/actions/notifiers/OverlayNotifier.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/OverlayNotifier.ts#L11)

___

### \_sticky

• `Private` `Readonly` **\_sticky**: `boolean`

#### Defined in

[src/common/web/ui/actions/notifiers/OverlayNotifier.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/OverlayNotifier.ts#L12)

___

### \_type

• `Private` `Readonly` **\_type**: [`OverlayNotificationType`](../enums/common_web_ui_notifications_OverlayNotifications.OverlayNotificationType.md)

#### Defined in

[src/common/web/ui/actions/notifiers/OverlayNotifier.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/OverlayNotifier.ts#L9)

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

[src/common/web/ui/actions/notifiers/OverlayNotifier.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/actions/notifiers/OverlayNotifier.ts#L29)
