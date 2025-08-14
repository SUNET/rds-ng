---
id: "frontend_src_ui_tools_resource_ResourceTools"
title: "Module: frontend/src/ui/tools/resource/ResourceTools"
sidebar_label: "frontend/src/ui/tools/resource/ResourceTools"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### useResourceTools

▸ **useResourceTools**(`comp`): `Object`

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](../classes/frontend_src_component_FrontendComponent.FrontendComponent.md) |

#### Returns

`Object`

| Name | Type |
| :------ | :------ |
| `clearResourcesListCache` | () => `void` |
| `resourceDataToBlob` | (`resource`: [`Resource`](../classes/common_web_data_entities_resource_Resource.Resource.md), `data`: `undefined` \| `ArrayBuffer`) => `string` |
| `resourceDataToTagValue` | (`resource`: [`Resource`](../classes/common_web_data_entities_resource_Resource.Resource.md), `data`: `undefined` \| `ArrayBuffer`) => `string` |
| `retrieveResourceData` | (`resource`: [`Resource`](../classes/common_web_data_entities_resource_Resource.Resource.md)) => `Promise`<`ArrayBuffer` \| `undefined`\> |
| `retrieveResourcesList` | (`root`: `string`, `path`: `string`, `recursive`: `boolean`) => `Promise`<[`ResourcesList`](../classes/common_web_data_entities_resource_ResourcesList.ResourcesList.md)\> |

#### Defined in

[src/frontend/src/ui/tools/resource/ResourceTools.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/tools/resource/ResourceTools.ts#L11)
