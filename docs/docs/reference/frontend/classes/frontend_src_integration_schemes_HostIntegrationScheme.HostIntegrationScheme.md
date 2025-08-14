---
id: "frontend_src_integration_schemes_HostIntegrationScheme.HostIntegrationScheme"
title: "Class: HostIntegrationScheme"
sidebar_label: "HostIntegrationScheme"
custom_edit_url: null
---

[frontend/src/integration/schemes/HostIntegrationScheme](../modules/frontend_src_integration_schemes_HostIntegrationScheme.md).HostIntegrationScheme

Basic authentication using a simple username.

## Hierarchy

- [`IntegrationScheme`](frontend_src_integration_IntegrationScheme.IntegrationScheme.md)

  ↳ **`HostIntegrationScheme`**

## Constructors

### constructor

• **new HostIntegrationScheme**(`comp`): [`HostIntegrationScheme`](frontend_src_integration_schemes_HostIntegrationScheme.HostIntegrationScheme.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) |

#### Returns

[`HostIntegrationScheme`](frontend_src_integration_schemes_HostIntegrationScheme.HostIntegrationScheme.md)

#### Overrides

[IntegrationScheme](frontend_src_integration_IntegrationScheme.IntegrationScheme.md).[constructor](frontend_src_integration_IntegrationScheme.IntegrationScheme.md#constructor)

#### Defined in

[src/frontend/src/integration/schemes/HostIntegrationScheme.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/schemes/HostIntegrationScheme.ts#L22)

## Properties

### \_component

• `Protected` `Readonly` **\_component**: [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

#### Inherited from

[IntegrationScheme](frontend_src_integration_IntegrationScheme.IntegrationScheme.md).[_component](frontend_src_integration_IntegrationScheme.IntegrationScheme.md#_component)

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L19)

___

### Scheme

▪ `Static` `Readonly` **Scheme**: ``"host"``

#### Defined in

[src/frontend/src/integration/schemes/HostIntegrationScheme.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/schemes/HostIntegrationScheme.ts#L20)

## Accessors

### integrationComponent

• `get` **integrationComponent**(): [`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent)

The integration component used during the login process.

#### Returns

[`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent)

#### Inherited from

IntegrationScheme.integrationComponent

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L101)

___

### isIntegrated

• `get` **isIntegrated**(): `boolean`

Checks whether the integration has completed.

#### Returns

`boolean`

#### Inherited from

IntegrationScheme.isIntegrated

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:51](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L51)

___

### scheme

• `get` **scheme**(): `string`

The scheme identifier.

#### Returns

`string`

#### Inherited from

IntegrationScheme.scheme

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:94](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L94)

## Methods

### authenticator

▸ **authenticator**(`token`): [`Authenticator`](frontend_src_integration_authentication_Authenticator.Authenticator.md)

Creates a new authenticator.

#### Parameters

| Name | Type |
| :------ | :------ |
| `token` | [`HostUserToken`](../interfaces/frontend_src_integration_HostTypes.HostUserToken.md) |

#### Returns

[`Authenticator`](frontend_src_integration_authentication_Authenticator.Authenticator.md)

#### Overrides

[IntegrationScheme](frontend_src_integration_IntegrationScheme.IntegrationScheme.md).[authenticator](frontend_src_integration_IntegrationScheme.IntegrationScheme.md#authenticator)

#### Defined in

[src/frontend/src/integration/schemes/HostIntegrationScheme.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/schemes/HostIntegrationScheme.ts#L30)

___

### authorizer

▸ **authorizer**(`hostAuth`): [`Authorizer`](frontend_src_integration_authorization_Authorizer.Authorizer.md)

Creates a new authorizer.

#### Parameters

| Name | Type |
| :------ | :------ |
| `hostAuth` | [`AuthorizationSettings`](../interfaces/common_web_data_entities_authorization_AuthorizationSettings.AuthorizationSettings.md) |

#### Returns

[`Authorizer`](frontend_src_integration_authorization_Authorizer.Authorizer.md)

#### Overrides

[IntegrationScheme](frontend_src_integration_IntegrationScheme.IntegrationScheme.md).[authorizer](frontend_src_integration_IntegrationScheme.IntegrationScheme.md#authorizer)

#### Defined in

[src/frontend/src/integration/schemes/HostIntegrationScheme.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/schemes/HostIntegrationScheme.ts#L34)

___

### endSession

▸ **endSession**(): `void`

Called when the user leaves the main view.

#### Returns

`void`

#### Inherited from

[IntegrationScheme](frontend_src_integration_IntegrationScheme.IntegrationScheme.md).[endSession](frontend_src_integration_IntegrationScheme.IntegrationScheme.md#endsession)

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L89)

___

### enter

▸ **enter**(): `void`

Called when the user enters the app.

#### Returns

`void`

#### Overrides

[IntegrationScheme](frontend_src_integration_IntegrationScheme.IntegrationScheme.md).[enter](frontend_src_integration_IntegrationScheme.IntegrationScheme.md#enter)

#### Defined in

[src/frontend/src/integration/schemes/HostIntegrationScheme.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/schemes/HostIntegrationScheme.ts#L42)

___

### leave

▸ **leave**(): `void`

Called when the user leaves the app (e.g., by closing or refreshing it).

#### Returns

`void`

#### Overrides

[IntegrationScheme](frontend_src_integration_IntegrationScheme.IntegrationScheme.md).[leave](frontend_src_integration_IntegrationScheme.IntegrationScheme.md#leave)

#### Defined in

[src/frontend/src/integration/schemes/HostIntegrationScheme.ts:48](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/schemes/HostIntegrationScheme.ts#L48)

___

### resetLogin

▸ **resetLogin**(): `void`

#### Returns

`void`

#### Defined in

[src/frontend/src/integration/schemes/HostIntegrationScheme.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/schemes/HostIntegrationScheme.ts#L54)

___

### resourcesBroker

▸ **resourcesBroker**(`hostResources`): [`ResourcesBroker`](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md)

Creates a new resources broker.

#### Parameters

| Name | Type |
| :------ | :------ |
| `hostResources` | [`HostResources`](../interfaces/frontend_src_integration_HostTypes.HostResources.md) |

#### Returns

[`ResourcesBroker`](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md)

#### Overrides

[IntegrationScheme](frontend_src_integration_IntegrationScheme.IntegrationScheme.md).[resourcesBroker](frontend_src_integration_IntegrationScheme.IntegrationScheme.md#resourcesbroker)

#### Defined in

[src/frontend/src/integration/schemes/HostIntegrationScheme.ts:38](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/schemes/HostIntegrationScheme.ts#L38)

___

### startSession

▸ **startSession**(): `Promise`<`void`\>

Called when the app has launched after completed integration.

#### Returns

`Promise`<`void`\>

- A promise that can be used to perform tasks after post-initialization.

#### Inherited from

[IntegrationScheme](frontend_src_integration_IntegrationScheme.IntegrationScheme.md).[startSession](frontend_src_integration_IntegrationScheme.IntegrationScheme.md#startsession)

#### Defined in

[src/frontend/src/integration/IntegrationScheme.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationScheme.ts#L72)
