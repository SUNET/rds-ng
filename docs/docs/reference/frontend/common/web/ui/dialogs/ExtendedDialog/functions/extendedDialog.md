# Function: extendedDialog()

> **extendedDialog**\<`UserDataType`\>(`comp`, `dialogComponent`, `dialogProps`, `data`, `options`, `processDataCallback`, `ignoreReject`): [`ExtendedDialogResult`](../type-aliases/ExtendedDialogResult.md)\<`UserDataType`\>

Defined in: [src/common/web/ui/dialogs/ExtendedDialog.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/dialogs/ExtendedDialog.ts#L76)

Shows a (popup) dialog with extended functionality.

## Type Parameters

### UserDataType

`UserDataType`

## Parameters

### comp

[`WebComponent`](../../../../component/WebComponent/classes/WebComponent.md)

The global component.

### dialogComponent

[`VueComponent`](../../../../component/WebComponent/type-aliases/VueComponent.md)

The main dialog component to load.

### dialogProps

`DialogProps`

Vue dialog properties.

### data

`UserDataType`

Optional user data to pass to the dialog.

### options

Extended dialog options.

`undefined` | [`ExtendedDialogOptions`](../interfaces/ExtendedDialogOptions.md)

### processDataCallback

A callback that is called before the dialog is being accepted to pre-process the dialog data.

`undefined` | (`data`) => `void`

### ignoreReject

`boolean` = `true`

If true, nothing will happen if the user rejects the dialog.

## Returns

[`ExtendedDialogResult`](../type-aliases/ExtendedDialogResult.md)\<`UserDataType`\>
