---
id: "frontend_src_data_entities_connector_categories_ConnectorCategory.ConnectorCategory"
title: "Class: ConnectorCategory"
sidebar_label: "ConnectorCategory"
custom_edit_url: null
---

[frontend/src/data/entities/connector/categories/ConnectorCategory](../modules/frontend_src_data_entities_connector_categories_ConnectorCategory.md).ConnectorCategory

Descriptor for a connector category.

**`Param`**

The category name.

**`Param`**

An optional description.

## Hierarchy

- **`ConnectorCategory`**

  ↳ [`ArchiveConnectorCategory`](frontend_src_data_entities_connector_categories_ArchiveConnectorCategory.ArchiveConnectorCategory.md)

  ↳ [`RepositoryConnectorCategory`](frontend_src_data_entities_connector_categories_RepositoryConnectorCategory.RepositoryConnectorCategory.md)

## Constructors

### constructor

• **new ConnectorCategory**(`name`, `description`, `verbAction`, `verbNoun`, `verbNounPlural`, `verbStatusProgressing`, `verbStatusDone`, `tagClass?`, `buttonClass?`): [`ConnectorCategory`](frontend_src_data_entities_connector_categories_ConnectorCategory.ConnectorCategory.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `name` | `string` |
| `description` | `string` |
| `verbAction` | `string` |
| `verbNoun` | `string` |
| `verbNounPlural` | `string` |
| `verbStatusProgressing` | `string` |
| `verbStatusDone` | `string` |
| `tagClass?` | `string` |
| `buttonClass?` | `string` |

#### Returns

[`ConnectorCategory`](frontend_src_data_entities_connector_categories_ConnectorCategory.ConnectorCategory.md)

#### Defined in

[src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts#L19)

## Properties

### description

• `Readonly` **description**: `string`

#### Defined in

[src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts#L9)

___

### name

• `Readonly` **name**: `string`

#### Defined in

[src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts#L8)

___

### tagClass

• `Readonly` **tagClass**: `undefined` \| `string`

#### Defined in

[src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts#L17)

___

### verbAction

• `Readonly` **verbAction**: `string`

#### Defined in

[src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts#L11)

___

### verbNoun

• `Readonly` **verbNoun**: `string`

#### Defined in

[src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts#L12)

___

### verbNounPlural

• `Readonly` **verbNounPlural**: `string`

#### Defined in

[src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts#L13)

___

### verbStatusDone

• `Readonly` **verbStatusDone**: `string`

#### Defined in

[src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts#L15)

___

### verbStatusProgressing

• `Readonly` **verbStatusProgressing**: `string`

#### Defined in

[src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/connector/categories/ConnectorCategory.ts#L14)
