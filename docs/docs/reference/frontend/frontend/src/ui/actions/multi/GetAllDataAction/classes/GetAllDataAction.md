# Class: GetAllDataAction

Defined in: [src/frontend/src/ui/actions/multi/GetAllDataAction.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/multi/GetAllDataAction.ts#L19)

Multi-action to fetch all data from the server.

## Extends

- [`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md)

## Constructors

### Constructor

> **new GetAllDataAction**(`suppressDefaultNotifiers`): `GetAllDataAction`

Defined in: [src/common/web/ui/actions/ActionBase.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L33)

#### Parameters

##### suppressDefaultNotifiers

`boolean` = `false`

Suppress default notifiers.

#### Returns

`GetAllDataAction`

#### Inherited from

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`constructor`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#constructor)

## Properties

### \_state

> `protected` **\_state**: [`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L23)

#### Inherited from

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`_state`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#_state)

## Accessors

### state

#### Get Signature

> **get** **state**(): [`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:143](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L143)

The current state of the action.

##### Returns

[`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

#### Inherited from

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`state`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#state)

## Methods

### addActions()

> **addActions**(`actions`): `void`

Defined in: [src/common/web/ui/actions/MultiAction.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/MultiAction.ts#L18)

Enqueues new actions.

Note that actions are executed synchronously in the order in which they were added.

#### Parameters

##### actions

[`ActionBase`](../../../../../../../common/web/ui/actions/ActionBase/classes/ActionBase.md)[]

The actions to add.

#### Returns

`void`

#### Inherited from

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`addActions`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#addactions)

***

### addDefaultNotifiers()

> `protected` **addDefaultNotifiers**(): `void`

Defined in: [src/frontend/src/ui/actions/multi/GetAllDataAction.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/multi/GetAllDataAction.ts#L50)

#### Returns

`void`

#### Overrides

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`addDefaultNotifiers`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#adddefaultnotifiers)

***

### addNotifier()

> **addNotifier**(`state`, `notifier`, `verboseOnly`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L66)

Adds a new notifier for the specified state.

#### Parameters

##### state

[`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

The state the notifier should react to.

##### notifier

The notifier.

[`ActionNotifier`](../../../../../../../common/web/ui/actions/notifiers/ActionNotifier/classes/ActionNotifier.md) | [`ActionNotifier`](../../../../../../../common/web/ui/actions/notifiers/ActionNotifier/classes/ActionNotifier.md)[]

##### verboseOnly

`boolean` = `false`

If true, the notification will only be added in verbose mode.

#### Returns

`void`

#### Inherited from

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`addNotifier`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#addnotifier)

***

### completed()

> **completed**(`cb`): `this`

Defined in: [src/common/web/ui/actions/ActionBase.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L44)

Adds a callback for action completion.

#### Parameters

##### cb

[`ActionDoneCallback`](../../../../../../../common/web/ui/actions/ActionBase/type-aliases/ActionDoneCallback.md)

The callback to add.

#### Returns

`this`

#### Inherited from

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`completed`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#completed)

***

### execute()

> **execute**(): `void`

Defined in: [src/common/web/ui/actions/MultiAction.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/MultiAction.ts#L30)

Executes the action (i.e., all enqueued messages will be executed).

#### Returns

`void`

#### Inherited from

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`execute`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#execute)

***

### failed()

> **failed**(`cb`): `this`

Defined in: [src/common/web/ui/actions/ActionBase.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L54)

Adds a callback for action failure.

#### Parameters

##### cb

[`ActionFailCallback`](../../../../../../../common/web/ui/actions/ActionBase/type-aliases/ActionFailCallback.md)

The callback to add.

#### Returns

`this`

#### Inherited from

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`failed`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#failed)

***

### onStateChanged()

> `protected` **onStateChanged**(`newState`, `oldState`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:134](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L134)

#### Parameters

##### newState

[`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

##### oldState

[`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

#### Returns

`void`

#### Inherited from

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`onStateChanged`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#onstatechanged)

***

### postExecution()

> `protected` **postExecution**(): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:138](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L138)

#### Returns

`void`

#### Inherited from

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`postExecution`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#postexecution)

***

### preExecution()

> `protected` **preExecution**(): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:136](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L136)

#### Returns

`void`

#### Inherited from

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`preExecution`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#preexecution)

***

### prepare()

> **prepare**(`comp`): `void`

Defined in: [src/frontend/src/ui/actions/multi/GetAllDataAction.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/multi/GetAllDataAction.ts#L20)

#### Parameters

##### comp

[`FrontendComponent`](../../../../../component/FrontendComponent/classes/FrontendComponent.md)

#### Returns

`void`

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

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`prepareNotifiers`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#preparenotifiers)

***

### setState()

> `protected` **setState**(`state`, `message`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:103](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L103)

Sets the active state of this action.

#### Parameters

##### state

[`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

The state to apply

##### message

`string` = `""`

An optional notification message.

#### Returns

`void`

#### Inherited from

[`MultiAction`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md).[`setState`](../../../../../../../common/web/ui/actions/MultiAction/classes/MultiAction.md#setstate)
