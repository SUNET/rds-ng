---
id: "common_web_component_Session.Session"
title: "Class: Session"
sidebar_label: "Session"
custom_edit_url: null
---

[common/web/component/Session](../modules/common_web_component_Session.md).Session

Class for simple session management.

## Constructors

### constructor

• **new Session**(`compID`): [`Session`](common_web_component_Session.Session.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `compID` | [`UnitID`](common_web_utils_UnitID.UnitID.md) |

#### Returns

[`Session`](common_web_component_Session.Session.md)

#### Defined in

[src/common/web/component/Session.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/Session.ts#L15)

## Properties

### \_compID

• `Private` `Readonly` **\_compID**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Defined in

[src/common/web/component/Session.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/Session.ts#L11)

___

### \_sessionID

• `Private` `Readonly` **\_sessionID**: `RemovableRef`<`string`\>

#### Defined in

[src/common/web/component/Session.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/Session.ts#L13)

## Accessors

### sessionID

• `get` **sessionID**(): `string`

The current session ID.

#### Returns

`string`

#### Defined in

[src/common/web/component/Session.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/Session.ts#L37)

## Methods

### sessionValue

▸ **sessionValue**<`ValueType`\>(`key`, `defaultValue`): `RemovableRef`<`ValueType`\>

Retrieves an arbitrary value stored for the current session.

#### Type parameters

| Name |
| :------ |
| `ValueType` |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `key` | `string` | The value key. |
| `defaultValue` | `ValueType` | A default value used if the value doesn't exist yet. |

#### Returns

`RemovableRef`<`ValueType`\>

- The stored value or the default one otherwise.

#### Defined in

[src/common/web/component/Session.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/Session.ts#L30)
