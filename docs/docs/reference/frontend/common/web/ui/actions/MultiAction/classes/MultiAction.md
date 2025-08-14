# Class: MultiAction

Defined in: [src/common/web/ui/actions/MultiAction.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/MultiAction.ts#L7)

An action that encapsulates multiple other actions that are executed in order.

## Extends

- [`ActionBase`](../../ActionBase/classes/ActionBase.md)

## Extended by

- [`GetAllDataAction`](../../../../../../frontend/src/ui/actions/multi/GetAllDataAction/classes/GetAllDataAction.md)

## Constructors

### Constructor

> **new MultiAction**(`suppressDefaultNotifiers`): `MultiAction`

Defined in: [src/common/web/ui/actions/ActionBase.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L33)

#### Parameters

##### suppressDefaultNotifiers

`boolean` = `false`

Suppress default notifiers.

#### Returns

`MultiAction`

#### Inherited from

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`constructor`](../../ActionBase/classes/ActionBase.md#constructor)

## Properties

### \_state

> `protected` **\_state**: [`ActionState`](../../ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L23)

#### Inherited from

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`_state`](../../ActionBase/classes/ActionBase.md#_state)

## Accessors

### state

#### Get Signature

> **get** **state**(): [`ActionState`](../../ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:143](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L143)

The current state of the action.

##### Returns

[`ActionState`](../../ActionBase/enumerations/ActionState.md)

#### Inherited from

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`state`](../../ActionBase/classes/ActionBase.md#state)

## Methods

### addActions()

> **addActions**(`actions`): `void`

Defined in: [src/common/web/ui/actions/MultiAction.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/MultiAction.ts#L18)

Enqueues new actions.

Note that actions are executed synchronously in the order in which they were added.

#### Parameters

##### actions

[`ActionBase`](../../ActionBase/classes/ActionBase.md)[]

The actions to add.

#### Returns

`void`

***

### addDefaultNotifiers()

> `protected` **addDefaultNotifiers**(...`args`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:90](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L90)

#### Parameters

##### args

...`any`[]

#### Returns

`void`

#### Inherited from

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`addDefaultNotifiers`](../../ActionBase/classes/ActionBase.md#adddefaultnotifiers)

***

### addNotifier()

> **addNotifier**(`state`, `notifier`, `verboseOnly`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L66)

Adds a new notifier for the specified state.

#### Parameters

##### state

[`ActionState`](../../ActionBase/enumerations/ActionState.md)

The state the notifier should react to.

##### notifier

The notifier.

[`ActionNotifier`](../../notifiers/ActionNotifier/classes/ActionNotifier.md) | [`ActionNotifier`](../../notifiers/ActionNotifier/classes/ActionNotifier.md)[]

##### verboseOnly

`boolean` = `false`

If true, the notification will only be added in verbose mode.

#### Returns

`void`

#### Inherited from

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`addNotifier`](../../ActionBase/classes/ActionBase.md#addnotifier)

***

### completed()

> **completed**(`cb`): `this`

Defined in: [src/common/web/ui/actions/ActionBase.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L44)

Adds a callback for action completion.

#### Parameters

##### cb

[`ActionDoneCallback`](../../ActionBase/type-aliases/ActionDoneCallback.md)

The callback to add.

#### Returns

`this`

#### Inherited from

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`completed`](../../ActionBase/classes/ActionBase.md#completed)

***

### execute()

> **execute**(): `void`

Defined in: [src/common/web/ui/actions/MultiAction.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/MultiAction.ts#L30)

Executes the action (i.e., all enqueued messages will be executed).

#### Returns

`void`

#### Overrides

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`execute`](../../ActionBase/classes/ActionBase.md#execute)

***

### failed()

> **failed**(`cb`): `this`

Defined in: [src/common/web/ui/actions/ActionBase.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L54)

Adds a callback for action failure.

#### Parameters

##### cb

[`ActionFailCallback`](../../ActionBase/type-aliases/ActionFailCallback.md)

The callback to add.

#### Returns

`this`

#### Inherited from

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`failed`](../../ActionBase/classes/ActionBase.md#failed)

***

### onStateChanged()

> `protected` **onStateChanged**(`newState`, `oldState`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:134](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L134)

#### Parameters

##### newState

[`ActionState`](../../ActionBase/enumerations/ActionState.md)

##### oldState

[`ActionState`](../../ActionBase/enumerations/ActionState.md)

#### Returns

`void`

#### Inherited from

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`onStateChanged`](../../ActionBase/classes/ActionBase.md#onstatechanged)

***

### postExecution()

> `protected` **postExecution**(): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:138](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L138)

#### Returns

`void`

#### Inherited from

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`postExecution`](../../ActionBase/classes/ActionBase.md#postexecution)

***

### preExecution()

> `protected` **preExecution**(): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:136](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L136)

#### Returns

`void`

#### Inherited from

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`preExecution`](../../ActionBase/classes/ActionBase.md#preexecution)

***

### prepareNotifiers()

> `protected` **prepareNotifiers**(...`args`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:84](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L84)

#### Parameters

##### args

...`any`[]

#### Returns

`void`

#### Inherited from

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`prepareNotifiers`](../../ActionBase/classes/ActionBase.md#preparenotifiers)

***

### setState()

> `protected` **setState**(`state`, `message`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:103](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L103)

Sets the active state of this action.

#### Parameters

##### state

[`ActionState`](../../ActionBase/enumerations/ActionState.md)

The state to apply

##### message

`string` = `""`

An optional notification message.

#### Returns

`void`

#### Inherited from

[`ActionBase`](../../ActionBase/classes/ActionBase.md).[`setState`](../../ActionBase/classes/ActionBase.md#setstate)
