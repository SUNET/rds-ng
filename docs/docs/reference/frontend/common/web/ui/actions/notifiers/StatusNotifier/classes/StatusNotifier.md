# Class: StatusNotifier

Defined in: [src/common/web/ui/actions/notifiers/StatusNotifier.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/StatusNotifier.ts#L8)

Notifications displayed via status messages.

## Extends

- [`ActionNotifier`](../../ActionNotifier/classes/ActionNotifier.md)

## Constructors

### Constructor

> **new StatusNotifier**(`type`, `message`, `icon`, `sticky`): `StatusNotifier`

Defined in: [src/common/web/ui/actions/notifiers/StatusNotifier.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/StatusNotifier.ts#L20)

#### Parameters

##### type

[`OverlayNotificationType`](../../../../notifications/OverlayNotifications/enumerations/OverlayNotificationType.md)

The notification type.

##### message

`string`

The message.

##### icon

`string`

The message icon.

##### sticky

`boolean` = `false`

Whether the notification will be sticky.

#### Returns

`StatusNotifier`

#### Overrides

[`ActionNotifier`](../../ActionNotifier/classes/ActionNotifier.md).[`constructor`](../../ActionNotifier/classes/ActionNotifier.md#constructor)

## Properties

### MessagePlaceholder

> `readonly` `static` **MessagePlaceholder**: `"$MSG$"` = `"$MSG$"`

Defined in: [src/common/web/ui/actions/notifiers/ActionNotifier.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L7)

#### Inherited from

[`ActionNotifier`](../../ActionNotifier/classes/ActionNotifier.md).[`MessagePlaceholder`](../../ActionNotifier/classes/ActionNotifier.md#messageplaceholder)

## Methods

### formatMessage()

> `protected` **formatMessage**(`displayMessage`, `message`): `string`

Defined in: [src/common/web/ui/actions/notifiers/ActionNotifier.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L21)

#### Parameters

##### displayMessage

`string`

##### message

`string`

#### Returns

`string`

#### Inherited from

[`ActionNotifier`](../../ActionNotifier/classes/ActionNotifier.md).[`formatMessage`](../../ActionNotifier/classes/ActionNotifier.md#formatmessage)

***

### onFinished()

> **onFinished**(): `void`

Defined in: [src/common/web/ui/actions/notifiers/ActionNotifier.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L18)

Called when the action has finished (independent of its success).

#### Returns

`void`

#### Inherited from

[`ActionNotifier`](../../ActionNotifier/classes/ActionNotifier.md).[`onFinished`](../../ActionNotifier/classes/ActionNotifier.md#onfinished)

***

### onNotify()

> **onNotify**(`message`): `void`

Defined in: [src/common/web/ui/actions/notifiers/StatusNotifier.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/StatusNotifier.ts#L29)

Called when the action triggers its notification.

#### Parameters

##### message

`string`

#### Returns

`void`

#### Overrides

[`ActionNotifier`](../../ActionNotifier/classes/ActionNotifier.md).[`onNotify`](../../ActionNotifier/classes/ActionNotifier.md#onnotify)
