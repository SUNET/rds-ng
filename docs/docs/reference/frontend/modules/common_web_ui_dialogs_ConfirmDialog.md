---
id: "common_web_ui_dialogs_ConfirmDialog"
title: "Module: common/web/ui/dialogs/ConfirmDialog"
sidebar_label: "common/web/ui/dialogs/ConfirmDialog"
sidebar_position: 0
custom_edit_url: null
---

## Type Aliases

### ConfirmDialogResult

Ƭ **ConfirmDialogResult**: `Promise`<`void`\>

The result of a confirmation dialog in form of a `Promise`.

#### Defined in

[src/common/web/ui/dialogs/ConfirmDialog.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ConfirmDialog.ts#L8)

## Functions

### confirmDialog

▸ **confirmDialog**(`comp`, `options`, `ignoreReject?`): [`ConfirmDialogResult`](common_web_ui_dialogs_ConfirmDialog.md#confirmdialogresult)

Shows a confirmation (popup) dialog.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `comp` | [`WebComponent`](../classes/common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](../classes/common_web_ui_UserInterface.UserInterface.md)\> | `undefined` | The global component. |
| `options` | `ConfirmationOptions` | `undefined` | Confirmation dialog options; note that the `accept` and `reject` callbacks are handled through the returned ``Promise``. |
| `ignoreReject` | `boolean` | `true` | If true, nothing will happen if the user rejects the dialog. |

#### Returns

[`ConfirmDialogResult`](common_web_ui_dialogs_ConfirmDialog.md#confirmdialogresult)

#### Defined in

[src/common/web/ui/dialogs/ConfirmDialog.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/dialogs/ConfirmDialog.ts#L17)
