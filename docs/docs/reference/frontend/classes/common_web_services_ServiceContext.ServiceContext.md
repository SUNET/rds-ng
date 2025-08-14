---
id: "common_web_services_ServiceContext.ServiceContext"
title: "Class: ServiceContext"
sidebar_label: "ServiceContext"
custom_edit_url: null
---

[common/web/services/ServiceContext](../modules/common_web_services_ServiceContext.md).ServiceContext

An execution context for messages dispatched by the message bus to a service.

This class is an extension to the more general ``MessageContext`` specifically used by ``Service`` and its message handlers.

## Hierarchy

- [`MessageContext`](common_web_core_messaging_handlers_MessageContext.MessageContext.md)

  ↳ **`ServiceContext`**

  ↳↳ [`FrontendServiceContext`](frontend_src_services_FrontendServiceContext.FrontendServiceContext.md)

## Constructors

### constructor

• **new ServiceContext**(`msgMeta`, `msgOrigin`, `msgBuilder`, `logger`, `config`): [`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msgMeta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) | The meta information of the message. |
| `msgOrigin` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | The origin of the message. |
| `msgBuilder` | [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md) | A ``MessageBuilder`` to be assigned to this context. |
| `logger` | [`LoggerProxy`](common_web_core_logging_LoggerProxy.LoggerProxy.md) | A logger that is configured to automatically print the trace belonging to the message that caused the handler to be executed. |
| `config` | [`Configuration`](common_web_utils_config_Configuration.Configuration.md) | The global component configuration. |

#### Returns

[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)

#### Inherited from

[MessageContext](common_web_core_messaging_handlers_MessageContext.MessageContext.md).[constructor](common_web_core_messaging_handlers_MessageContext.MessageContext.md#constructor)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:38](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L38)

## Properties

### \_config

• `Protected` `Readonly` **\_config**: [`Configuration`](common_web_utils_config_Configuration.Configuration.md)

#### Inherited from

[MessageContext](common_web_core_messaging_handlers_MessageContext.MessageContext.md).[_config](common_web_core_messaging_handlers_MessageContext.MessageContext.md#_config)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L27)

___

### \_logger

• `Protected` `Readonly` **\_logger**: [`LoggerProxy`](common_web_core_logging_LoggerProxy.LoggerProxy.md)

#### Inherited from

[MessageContext](common_web_core_messaging_handlers_MessageContext.MessageContext.md).[_logger](common_web_core_messaging_handlers_MessageContext.MessageContext.md#_logger)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L26)

___

### \_msgBuilder

• `Protected` `Readonly` **\_msgBuilder**: [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Inherited from

[MessageContext](common_web_core_messaging_handlers_MessageContext.MessageContext.md).[_msgBuilder](common_web_core_messaging_handlers_MessageContext.MessageContext.md#_msgbuilder)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L24)

___

### \_msgMeta

• `Protected` `Readonly` **\_msgMeta**: [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

#### Inherited from

[MessageContext](common_web_core_messaging_handlers_MessageContext.MessageContext.md).[_msgMeta](common_web_core_messaging_handlers_MessageContext.MessageContext.md#_msgmeta)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L22)

___

### \_msgOrigin

• `Protected` `Readonly` **\_msgOrigin**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Inherited from

[MessageContext](common_web_core_messaging_handlers_MessageContext.MessageContext.md).[_msgOrigin](common_web_core_messaging_handlers_MessageContext.MessageContext.md#_msgorigin)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L23)

___

### \_requiresReply

• `Protected` **\_requiresReply**: `boolean` = `false`

#### Inherited from

[MessageContext](common_web_core_messaging_handlers_MessageContext.MessageContext.md).[_requiresReply](common_web_core_messaging_handlers_MessageContext.MessageContext.md#_requiresreply)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L29)

## Accessors

### config

• `get` **config**(): [`Configuration`](common_web_utils_config_Configuration.Configuration.md)

The global component configuration.

#### Returns

[`Configuration`](common_web_utils_config_Configuration.Configuration.md)

#### Inherited from

MessageContext.config

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:123](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L123)

___

### isEntrypointClient

• `get` **isEntrypointClient**(): `boolean`

Whether the message entered through the client.

#### Returns

`boolean`

#### Inherited from

MessageContext.isEntrypointClient

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:95](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L95)

___

### isEntrypointLocal

• `get` **isEntrypointLocal**(): `boolean`

Whether the message entered locally.

#### Returns

`boolean`

#### Inherited from

MessageContext.isEntrypointLocal

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:81](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L81)

___

### isEntrypointServer

• `get` **isEntrypointServer**(): `boolean`

Whether the message entered through the server.

#### Returns

`boolean`

#### Inherited from

MessageContext.isEntrypointServer

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:88](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L88)

___

### logger

• `get` **logger**(): [`LoggerProxy`](common_web_core_logging_LoggerProxy.LoggerProxy.md)

The logger to be used within this context.

#### Returns

[`LoggerProxy`](common_web_core_logging_LoggerProxy.LoggerProxy.md)

#### Inherited from

MessageContext.logger

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:116](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L116)

___

### messageBuilder

• `get` **messageBuilder**(): [`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

The message builder to be used within this context.

#### Returns

[`MessageBuilder`](common_web_core_messaging_composers_MessageBuilder.MessageBuilder.md)

#### Inherited from

MessageContext.messageBuilder

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:109](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L109)

___

### origin

• `get` **origin**(): [`UnitID`](common_web_utils_UnitID.UnitID.md)

The origin of the message.

#### Returns

[`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Inherited from

MessageContext.origin

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

#### Inherited from

[MessageContext](common_web_core_messaging_handlers_MessageContext.MessageContext.md).[begin](common_web_core_messaging_handlers_MessageContext.MessageContext.md#begin)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L52)

___

### end

▸ **end**(): `void`

Finishes execution within this context.

#### Returns

`void`

#### Inherited from

[MessageContext](common_web_core_messaging_handlers_MessageContext.MessageContext.md).[end](common_web_core_messaging_handlers_MessageContext.MessageContext.md#end)

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

#### Inherited from

[MessageContext](common_web_core_messaging_handlers_MessageContext.MessageContext.md).[reportError](common_web_core_messaging_handlers_MessageContext.MessageContext.md#reporterror)

#### Defined in

[src/common/web/core/messaging/handlers/MessageContext.ts:68](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/handlers/MessageContext.ts#L68)
