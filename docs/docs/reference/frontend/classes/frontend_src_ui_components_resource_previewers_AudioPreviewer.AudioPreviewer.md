---
id: "frontend_src_ui_components_resource_previewers_AudioPreviewer.AudioPreviewer"
title: "Class: AudioPreviewer"
sidebar_label: "AudioPreviewer"
custom_edit_url: null
---

[frontend/src/ui/components/resource/previewers/AudioPreviewer](../modules/frontend_src_ui_components_resource_previewers_AudioPreviewer.md).AudioPreviewer

A resource previewer for images.

## Hierarchy

- [`ResourcePreviewer`](frontend_src_ui_components_resource_ResourcePreviewer.ResourcePreviewer.md)

  ↳ **`AudioPreviewer`**

## Constructors

### constructor

• **new AudioPreviewer**(): [`AudioPreviewer`](frontend_src_ui_components_resource_previewers_AudioPreviewer.AudioPreviewer.md)

#### Returns

[`AudioPreviewer`](frontend_src_ui_components_resource_previewers_AudioPreviewer.AudioPreviewer.md)

#### Overrides

[ResourcePreviewer](frontend_src_ui_components_resource_ResourcePreviewer.ResourcePreviewer.md).[constructor](frontend_src_ui_components_resource_ResourcePreviewer.ResourcePreviewer.md#constructor)

#### Defined in

[src/frontend/src/ui/components/resource/previewers/AudioPreviewer.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/components/resource/previewers/AudioPreviewer.ts#L10)

## Accessors

### component

• `get` **component**(): [`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent)

Gets the dynamic component for this previewer.

#### Returns

[`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent)

#### Overrides

ResourcePreviewer.component

#### Defined in

[src/frontend/src/ui/components/resource/previewers/AudioPreviewer.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/components/resource/previewers/AudioPreviewer.ts#L14)

___

### mimeTypes

• `get` **mimeTypes**(): `string`[]

The MIME types.

#### Returns

`string`[]

#### Inherited from

ResourcePreviewer.mimeTypes

#### Defined in

[src/frontend/src/ui/components/resource/ResourcePreviewer.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/components/resource/ResourcePreviewer.ts#L42)

## Methods

### matches

▸ **matches**(`mimeType`): `boolean`

Checks if the MIME type matches the types supported by this previewer.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `mimeType` | `string` | The MIME type to check. |

#### Returns

`boolean`

#### Inherited from

[ResourcePreviewer](frontend_src_ui_components_resource_ResourcePreviewer.ResourcePreviewer.md).[matches](frontend_src_ui_components_resource_ResourcePreviewer.ResourcePreviewer.md#matches)

#### Defined in

[src/frontend/src/ui/components/resource/ResourcePreviewer.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/components/resource/ResourcePreviewer.ts#L29)
