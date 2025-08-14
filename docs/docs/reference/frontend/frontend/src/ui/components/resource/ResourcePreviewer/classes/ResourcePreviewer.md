# Abstract Class: ResourcePreviewer

Defined in: [src/frontend/src/ui/components/resource/ResourcePreviewer.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/components/resource/ResourcePreviewer.ts#L14)

A resource previewer encapsulates a preview component for specific MIME types.

## Extended by

- [`AudioPreviewer`](../../previewers/AudioPreviewer/classes/AudioPreviewer.md)
- [`ImagePreviewer`](../../previewers/ImagePreviewer/classes/ImagePreviewer.md)
- [`MarkdownPreviewer`](../../previewers/MarkdownPreviewer/classes/MarkdownPreviewer.md)
- [`PdfPreviewer`](../../previewers/PdfPreviewer/classes/PdfPreviewer.md)
- [`TextPreviewer`](../../previewers/TextPreviewer/classes/TextPreviewer.md)
- [`VideoPreviewer`](../../previewers/VideoPreviewer/classes/VideoPreviewer.md)

## Constructors

### Constructor

> `protected` **new ResourcePreviewer**(`mimeTypes`): `ResourcePreviewer`

Defined in: [src/frontend/src/ui/components/resource/ResourcePreviewer.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/components/resource/ResourcePreviewer.ts#L20)

#### Parameters

##### mimeTypes

`string`[]

List of MIME types; wildcards are supported.

#### Returns

`ResourcePreviewer`

## Accessors

### component

#### Get Signature

> **get** `abstract` **component**(): [`VueComponent`](../../../../../../../common/web/component/WebComponent/type-aliases/VueComponent.md)

Defined in: [src/frontend/src/ui/components/resource/ResourcePreviewer.ts:49](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/components/resource/ResourcePreviewer.ts#L49)

Gets the dynamic component for this previewer.

##### Returns

[`VueComponent`](../../../../../../../common/web/component/WebComponent/type-aliases/VueComponent.md)

***

### mimeTypes

#### Get Signature

> **get** **mimeTypes**(): `string`[]

Defined in: [src/frontend/src/ui/components/resource/ResourcePreviewer.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/components/resource/ResourcePreviewer.ts#L42)

The MIME types.

##### Returns

`string`[]

## Methods

### matches()

> **matches**(`mimeType`): `boolean`

Defined in: [src/frontend/src/ui/components/resource/ResourcePreviewer.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/components/resource/ResourcePreviewer.ts#L29)

Checks if the MIME type matches the types supported by this previewer.

#### Parameters

##### mimeType

`string`

The MIME type to check.

#### Returns

`boolean`
