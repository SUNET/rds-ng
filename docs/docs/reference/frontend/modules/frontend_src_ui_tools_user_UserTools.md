---
id: "frontend_src_ui_tools_user_UserTools"
title: "Module: frontend/src/ui/tools/user/UserTools"
sidebar_label: "frontend/src/ui/tools/user/UserTools"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### useUserTools

▸ **useUserTools**(`comp`): `Object`

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](../classes/frontend_src_component_FrontendComponent.FrontendComponent.md) |

#### Returns

`Object`

| Name | Type |
| :------ | :------ |
| `editUserSettings` | (`userSettings`: [`UserSettings`](../classes/common_web_data_entities_user_UserSettings.UserSettings.md), `activePage`: [`UserSettingsPage`](../enums/frontend_src_ui_dialogs_user_settings_UserSettingsDialog.UserSettingsPage.md)) => `void` |
| `saveUserSettings` | (`userSettings`: [`UserSettings`](../classes/common_web_data_entities_user_UserSettings.UserSettings.md)) => `void` |
| `userSettingsUpdating` | `Ref`<`boolean`, `boolean`\> |

#### Defined in

[src/frontend/src/ui/tools/user/UserTools.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/tools/user/UserTools.ts#L11)
