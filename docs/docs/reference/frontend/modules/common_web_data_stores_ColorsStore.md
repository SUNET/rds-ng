---
id: "common_web_data_stores_ColorsStore"
title: "Module: common/web/data/stores/ColorsStore"
sidebar_label: "common/web/data/stores/ColorsStore"
sidebar_position: 0
custom_edit_url: null
---

## Namespaces

- [useColorsStore](../namespaces/common_web_data_stores_ColorsStore.useColorsStore.md)

## Functions

### useColorsStore

▸ **useColorsStore**(`pinia?`, `hot?`): `Store`<``"colorsStore"``, `Pick`<\{ `color`: (`colorID`: `string`, `lightness`: `number`, `amount`: `number`, `alpha`: `number`) => `string` ; `populateFromConnectorsList`: (`connectors`: [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[]) => `void` ; `populateFromProfileContainerList`: (`profiles`: [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)) => `void` ; `reset`: () => `void`  }, `never`\>, `Pick`<\{ `color`: (`colorID`: `string`, `lightness`: `number`, `amount`: `number`, `alpha`: `number`) => `string` ; `populateFromConnectorsList`: (`connectors`: [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[]) => `void` ; `populateFromProfileContainerList`: (`profiles`: [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)) => `void` ; `reset`: () => `void`  }, `never`\>, `Pick`<\{ `color`: (`colorID`: `string`, `lightness`: `number`, `amount`: `number`, `alpha`: `number`) => `string` ; `populateFromConnectorsList`: (`connectors`: [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[]) => `void` ; `populateFromProfileContainerList`: (`profiles`: [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)) => `void` ; `reset`: () => `void`  }, ``"reset"`` \| ``"color"`` \| ``"populateFromProfileContainerList"`` \| ``"populateFromConnectorsList"``\>\>

The global store for auto-assigned colors.

#### Parameters

| Name | Type |
| :------ | :------ |
| `pinia?` | ``null`` \| `Pinia` |
| `hot?` | `StoreGeneric` |

#### Returns

`Store`<``"colorsStore"``, `Pick`<\{ `color`: (`colorID`: `string`, `lightness`: `number`, `amount`: `number`, `alpha`: `number`) => `string` ; `populateFromConnectorsList`: (`connectors`: [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[]) => `void` ; `populateFromProfileContainerList`: (`profiles`: [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)) => `void` ; `reset`: () => `void`  }, `never`\>, `Pick`<\{ `color`: (`colorID`: `string`, `lightness`: `number`, `amount`: `number`, `alpha`: `number`) => `string` ; `populateFromConnectorsList`: (`connectors`: [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[]) => `void` ; `populateFromProfileContainerList`: (`profiles`: [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)) => `void` ; `reset`: () => `void`  }, `never`\>, `Pick`<\{ `color`: (`colorID`: `string`, `lightness`: `number`, `amount`: `number`, `alpha`: `number`) => `string` ; `populateFromConnectorsList`: (`connectors`: [`Connector`](../classes/common_web_data_entities_connector_Connector.Connector.md)[]) => `void` ; `populateFromProfileContainerList`: (`profiles`: [`MetadataProfileContainerList`](common_web_data_entities_metadata_MetadataProfileContainer.md#metadataprofilecontainerlist)) => `void` ; `reset`: () => `void`  }, ``"reset"`` \| ``"color"`` \| ``"populateFromProfileContainerList"`` \| ``"populateFromConnectorsList"``\>\>

#### Defined in

src/node_modules/pinia/dist/pinia.d.ts:686
