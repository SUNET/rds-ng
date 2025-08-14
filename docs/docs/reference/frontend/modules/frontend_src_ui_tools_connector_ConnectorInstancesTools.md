---
id: "frontend_src_ui_tools_connector_ConnectorInstancesTools"
title: "Module: frontend/src/ui/tools/connector/ConnectorInstancesTools"
sidebar_label: "frontend/src/ui/tools/connector/ConnectorInstancesTools"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### useConnectorInstancesTools

▸ **useConnectorInstancesTools**(`comp`): `Object`

Tools for working with connector instances.

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](../classes/frontend_src_component_FrontendComponent.FrontendComponent.md) |

#### Returns

`Object`

| Name | Type |
| :------ | :------ |
| `deleteInstance` | (`instances`: [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)[], `instance`: [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)) => `void` |
| `editInstance` | (`instances`: [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)[], `instance`: [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md), `connector?`: [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)) => `Promise`<[`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)\> |
| `newInstance` | (`instances`: [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)[], `connector`: [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)) => `Promise`<[`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md)\> |
| `requestInstanceAuthorization` | (`instance`: [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md), `connectors`: [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[], `authorizations`: `string`[]) => `void` |
| `revokeInstanceAuthorization` | (`instance`: [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md), `updateAuthState`: `boolean`) => `void` |

#### Defined in

[src/frontend/src/ui/tools/connector/ConnectorInstancesTools.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/tools/connector/ConnectorInstancesTools.ts#L19)
