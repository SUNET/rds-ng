---
id: "common_web_data_stores_NetworkStore.ConnectionState"
title: "Enumeration: ConnectionState"
sidebar_label: "ConnectionState"
custom_edit_url: null
---

[common/web/data/stores/NetworkStore](../modules/common_web_data_stores_NetworkStore.md).ConnectionState

The state of the connection to the server:
    - **Disconnected**: No connection is established
    - **Connected**: A connection has been established, but no remote information has been received yet
    - **Ready**: The connection has been established and the remote information has been received; the connection is ready to use

## Enumeration Members

### Connected

• **Connected** = ``1``

#### Defined in

[src/common/web/data/stores/NetworkStore.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/stores/NetworkStore.ts#L14)

___

### Disconnected

• **Disconnected** = ``0``

#### Defined in

[src/common/web/data/stores/NetworkStore.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/stores/NetworkStore.ts#L13)

___

### Ready

• **Ready** = ``2``

#### Defined in

[src/common/web/data/stores/NetworkStore.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/stores/NetworkStore.ts#L15)
