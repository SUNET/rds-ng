---
id: "frontend_src_integration_authorization_AuthorizationRequestsHandler.AuthorizationRequestsHandler"
title: "Class: AuthorizationRequestsHandler"
sidebar_label: "AuthorizationRequestsHandler"
custom_edit_url: null
---

[frontend/src/integration/authorization/AuthorizationRequestsHandler](../modules/frontend_src_integration_authorization_AuthorizationRequestsHandler.md).AuthorizationRequestsHandler

Class to handle pending authorization requests (except for host authorization).

## Constructors

### constructor

• **new AuthorizationRequestsHandler**(`comp`, `svc`): [`AuthorizationRequestsHandler`](frontend_src_integration_authorization_AuthorizationRequestsHandler.AuthorizationRequestsHandler.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `comp` | [`WebComponent`](common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](common_web_ui_UserInterface.UserInterface.md)\> | The global component. |
| `svc` | [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\> | The service used for message sending. |

#### Returns

[`AuthorizationRequestsHandler`](frontend_src_integration_authorization_AuthorizationRequestsHandler.AuthorizationRequestsHandler.md)

#### Defined in

[src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts#L24)

## Properties

### \_component

• `Private` `Readonly` **\_component**: [`WebComponent`](common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](common_web_ui_UserInterface.UserInterface.md)\>

#### Defined in

[src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts#L17)

___

### \_service

• `Private` `Readonly` **\_service**: [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

#### Defined in

[src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts#L18)

## Methods

### createAuthStrategy

▸ **createAuthStrategy**(`authRequest`): `undefined` \| [`AuthorizationStrategy`](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `authRequest` | [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md) |

#### Returns

`undefined` \| [`AuthorizationStrategy`](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md)

#### Defined in

[src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts:56](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts#L56)

___

### createAuthStrategyForConnectorInstance

▸ **createAuthStrategyForConnectorInstance**(`authRequest`): `undefined` \| [`AuthorizationStrategy`](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `authRequest` | [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md) |

#### Returns

`undefined` \| [`AuthorizationStrategy`](common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md)

#### Defined in

[src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts:67](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts#L67)

___

### getLoggingParams

▸ **getLoggingParams**(`authRequest`): `Record`<`string`, `any`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `authRequest` | [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md) |

#### Returns

`Record`<`string`, `any`\>

#### Defined in

[src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts:78](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts#L78)

___

### handlePendingRequests

▸ **handlePendingRequests**(): `Promise`<`void`\>

#### Returns

`Promise`<`void`\>

#### Defined in

[src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts#L29)

___

### handleRequest

▸ **handleRequest**(`authRequest`, `resolve`, `reject`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `authRequest` | [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md) |
| `resolve` | () => `void` |
| `reject` | (`msg`: `string`) => `void` |

#### Returns

`void`

#### Defined in

[src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts#L37)
