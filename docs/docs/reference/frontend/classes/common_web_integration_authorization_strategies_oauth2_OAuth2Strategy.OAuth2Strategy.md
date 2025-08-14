---
id: "common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2Strategy"
title: "Class: OAuth2Strategy"
sidebar_label: "OAuth2Strategy"
custom_edit_url: null
---

[common/web/integration/authorization/strategies/oauth2/OAuth2Strategy](../modules/common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.md).OAuth2Strategy

OAuth2 authorization strategy.

## Hierarchy

- [`AuthorizationStrategy`](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md)

  ↳ **`OAuth2Strategy`**

## Constructors

### constructor

• **new OAuth2Strategy**(`comp`, `svc`, `config`): [`OAuth2Strategy`](common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2Strategy.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`WebComponent`](common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](common_web_ui_UserInterface.UserInterface.md)\> |
| `svc` | [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\> |
| `config` | [`OAuth2StrategyConfiguration`](../interfaces/common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2StrategyConfiguration.md) |

#### Returns

[`OAuth2Strategy`](common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2Strategy.md)

#### Overrides

[AuthorizationStrategy](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md).[constructor](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md#constructor)

#### Defined in

[src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L34)

## Properties

### \_component

• `Protected` `Readonly` **\_component**: [`WebComponent`](common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](common_web_ui_UserInterface.UserInterface.md)\>

#### Inherited from

[AuthorizationStrategy](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md).[_component](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md#_component)

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L20)

___

### \_config

• `Private` `Readonly` **\_config**: [`OAuth2StrategyConfiguration`](../interfaces/common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2StrategyConfiguration.md)

#### Defined in

[src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L32)

___

### \_redirectionTarget

• `Protected` `Readonly` **\_redirectionTarget**: [`RedirectionTarget`](../enums/common_web_utils_HTMLUtils.RedirectionTarget.md)

#### Inherited from

[AuthorizationStrategy](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md).[_redirectionTarget](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md#_redirectiontarget)

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L23)

___

### \_service

• `Protected` `Readonly` **\_service**: [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

#### Inherited from

[AuthorizationStrategy](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md).[_service](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md#_service)

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L21)

___

### Strategy

▪ `Static` `Readonly` **Strategy**: ``"oauth2"``

#### Defined in

[src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L30)

## Accessors

### strategy

• `get` **strategy**(): `string`

The strategy identifier.

#### Returns

`string`

#### Inherited from

AuthorizationStrategy.strategy

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:159](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L159)

## Methods

### executeAuthorizationRequest

▸ **executeAuthorizationRequest**(`authRequest`): `Promise`<[`AuthorizationState`](../enums/common_web_data_entities_authorization_AuthorizationState.AuthorizationState.md)\>

Executes an authorization requests (requires a preceding initiation).

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `authRequest` | [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md) | The authorization request. |

#### Returns

`Promise`<[`AuthorizationState`](../enums/common_web_data_entities_authorization_AuthorizationState.AuthorizationState.md)\>

#### Inherited from

[AuthorizationStrategy](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md).[executeAuthorizationRequest](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md#executeauthorizationrequest)

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L52)

___

### finishRequest

▸ **finishRequest**(): `void`

#### Returns

`void`

#### Overrides

[AuthorizationStrategy](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md).[finishRequest](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md#finishrequest)

#### Defined in

[src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L70)

___

### getRequestData

▸ **getRequestData**(`_`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `_` | [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md) |

#### Returns

`any`

#### Overrides

[AuthorizationStrategy](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md).[getRequestData](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md#getrequestdata)

#### Defined in

[src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L52)

___

### initiateAuthorizationRequest

▸ **initiateAuthorizationRequest**(`authRequest`): `void`

Initiates an authorization request.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `authRequest` | [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md) | The authorization request. |

#### Returns

`void`

#### Inherited from

[AuthorizationStrategy](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md).[initiateAuthorizationRequest](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md#initiateauthorizationrequest)

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L43)

___

### initiateRequest

▸ **initiateRequest**(`authRequest`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `authRequest` | [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md) |

#### Returns

`void`

#### Overrides

[AuthorizationStrategy](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md).[initiateRequest](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md#initiaterequest)

#### Defined in

[src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L40)

___

### redirect

▸ **redirect**(`url`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `url` | `string` |

#### Returns

`void`

#### Inherited from

[AuthorizationStrategy](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md).[redirect](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md#redirect)

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:117](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L117)

___

### requestAuthorization

▸ **requestAuthorization**(`authState`, `authRequest`): `Promise`<[`AuthorizationState`](../enums/common_web_data_entities_authorization_AuthorizationState.AuthorizationState.md)\>

Requests user authorization, handling all steps automatically.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `authState` | [`AuthorizationState`](../enums/common_web_data_entities_authorization_AuthorizationState.AuthorizationState.md) | The current authorization state. |
| `authRequest` | [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md) | The authorization request. |

#### Returns

`Promise`<[`AuthorizationState`](../enums/common_web_data_entities_authorization_AuthorizationState.AuthorizationState.md)\>

#### Inherited from

[AuthorizationStrategy](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md).[requestAuthorization](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md#requestauthorization)

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:84](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L84)

___

### requestCompleted

▸ **requestCompleted**(`cb`): [`OAuth2Strategy`](common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2Strategy.md)

Adds a callback for completed requests.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`AuthorizationRequestCallback`](../modules/common_web_integration_authorization_strategies_AuthorizationStrategy.md#authorizationrequestcallback) | The callback to add. |

#### Returns

[`OAuth2Strategy`](common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2Strategy.md)

#### Inherited from

[AuthorizationStrategy](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md).[requestCompleted](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md#requestcompleted)

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:106](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L106)
