---
id: "common_web_data_entities_user_UserToken"
title: "Module: common/web/data/entities/user/UserToken"
sidebar_label: "common/web/data/entities/user/UserToken"
sidebar_position: 0
custom_edit_url: null
---

## Interfaces

- [UserToken](../interfaces/common_web_data_entities_user_UserToken.UserToken.md)

## Functions

### createUserToken

▸ **createUserToken**(`userID`, `userName?`, `systemID?`, `accessID?`): [`UserToken`](../interfaces/common_web_data_entities_user_UserToken.UserToken.md)

Creates a new user token.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `userID` | `string` | The user ID. |
| `userName?` | `string` | The username. |
| `systemID?` | `string` | The user's system-specific ID. |
| `accessID?` | `string` | A well-formatted ID used to access resources. |

#### Returns

[`UserToken`](../interfaces/common_web_data_entities_user_UserToken.UserToken.md)

#### Defined in

[src/common/web/data/entities/user/UserToken.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/user/UserToken.ts#L20)

___

### isUserTokenValid

▸ **isUserTokenValid**(`token`): `boolean`

Checks whether a user token is valid.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `token` | [`UserToken`](../interfaces/common_web_data_entities_user_UserToken.UserToken.md) | The user token. |

#### Returns

`boolean`

#### Defined in

[src/common/web/data/entities/user/UserToken.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/user/UserToken.ts#L34)
