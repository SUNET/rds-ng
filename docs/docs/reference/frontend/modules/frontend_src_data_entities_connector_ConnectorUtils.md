---
id: "frontend_src_data_entities_connector_ConnectorUtils"
title: "Module: frontend/src/data/entities/connector/ConnectorUtils"
sidebar_label: "frontend/src/data/entities/connector/ConnectorUtils"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### findConnectorCategory

▸ **findConnectorCategory**(`connector`): [`ConnectorCategory`](../classes/frontend_src_data_entities_connector_categories_ConnectorCategory.ConnectorCategory.md) \| `undefined`

Retrieves the category of a connector or undefined otherwise.

#### Parameters

| Name | Type |
| :------ | :------ |
| `connector` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md) |

#### Returns

[`ConnectorCategory`](../classes/frontend_src_data_entities_connector_categories_ConnectorCategory.ConnectorCategory.md) \| `undefined`

#### Defined in

[src/frontend/src/data/entities/connector/ConnectorUtils.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/connector/ConnectorUtils.ts#L11)

___

### findConnectorCategoryByInstanceID

▸ **findConnectorCategoryByInstanceID**(`connectors`, `connectorInstances`, `instanceID`): [`ConnectorCategory`](../classes/frontend_src_data_entities_connector_categories_ConnectorCategory.ConnectorCategory.md) \| `undefined`

Retrieves the category of a connector instance.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectors` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[] | The connectors. |
| `connectorInstances` | [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)[] | The connector instances. |
| `instanceID` | `string` | The instance ID. |

#### Returns

[`ConnectorCategory`](../classes/frontend_src_data_entities_connector_categories_ConnectorCategory.ConnectorCategory.md) \| `undefined`

- The connector category, if any.

#### Defined in

[src/frontend/src/data/entities/connector/ConnectorUtils.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/connector/ConnectorUtils.ts#L24)
