# Variable: useComponentStore

> `const` **useComponentStore**: `StoreDefinition`\<`"componentStore"`, `Pick`\<\{ `componentState`: `Ref`\<[`ComponentState`](../enumerations/ComponentState.md), [`ComponentState`](../enumerations/ComponentState.md)\>; `componentStateMessage`: `Ref`\<`string`, `string`\>; `queryParams`: `Ref`\<\{ `size`: `number`; `append`: `void`; `delete`: `void`; `forEach`: `void`; `get`: `null` \| `string`; `getAll`: `string`[]; `has`: `boolean`; `set`: `void`; `sort`: `void`; `toString`: `string`; \}, `URLSearchParams` \| \{ `size`: `number`; `append`: `void`; `delete`: `void`; `forEach`: `void`; `get`: `null` \| `string`; `getAll`: `string`[]; `has`: `boolean`; `set`: `void`; `sort`: `void`; `toString`: `string`; \}\>; `reset`: () => `void`; \}, `"componentState"` \| `"componentStateMessage"` \| `"queryParams"`\>, `Pick`\<\{ `componentState`: `Ref`\<[`ComponentState`](../enumerations/ComponentState.md), [`ComponentState`](../enumerations/ComponentState.md)\>; `componentStateMessage`: `Ref`\<`string`, `string`\>; `queryParams`: `Ref`\<\{ `size`: `number`; `append`: `void`; `delete`: `void`; `forEach`: `void`; `get`: `null` \| `string`; `getAll`: `string`[]; `has`: `boolean`; `set`: `void`; `sort`: `void`; `toString`: `string`; \}, `URLSearchParams` \| \{ `size`: `number`; `append`: `void`; `delete`: `void`; `forEach`: `void`; `get`: `null` \| `string`; `getAll`: `string`[]; `has`: `boolean`; `set`: `void`; `sort`: `void`; `toString`: `string`; \}\>; `reset`: () => `void`; \}, `never`\>, `Pick`\<\{ `componentState`: `Ref`\<[`ComponentState`](../enumerations/ComponentState.md), [`ComponentState`](../enumerations/ComponentState.md)\>; `componentStateMessage`: `Ref`\<`string`, `string`\>; `queryParams`: `Ref`\<\{ `size`: `number`; `append`: `void`; `delete`: `void`; `forEach`: `void`; `get`: `null` \| `string`; `getAll`: `string`[]; `has`: `boolean`; `set`: `void`; `sort`: `void`; `toString`: `string`; \}, `URLSearchParams` \| \{ `size`: `number`; `append`: `void`; `delete`: `void`; `forEach`: `void`; `get`: `null` \| `string`; `getAll`: `string`[]; `has`: `boolean`; `set`: `void`; `sort`: `void`; `toString`: `string`; \}\>; `reset`: () => `void`; \}, `"reset"`\>\>

Defined in: [src/common/web/data/stores/ComponentStore.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/stores/ComponentStore.ts#L23)

The global store for all component-related data.

## Param

The overall state of the component.

## Param

An additional message about the component state.
