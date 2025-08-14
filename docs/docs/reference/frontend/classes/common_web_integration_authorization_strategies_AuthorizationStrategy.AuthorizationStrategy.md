---
id: "common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy"
title: "Class: AuthorizationStrategy"
sidebar_label: "AuthorizationStrategy"
custom_edit_url: null
---

[common/web/integration/authorization/strategies/AuthorizationStrategy](../modules/common_web_integration_authorization_strategies_AuthorizationStrategy.md).AuthorizationStrategy

Base class for all authorization strategies.

## Hierarchy

- **`AuthorizationStrategy`**

  ↳ [`OAuth2Strategy`](common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2Strategy.md)

## Constructors

### constructor

• **new AuthorizationStrategy**(`comp`, `svc`, `strategy`, `redirectionTarget?`): [`AuthorizationStrategy`](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `comp` | [`WebComponent`](common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](common_web_ui_UserInterface.UserInterface.md)\> | `undefined` |
| `svc` | [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\> | `undefined` |
| `strategy` | `string` | `undefined` |
| `redirectionTarget` | [`RedirectionTarget`](../enums/common_web_utils_HTMLUtils.RedirectionTarget.md) | `RedirectionTarget.Current` |

#### Returns

[`AuthorizationStrategy`](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md)

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L29)

## Properties

### \_component

• `Protected` `Readonly` **\_component**: [`WebComponent`](common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](common_web_ui_UserInterface.UserInterface.md)\>

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L20)

___

### \_executionCallbacks

• `Private` `Readonly` **\_executionCallbacks**: [`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<[`AuthorizationRequestCallback`](../modules/common_web_integration_authorization_strategies_AuthorizationStrategy.md#authorizationrequestcallback), [`AuthorizationRequestCallback`](../modules/common_web_integration_authorization_strategies_AuthorizationStrategy.md#authorizationrequestcallback)\>

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L27)

___

### \_redirectionTarget

• `Protected` `Readonly` **\_redirectionTarget**: [`RedirectionTarget`](../enums/common_web_utils_HTMLUtils.RedirectionTarget.md)

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L23)

___

### \_service

• `Protected` `Readonly` **\_service**: [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L21)

___

### \_strategy

• `Private` `Readonly` **\_strategy**: `string`

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L25)

## Accessors

### strategy

• `get` **strategy**(): `string`

The strategy identifier.

#### Returns

`string`

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

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L52)

___

### finishRequest

▸ **finishRequest**(): `void`

#### Returns

`void`

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:115](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L115)

___

### getRequestData

▸ **getRequestData**(`authRequest`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `authRequest` | [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md) |

#### Returns

`any`

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:113](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L113)

___

### handleRequestCompletion

▸ **handleRequestCompletion**(): `void`

#### Returns

`void`

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:151](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L151)

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

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:111](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L111)

___

### redirect

▸ **redirect**(`url`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `url` | `string` |

#### Returns

`void`

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

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:84](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L84)

___

### requestCompleted

▸ **requestCompleted**(`cb`): [`AuthorizationStrategy`](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md)

Adds a callback for completed requests.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`AuthorizationRequestCallback`](../modules/common_web_integration_authorization_strategies_AuthorizationStrategy.md#authorizationrequestcallback) | The callback to add. |

#### Returns

[`AuthorizationStrategy`](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md)

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:106](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L106)
