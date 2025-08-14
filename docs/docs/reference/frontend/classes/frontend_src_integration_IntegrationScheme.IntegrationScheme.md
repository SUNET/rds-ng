---
id: "frontend_src_integration_IntegrationScheme.IntegrationScheme"
title: "Class: IntegrationScheme"
sidebar_label: "IntegrationScheme"
custom_edit_url: null
---

[frontend/src/integration/IntegrationScheme](../modules/frontend_src_integration_IntegrationScheme.md).IntegrationScheme

Base class for integration schemes.

## Hierarchy

- **`IntegrationScheme`**

  ↳ [`BasicIntegrationScheme`](frontend_src_integration_schemes_BasicIntegrationScheme.BasicIntegrationScheme.md)

  ↳ [`HostIntegrationScheme`](frontend_src_integration_schemes_HostIntegrationScheme.HostIntegrationScheme.md)

## Constructors

### constructor

• **new IntegrationScheme**(`comp`, `scheme`, `integrationComponent`): [`IntegrationScheme`](frontend_src_integration_IntegrationScheme.IntegrationScheme.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) |
| `scheme` | `string` |
| `integrationComponent` | [`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent) |

#### Returns

[`IntegrationScheme`](frontend_src_integration_IntegrationScheme.IntegrationScheme.md)

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L25)

## Properties

### \_component

• `Protected` `Readonly` **\_component**: [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L19)

___

### \_integrationComponent

• `Private` `Readonly` **\_integrationComponent**: [`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent)

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L23)

___

### \_scheme

• `Private` `Readonly` **\_scheme**: `string`

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L21)

## Accessors

### integrationComponent

• `get` **integrationComponent**(): [`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent)

The integration component used during the login process.

#### Returns

[`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent)

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L101)

___

### isIntegrated

• `get` **isIntegrated**(): `boolean`

Checks whether the integration has completed.

#### Returns

`boolean`

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:51](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L51)

___

### scheme

• `get` **scheme**(): `string`

The scheme identifier.

#### Returns

`string`

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:94](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L94)

## Methods

### authenticator

▸ **authenticator**(`...args`): [`Authenticator`](frontend_src_integration_authentication_Authenticator.Authenticator.md)

Creates a new authenticator.

#### Parameters

| Name | Type |
| :------ | :------ |
| `...args` | `any`[] |

#### Returns

[`Authenticator`](frontend_src_integration_authentication_Authenticator.Authenticator.md)

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L36)

___

### authorizer

▸ **authorizer**(`...args`): [`Authorizer`](frontend_src_integration_authorization_Authorizer.Authorizer.md)

Creates a new authorizer.

#### Parameters

| Name | Type |
| :------ | :------ |
| `...args` | `any`[] |

#### Returns

[`Authorizer`](frontend_src_integration_authorization_Authorizer.Authorizer.md)

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L41)

___

### endSession

▸ **endSession**(): `void`

Called when the user leaves the main view.

#### Returns

`void`

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L89)

___

### enter

▸ **enter**(): `void`

Called when the user enters the app.

#### Returns

`void`

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:60](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L60)

___

### handlePendingAuthorizationRequests

▸ **handlePendingAuthorizationRequests**(): `Promise`<`void`\>

#### Returns

`Promise`<`void`\>

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:105](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L105)

___

### leave

▸ **leave**(): `void`

Called when the user leaves the app (e.g., by closing or refreshing it).

#### Returns

`void`

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:65](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L65)

___

### resourcesBroker

▸ **resourcesBroker**(`...args`): [`ResourcesBroker`](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md)

Creates a new resources broker.

#### Parameters

| Name | Type |
| :------ | :------ |
| `...args` | `any`[] |

#### Returns

[`ResourcesBroker`](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md)

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L46)

___

### startSession

▸ **startSession**(): `Promise`<`void`\>

Called when the app has launched after completed integration.

#### Returns

`Promise`<`void`\>

- A promise that can be used to perform tasks after post-initialization.

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L72)
