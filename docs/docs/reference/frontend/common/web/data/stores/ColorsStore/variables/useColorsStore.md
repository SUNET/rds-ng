# Variable: useColorsStore

> `const` **useColorsStore**: `StoreDefinition`\<`"colorsStore"`, `Pick`\<\{ `color`: (`colorID`, `lightness`, `amount`, `alpha`) => `string`; `populateFromConnectorsList`: (`connectors`) => `void`; `populateFromProfileContainerList`: (`profiles`) => `void`; `reset`: () => `void`; \}, `never`\>, `Pick`\<\{ `color`: (`colorID`, `lightness`, `amount`, `alpha`) => `string`; `populateFromConnectorsList`: (`connectors`) => `void`; `populateFromProfileContainerList`: (`profiles`) => `void`; `reset`: () => `void`; \}, `never`\>, `Pick`\<\{ `color`: (`colorID`, `lightness`, `amount`, `alpha`) => `string`; `populateFromConnectorsList`: (`connectors`) => `void`; `populateFromProfileContainerList`: (`profiles`) => `void`; `reset`: () => `void`; \}, `"reset"` \| `"color"` \| `"populateFromProfileContainerList"` \| `"populateFromConnectorsList"`\>\>

Defined in: [src/common/web/data/stores/ColorsStore.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/stores/ColorsStore.ts#L12)

The global store for auto-assigned colors.
