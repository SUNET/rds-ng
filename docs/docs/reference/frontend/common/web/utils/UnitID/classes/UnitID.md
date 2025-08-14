# Class: UnitID

Defined in: [src/common/web/utils/UnitID.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/UnitID.ts#L8)

A general unit identifier.

A *unit* basically is something that has a unique identifier consisting of three parts: The general ``type`` (e.g., *'infra'* for components
belonging to the overall infrastructure), the ``unit`` name itself (e.g., *'server'*), and an ``instance`` specifier (used to
distinguish multiple instances of the same unit).

## Constructors

### Constructor

> **new UnitID**(`type`, `unit`, `instance?`): `UnitID`

Defined in: [src/common/web/utils/UnitID.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/UnitID.ts#L16)

#### Parameters

##### type

`string`

The unit type.

##### unit

`string`

The unit name.

##### instance?

`string`

The instance specifier.

#### Returns

`UnitID`

## Properties

### instance?

> `readonly` `optional` **instance**: `string`

Defined in: [src/common/web/utils/UnitID.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/UnitID.ts#L19)

The instance specifier.

***

### type

> `readonly` **type**: `string`

Defined in: [src/common/web/utils/UnitID.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/UnitID.ts#L17)

The unit type.

***

### unit

> `readonly` **unit**: `string`

Defined in: [src/common/web/utils/UnitID.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/UnitID.ts#L18)

The unit name.

## Methods

### equals()

> **equals**(`other`): `boolean`

Defined in: [src/common/web/utils/UnitID.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/UnitID.ts#L31)

Compares this identifier to another one.

Note that the ``instance`` specifiers are only compared if both are not ``undefined``.

#### Parameters

##### other

`this`

The unit identifier to compare this one to.

#### Returns

`boolean`

- Whether both identifiers are equal.

***

### toString()

> **toString**(): `string`

Defined in: [src/common/web/utils/UnitID.ts:73](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/UnitID.ts#L73)

Converts the unit ID to a string of the form ``<type>/<unit>/<instance>`` or ``<type>/<unit>``.

#### Returns

`string`

***

### fromString()

> `static` **fromString**(`str`): `UnitID`

Defined in: [src/common/web/utils/UnitID.ts:56](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/UnitID.ts#L56)

Creates a new ``UnitID`` from a string.

The string must be of the form ``<type>/<unit>/<instance>`` or ``<type>/<unit>``.

#### Parameters

##### str

`string`

The unit identifier string.

#### Returns

`UnitID`

- The newly created ``UnitID``.

#### Throws

Error - If the passed string is invalid.
