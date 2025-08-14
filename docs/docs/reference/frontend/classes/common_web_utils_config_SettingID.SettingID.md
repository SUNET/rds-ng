---
id: "common_web_utils_config_SettingID.SettingID"
title: "Class: SettingID"
sidebar_label: "SettingID"
custom_edit_url: null
---

[common/web/utils/config/SettingID](../modules/common_web_utils_config_SettingID.md).SettingID

A setting identifier.

Settings are specified by a category they belong to, as well as their actual name.

Categories support sub-categories by separating them using dots (.);
when represented as a string, all component tokens are separated by dots.

## Constructors

### constructor

• **new SettingID**(`category`, `name`): [`SettingID`](common_web_utils_config_SettingID.SettingID.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `category` | `string` |
| `name` | `string` |

#### Returns

[`SettingID`](common_web_utils_config_SettingID.SettingID.md)

#### Defined in

[src/common/web/utils/config/SettingID.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/SettingID.ts#L10)

## Properties

### category

• `Readonly` **category**: `string`

#### Defined in

[src/common/web/utils/config/SettingID.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/SettingID.ts#L10)

___

### name

• `Readonly` **name**: `string`

#### Defined in

[src/common/web/utils/config/SettingID.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/SettingID.ts#L10)

## Methods

### envName

▸ **envName**(`prefix`): `string`

Generates an environment variable name for this identifier.

A setting identifier is translated to its corresponding environment variable name by replacing all dots (.) with underscores (_),
prepending a ``prefix``, as well as making everything uppercase.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `prefix` | `string` | prefix: The prefix to prepend. |

#### Returns

`string`

- The corresponding environment variable name.

#### Defined in

[src/common/web/utils/config/SettingID.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/SettingID.ts#L32)

___

### split

▸ **split**(): `string`[]

Splits the entire identifier into single string tokens.

#### Returns

`string`[]

- The tokens list.

#### Defined in

[src/common/web/utils/config/SettingID.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/SettingID.ts#L18)

___

### toString

▸ **toString**(): `string`

Converts the setting ID to a string.

#### Returns

`string`

- The string representation of this setting ID.

#### Defined in

[src/common/web/utils/config/SettingID.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/SettingID.ts#L41)
