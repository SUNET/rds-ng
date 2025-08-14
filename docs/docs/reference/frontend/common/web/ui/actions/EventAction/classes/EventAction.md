# Abstract Class: EventAction\<EventType, CompType\>

Defined in: [src/common/web/ui/actions/EventAction.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/EventAction.ts#L9)

Actions specific to ``Event``.

## Extends

- [`Action`](../../Action/classes/Action.md)\<`EventType`, `CompType`\>

## Extended by

- [`FrontendEventAction`](../../../../../../frontend/src/ui/actions/FrontendEventAction/classes/FrontendEventAction.md)

## Type Parameters

### EventType

`EventType` *extends* [`Event`](../../../../core/messaging/Event/classes/Event.md)

### CompType

`CompType` *extends* [`EventComposer`](../../../../core/messaging/composers/EventComposer/classes/EventComposer.md)\<`EventType`\>

## Constructors

### Constructor

> **new EventAction**\<`EventType`, `CompType`\>(`service`, `suppressDefaultNotifiers`): `EventAction`\<`EventType`, `CompType`\>

Defined in: [src/common/web/ui/actions/Action.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L25)

#### Parameters

##### service

[`Service`](../../../../services/Service/classes/Service.md)

The service to use for message emission.

##### suppressDefaultNotifiers

`boolean` = `false`

Suppress default notifiers.

#### Returns

`EventAction`\<`EventType`, `CompType`\>

#### Inherited from

[`Action`](../../Action/classes/Action.md).[`constructor`](../../Action/classes/Action.md#constructor)

## Properties

### \_composer

> `protected` **\_composer**: `null` \| `CompType` = `null`

Defined in: [src/common/web/ui/actions/Action.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L19)

#### Inherited from

[`Action`](../../Action/classes/Action.md).[`_composer`](../../Action/classes/Action.md#_composer)

***

### \_state

> `protected` **\_state**: [`ActionState`](../../ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L23)

#### Inherited from

[`Action`](../../Action/classes/Action.md).[`_state`](../../Action/classes/Action.md#_state)

## Accessors

### messageBuilder

#### Get Signature

> **get** `protected` **messageBuilder**(): [`MessageBuilder`](../../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/ui/actions/Action.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L59)

##### Returns

[`MessageBuilder`](../../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

#### Inherited from

[`Action`](../../Action/classes/Action.md).[`messageBuilder`](../../Action/classes/Action.md#messagebuilder)

***

### state

#### Get Signature

> **get** **state**(): [`ActionState`](../../ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:143](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L143)

The current state of the action.

##### Returns

[`ActionState`](../../ActionBase/enumerations/ActionState.md)

#### Inherited from

[`Action`](../../Action/classes/Action.md).[`state`](../../Action/classes/Action.md#state)

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

[`Action`](../../Action/classes/Action.md).[`addDefaultNotifiers`](../../Action/classes/Action.md#adddefaultnotifiers)

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

[`Action`](../../Action/classes/Action.md).[`addNotifier`](../../Action/classes/Action.md#addnotifier)

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

[`Action`](../../Action/classes/Action.md).[`completed`](../../Action/classes/Action.md#completed)

***

### execute()

> **execute**(): `void`

Defined in: [src/common/web/ui/actions/Action.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L44)

Executes the action (i.e., the message will be emitted).

#### Returns

`void`

#### Inherited from

[`Action`](../../Action/classes/Action.md).[`execute`](../../Action/classes/Action.md#execute)

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

[`Action`](../../Action/classes/Action.md).[`failed`](../../Action/classes/Action.md#failed)

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

[`Action`](../../Action/classes/Action.md).[`onStateChanged`](../../Action/classes/Action.md#onstatechanged)

***

### postExecution()

> `protected` **postExecution**(): `void`

Defined in: [src/common/web/ui/actions/EventAction.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/EventAction.ts#L10)

#### Returns

`void`

#### Overrides

[`Action`](../../Action/classes/Action.md).[`postExecution`](../../Action/classes/Action.md#postexecution)

***

### preExecution()

> `protected` **preExecution**(): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:136](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L136)

#### Returns

`void`

#### Inherited from

[`Action`](../../Action/classes/Action.md).[`preExecution`](../../Action/classes/Action.md#preexecution)

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

[`Action`](../../Action/classes/Action.md).[`prepare`](../../Action/classes/Action.md#prepare)

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

[`Action`](../../Action/classes/Action.md).[`prepareNotifiers`](../../Action/classes/Action.md#preparenotifiers)

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

[`Action`](../../Action/classes/Action.md).[`setState`](../../Action/classes/Action.md#setstate)
