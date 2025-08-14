---
id: "common_web_integration_authorization_AuthorizationRequest.AuthorizationRequestPayload"
title: "Interface: AuthorizationRequestPayload"
sidebar_label: "AuthorizationRequestPayload"
custom_edit_url: null
---

[common/web/integration/authorization/AuthorizationRequest](../modules/common_web_integration_authorization_AuthorizationRequest.md).AuthorizationRequestPayload

The payload that is sent with authorization requests.

## Properties

### auth\_bearer

• **auth\_bearer**: `string`

The entity that will be authorized against.

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L15)

___

### auth\_id

• **auth\_id**: `string`

The authorization ID.

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L9)

___

### auth\_issuer

• **auth\_issuer**: `string`

The entity that requires the authorization.

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L13)

___

### auth\_type

• **auth\_type**: [`AuthorizationTokenType`](../enums/common_web_data_entities_authorization_AuthorizationToken.AuthorizationTokenType.md)

The authorization type.

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L11)

___

### fingerprint

• **fingerprint**: `string`

The user's fingerprint.

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L17)
