# Abstract Class: ActionNotifier

Defined in: [src/common/web/ui/actions/notifiers/ActionNotifier.ts:6](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L6)

A snap-in for actions to display arbitrary notifications about the action execution.

## Extended by

- [`CallbackNotifier`](../../CallbackNotifier/classes/CallbackNotifier.md)
- [`OverlayNotifier`](../../OverlayNotifier/classes/OverlayNotifier.md)
- [`StatusNotifier`](../../StatusNotifier/classes/StatusNotifier.md)

## Constructors

### Constructor

> **new ActionNotifier**(): `ActionNotifier`

#### Returns

`ActionNotifier`

## Properties

### MessagePlaceholder

> `readonly` `static` **MessagePlaceholder**: `"$MSG$"` = `"$MSG$"`

Defined in: [src/common/web/ui/actions/notifiers/ActionNotifier.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L7)

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

***

### onFinished()

> **onFinished**(): `void`

Defined in: [src/common/web/ui/actions/notifiers/ActionNotifier.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L18)

Called when the action has finished (independent of its success).

#### Returns

`void`

***

### onNotify()

> **onNotify**(`message`): `void`

Defined in: [src/common/web/ui/actions/notifiers/ActionNotifier.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/ActionNotifier.ts#L12)

Called when the action triggers its notification.

#### Parameters

##### message

`string` = `""`

#### Returns

`void`
