# Class: OverlayNotifications

Defined in: [src/common/web/ui/notifications/OverlayNotifications.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/notifications/OverlayNotifications.ts#L19)

A helper class to display notifications using PrimeVue's Toast.

## Constructors

### Constructor

> **new OverlayNotifications**(`comp`): `OverlayNotifications`

Defined in: [src/common/web/ui/notifications/OverlayNotifications.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/notifications/OverlayNotifications.ts#L26)

#### Parameters

##### comp

[`WebComponent`](../../../../component/WebComponent/classes/WebComponent.md)

The global component.

#### Returns

`OverlayNotifications`

## Methods

### clearStatus()

> **clearStatus**(`options`): `void`

Defined in: [src/common/web/ui/notifications/OverlayNotifications.ts:121](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/notifications/OverlayNotifications.ts#L121)

Clear any status notifications.

#### Parameters

##### options

`any` = `undefined`

An optional message to clear.

#### Returns

`void`

***

### error()

> **error**(`caption`, `message`, `sticky`): `void`

Defined in: [src/common/web/ui/notifications/OverlayNotifications.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/notifications/OverlayNotifications.ts#L72)

Display an error notification.

#### Parameters

##### caption

`string`

The notification caption.

##### message

`string`

The notification message.

##### sticky

`boolean` = `false`

Whether the notification will be sticky.

#### Returns

`void`

***

### info()

> **info**(`caption`, `message`, `sticky`): `void`

Defined in: [src/common/web/ui/notifications/OverlayNotifications.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/notifications/OverlayNotifications.ts#L39)

Display an info notification.

#### Parameters

##### caption

`string`

The notification caption.

##### message

`string`

The notification message.

##### sticky

`boolean` = `false`

Whether the notification will be sticky.

#### Returns

`void`

***

### notify()

> **notify**(`type`, `caption`, `message`, `sticky`): `void`

Defined in: [src/common/web/ui/notifications/OverlayNotifications.ts:84](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/notifications/OverlayNotifications.ts#L84)

Display a notification.

#### Parameters

##### type

[`OverlayNotificationType`](../enumerations/OverlayNotificationType.md)

The notification type.

##### caption

`string`

The notification caption.

##### message

`string`

The notification message.

##### sticky

`boolean`

Whether the notification will be sticky.

#### Returns

`void`

***

### notifyStatus()

> **notifyStatus**(`type`, `message`, `icon`, `sticky`): `any`

Defined in: [src/common/web/ui/notifications/OverlayNotifications.ts:102](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/notifications/OverlayNotifications.ts#L102)

Display a status notification.

#### Parameters

##### type

[`OverlayNotificationType`](../enumerations/OverlayNotificationType.md)

The notification type.

##### message

`string`

The notification message.

##### icon

The notification icon.

`undefined` | `string`

##### sticky

`boolean` = `true`

Whether the notification will be sticky.

#### Returns

`any`

***

### success()

> **success**(`caption`, `message`, `sticky`): `void`

Defined in: [src/common/web/ui/notifications/OverlayNotifications.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/notifications/OverlayNotifications.ts#L50)

Display a success notification.

#### Parameters

##### caption

`string`

The notification caption.

##### message

`string`

The notification message.

##### sticky

`boolean` = `false`

Whether the notification will be sticky.

#### Returns

`void`

***

### warning()

> **warning**(`caption`, `message`, `sticky`): `void`

Defined in: [src/common/web/ui/notifications/OverlayNotifications.ts:61](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/notifications/OverlayNotifications.ts#L61)

Display a warning notification.

#### Parameters

##### caption

`string`

The notification caption.

##### message

`string`

The notification message.

##### sticky

`boolean` = `false`

Whether the notification will be sticky.

#### Returns

`void`
