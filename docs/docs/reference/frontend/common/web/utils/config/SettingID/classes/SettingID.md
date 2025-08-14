# Class: SettingID

Defined in: [src/common/web/utils/config/SettingID.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/config/SettingID.ts#L9)

A setting identifier.

Settings are specified by a category they belong to, as well as their actual name.

Categories support sub-categories by separating them using dots (.);
when represented as a string, all component tokens are separated by dots.

## Constructors

### Constructor

> **new SettingID**(`category`, `name`): `SettingID`

Defined in: [src/common/web/utils/config/SettingID.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/config/SettingID.ts#L10)

#### Parameters

##### category

`string`

##### name

`string`

#### Returns

`SettingID`

## Properties

### category

> `readonly` **category**: `string`

Defined in: [src/common/web/utils/config/SettingID.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/config/SettingID.ts#L10)

***

### name

> `readonly` **name**: `string`

Defined in: [src/common/web/utils/config/SettingID.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/config/SettingID.ts#L10)

## Methods

### envName()

> **envName**(`prefix`): `string`

Defined in: [src/common/web/utils/config/SettingID.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/config/SettingID.ts#L32)

Generates an environment variable name for this identifier.

A setting identifier is translated to its corresponding environment variable name by replacing all dots (.) with underscores (_),
prepending a ``prefix``, as well as making everything uppercase.

#### Parameters

##### prefix

`string`

prefix: The prefix to prepend.

#### Returns

`string`

- The corresponding environment variable name.

***

### split()

> **split**(): `string`[]

Defined in: [src/common/web/utils/config/SettingID.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/config/SettingID.ts#L18)

Splits the entire identifier into single string tokens.

#### Returns

`string`[]

- The tokens list.

***

### toString()

> **toString**(): `string`

Defined in: [src/common/web/utils/config/SettingID.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/config/SettingID.ts#L41)

Converts the setting ID to a string.

#### Returns

`string`

- The string representation of this setting ID.
