# Class: TextPreviewer

Defined in: [src/frontend/src/ui/components/resource/previewers/TextPreviewer.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/components/resource/previewers/TextPreviewer.ts#L9)

A resource previewer for PDFs.

## Extends

- [`ResourcePreviewer`](../../../ResourcePreviewer/classes/ResourcePreviewer.md)

## Constructors

### Constructor

> **new TextPreviewer**(): `TextPreviewer`

Defined in: [src/frontend/src/ui/components/resource/previewers/TextPreviewer.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/components/resource/previewers/TextPreviewer.ts#L10)

#### Returns

`TextPreviewer`

#### Overrides

[`ResourcePreviewer`](../../../ResourcePreviewer/classes/ResourcePreviewer.md).[`constructor`](../../../ResourcePreviewer/classes/ResourcePreviewer.md#constructor)

## Accessors

### component

#### Get Signature

> **get** **component**(): [`VueComponent`](../../../../../../../../common/web/component/WebComponent/type-aliases/VueComponent.md)

Defined in: [src/frontend/src/ui/components/resource/previewers/TextPreviewer.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/components/resource/previewers/TextPreviewer.ts#L14)

Gets the dynamic component for this previewer.

##### Returns

[`VueComponent`](../../../../../../../../common/web/component/WebComponent/type-aliases/VueComponent.md)

#### Overrides

[`ResourcePreviewer`](../../../ResourcePreviewer/classes/ResourcePreviewer.md).[`component`](../../../ResourcePreviewer/classes/ResourcePreviewer.md#component)

***

### mimeTypes

#### Get Signature

> **get** **mimeTypes**(): `string`[]

Defined in: [src/frontend/src/ui/components/resource/ResourcePreviewer.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/components/resource/ResourcePreviewer.ts#L42)

The MIME types.

##### Returns

`string`[]

#### Inherited from

[`ResourcePreviewer`](../../../ResourcePreviewer/classes/ResourcePreviewer.md).[`mimeTypes`](../../../ResourcePreviewer/classes/ResourcePreviewer.md#mimetypes)

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

#### Inherited from

[`ResourcePreviewer`](../../../ResourcePreviewer/classes/ResourcePreviewer.md).[`matches`](../../../ResourcePreviewer/classes/ResourcePreviewer.md#matches)
