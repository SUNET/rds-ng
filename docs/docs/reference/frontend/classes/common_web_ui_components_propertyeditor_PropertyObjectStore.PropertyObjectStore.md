---
id: "common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObjectStore"
title: "Class: PropertyObjectStore"
sidebar_label: "PropertyObjectStore"
custom_edit_url: null
---

[common/web/ui/components/propertyeditor/PropertyObjectStore](../modules/common_web_ui_components_propertyeditor_PropertyObjectStore.md).PropertyObjectStore

Represents a store for project objects.

## Constructors

### constructor

• **new PropertyObjectStore**(): [`PropertyObjectStore`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObjectStore.md)

Constructs a new PropertyObjectStore instance.

#### Returns

[`PropertyObjectStore`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObjectStore.md)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:122](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L122)

## Properties

### \_objects

• **\_objects**: [`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)[]

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:117](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L117)

## Methods

### \_removeRefs

▸ **_removeRefs**(`id`): `void`

Removes references to a project object by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` \| `string`[] | The ID of the project object. |

#### Returns

`void`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:180](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L180)

___

### add

▸ **add**(`object`): [`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)

Adds a project object to the store if no object with that ID exists.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `object` | [`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md) | The project object to add. |

#### Returns

[`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)

The project object with that ID, either existing or newly created.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:148](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L148)

___

### addRef

▸ **addRef**(`id`, `ref`): `undefined` \| [`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)

Adds a reference to a project object.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the project object. |
| `ref` | `string` | The reference ID to add. |

#### Returns

`undefined` \| [`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)

The updated project object, or undefined if the project object is not found.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:214](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L214)

___

### exportObjects

▸ **exportObjects**(): [`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)[]

Exports the objects from the store.

#### Returns

[`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)[]

An array of project objects.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:138](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L138)

___

### get

▸ **get**(`id`): `undefined` \| [`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)

Retrieves a project object by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the project object. |

#### Returns

`undefined` \| [`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)

The project object with the specified ID, or undefined if not found.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:163](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L163)

___

### getObjectsByType

▸ **getObjectsByType**(`type`): [`SharedPropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.SharedPropertyObject.md)[]

Retrieves project objects of a specific type.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `type` | `string` | The type of project objects to retrieve. |

#### Returns

[`SharedPropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.SharedPropertyObject.md)[]

An array of project objects of the specified type.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:252](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L252)

___

### getReferencedObjects

▸ **getReferencedObjects**(`id`): `string`[]

Retrieves the referenced objects of a project object.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the project object. |

#### Returns

`string`[]

An array of reference IDs of the referenced objects.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:241](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L241)

___

### remove

▸ **remove**(`id`): `void`

Removes a project object from the store by its ID. Also removes all references to the object.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the project object to remove. |

#### Returns

`void`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:171](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L171)

___

### removeRef

▸ **removeRef**(`id`, `ref`): `void`

Removes a reference from a project object.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the project object. |
| `ref` | `string` | The reference ID to remove. |

#### Returns

`void`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:227](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L227)

___

### setObjects

▸ **setObjects**(`objects`): `void`

Sets the objects in the store.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `objects` | [`PropertyObject`](common_web_ui_components_propertyeditor_PropertyObjectStore.PropertyObject.md)[] | An array of project objects. |

#### Returns

`void`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:130](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L130)

___

### update

▸ **update**(`inputId`, `id`, `value`): `void`

Updates the value of a project object.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `inputId` | `string` | The input ID of the project object. |
| `id` | `string` | The ID of the project object. |
| `value` | `any` | The new value for the project object. |

#### Returns

`void`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:198](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L198)
