---
id: "frontend_src_ui_components_resource_ResourcePreviewer.ResourcePreviewer"
title: "Class: ResourcePreviewer"
sidebar_label: "ResourcePreviewer"
custom_edit_url: null
---

[frontend/src/ui/components/resource/ResourcePreviewer](../modules/frontend_src_ui_components_resource_ResourcePreviewer.md).ResourcePreviewer

A resource previewer encapsulates a preview component for specific MIME types.

## Hierarchy

- **`ResourcePreviewer`**

  ↳ [`AudioPreviewer`](frontend_src_ui_components_resource_previewers_AudioPreviewer.AudioPreviewer.md)

  ↳ [`ImagePreviewer`](frontend_src_ui_components_resource_previewers_ImagePreviewer.ImagePreviewer.md)

  ↳ [`MarkdownPreviewer`](frontend_src_ui_components_resource_previewers_MarkdownPreviewer.MarkdownPreviewer.md)

  ↳ [`PdfPreviewer`](frontend_src_ui_components_resource_previewers_PdfPreviewer.PdfPreviewer.md)

  ↳ [`TextPreviewer`](frontend_src_ui_components_resource_previewers_TextPreviewer.TextPreviewer.md)

  ↳ [`VideoPreviewer`](frontend_src_ui_components_resource_previewers_VideoPreviewer.VideoPreviewer.md)

## Constructors

### constructor

• **new ResourcePreviewer**(`mimeTypes`): [`ResourcePreviewer`](frontend_src_ui_components_resource_ResourcePreviewer.ResourcePreviewer.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `mimeTypes` | `string`[] | List of MIME types; wildcards are supported. |

#### Returns

[`ResourcePreviewer`](frontend_src_ui_components_resource_ResourcePreviewer.ResourcePreviewer.md)

#### Defined in

[src/frontend/src/ui/components/resource/ResourcePreviewer.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/components/resource/ResourcePreviewer.ts#L20)

## Properties

### \_mimeTypes

• `Private` `Readonly` **\_mimeTypes**: `string`[]

#### Defined in

[src/frontend/src/ui/components/resource/ResourcePreviewer.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/components/resource/ResourcePreviewer.ts#L15)

## Accessors

### component

• `get` **component**(): [`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent)

Gets the dynamic component for this previewer.

#### Returns

[`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent)

#### Defined in

[src/frontend/src/ui/components/resource/ResourcePreviewer.ts:49](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/components/resource/ResourcePreviewer.ts#L49)

___

### mimeTypes

• `get` **mimeTypes**(): `string`[]

The MIME types.

#### Returns

`string`[]

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

#### Defined in

[src/frontend/src/ui/components/resource/ResourcePreviewer.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/components/resource/ResourcePreviewer.ts#L29)
