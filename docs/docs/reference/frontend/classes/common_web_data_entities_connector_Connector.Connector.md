---
id: "common_web_data_entities_connector_Connector.Connector"
title: "Class: Connector"
sidebar_label: "Connector"
custom_edit_url: null
---

[common/web/data/entities/connector/Connector](../modules/common_web_data_entities_connector_Connector.md).Connector

Data for a single **Connector**.

**`Param`**

The unique connector identifier.

**`Param`**

The target address of the connector.

**`Param`**

The connector category.

**`Param`**

The name of the connector.

**`Param`**

An optional connector description.

**`Param`**

Authorization settings for the connector.

**`Param`**

The connector options.

**`Param`**

Image data of the connector logos.

**`Param`**

The profiles for connector-specific data.

**`Param`**

The timestamp when the connector was last announced.

## Constructors

### constructor

• **new Connector**(`connectorID`, `connectorAddress`, `name`, `description`, `category`, `authorization?`, `options?`, `logos?`, `metadataProfiles?`): [`Connector`](common_web_data_entities_connector_Connector.Connector.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `connectorID` | `string` | `undefined` |
| `connectorAddress` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | `undefined` |
| `name` | `string` | `undefined` |
| `description` | `string` | `undefined` |
| `category` | `string` | `undefined` |
| `authorization` | [`AuthorizationSettings`](../interfaces/common_web_data_entities_authorization_AuthorizationSettings.AuthorizationSettings.md) | `undefined` |
| `options` | [`ConnectorOptions`](../enums/common_web_data_entities_connector_Connector.ConnectorOptions.md) | `ConnectorOptions.Default` |
| `logos` | [`ConnectorLogos`](common_web_data_entities_connector_Connector.ConnectorLogos.md) | `undefined` |
| `metadataProfiles` | [`MetadataProfileContainerList`](../modules/common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist) | `[]` |

#### Returns

[`Connector`](common_web_data_entities_connector_Connector.Connector.md)

#### Defined in

[src/common/web/data/entities/connector/Connector.ts:80](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/Connector.ts#L80)

## Properties

### announce\_timestamp

• `Readonly` **announce\_timestamp**: `Number` = `0.0`

#### Defined in

[src/common/web/data/entities/connector/Connector.ts:78](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/Connector.ts#L78)

___

### authorization

• `Readonly` **authorization**: [`AuthorizationSettings`](../interfaces/common_web_data_entities_authorization_AuthorizationSettings.AuthorizationSettings.md)

#### Defined in

[src/common/web/data/entities/connector/Connector.ts:67](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/Connector.ts#L67)

___

### category

• `Readonly` **category**: `string`

#### Defined in

[src/common/web/data/entities/connector/Connector.ts:65](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/Connector.ts#L65)

___

### connector\_address

• `Readonly` **connector\_address**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Defined in

[src/common/web/data/entities/connector/Connector.ts:61](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/Connector.ts#L61)

___

### connector\_id

• `Readonly` **connector\_id**: `string`

#### Defined in

[src/common/web/data/entities/connector/Connector.ts:58](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/Connector.ts#L58)

___

### description

• `Readonly` **description**: `string`

#### Defined in

[src/common/web/data/entities/connector/Connector.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/Connector.ts#L64)

___

### logos

• `Readonly` **logos**: [`ConnectorLogos`](common_web_data_entities_connector_Connector.ConnectorLogos.md)

#### Defined in

[src/common/web/data/entities/connector/Connector.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/Connector.ts#L72)

___

### metadata\_profiles

• `Readonly` **metadata\_profiles**: [`MetadataProfileContainerList`](../modules/common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist) = `[]`

#### Defined in

[src/common/web/data/entities/connector/Connector.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/Connector.ts#L76)

___

### name

• `Readonly` **name**: `string`

#### Defined in

[src/common/web/data/entities/connector/Connector.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/Connector.ts#L63)

___

### options

• `Readonly` **options**: [`ConnectorOptions`](../enums/common_web_data_entities_connector_Connector.ConnectorOptions.md)

#### Defined in

[src/common/web/data/entities/connector/Connector.ts:68](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/Connector.ts#L68)
