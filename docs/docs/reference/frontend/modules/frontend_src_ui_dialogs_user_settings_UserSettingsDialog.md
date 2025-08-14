---
id: "frontend_src_ui_dialogs_user_settings_UserSettingsDialog"
title: "Module: frontend/src/ui/dialogs/user/settings/UserSettingsDialog"
sidebar_label: "frontend/src/ui/dialogs/user/settings/UserSettingsDialog"
sidebar_position: 0
custom_edit_url: null
---

## Enumerations

- [UserSettingsPage](../enums/frontend_src_ui_dialogs_user_settings_UserSettingsDialog.UserSettingsPage.md)

## Interfaces

- [UserSettingsDialogData](../interfaces/frontend_src_ui_dialogs_user_settings_UserSettingsDialog.UserSettingsDialogData.md)

## Functions

### userSettingsDialog

▸ **userSettingsDialog**(`comp`, `userSettings`, `activePage?`): [`ExtendedDialogResult`](common_web_ui_dialogs_ExtendedDialog.md#extendeddialogresult)<[`UserSettingsDialogData`](../interfaces/frontend_src_ui_dialogs_user_settings_UserSettingsDialog.UserSettingsDialogData.md)\>

Shows the user settings dialog.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `comp` | [`FrontendComponent`](../classes/frontend_src_component_FrontendComponent.FrontendComponent.md) | `undefined` | The global component. |
| `userSettings` | [`UserSettings`](../classes/common_web_data_entities_user_UserSettings.UserSettings.md) | `undefined` | The current user settings. |
| `activePage` | [`UserSettingsPage`](../enums/frontend_src_ui_dialogs_user_settings_UserSettingsDialog.UserSettingsPage.md) | `UserSettingsPage.Connections` | The page to activate immediately. |

#### Returns

[`ExtendedDialogResult`](common_web_ui_dialogs_ExtendedDialog.md#extendeddialogresult)<[`UserSettingsDialogData`](../interfaces/frontend_src_ui_dialogs_user_settings_UserSettingsDialog.UserSettingsDialogData.md)\>

#### Defined in

[src/frontend/src/ui/dialogs/user/settings/UserSettingsDialog.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/dialogs/user/settings/UserSettingsDialog.ts#L34)
