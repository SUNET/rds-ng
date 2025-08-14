---
id: "frontend_src_integration_HostIntegration"
title: "Module: frontend/src/integration/HostIntegration"
sidebar_label: "frontend/src/integration/HostIntegration"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### useHostIntegration

▸ **useHostIntegration**(`comp`): `Object`

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](../classes/frontend_src_component_FrontendComponent.FrontendComponent.md) |

#### Returns

`Object`

| Name | Type |
| :------ | :------ |
| `getHostAuthorizationSettings` | () => `Promise`<[`AuthorizationSettings`](../interfaces/common_web_data_entities_authorization_AuthorizationSettings.AuthorizationSettings.md)\> |
| `getHostResources` | () => `Promise`<[`HostResources`](../interfaces/frontend_src_integration_HostTypes.HostResources.md)\> |
| `getHostUserToken` | () => `Promise`<[`HostUserToken`](../interfaces/frontend_src_integration_HostTypes.HostUserToken.md)\> |

#### Defined in

[src/frontend/src/integration/HostIntegration.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/HostIntegration.ts#L11)
