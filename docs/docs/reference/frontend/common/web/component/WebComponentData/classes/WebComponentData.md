# Class: WebComponentData

Defined in: [src/common/web/component/WebComponentData.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponentData.ts#L12)

Holds general data and information about the component.

Objects of this class are passed to certain parts of the core for easy access to frequently
used component information and data.

## Constructors

### Constructor

> **new WebComponentData**(`compID`, `config`, `title`, `name`, `version`): `WebComponentData`

Defined in: [src/common/web/component/WebComponentData.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponentData.ts#L20)

#### Parameters

##### compID

[`UnitID`](../../../utils/UnitID/classes/UnitID.md)

The component identifier.

##### config

[`Configuration`](../../../utils/config/Configuration/classes/Configuration.md)

The configuration.

##### title

`string`

The project title.

##### name

`string`

The component name.

##### version

`SemVer`

The project version.

#### Returns

`WebComponentData`

## Properties

### compID

> `readonly` **compID**: [`UnitID`](../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/component/WebComponentData.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponentData.ts#L20)

The component identifier.

***

### config

> `readonly` **config**: [`Configuration`](../../../utils/config/Configuration/classes/Configuration.md)

Defined in: [src/common/web/component/WebComponentData.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponentData.ts#L20)

The configuration.

***

### name

> `readonly` **name**: `string`

Defined in: [src/common/web/component/WebComponentData.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponentData.ts#L21)

The component name.

***

### title

> `readonly` **title**: `string`

Defined in: [src/common/web/component/WebComponentData.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponentData.ts#L21)

The project title.

***

### version

> `readonly` **version**: `SemVer`

Defined in: [src/common/web/component/WebComponentData.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponentData.ts#L21)

The project version.
