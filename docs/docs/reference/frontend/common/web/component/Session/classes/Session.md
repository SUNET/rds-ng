# Class: Session

Defined in: [src/common/web/component/Session.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/Session.ts#L10)

Class for simple session management.

## Constructors

### Constructor

> **new Session**(`compID`): `Session`

Defined in: [src/common/web/component/Session.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/Session.ts#L15)

#### Parameters

##### compID

[`UnitID`](../../../utils/UnitID/classes/UnitID.md)

#### Returns

`Session`

## Accessors

### sessionID

#### Get Signature

> **get** **sessionID**(): `string`

Defined in: [src/common/web/component/Session.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/Session.ts#L37)

The current session ID.

##### Returns

`string`

## Methods

### sessionValue()

> **sessionValue**\<`ValueType`\>(`key`, `defaultValue`): `RemovableRef`\<`ValueType`\>

Defined in: [src/common/web/component/Session.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/Session.ts#L30)

Retrieves an arbitrary value stored for the current session.

#### Type Parameters

##### ValueType

`ValueType`

#### Parameters

##### key

`string`

The value key.

##### defaultValue

`ValueType`

A default value used if the value doesn't exist yet.

#### Returns

`RemovableRef`\<`ValueType`\>

- The stored value or the default one otherwise.
