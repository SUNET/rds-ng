---
id: "common_web_integration_HostCommunication"
title: "Module: common/web/integration/HostCommunication"
sidebar_label: "common/web/integration/HostCommunication"
sidebar_position: 0
custom_edit_url: null
---

## Enumerations

- [HostCommuncationAction](../enums/common_web_integration_HostCommunication.HostCommuncationAction.md)

## Interfaces

- [HostCommunicationActionMessage](../interfaces/common_web_integration_HostCommunication.HostCommunicationActionMessage.md)

## Functions

### sendActionToHost

▸ **sendActionToHost**(`action`, `data?`): `void`

Sends an action to the host (parent).

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `action` | [`HostCommuncationAction`](../enums/common_web_integration_HostCommunication.HostCommuncationAction.md) | `undefined` | The action to send. |
| `data` | `any` | `undefined` | Optional action data. |

#### Returns

`void`

#### Defined in

[src/common/web/integration/HostCommunication.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/HostCommunication.ts#L23)
