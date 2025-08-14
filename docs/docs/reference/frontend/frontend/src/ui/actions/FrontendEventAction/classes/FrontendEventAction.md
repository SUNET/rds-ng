# Abstract Class: FrontendEventAction\<EventType, CompType\>

Defined in: [src/frontend/src/ui/actions/FrontendEventAction.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/FrontendEventAction.ts#L10)

Event actions specific to the frontend.

## Extends

- [`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md)\<`EventType`, `CompType`\>

## Extended by

- [`TouchProjectAction`](../../project/TouchProjectAction/classes/TouchProjectAction.md)

## Type Parameters

### EventType

`EventType` *extends* [`Event`](../../../../../../common/web/core/messaging/Event/classes/Event.md)

### CompType

`CompType` *extends* [`EventComposer`](../../../../../../common/web/core/messaging/composers/EventComposer/classes/EventComposer.md)\<`EventType`\>

## Constructors

### Constructor

> **new FrontendEventAction**\<`EventType`, `CompType`\>(`comp`, `suppressDefaultNotifiers`): `FrontendEventAction`\<`EventType`, `CompType`\>

Defined in: [src/frontend/src/ui/actions/FrontendEventAction.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/FrontendEventAction.ts#L15)

#### Parameters

##### comp

[`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

The main frontend component.

##### suppressDefaultNotifiers

`boolean` = `false`

Suppress default notifiers.

#### Returns

`FrontendEventAction`\<`EventType`, `CompType`\>

#### Overrides

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`constructor`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#constructor)

## Properties

### \_composer

> `protected` **\_composer**: `null` \| `CompType` = `null`

Defined in: [src/common/web/ui/actions/Action.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L19)

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`_composer`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#_composer)

***

### \_state

> `protected` **\_state**: [`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L23)

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`_state`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#_state)

## Accessors

### messageBuilder

#### Get Signature

> **get** `protected` **messageBuilder**(): [`MessageBuilder`](../../../../../../common/web/core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/ui/actions/Action.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L59)

##### Returns

[`MessageBuilder`](../../../../../../common/web/core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`messageBuilder`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#messagebuilder)

***

### state

#### Get Signature

> **get** **state**(): [`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:143](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L143)

The current state of the action.

##### Returns

[`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`state`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#state)

## Methods

### addDefaultNotifiers()

> `protected` **addDefaultNotifiers**(...`args`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:90](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L90)

#### Parameters

##### args

...`any`[]

#### Returns

`void`

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`addDefaultNotifiers`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#adddefaultnotifiers)

***

### addNotifier()

> **addNotifier**(`state`, `notifier`, `verboseOnly`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L66)

Adds a new notifier for the specified state.

#### Parameters

##### state

[`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

The state the notifier should react to.

##### notifier

The notifier.

[`ActionNotifier`](../../../../../../common/web/ui/actions/notifiers/ActionNotifier/classes/ActionNotifier.md) | [`ActionNotifier`](../../../../../../common/web/ui/actions/notifiers/ActionNotifier/classes/ActionNotifier.md)[]

##### verboseOnly

`boolean` = `false`

If true, the notification will only be added in verbose mode.

#### Returns

`void`

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`addNotifier`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#addnotifier)

***

### completed()

> **completed**(`cb`): `this`

Defined in: [src/common/web/ui/actions/ActionBase.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L44)

Adds a callback for action completion.

#### Parameters

##### cb

[`ActionDoneCallback`](../../../../../../common/web/ui/actions/ActionBase/type-aliases/ActionDoneCallback.md)

The callback to add.

#### Returns

`this`

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`completed`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#completed)

***

### execute()

> **execute**(): `void`

Defined in: [src/common/web/ui/actions/Action.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L44)

Executes the action (i.e., the message will be emitted).

#### Returns

`void`

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`execute`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#execute)

***

### failed()

> **failed**(`cb`): `this`

Defined in: [src/common/web/ui/actions/ActionBase.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L54)

Adds a callback for action failure.

#### Parameters

##### cb

[`ActionFailCallback`](../../../../../../common/web/ui/actions/ActionBase/type-aliases/ActionFailCallback.md)

The callback to add.

#### Returns

`this`

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`failed`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#failed)

***

### onStateChanged()

> `protected` **onStateChanged**(`newState`, `oldState`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:134](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L134)

#### Parameters

##### newState

[`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

##### oldState

[`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

#### Returns

`void`

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`onStateChanged`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#onstatechanged)

***

### postExecution()

> `protected` **postExecution**(): `void`

Defined in: [src/common/web/ui/actions/EventAction.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/EventAction.ts#L10)

#### Returns

`void`

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`postExecution`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#postexecution)

***

### preExecution()

> `protected` **preExecution**(): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:136](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L136)

#### Returns

`void`

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`preExecution`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#preexecution)

***

### prepare()

> `abstract` **prepare**(...`args`): `CompType`

Defined in: [src/common/web/ui/actions/Action.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L39)

Prepares this action.

#### Parameters

##### args

...`any`[]

#### Returns

`CompType`

- A message composer that can be further modified.

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`prepare`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#prepare)

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

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`prepareNotifiers`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#preparenotifiers)

***

### setState()

> `protected` **setState**(`state`, `message`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:103](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L103)

Sets the active state of this action.

#### Parameters

##### state

[`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

The state to apply

##### message

`string` = `""`

An optional notification message.

#### Returns

`void`

#### Inherited from

[`EventAction`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md).[`setState`](../../../../../../common/web/ui/actions/EventAction/classes/EventAction.md#setstate)
