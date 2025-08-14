---
id: "common_web_core_messaging_handlers_MessageContext.MessageContext"
title: "Class: MessageContext"
sidebar_label: "MessageContext"
custom_edit_url: null
---

[common/web/core/messaging/handlers/MessageContext](../modules/common_web_core_messaging_handlers_MessageContext.md).MessageContext

An execution context for messages dispatched by the message bus.

When a message handler gets executed (i.e., called by the message bus dispatchers), an instance of ``MessageContext`` (or a subclass)
is passed to the handler. This context can be seen as a *unit of work* that exists during the execution of the handler. Its main task is to
hold data that is specific to this single execution.

A message context is used as a context manager. In its ``__exit__`` method, any exceptions will be catched, printed and passed on. This
makes tracing of errors that occur during message handling easier.

It is also possible to have message handlers receive custom subtypes of this class. See ``WebComponent`` and its ``create_service`` method for
details.

## Hierarchy

- **`MessageContext`**

  ↳ [`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)

## Constructors

### constructor

• **new MessageContext**(`msgMeta`, `msgOrigin`, `msgBuilder`, `logger`, `config`): [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) | The meta information of the message. |
| `msgOrigin` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | The origin of the message. |
| `msgBuilder` | [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md) | A ``MessageBuilder`` to be assigned to this context. |
| `logger` | [`LoggerProxy`](common_web_core_logging_LoggerProxy.LoggerProxy.md) | A logger that is configured to automatically print the trace belonging to the message that caused the handler to be executed. |
| `config` | [`Configuration`](common_web_utils_config_Configuration.Configuration.md) | The global component configuration. |

#### Returns

[`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:38](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L38)

## Properties

### \_config

• `Protected` `Readonly` **\_config**: [`Configuration`](common_web_utils_config_Configuration.Configuration.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L27)

___

### \_logger

• `Protected` `Readonly` **\_logger**: [`LoggerProxy`](common_web_core_logging_LoggerProxy.LoggerProxy.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L26)

___

### \_msgBuilder

• `Protected` `Readonly` **\_msgBuilder**: [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L24)

___

### \_msgMeta

• `Protected` `Readonly` **\_msgMeta**: [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L22)

___

### \_msgOrigin

• `Protected` `Readonly` **\_msgOrigin**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L23)

___

### \_requiresReply

• `Protected` **\_requiresReply**: `boolean` = `false`

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L29)

## Accessors

### config

• `get` **config**(): [`Configuration`](common_web_utils_config_Configuration.Configuration.md)

The global component configuration.

#### Returns

[`Configuration`](common_web_utils_config_Configuration.Configuration.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:123](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L123)

___

### isEntrypointClient

• `get` **isEntrypointClient**(): `boolean`

Whether the message entered through the client.

#### Returns

`boolean`

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:95](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L95)

___

### isEntrypointLocal

• `get` **isEntrypointLocal**(): `boolean`

Whether the message entered locally.

#### Returns

`boolean`

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:81](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L81)

___

### isEntrypointServer

• `get` **isEntrypointServer**(): `boolean`

Whether the message entered through the server.

#### Returns

`boolean`

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:88](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L88)

___

### logger

• `get` **logger**(): [`LoggerProxy`](common_web_core_logging_LoggerProxy.LoggerProxy.md)

The logger to be used within this context.

#### Returns

[`LoggerProxy`](common_web_core_logging_LoggerProxy.LoggerProxy.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:116](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L116)

___

### messageBuilder

• `get` **messageBuilder**(): [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

The message builder to be used within this context.

#### Returns

[`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:109](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L109)

___

### origin

• `get` **origin**(): [`UnitID`](common_web_utils_UnitID.UnitID.md)

The origin of the message.

#### Returns

[`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:102](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L102)

## Methods

### begin

▸ **begin**(`requiresReply`): `void`

Initiates execution within this context.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `requiresReply` | `boolean` | Whether a reply is required. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L52)

___

### checkCommandReply

▸ **checkCommandReply**(): `void`

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L72)

___

### end

▸ **end**(): `void`

Finishes execution within this context.

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L59)

___

### reportError

▸ **reportError**(`err`): `void`

Reports an error occurred during context execution.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `err` | `any` | The error to report. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:68](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L68)
