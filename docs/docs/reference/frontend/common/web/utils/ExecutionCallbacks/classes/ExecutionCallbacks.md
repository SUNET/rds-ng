# Class: ExecutionCallbacks\<DoneCallback, FailCallback\>

Defined in: [src/common/web/utils/ExecutionCallbacks.ts:4](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ExecutionCallbacks.ts#L4)

Helper class for running 'Done' and 'Failed' callbacks during arbitrary executions.

## Type Parameters

### DoneCallback

`DoneCallback` *extends* `Function`

### FailCallback

`FailCallback` *extends* `Function`

## Constructors

### Constructor

> **new ExecutionCallbacks**\<`DoneCallback`, `FailCallback`\>(): `ExecutionCallbacks`\<`DoneCallback`, `FailCallback`\>

Defined in: [src/common/web/utils/ExecutionCallbacks.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ExecutionCallbacks.ts#L8)

#### Returns

`ExecutionCallbacks`\<`DoneCallback`, `FailCallback`\>

## Accessors

### doneCallbacks

#### Get Signature

> **get** **doneCallbacks**(): `DoneCallback`[]

Defined in: [src/common/web/utils/ExecutionCallbacks.ts:67](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ExecutionCallbacks.ts#L67)

All *Done* callbacks.

##### Returns

`DoneCallback`[]

***

### failCallbacks

#### Get Signature

> **get** **failCallbacks**(): `FailCallback`[]

Defined in: [src/common/web/utils/ExecutionCallbacks.ts:74](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ExecutionCallbacks.ts#L74)

All *Fail* callbacks.

##### Returns

`FailCallback`[]

## Methods

### done()

> **done**(`cb`): `this`

Defined in: [src/common/web/utils/ExecutionCallbacks.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ExecutionCallbacks.ts#L17)

Adds a *Done* callback.

#### Parameters

##### cb

`DoneCallback`

The callback to add.

#### Returns

`this`

- This instance to allow call chaining.

***

### failed()

> **failed**(`cb`): `this`

Defined in: [src/common/web/utils/ExecutionCallbacks.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ExecutionCallbacks.ts#L29)

Adds a *Fail* callback.

#### Parameters

##### cb

`FailCallback`

The callback to add.

#### Returns

`this`

- This instance to allow call chaining.

***

### invokeDoneCallbacks()

> **invokeDoneCallbacks**(...`args`): `void`

Defined in: [src/common/web/utils/ExecutionCallbacks.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ExecutionCallbacks.ts#L39)

Invokes all *Done* callbacks.

#### Parameters

##### args

...`any`[]

Arguments passed to the callbacks.

#### Returns

`void`

***

### invokeFailCallbacks()

> **invokeFailCallbacks**(...`args`): `void`

Defined in: [src/common/web/utils/ExecutionCallbacks.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ExecutionCallbacks.ts#L50)

Invokes all *Fail* callbacks.

#### Parameters

##### args

...`any`[]

Arguments passed to the callbacks.

#### Returns

`void`

***

### reset()

> **reset**(): `void`

Defined in: [src/common/web/utils/ExecutionCallbacks.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ExecutionCallbacks.ts#L59)

Removecs all callbacks.

#### Returns

`void`
