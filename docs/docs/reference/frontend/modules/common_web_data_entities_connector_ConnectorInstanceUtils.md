---
id: "common_web_data_entities_connector_ConnectorInstanceUtils"
title: "Module: common/web/data/entities/connector/ConnectorInstanceUtils"
sidebar_label: "common/web/data/entities/connector/ConnectorInstanceUtils"
sidebar_position: 0
custom_edit_url: null
---

## Interfaces

- [ConnectorInstancesGroup](../interfaces/common_web_data_entities_connector_ConnectorInstanceUtils.ConnectorInstancesGroup.md)

## Functions

### connectorInstanceIsAuthorized

▸ **connectorInstanceIsAuthorized**(`instance`, `authorizations`): `boolean`

Checks whether a connector instance is authorized.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `instance` | [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md) | The connector instance. |
| `authorizations` | `string`[] | A list of all granted authorizations. |

#### Returns

`boolean`

#### Defined in

[src/common/web/data/entities/connector/ConnectorInstanceUtils.ts:99](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorInstanceUtils.ts#L99)

___

### createAuthorizationStrategyFromConnectorInstance

▸ **createAuthorizationStrategyFromConnectorInstance**(`comp`, `svc`, `instance`, `connectors`): [`AuthorizationStrategy`](../classes/common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md) \| `undefined`

Creates the authorization strategy configured in a connector instance.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `comp` | [`WebComponent`](../classes/common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](../classes/common_web_ui_UserInterface.UserInterface.md)\> | The global component. |
| `svc` | [`Service`](../classes/common_web_services_Service.Service.md)<[`ServiceContext`](../classes/common_web_services_ServiceContext.ServiceContext.md)\> | The service to use for message sending. |
| `instance` | [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md) | The connector instance. |
| `connectors` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[] | List of all connectors. |

#### Returns

[`AuthorizationStrategy`](../classes/common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md) \| `undefined`

- The authorization strategy or **undefined** if none is required.

#### Defined in

[src/common/web/data/entities/connector/ConnectorInstanceUtils.ts:83](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorInstanceUtils.ts#L83)

___

### findConnectorByInstanceID

▸ **findConnectorByInstanceID**(`connectors`, `connectorInstances`, `instanceID`): [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md) \| `undefined`

Searches for a connector using a connector instance ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectors` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[] | The list of connectors. |
| `connectorInstances` | [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)[] | The list of connector instances. |
| `instanceID` | `string` | The connector instance ID. |

#### Returns

[`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md) \| `undefined`

- The found connector or **undefined** otherwise.

#### Defined in

[src/common/web/data/entities/connector/ConnectorInstanceUtils.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorInstanceUtils.ts#L64)

___

### groupConnectorInstances

▸ **groupConnectorInstances**(`connectorInstances`, `connectors?`): [`ConnectorInstancesGroup`](../interfaces/common_web_data_entities_connector_ConnectorInstanceUtils.ConnectorInstancesGroup.md)[]

Function to return all connector instances grouped by their used connectors. By default, the groups are sorted by their IDs; if a list of
connectors is given, the display name is used instead.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectorInstances` | [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)[] | The connector instances. |
| `connectors?` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[] | List of available connectors used to sort the groups by their display names. |

#### Returns

[`ConnectorInstancesGroup`](../interfaces/common_web_data_entities_connector_ConnectorInstanceUtils.ConnectorInstancesGroup.md)[]

- The grouped connector instances.

#### Defined in

[src/common/web/data/entities/connector/ConnectorInstanceUtils.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/connector/ConnectorInstanceUtils.ts#L26)
