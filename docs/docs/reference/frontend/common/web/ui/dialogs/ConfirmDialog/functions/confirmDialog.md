# Function: confirmDialog()

> **confirmDialog**(`comp`, `options`, `ignoreReject`): [`ConfirmDialogResult`](../type-aliases/ConfirmDialogResult.md)

Defined in: [src/common/web/ui/dialogs/ConfirmDialog.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ConfirmDialog.ts#L17)

Shows a confirmation (popup) dialog.

## Parameters

### comp

[`WebComponent`](../../../../component/WebComponent/classes/WebComponent.md)

The global component.

### options

`ConfirmationOptions`

Confirmation dialog options; note that the `accept` and `reject` callbacks are handled through the returned ``Promise``.

### ignoreReject

`boolean` = `true`

If true, nothing will happen if the user rejects the dialog.

## Returns

[`ConfirmDialogResult`](../type-aliases/ConfirmDialogResult.md)
