# Function: userSettingsDialog()

> **userSettingsDialog**(`comp`, `userSettings`, `activePage`): [`ExtendedDialogResult`](../../../../../../../../common/web/ui/dialogs/ExtendedDialog/type-aliases/ExtendedDialogResult.md)\<[`UserSettingsDialogData`](../interfaces/UserSettingsDialogData.md)\>

Defined in: [src/frontend/src/ui/dialogs/user/settings/UserSettingsDialog.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/dialogs/user/settings/UserSettingsDialog.ts#L34)

Shows the user settings dialog.

## Parameters

### comp

[`FrontendComponent`](../../../../../../component/FrontendComponent/classes/FrontendComponent.md)

The global component.

### userSettings

[`UserSettings`](../../../../../../../../common/web/data/entities/user/UserSettings/classes/UserSettings.md)

The current user settings.

### activePage

[`UserSettingsPage`](../enumerations/UserSettingsPage.md) = `UserSettingsPage.Connections`

The page to activate immediately.

## Returns

[`ExtendedDialogResult`](../../../../../../../../common/web/ui/dialogs/ExtendedDialog/type-aliases/ExtendedDialogResult.md)\<[`UserSettingsDialogData`](../interfaces/UserSettingsDialogData.md)\>
