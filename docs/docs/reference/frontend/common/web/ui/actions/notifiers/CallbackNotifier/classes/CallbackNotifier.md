# Class: CallbackNotifier

Defined in: [src/common/web/ui/actions/notifiers/CallbackNotifier.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/CallbackNotifier.ts#L8)

A simple action notifier that calls a callback function on notification.

## Extends

- [`ActionNotifier`](../../ActionNotifier/classes/ActionNotifier.md)

## Constructors

### Constructor

> **new CallbackNotifier**(`callback`): `CallbackNotifier`

Defined in: [src/common/web/ui/actions/notifiers/CallbackNotifier.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/CallbackNotifier.ts#L11)

#### Parameters

##### callback

[`NotifierCallback`](../type-aliases/NotifierCallback.md)

#### Returns

`CallbackNotifier`

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

Defined in: [src/common/web/ui/actions/notifiers/CallbackNotifier.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/notifiers/CallbackNotifier.ts#L17)

Called when the action triggers its notification.

#### Parameters

##### message

`string`

#### Returns

`void`

#### Overrides

[`ActionNotifier`](../../ActionNotifier/classes/ActionNotifier.md).[`onNotify`](../../ActionNotifier/classes/ActionNotifier.md#onnotify)
