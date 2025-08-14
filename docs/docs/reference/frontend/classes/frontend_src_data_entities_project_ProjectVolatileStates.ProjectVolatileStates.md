---
id: "frontend_src_data_entities_project_ProjectVolatileStates.ProjectVolatileStates"
title: "Class: ProjectVolatileStates"
sidebar_label: "ProjectVolatileStates"
custom_edit_url: null
---

[frontend/src/data/entities/project/ProjectVolatileStates](../modules/frontend_src_data_entities_project_ProjectVolatileStates.md).ProjectVolatileStates

Manages project volatile states.

## Constructors

### constructor

• **new ProjectVolatileStates**(): [`ProjectVolatileStates`](frontend_src_data_entities_project_ProjectVolatileStates.ProjectVolatileStates.md)

#### Returns

[`ProjectVolatileStates`](frontend_src_data_entities_project_ProjectVolatileStates.ProjectVolatileStates.md)

## Properties

### \_states

• `Private` `Readonly` **\_states**: [`ProjectVolatileState`](frontend_src_data_entities_project_ProjectVolatileState.ProjectVolatileState.md)[] = `[]`

#### Defined in

[src/frontend/src/data/entities/project/ProjectVolatileStates.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/project/ProjectVolatileStates.ts#L11)

## Methods

### addState

▸ **addState**(`projectID`, `connectorInstance`, `externalState`): `void`

Adds a new volatile state or updates an existing one.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `projectID` | `number` | The project ID. |
| `connectorInstance` | `string` | The connector instance. |
| `externalState` | [`ProjectExternalState`](common_web_data_entities_project_ProjectExternalState.ProjectExternalState.md) | The external state. |

#### Returns

`void`

#### Defined in

[src/frontend/src/data/entities/project/ProjectVolatileStates.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/project/ProjectVolatileStates.ts#L20)

___

### findState

▸ **findState**(`projectID`, `connectorInstance`): `undefined` \| [`ProjectVolatileState`](frontend_src_data_entities_project_ProjectVolatileState.ProjectVolatileState.md)

Finds the volatile state for a certain project and connector instance.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `projectID` | `number` | The project ID. |
| `connectorInstance` | `string` | The connector instance. |

#### Returns

`undefined` \| [`ProjectVolatileState`](frontend_src_data_entities_project_ProjectVolatileState.ProjectVolatileState.md)

The found volatile state or **undefined** otherwise.

#### Defined in

[src/frontend/src/data/entities/project/ProjectVolatileStates.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/project/ProjectVolatileStates.ts#L40)
