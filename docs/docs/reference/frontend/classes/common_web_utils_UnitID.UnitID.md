---
id: "common_web_utils_UnitID.UnitID"
title: "Class: UnitID"
sidebar_label: "UnitID"
custom_edit_url: null
---

[common/web/utils/UnitID](../modules/common_web_utils_UnitID.md).UnitID

A general unit identifier.

A *unit* basically is something that has a unique identifier consisting of three parts: The general ``type`` (e.g., *'infra'* for components
belonging to the overall infrastructure), the ``unit`` name itself (e.g., *'server'*), and an ``instance`` specifier (used to
distinguish multiple instances of the same unit).

## Constructors

### constructor

• **new UnitID**(`type`, `unit`, `instance?`): [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `type` | `string` | The unit type. |
| `unit` | `string` | The unit name. |
| `instance?` | `string` | The instance specifier. |

#### Returns

[`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Defined in

[src/common/web/utils/UnitID.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/UnitID.ts#L16)

## Properties

### instance

• `Optional` `Readonly` **instance**: `string`

The instance specifier.

#### Defined in

[src/common/web/utils/UnitID.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/UnitID.ts#L19)

___

### type

• `Readonly` **type**: `string`

The unit type.

#### Defined in

[src/common/web/utils/UnitID.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/UnitID.ts#L17)

___

### unit

• `Readonly` **unit**: `string`

The unit name.

#### Defined in

[src/common/web/utils/UnitID.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/UnitID.ts#L18)

___

### \_delimiter

▪ `Static` `Private` `Readonly` **\_delimiter**: ``"/"``

#### Defined in

[src/common/web/utils/UnitID.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/UnitID.ts#L9)

## Methods

### equals

▸ **equals**(`other`): `boolean`

Compares this identifier to another one.

Note that the ``instance`` specifiers are only compared if both are not ``undefined``.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `other` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | The unit identifier to compare this one to. |

#### Returns

`boolean`

- Whether both identifiers are equal.

#### Defined in

[src/common/web/utils/UnitID.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/UnitID.ts#L31)

___

### toString

▸ **toString**(): `string`

Converts the unit ID to a string of the form ``<type>/<unit>/<instance>`` or ``<type>/<unit>``.

#### Returns

`string`

#### Defined in

[src/common/web/utils/UnitID.ts:73](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/UnitID.ts#L73)

___

### fromString

▸ **fromString**(`str`): [`UnitID`](common_web_utils_UnitID.UnitID.md)

Creates a new ``UnitID`` from a string.

The string must be of the form ``<type>/<unit>/<instance>`` or ``<type>/<unit>``.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `str` | `string` | The unit identifier string. |

#### Returns

[`UnitID`](common_web_utils_UnitID.UnitID.md)

- The newly created ``UnitID``.

**`Throws`**

Error - If the passed string is invalid.

#### Defined in

[src/common/web/utils/UnitID.ts:56](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/UnitID.ts#L56)
