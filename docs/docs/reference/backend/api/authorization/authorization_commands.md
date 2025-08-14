---
sidebar_label: authorization_commands
title: api.authorization.authorization_commands
---

## RequestAuthorizationCommand Objects

```python
@Message.define("command/authorization/request")
class RequestAuthorizationCommand(Command)
```

Command to perform an authorization request.

**Notes**:

  Requires a ``RequestAuthorizationReply`` reply.
  

**Arguments**:

- `request_payload` - The authorization request information.
- `strategy` - The token strategy (e.g., OAuth2).
- `data` - The actual token request data.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          request_payload: AuthorizationRequestPayload,
          strategy: str,
          data: typing.Dict[str, typing.Any],
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## RequestAuthorizationReply Objects

```python
@Message.define("command/authorization/request/reply")
class RequestAuthorizationReply(CommandReply)
```

Reply to ``RequestAuthorizationCommand``.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: RequestAuthorizationCommand,
          *,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.

## RevokeAuthorizationCommand Objects

```python
@Message.define("command/authorization/revoke")
class RevokeAuthorizationCommand(Command)
```

Command to revoke an authorization.

**Notes**:

  Requires a ``RevokeAuthorizationReply`` reply.
  

**Arguments**:

- `user_id` - The user ID.
- `auth_id` - The ID of the token to revoke.
- `force` - If true, the token will be removed immediately; otherwise, it will be marked as invalid only

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          user_id: UserID,
          auth_id: str,
          force: bool = True,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## RevokeAuthorizationReply Objects

```python
@Message.define("command/authorization/revoke/reply")
class RevokeAuthorizationReply(CommandReply)
```

Reply to ``RevokeAuthorizationCommand``.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: RevokeAuthorizationCommand,
          *,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.

## GetAuthorizationTokenCommand Objects

```python
@Message.define("command/authorization/token/get", is_protected=True)
class GetAuthorizationTokenCommand(Command)
```

Command to retrieve an authorization token.

**Notes**:

  This message is protected and requires an API key. Requires a ``GetAuthorizationTokenReply`` reply.
  

**Arguments**:

- `user_id` - The user ID.
- `auth_id` - The ID of the token to revoke.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          user_id: UserID,
          auth_id: str,
          api_key: str,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## GetAuthorizationTokenReply Objects

```python
@Message.define("command/authorization/token/get/reply", is_protected=True)
class GetAuthorizationTokenReply(CommandReply)
```

Reply to ``GetAuthorizationTokenCommand``.

**Notes**:

  This message is protected and requires an API key.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: GetAuthorizationTokenCommand,
          *,
          auth_token: AuthorizationToken | None,
          api_key: str,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.

