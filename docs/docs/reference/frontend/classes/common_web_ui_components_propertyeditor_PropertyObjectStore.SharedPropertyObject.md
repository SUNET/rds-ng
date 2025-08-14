---
id: "common_web_ui_components_propertyeditor_PropertyObjectStore.SharedPropertyObject"
title: "Class: SharedPropertyObject"
sidebar_label: "SharedPropertyObject"
custom_edit_url: null
---

[common/web/ui/components/propertyeditor/PropertyObjectStore](../modules/common_web_ui_components_propertyeditor_PropertyObjectStore.md).SharedPropertyObject

Represents a shared object that extends the `PropertyObject` class.

## Hierarchy

- [`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)

  ↳ **`SharedPropertyObject`**

## Constructors

### constructor

• **new SharedPropertyObject**(`type`, `id?`, `value?`, `refs?`): [`SharedPropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.SharedPropertyObject.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `type` | `string` | `undefined` |
| `id?` | `string` | `undefined` |
| `value` | `any` | `{}` |
| `refs` | `string`[] | `[]` |

#### Returns

[`SharedPropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.SharedPropertyObject.md)

#### Overrides

[PropertyObject](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md).[constructor](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md#constructor)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:98](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L98)

## Properties

### id

• **id**: `string`

#### Inherited from

[PropertyObject](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md).[id](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md#id)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L14)

___

### refs

• **refs**: `string`[]

#### Inherited from

[PropertyObject](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md).[refs](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md#refs)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L16)

___

### type

• **type**: `string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:96](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L96)

___

### value

• **value**: `Object`

#### Index signature

▪ [key: `string`]: `any`

#### Inherited from

[PropertyObject](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md).[value](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md#value)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L15)

## Methods

### getId

▸ **getId**(): `string`

Retrieves the unique identifier of the project object.

#### Returns

`string`

The unique identifier of the project object.

#### Inherited from

[PropertyObject](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md).[getId](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md#getid)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L35)

___

### getReferences

▸ **getReferences**(): `string`[]

Retrieves the list of the references that the object holds.

#### Returns

`string`[]

An array of reference strings.

#### Inherited from

[PropertyObject](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md).[getReferences](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md#getreferences)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L53)

___

### getType

▸ **getType**(): `string`

Retrieves the type of the shared object.

#### Returns

`string`

The type of the shared object.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:108](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L108)

___

### getValues

▸ **getValues**(): `Object`

Retrieves the current values stored in the PropertyObject.

#### Returns

`Object`

An object where the keys are strings and the values can be of any type.

#### Inherited from

[PropertyObject](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md).[getValues](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md#getvalues)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L44)

___

### isEmpty

▸ **isEmpty**(): `boolean`

#### Returns

`boolean`

#### Inherited from

[PropertyObject](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md).[isEmpty](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md#isempty)

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

#### Inherited from

[PropertyObject](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md).[pushReference](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md#pushreference)

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

#### Inherited from

[PropertyObject](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md).[setReferences](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md#setreferences)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:62](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L62)
