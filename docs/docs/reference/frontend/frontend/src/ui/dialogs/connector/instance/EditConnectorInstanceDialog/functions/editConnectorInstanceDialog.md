# Function: editConnectorInstanceDialog()

> **editConnectorInstanceDialog**(`comp`, `instance?`, `connector?`): [`ExtendedDialogResult`](../../../../../../../../common/web/ui/dialogs/ExtendedDialog/type-aliases/ExtendedDialogResult.md)\<[`EditConnectorInstanceDialogData`](../interfaces/EditConnectorInstanceDialogData.md)\>

Defined in: [src/frontend/src/ui/dialogs/connector/instance/EditConnectorInstanceDialog.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/dialogs/connector/instance/EditConnectorInstanceDialog.ts#L24)

Shows the edit dialog for a connector instance.

## Parameters

### comp

[`FrontendComponent`](../../../../../../component/FrontendComponent/classes/FrontendComponent.md)

The global component.

### instance?

[`ConnectorInstance`](../../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)

The connector instance to edit.

### connector?

[`Connector`](../../../../../../../../common/web/data/entities/connector/Connector/classes/Connector.md)

The connector used by the instance.

## Returns

[`ExtendedDialogResult`](../../../../../../../../common/web/ui/dialogs/ExtendedDialog/type-aliases/ExtendedDialogResult.md)\<[`EditConnectorInstanceDialogData`](../interfaces/EditConnectorInstanceDialogData.md)\>
