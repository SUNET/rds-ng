---
id: "common_web_ui_dialogs_ExtendedDialogValidator.ExtendedDialogValidator"
title: "Class: ExtendedDialogValidator<FormType, ShapeType>"
sidebar_label: "ExtendedDialogValidator"
custom_edit_url: null
---

[common/web/ui/dialogs/ExtendedDialogValidator](../modules/common_web_ui_dialogs_ExtendedDialogValidator.md).ExtendedDialogValidator

A wrapper class for form validation.

## Type parameters

| Name | Type |
| :------ | :------ |
| `FormType` | `FormType` |
| `ShapeType` | extends `yup.ObjectShape` |

## Constructors

### constructor

• **new ExtendedDialogValidator**<`FormType`, `ShapeType`\>(`form`, `shape`): [`ExtendedDialogValidator`](common_web_ui_dialogs_ExtendedDialogValidator.ExtendedDialogValidator.md)<`FormType`, `ShapeType`\>

#### Type parameters

| Name | Type |
| :------ | :------ |
| `FormType` | `FormType` |
| `ShapeType` | extends `ObjectShape` |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `form` | `FormType` | The form to use. |
| `shape` | `ShapeType` | The value shape used for validation. |

#### Returns

[`ExtendedDialogValidator`](common_web_ui_dialogs_ExtendedDialogValidator.ExtendedDialogValidator.md)<`FormType`, `ShapeType`\>

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialogValidator.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L20)

## Properties

### \_form

• `Private` `Readonly` **\_form**: `FormType`

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialogValidator.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L11)

___

### \_resolver

• `Private` `Readonly` **\_resolver**: `any`

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialogValidator.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L12)

___

### \_validationErrors

• `Private` `Readonly` **\_validationErrors**: `ValidationError`[] = `[]`

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialogValidator.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L14)

## Accessors

### errorMessages

• `get` **errorMessages**(): `string`[]

Gets an array of all error messages.

#### Returns

`string`[]

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialogValidator.ts:105](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L105)

___

### errors

• `get` **errors**(): `ValidationError`[]

Gets an array of all errors.

#### Returns

`ValidationError`[]

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialogValidator.ts:98](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L98)

___

### isValid

• `get` **isValid**(): `boolean`

Whether the form is currently valid.

#### Returns

`boolean`

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialogValidator.ts:81](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L81)

___

### resolver

• `get` **resolver**(): `any`

The resolver for the underlying form.

#### Returns

`any`

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialogValidator.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L28)

## Methods

### hasError

▸ **hasError**(`field`): `boolean`

Checks if a specific field is erroneous.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `field` | `string` | The field to check. |

#### Returns

`boolean`

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialogValidator.ts:91](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L91)

___

### processValidation

▸ **processValidation**(`validation`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `validation` | `any` |

#### Returns

`void`

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialogValidator.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L70)

___

### refresh

▸ **refresh**(): `void`

Refreshes the form validation state.

#### Returns

`void`

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialogValidator.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L66)

___

### validate

▸ **validate**(): `Promise`<`void`\>

Validates the form.

#### Returns

`Promise`<`void`\>

- A Promise that succeeds if the form is filled out correctly and fails otherwise, reporting all errors.

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialogValidator.ts:45](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialogValidator.ts#L45)
