---
id: "frontend_src_integration_HostTypes"
title: "Module: frontend/src/integration/HostTypes"
sidebar_label: "frontend/src/integration/HostTypes"
sidebar_position: 0
custom_edit_url: null
---

## Interfaces

- [HostResources](../interfaces/frontend_src_integration_HostTypes.HostResources.md)
- [HostUserToken](../interfaces/frontend_src_integration_HostTypes.HostUserToken.md)

## Functions

### hostUserTokenFromData

▸ **hostUserTokenFromData**(`data`): [`HostUserToken`](../interfaces/frontend_src_integration_HostTypes.HostUserToken.md)

Converts an object (usually JSON) into a HostUserToken.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `data` | `Record`<`string`, `any`\> | The JSON data. |

#### Returns

[`HostUserToken`](../interfaces/frontend_src_integration_HostTypes.HostUserToken.md)

- The host user token.

#### Defined in

[src/frontend/src/integration/HostTypes.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/HostTypes.ts#L19)
