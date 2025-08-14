# Function: useResourceTools()

> **useResourceTools**(`comp`): `object`

Defined in: [src/frontend/src/ui/tools/resource/ResourceTools.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/tools/resource/ResourceTools.ts#L11)

## Parameters

### comp

[`FrontendComponent`](../../../../../component/FrontendComponent/classes/FrontendComponent.md)

## Returns

`object`

### clearResourcesListCache()

> **clearResourcesListCache**: () => `void`

#### Returns

`void`

### resourceDataToBlob()

> **resourceDataToBlob**: (`resource`, `data`) => `string`

#### Parameters

##### resource

[`Resource`](../../../../../../../common/web/data/entities/resource/Resource/classes/Resource.md)

##### data

`undefined` | `ArrayBuffer`

#### Returns

`string`

### resourceDataToTagValue()

> **resourceDataToTagValue**: (`resource`, `data`) => `string`

#### Parameters

##### resource

[`Resource`](../../../../../../../common/web/data/entities/resource/Resource/classes/Resource.md)

##### data

`undefined` | `ArrayBuffer`

#### Returns

`string`

### retrieveResourceData()

> **retrieveResourceData**: (`resource`) => `Promise`\<`undefined` \| `ArrayBuffer`\>

#### Parameters

##### resource

[`Resource`](../../../../../../../common/web/data/entities/resource/Resource/classes/Resource.md)

#### Returns

`Promise`\<`undefined` \| `ArrayBuffer`\>

### retrieveResourcesList()

> **retrieveResourcesList**: (`root`, `path`, `recursive`) => `Promise`\<[`ResourcesList`](../../../../../../../common/web/data/entities/resource/ResourcesList/classes/ResourcesList.md)\>

#### Parameters

##### root

`string`

##### path

`string`

##### recursive

`boolean` = `true`

#### Returns

`Promise`\<[`ResourcesList`](../../../../../../../common/web/data/entities/resource/ResourcesList/classes/ResourcesList.md)\>
