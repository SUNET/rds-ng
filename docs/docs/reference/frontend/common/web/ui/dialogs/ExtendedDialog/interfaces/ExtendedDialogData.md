# Interface: ExtendedDialogData\<UserDataType\>

Defined in: [src/common/web/ui/dialogs/ExtendedDialog.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialog.ts#L40)

Data for dynamic extended dialogs.

## Type Parameters

### UserDataType

`UserDataType`

## Properties

### accept()?

> `optional` **accept**: (`data`) => `void`

Defined in: [src/common/web/ui/dialogs/ExtendedDialog.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialog.ts#L54)

Called when the dialog was accepted.

#### Parameters

##### data

`UserDataType`

#### Returns

`void`

***

### options

> **options**: [`ExtendedDialogOptions`](ExtendedDialogOptions.md)

Defined in: [src/common/web/ui/dialogs/ExtendedDialog.ts:45](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialog.ts#L45)

Various display properties

***

### processData()?

> `optional` **processData**: (`data`) => `void`

Defined in: [src/common/web/ui/dialogs/ExtendedDialog.ts:51](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialog.ts#L51)

Called before accepting the dialog to pre-process the dialog data.

#### Parameters

##### data

`UserDataType`

#### Returns

`void`

***

### reject()?

> `optional` **reject**: () => `void`

Defined in: [src/common/web/ui/dialogs/ExtendedDialog.ts:57](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialog.ts#L57)

Called when the dialog was dismissed.

#### Returns

`void`

***

### userData

> **userData**: `UserDataType`

Defined in: [src/common/web/ui/dialogs/ExtendedDialog.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialog.ts#L42)

Custom user data.

***

### validator?

> `optional` **validator**: [`ExtendedDialogValidator`](../../ExtendedDialogValidator/classes/ExtendedDialogValidator.md)\<`any`, `any`\>

Defined in: [src/common/web/ui/dialogs/ExtendedDialog.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialog.ts#L48)

A form validator if a schema was provided in the options.
