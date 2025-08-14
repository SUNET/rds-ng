---
id: "common_web_ui_dialogs_ExtendedDialog.ExtendedDialogData"
title: "Interface: ExtendedDialogData<UserDataType>"
sidebar_label: "ExtendedDialogData"
custom_edit_url: null
---

[common/web/ui/dialogs/ExtendedDialog](../modules/common_web_ui_dialogs_ExtendedDialog.md).ExtendedDialogData

Data for dynamic extended dialogs.

## Type parameters

| Name |
| :------ |
| `UserDataType` |

## Properties

### accept

• `Optional` **accept**: (`data`: `UserDataType`) => `void`

#### Type declaration

▸ (`data`): `void`

Called when the dialog was accepted.

##### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `UserDataType` |

##### Returns

`void`

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialog.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialog.ts#L54)

___

### options

• **options**: [`ExtendedDialogOptions`](common_web_ui_dialogs_ExtendedDialog.ExtendedDialogOptions.md)

Various display properties

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialog.ts:45](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialog.ts#L45)

___

### processData

• `Optional` **processData**: (`data`: `UserDataType`) => `void`

#### Type declaration

▸ (`data`): `void`

Called before accepting the dialog to pre-process the dialog data.

##### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `UserDataType` |

##### Returns

`void`

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialog.ts:51](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialog.ts#L51)

___

### reject

• `Optional` **reject**: () => `void`

#### Type declaration

▸ (): `void`

Called when the dialog was dismissed.

##### Returns

`void`

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialog.ts:57](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialog.ts#L57)

___

### userData

• **userData**: `UserDataType`

Custom user data.

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialog.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialog.ts#L42)

___

### validator

• `Optional` **validator**: [`ExtendedDialogValidator`](../classes/common_web_ui_dialogs_ExtendedDialogValidator.ExtendedDialogValidator.md)<`any`, `any`\>

A form validator if a schema was provided in the options.

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialog.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialog.ts#L48)
