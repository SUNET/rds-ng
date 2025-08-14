---
id: "common_web_data_entities_connector_ConnectorInstance.ConnectorInstance"
title: "Class: ConnectorInstance"
sidebar_label: "ConnectorInstance"
custom_edit_url: null
---

[common/web/data/entities/connector/ConnectorInstance](../modules/common_web_data_entities_connector_ConnectorInstance.md).ConnectorInstance

A configured connector instance (i.e., a connector the user has added to his configuration).

**`Param`**

The ID of the connector instance.

**`Param`**

The assigned connector.

**`Param`**

The name of this connector instance.

**`Param`**

The instance description.

## Constructors

### constructor

• **new ConnectorInstance**(`instanceID`, `connectorID`, `name`, `description?`): [`ConnectorInstance`](common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `instanceID` | `string` | `undefined` |
| `connectorID` | `string` | `undefined` |
| `name` | `string` | `undefined` |
| `description` | `string` | `""` |

#### Returns

[`ConnectorInstance`](common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)

#### Defined in

[src/common/web/data/entities/connector/ConnectorInstance.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorInstance.ts#L24)

## Properties

### connector\_id

• `Readonly` **connector\_id**: `string`

#### Defined in

[src/common/web/data/entities/connector/ConnectorInstance.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorInstance.ts#L19)

___

### description

• `Readonly` **description**: `string`

#### Defined in

[src/common/web/data/entities/connector/ConnectorInstance.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorInstance.ts#L22)

___

### instance\_id

• `Readonly` **instance\_id**: `string`

#### Defined in

[src/common/web/data/entities/connector/ConnectorInstance.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorInstance.ts#L17)

___

### name

• `Readonly` **name**: `string`

#### Defined in

[src/common/web/data/entities/connector/ConnectorInstance.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorInstance.ts#L21)
