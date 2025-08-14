# Class: ExtendedDialogValidator\<FormType, ShapeType\>

Defined in: [src/common/web/ui/dialogs/ExtendedDialogValidator.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L10)

A wrapper class for form validation.

## Type Parameters

### FormType

`FormType`

### ShapeType

`ShapeType` *extends* `yup.ObjectShape`

## Constructors

### Constructor

> **new ExtendedDialogValidator**\<`FormType`, `ShapeType`\>(`form`, `shape`): `ExtendedDialogValidator`\<`FormType`, `ShapeType`\>

Defined in: [src/common/web/ui/dialogs/ExtendedDialogValidator.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L20)

#### Parameters

##### form

`FormType`

The form to use.

##### shape

`ShapeType`

The value shape used for validation.

#### Returns

`ExtendedDialogValidator`\<`FormType`, `ShapeType`\>

## Accessors

### errorMessages

#### Get Signature

> **get** **errorMessages**(): `string`[]

Defined in: [src/common/web/ui/dialogs/ExtendedDialogValidator.ts:105](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L105)

Gets an array of all error messages.

##### Returns

`string`[]

***

### errors

#### Get Signature

> **get** **errors**(): `ValidationError`[]

Defined in: [src/common/web/ui/dialogs/ExtendedDialogValidator.ts:98](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L98)

Gets an array of all errors.

##### Returns

`ValidationError`[]

***

### isValid

#### Get Signature

> **get** **isValid**(): `boolean`

Defined in: [src/common/web/ui/dialogs/ExtendedDialogValidator.ts:81](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L81)

Whether the form is currently valid.

##### Returns

`boolean`

***

### resolver

#### Get Signature

> **get** **resolver**(): `any`

Defined in: [src/common/web/ui/dialogs/ExtendedDialogValidator.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L28)

The resolver for the underlying form.

##### Returns

`any`

## Methods

### hasError()

> **hasError**(`field`): `boolean`

Defined in: [src/common/web/ui/dialogs/ExtendedDialogValidator.ts:91](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L91)

Checks if a specific field is erroneous.

#### Parameters

##### field

`string`

The field to check.

#### Returns

`boolean`

***

### refresh()

> **refresh**(): `void`

Defined in: [src/common/web/ui/dialogs/ExtendedDialogValidator.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L66)

Refreshes the form validation state.

#### Returns

`void`

***

### validate()

> **validate**(): `Promise`\<`void`\>

Defined in: [src/common/web/ui/dialogs/ExtendedDialogValidator.ts:45](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L45)

Validates the form.

#### Returns

`Promise`\<`void`\>

- A Promise that succeeds if the form is filled out correctly and fails otherwise, reporting all errors.
