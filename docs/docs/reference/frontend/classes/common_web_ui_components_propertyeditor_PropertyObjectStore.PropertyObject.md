---
id: "common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject"
title: "Class: PropertyObject"
sidebar_label: "PropertyObject"
custom_edit_url: null
---

[common/web/ui/components/propertyeditor/PropertyObjectStore](../modules/common_web_ui_components_propertyeditor_PropertyObjectStore.md).PropertyObject

Represents a project object with an ID, value, and references.

**`Abstract`**

## Hierarchy

- **`PropertyObject`**

  ↳ [`LayoutPropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.LayoutPropertyObject.md)

  ↳ [`SharedPropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.SharedPropertyObject.md)

## Constructors

### constructor

• **new PropertyObject**(`id?`, `value?`, `refs?`): [`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)

Creates a new instance of PropertyObject.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `id?` | `string` | `undefined` | The object ID. |
| `value` | `any` | `{}` | The object value. |
| `refs` | `string`[] | `[]` | The object references. |

#### Returns

[`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L24)

## Properties

### id

• **id**: `string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L14)

___

### refs

• **refs**: `string`[]

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L16)

___

### value

• **value**: `Object`

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L15)

## Methods

### getId

▸ **getId**(): `string`

Retrieves the unique identifier of the project object.

#### Returns

`string`

The unique identifier of the project object.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L35)

___

### getReferences

▸ **getReferences**(): `string`[]

Retrieves the list of the references that the object holds.

#### Returns

`string`[]

An array of reference strings.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L53)

___

### getValues

▸ **getValues**(): `Object`

Retrieves the current values stored in the PropertyObject.

#### Returns

`Object`

An object where the keys are strings and the values can be of any type.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L44)

___

### isEmpty

▸ **isEmpty**(): `boolean`

#### Returns

`boolean`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:75](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L75)

___

### pushReference

▸ **pushReference**(`ref`): `void`

Adds a reference string to the list of references.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ref` | `string` | The reference string to be added. |

#### Returns

`void`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:71](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L71)

___

### setReferences

▸ **setReferences**(`refs`): `void`

Sets the references for the project object.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `refs` | `string`[] | An array of reference strings to be set. |

#### Returns

`void`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:62](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L62)
