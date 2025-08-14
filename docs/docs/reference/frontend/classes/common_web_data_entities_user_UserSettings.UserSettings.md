---
id: "common_web_data_entities_user_UserSettings.UserSettings"
title: "Class: UserSettings"
sidebar_label: "UserSettings"
custom_edit_url: null
---

[common/web/data/entities/user/UserSettings](../modules/common_web_data_entities_user_UserSettings.md).UserSettings

User settings (i.e., the settings a user configures in the UI) data.

**`Param`**

A list of all configured connector instances.

## Constructors

### constructor

• **new UserSettings**(`connectorInstances?`): [`UserSettings`](common_web_data_entities_user_UserSettings.UserSettings.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `connectorInstances` | [`ConnectorInstance`](common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)[] | `[]` |

#### Returns

[`UserSettings`](common_web_data_entities_user_UserSettings.UserSettings.md)

#### Defined in

[src/common/web/data/entities/user/UserSettings.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/user/UserSettings.ts#L15)

## Properties

### connector\_instances

• `Readonly` **connector\_instances**: [`ConnectorInstance`](common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)[] = `[]`

#### Defined in

[src/common/web/data/entities/user/UserSettings.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/user/UserSettings.ts#L13)
