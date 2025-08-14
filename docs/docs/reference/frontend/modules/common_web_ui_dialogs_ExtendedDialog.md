---
id: "common_web_ui_dialogs_ExtendedDialog"
title: "Module: common/web/ui/dialogs/ExtendedDialog"
sidebar_label: "common/web/ui/dialogs/ExtendedDialog"
sidebar_position: 0
custom_edit_url: null
---

## Interfaces

- [ExtendedDialogData](../interfaces/common_web_ui_dialogs_ExtendedDialog.ExtendedDialogData.md)
- [ExtendedDialogOptions](../interfaces/common_web_ui_dialogs_ExtendedDialog.ExtendedDialogOptions.md)

## Type Aliases

### ExtendedDialogResult

Ƭ **ExtendedDialogResult**<`ResultType`\>: `Promise`<`ResultType`\>

The result of an extended dialog in form of a `Promise`.

#### Type parameters

| Name |
| :------ |
| `ResultType` |

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialog.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialog.ts#L63)

## Functions

### extendedDialog

▸ **extendedDialog**<`UserDataType`\>(`comp`, `dialogComponent`, `dialogProps`, `data`, `options?`, `processDataCallback?`, `ignoreReject?`): [`ExtendedDialogResult`](common_web_ui_dialogs_ExtendedDialog.md#extendeddialogresult)<`UserDataType`\>

Shows a (popup) dialog with extended functionality.

#### Type parameters

| Name |
| :------ |
| `UserDataType` |

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `comp` | [`WebComponent`](../classes/common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](../classes/common_web_ui_UserInterface.UserInterface.md)\> | `undefined` | The global component. |
| `dialogComponent` | [`VueComponent`](common_web_component_WebComponent.md#vuecomponent) | `undefined` | The main dialog component to load. |
| `dialogProps` | `DialogProps` | `undefined` | Vue dialog properties. |
| `data` | `UserDataType` | `undefined` | Optional user data to pass to the dialog. |
| `options` | `undefined` \| [`ExtendedDialogOptions`](../interfaces/common_web_ui_dialogs_ExtendedDialog.ExtendedDialogOptions.md) | `undefined` | Extended dialog options. |
| `processDataCallback` | `undefined` \| (`data`: `UserDataType`) => `void` | `undefined` | A callback that is called before the dialog is being accepted to pre-process the dialog data. |
| `ignoreReject` | `boolean` | `true` | If true, nothing will happen if the user rejects the dialog. |

#### Returns

[`ExtendedDialogResult`](common_web_ui_dialogs_ExtendedDialog.md#extendeddialogresult)<`UserDataType`\>

#### Defined in

[src/common/web/ui/dialogs/ExtendedDialog.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ExtendedDialog.ts#L76)
