# Class: Configuration

Defined in: [src/common/web/utils/config/Configuration.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/config/Configuration.ts#L35)

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

### Constructor

> **new Configuration**(`env`, `envPrefix`): `Configuration`

Defined in: [src/common/web/utils/config/Configuration.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/config/Configuration.ts#L46)

#### Parameters

##### env

[`SettingsContainer`](../type-aliases/SettingsContainer.md)

The global environment variables.

##### envPrefix

`string` = `"RDS"`

The prefix to use when generating the environment variable name of a setting.

#### Returns

`Configuration`

## Methods

### addDefaults()

> **addDefaults**(`defaults`): `void`

Defined in: [src/common/web/utils/config/Configuration.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/config/Configuration.ts#L76)

Adds default values for settings, merging the new defaults into the existing ones.

Notes:
    It is always necessary to add a default value for a setting before accessing it.

#### Parameters

##### defaults

`Map`\<[`SettingID`](../../SettingID/classes/SettingID.md), `any`\>

A map containing the new default values.

#### Returns

`void`

***

### load()

> **load**(): `void`

Defined in: [src/common/web/utils/config/Configuration.ts:56](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/config/Configuration.ts#L56)

Loads settings from the global *TOML* configuration file.

#### Returns

`void`

#### Throws

Error - If the configuration data couldn't be parsed.

***

### value()

> **value**\<`ValType`\>(`key`): `ValType`

Defined in: [src/common/web/utils/config/Configuration.ts:96](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/config/Configuration.ts#L96)

Gets the value of a setting.

The value is first looked up in the environment variables. If not found, the loaded settings are searched.
If that also fails, the defaults are used.

#### Type Parameters

##### ValType

`ValType` = `any`

#### Parameters

##### key

[`SettingID`](../../SettingID/classes/SettingID.md)

The identifier of the setting.

#### Returns

`ValType`

- The value of the setting.

#### Throws

Error - The setting identifier was not found in the defaults.
