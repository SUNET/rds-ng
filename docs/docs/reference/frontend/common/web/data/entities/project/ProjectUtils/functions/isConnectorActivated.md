# Function: isConnectorActivated()

> **isConnectorActivated**(`project`, `userSettings`, `connector`, `connectors`): `boolean`

Defined in: [src/common/web/data/entities/project/ProjectUtils.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectUtils.ts#L28)

Checks if a connector is activated and valid for a given project.

## Parameters

### project

[`Project`](../../Project/classes/Project.md)

The project.

### userSettings

[`UserSettings`](../../../user/UserSettings/classes/UserSettings.md)

The user settings.

### connector

[`Connector`](../../../connector/Connector/classes/Connector.md)

The connector to check.

### connectors

[`Connector`](../../../connector/Connector/classes/Connector.md)[]

A list of all known connectors.

## Returns

`boolean`
