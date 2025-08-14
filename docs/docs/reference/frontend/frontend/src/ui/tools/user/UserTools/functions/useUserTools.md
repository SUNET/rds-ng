# Function: useUserTools()

> **useUserTools**(`comp`): `object`

Defined in: [src/frontend/src/ui/tools/user/UserTools.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/tools/user/UserTools.ts#L11)

## Parameters

### comp

[`FrontendComponent`](../../../../../component/FrontendComponent/classes/FrontendComponent.md)

## Returns

`object`

### editUserSettings()

> **editUserSettings**: (`userSettings`, `activePage`) => `void`

#### Parameters

##### userSettings

[`UserSettings`](../../../../../../../common/web/data/entities/user/UserSettings/classes/UserSettings.md)

##### activePage

[`UserSettingsPage`](../../../../dialogs/user/settings/UserSettingsDialog/enumerations/UserSettingsPage.md) = `UserSettingsPage.Connections`

#### Returns

`void`

### saveUserSettings()

> **saveUserSettings**: (`userSettings`) => `void`

#### Parameters

##### userSettings

[`UserSettings`](../../../../../../../common/web/data/entities/user/UserSettings/classes/UserSettings.md)

#### Returns

`void`

### userSettingsUpdating

> **userSettingsUpdating**: `Ref`\<`boolean`, `boolean`\> = `_updatingUserSettings`
