---
id: "frontend_src_data_stores_FrontendStore"
title: "Module: frontend/src/data/stores/FrontendStore"
sidebar_label: "frontend/src/data/stores/FrontendStore"
sidebar_position: 0
custom_edit_url: null
---

## Namespaces

- [useFrontendStore](../namespaces/frontend_src_data_stores_FrontendStore.useFrontendStore.md)

## Enumerations

- [DisplayState](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md)

## Functions

### useFrontendStore

▸ **useFrontendStore**(`pinia?`, `hot?`): `Store`<``"frontendStore"``, `Pick`<\{ `displayState`: `Ref`<[`DisplayState`](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md), [`DisplayState`](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md)\> ; `initializationError`: `Ref`<`boolean`, `boolean`\> ; `initializationMessage`: `Ref`<`string`, `string`\> ; `reset`: () => `void`  }, ``"initializationMessage"`` \| ``"initializationError"`` \| ``"displayState"``\>, `Pick`<\{ `displayState`: `Ref`<[`DisplayState`](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md), [`DisplayState`](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md)\> ; `initializationError`: `Ref`<`boolean`, `boolean`\> ; `initializationMessage`: `Ref`<`string`, `string`\> ; `reset`: () => `void`  }, `never`\>, `Pick`<\{ `displayState`: `Ref`<[`DisplayState`](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md), [`DisplayState`](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md)\> ; `initializationError`: `Ref`<`boolean`, `boolean`\> ; `initializationMessage`: `Ref`<`string`, `string`\> ; `reset`: () => `void`  }, ``"reset"``\>\>

Frontend store for general application data.

#### Parameters

| Name | Type |
| :------ | :------ |
| `pinia?` | ``null`` \| `Pinia` |
| `hot?` | `StoreGeneric` |

#### Returns

`Store`<``"frontendStore"``, `Pick`<\{ `displayState`: `Ref`<[`DisplayState`](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md), [`DisplayState`](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md)\> ; `initializationError`: `Ref`<`boolean`, `boolean`\> ; `initializationMessage`: `Ref`<`string`, `string`\> ; `reset`: () => `void`  }, ``"initializationMessage"`` \| ``"initializationError"`` \| ``"displayState"``\>, `Pick`<\{ `displayState`: `Ref`<[`DisplayState`](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md), [`DisplayState`](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md)\> ; `initializationError`: `Ref`<`boolean`, `boolean`\> ; `initializationMessage`: `Ref`<`string`, `string`\> ; `reset`: () => `void`  }, `never`\>, `Pick`<\{ `displayState`: `Ref`<[`DisplayState`](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md), [`DisplayState`](../enums/frontend_src_data_stores_FrontendStore.DisplayState.md)\> ; `initializationError`: `Ref`<`boolean`, `boolean`\> ; `initializationMessage`: `Ref`<`string`, `string`\> ; `reset`: () => `void`  }, ``"reset"``\>\>

#### Defined in

src/node_modules/pinia/dist/pinia.d.ts:686
