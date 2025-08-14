---
id: "common_web_utils_config_Configuration.Configuration"
title: "Class: Configuration"
sidebar_label: "Configuration"
custom_edit_url: null
---

[common/web/utils/config/Configuration](../modules/common_web_utils_config_Configuration.md).Configuration

Encapsulates configuration settings and their fallback default values.

Settings can be loaded from a configuration file (in *TOML* format) or provided as environment variables (see below).

All settings are accessed by an identifier of type ``SettingID``, which represents settings in a path-like format;
``General.Debug``, for example, refers to a setting called ``Debug`` in the ``General` section.

A corresponding configuration file would look like this:
```
    [General]
    Debug = True
```

A setting identifier is translated to its corresponding environment variable name by replacing all dots (.) with underscores (_),
prepending a prefix (defaults to *'RDS'*), as well as making everything uppercase:
```
    General.Debug -> RDS_GENERAL_DEBUG
```

Notes:
    When accessing a setting value, a default value must *always* be present. This means that before a setting can be accessed,
    a default value must be added using ``add_defaults``.

## Constructors

### constructor

• **new Configuration**(`env`, `envPrefix?`): [`Configuration`](common_web_utils_config_Configuration.Configuration.md)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `env` | [`SettingsContainer`](../modules/common_web_utils_config_Configuration.md#settingscontainer) | `undefined` | The global environment variables. |
| `envPrefix` | `string` | `"RDS"` | The prefix to use when generating the environment variable name of a setting. |

#### Returns

[`Configuration`](common_web_utils_config_Configuration.Configuration.md)

#### Defined in

[src/common/web/utils/config/Configuration.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/Configuration.ts#L46)

## Properties

### \_defaults

• `Private` **\_defaults**: [`SettingsContainer`](../modules/common_web_utils_config_Configuration.md#settingscontainer) = `{}`

#### Defined in

[src/common/web/utils/config/Configuration.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/Configuration.ts#L37)

___

### \_env

• `Private` `Readonly` **\_env**: [`SettingsContainer`](../modules/common_web_utils_config_Configuration.md#settingscontainer)

#### Defined in

[src/common/web/utils/config/Configuration.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/Configuration.ts#L39)

___

### \_envPrefix

• `Private` `Readonly` **\_envPrefix**: `string`

#### Defined in

[src/common/web/utils/config/Configuration.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/Configuration.ts#L40)

___

### \_settings

• `Private` **\_settings**: [`SettingsContainer`](../modules/common_web_utils_config_Configuration.md#settingscontainer) = `{}`

#### Defined in

[src/common/web/utils/config/Configuration.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/Configuration.ts#L36)

## Methods

### addDefaults

▸ **addDefaults**(`defaults`): `void`

Adds default values for settings, merging the new defaults into the existing ones.

Notes:
    It is always necessary to add a default value for a setting before accessing it.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `defaults` | `Map`<[`SettingID`](common_web_utils_config_SettingID.SettingID.md), `any`\> | A map containing the new default values. |

#### Returns

`void`

#### Defined in

[src/common/web/utils/config/Configuration.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/Configuration.ts#L76)

___

### convertEnvType

▸ **convertEnvType**(`value`, `targetType`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `any` |
| `targetType` | `string` |

#### Returns

`any`

#### Defined in

[src/common/web/utils/config/Configuration.ts:132](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/Configuration.ts#L132)

___

### load

▸ **load**(): `void`

Loads settings from the global *TOML* configuration file.

#### Returns

`void`

**`Throws`**

Error - If the configuration data couldn't be parsed.

#### Defined in

[src/common/web/utils/config/Configuration.ts:56](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/Configuration.ts#L56)

___

### traverseSettings

▸ **traverseSettings**(`path`, `settings`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `path` | `string`[] |
| `settings` | [`SettingsContainer`](../modules/common_web_utils_config_Configuration.md#settingscontainer) |

#### Returns

`any`

#### Defined in

[src/common/web/utils/config/Configuration.ts:111](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/Configuration.ts#L111)

___

### unfoldSettingsItem

▸ **unfoldSettingsItem**(`path`, `settings`, `value`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `path` | `string`[] |
| `settings` | [`SettingsContainer`](../modules/common_web_utils_config_Configuration.md#settingscontainer) |
| `value` | `any` |

#### Returns

`void`

#### Defined in

[src/common/web/utils/config/Configuration.ts:119](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/Configuration.ts#L119)

___

### value

▸ **value**<`ValType`\>(`key`): `ValType`

Gets the value of a setting.

The value is first looked up in the environment variables. If not found, the loaded settings are searched.
If that also fails, the defaults are used.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `ValType` | `any` |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `key` | [`SettingID`](common_web_utils_config_SettingID.SettingID.md) | The identifier of the setting. |

#### Returns

`ValType`

- The value of the setting.

**`Throws`**

Error - The setting identifier was not found in the defaults.

#### Defined in

[src/common/web/utils/config/Configuration.ts:96](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/config/Configuration.ts#L96)
