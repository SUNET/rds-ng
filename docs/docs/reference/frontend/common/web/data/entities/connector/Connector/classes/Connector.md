# Class: Connector

Defined in: [src/common/web/data/entities/connector/Connector.ts:57](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/Connector.ts#L57)

Data for a single **Connector**.

## Param

The unique connector identifier.

## Param

The target address of the connector.

## Param

The connector category.

## Param

The name of the connector.

## Param

An optional connector description.

## Param

Authorization settings for the connector.

## Param

The connector options.

## Param

Image data of the connector logos.

## Param

The profiles for connector-specific data.

## Param

The timestamp when the connector was last announced.

## Constructors

### Constructor

> **new Connector**(`connectorID`, `connectorAddress`, `name`, `description`, `category`, `authorization`, `options`, `logos`, `metadataProfiles`): `Connector`

Defined in: [src/common/web/data/entities/connector/Connector.ts:80](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/Connector.ts#L80)

#### Parameters

##### connectorID

`string`

##### connectorAddress

[`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

##### name

`string`

##### description

`string`

##### category

`string`

##### authorization

[`AuthorizationSettings`](../../../authorization/AuthorizationSettings/interfaces/AuthorizationSettings.md) = `...`

##### options

[`ConnectorOptions`](../enumerations/ConnectorOptions.md) = `ConnectorOptions.Default`

##### logos

[`ConnectorLogos`](ConnectorLogos.md) = `...`

##### metadataProfiles

[`MetadataProfileContainerList`](../../../metadata/MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md) = `[]`

#### Returns

`Connector`

## Properties

### announce\_timestamp

> `readonly` **announce\_timestamp**: `Number` = `0.0`

Defined in: [src/common/web/data/entities/connector/Connector.ts:78](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/Connector.ts#L78)

***

### authorization

> `readonly` **authorization**: [`AuthorizationSettings`](../../../authorization/AuthorizationSettings/interfaces/AuthorizationSettings.md)

Defined in: [src/common/web/data/entities/connector/Connector.ts:67](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/Connector.ts#L67)

***

### category

> `readonly` **category**: `string`

Defined in: [src/common/web/data/entities/connector/Connector.ts:65](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/Connector.ts#L65)

***

### connector\_address

> `readonly` **connector\_address**: [`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/data/entities/connector/Connector.ts:61](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/Connector.ts#L61)

***

### connector\_id

> `readonly` **connector\_id**: `string`

Defined in: [src/common/web/data/entities/connector/Connector.ts:58](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/Connector.ts#L58)

***

### description

> `readonly` **description**: `string`

Defined in: [src/common/web/data/entities/connector/Connector.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/Connector.ts#L64)

***

### logos

> `readonly` **logos**: [`ConnectorLogos`](ConnectorLogos.md)

Defined in: [src/common/web/data/entities/connector/Connector.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/Connector.ts#L72)

***

### metadata\_profiles

> `readonly` **metadata\_profiles**: [`MetadataProfileContainerList`](../../../metadata/MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md) = `[]`

Defined in: [src/common/web/data/entities/connector/Connector.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/Connector.ts#L76)

***

### name

> `readonly` **name**: `string`

Defined in: [src/common/web/data/entities/connector/Connector.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/Connector.ts#L63)

***

### options

> `readonly` **options**: [`ConnectorOptions`](../enumerations/ConnectorOptions.md)

Defined in: [src/common/web/data/entities/connector/Connector.ts:68](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/Connector.ts#L68)
