---
id: "common_web_data_entities_connector_ConnectorUtils"
title: "Module: common/web/data/entities/connector/ConnectorUtils"
sidebar_label: "common/web/data/entities/connector/ConnectorUtils"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### connectorRequiresAuthorization

▸ **connectorRequiresAuthorization**(`connector`): `boolean`

Checks whether a connector requires authorization (and whether that authorization strategy is available).

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connector` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md) | The connector. |

#### Returns

`boolean`

#### Defined in

[src/common/web/data/entities/connector/ConnectorUtils.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorUtils.ts#L40)

___

### createAuthorizationStrategyFromConnector

▸ **createAuthorizationStrategyFromConnector**(`comp`, `svc`, `connector`): [`AuthorizationStrategy`](../classes/common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md) \| `undefined`

Creates the authorization strategy configured in a connector.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `comp` | [`WebComponent`](../classes/common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](../classes/common_web_ui_UserInterface.UserInterface.md)\> | The global component. |
| `svc` | [`Service`](../classes/common_web_services_Service.Service.md)<[`ServiceContext`](../classes/common_web_services_ServiceContext.ServiceContext.md)\> | The service to use for message sending. |
| `connector` | `undefined` \| [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md) | The connector. |

#### Returns

[`AuthorizationStrategy`](../classes/common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md) \| `undefined`

- The authorization strategy or **undefined** if none is required.

#### Defined in

[src/common/web/data/entities/connector/ConnectorUtils.ts:74](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorUtils.ts#L74)

___

### findConnectorByID

▸ **findConnectorByID**(`connectors`, `connectorID`): [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md) \| `undefined`

Searches for a connector by its ID within a list of connectors.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectors` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[] | The list of connectors. |
| `connectorID` | `string` | The connector to search for. |

#### Returns

[`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md) \| `undefined`

- The found connector or **undefined** otherwise.

#### Defined in

[src/common/web/data/entities/connector/ConnectorUtils.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorUtils.ts#L19)

___

### findConnectorInstanceByID

▸ **findConnectorInstanceByID**(`connectorInstances`, `instanceID`): [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md) \| `undefined`

Searches for a connector instance by its ID within a list of connector instances.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectorInstances` | [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)[] | The list of connector instances. |
| `instanceID` | `string` | The connector instance to search for. |

#### Returns

[`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md) \| `undefined`

- The found connector instance or **undefined** otherwise.

#### Defined in

[src/common/web/data/entities/connector/ConnectorUtils.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorUtils.ts#L31)

___

### getStrategyConfigurationFromConnector

▸ **getStrategyConfigurationFromConnector**(`connector`): `Record`<`string`, `any`\>

Creates a strategy configuration from the authorization settings of a connector.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connector` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md) | The connector. |

#### Returns

`Record`<`string`, `any`\>

- The strategy configuration.

#### Defined in

[src/common/web/data/entities/connector/ConnectorUtils.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorUtils.ts#L52)
