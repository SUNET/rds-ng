---
id: "frontend_src_ui_dialogs_connector_instance_EditConnectorInstanceDialog"
title: "Module: frontend/src/ui/dialogs/connector/instance/EditConnectorInstanceDialog"
sidebar_label: "frontend/src/ui/dialogs/connector/instance/EditConnectorInstanceDialog"
sidebar_position: 0
custom_edit_url: null
---

## Interfaces

- [EditConnectorInstanceDialogData](../interfaces/frontend_src_ui_dialogs_connector_instance_EditConnectorInstanceDialog.EditConnectorInstanceDialogData.md)

## Functions

### editConnectorInstanceDialog

▸ **editConnectorInstanceDialog**(`comp`, `instance?`, `connector?`): [`ExtendedDialogResult`](common_web_ui_dialogs_ExtendedDialog.md#extendeddialogresult)<[`EditConnectorInstanceDialogData`](../interfaces/frontend_src_ui_dialogs_connector_instance_EditConnectorInstanceDialog.EditConnectorInstanceDialogData.md)\>

Shows the edit dialog for a connector instance.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `comp` | [`FrontendComponent`](../classes/frontend_src_component_FrontendComponent.FrontendComponent.md) | The global component. |
| `instance?` | [`ConnectorInstance`](../classes/common_web_data_entities_connector_ConnectorInstance.ConnectorInstance.md) | The connector instance to edit. |
| `connector?` | [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md) | The connector used by the instance. |

#### Returns

[`ExtendedDialogResult`](common_web_ui_dialogs_ExtendedDialog.md#extendeddialogresult)<[`EditConnectorInstanceDialogData`](../interfaces/frontend_src_ui_dialogs_connector_instance_EditConnectorInstanceDialog.EditConnectorInstanceDialogData.md)\>

#### Defined in

[src/frontend/src/ui/dialogs/connector/instance/EditConnectorInstanceDialog.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/dialogs/connector/instance/EditConnectorInstanceDialog.ts#L24)
