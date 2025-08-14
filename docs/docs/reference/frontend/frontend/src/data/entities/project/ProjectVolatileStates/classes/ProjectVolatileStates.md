# Class: ProjectVolatileStates

Defined in: [src/frontend/src/data/entities/project/ProjectVolatileStates.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/project/ProjectVolatileStates.ts#L10)

Manages project volatile states.

## Constructors

### Constructor

> **new ProjectVolatileStates**(): `ProjectVolatileStates`

#### Returns

`ProjectVolatileStates`

## Methods

### addState()

> **addState**(`projectID`, `connectorInstance`, `externalState`): `void`

Defined in: [src/frontend/src/data/entities/project/ProjectVolatileStates.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/project/ProjectVolatileStates.ts#L20)

Adds a new volatile state or updates an existing one.

#### Parameters

##### projectID

`number`

The project ID.

##### connectorInstance

`string`

The connector instance.

##### externalState

[`ProjectExternalState`](../../../../../../../common/web/data/entities/project/ProjectExternalState/classes/ProjectExternalState.md)

The external state.

#### Returns

`void`

***

### findState()

> **findState**(`projectID`, `connectorInstance`): `undefined` \| [`ProjectVolatileState`](../../ProjectVolatileState/classes/ProjectVolatileState.md)

Defined in: [src/frontend/src/data/entities/project/ProjectVolatileStates.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/project/ProjectVolatileStates.ts#L40)

Finds the volatile state for a certain project and connector instance.

#### Parameters

##### projectID

`number`

The project ID.

##### connectorInstance

`string`

The connector instance.

#### Returns

`undefined` \| [`ProjectVolatileState`](../../ProjectVolatileState/classes/ProjectVolatileState.md)

The found volatile state or **undefined** otherwise.
