---
sidebar_label: user_commands
title: api.user.user_commands
---

## AuthenticateUserCommand Objects

```python
@Message.define("command/user/authenticate")
class AuthenticateUserCommand(Command)
```

Command to authenticate a user. Note that the actual login/authentication is performed by the underlying host system.

**Arguments**:

- `user_token` - The user token.
  

**Notes**:

  Requires a ``AuthenticateUserReply`` reply.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          user_token: UserToken,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## AuthenticateUserReply Objects

```python
@Message.define("command/user/authenticate/reply")
class AuthenticateUserReply(CommandReply)
```

Reply to ``AuthenticateUserCommand``.

**Arguments**:

- `authorization_state` - The authorization state of the user in his host system.
- `fingerprint` - The user&#x27;s fingerprint.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: AuthenticateUserCommand,
          *,
          authorization_state: AuthorizationState,
          fingerprint: str = "",
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.

## GetUserSettingsCommand Objects

```python
@Message.define("command/user/settings/get")
class GetUserSettingsCommand(Command)
```

Command to get the settings of the current user.

**Notes**:

  Requires a ``GetUserSettingsReply`` reply.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## GetUserSettingsReply Objects

```python
@Message.define("command/user/settings/get/reply")
class GetUserSettingsReply(CommandReply)
```

Reply to ``GetUserSettingsCommand``.

**Arguments**:

- `settings` - The user settings.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: GetUserSettingsCommand,
          *,
          settings: User.Settings,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.

## SetUserSettingsCommand Objects

```python
@Message.define("command/user/settings/set")
class SetUserSettingsCommand(Command)
```

Command to set the settings of the current user.

**Arguments**:

- `settings` - The new user settings.
  

**Notes**:

  Requires a ``SetUserSettingsReply`` reply.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          settings: User.Settings,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## SetUserSettingsReply Objects

```python
@Message.define("command/user/settings/set/reply")
class SetUserSettingsReply(CommandReply)
```

Reply to ``SetUserSettingsCommand``.

**Arguments**:

- `settings` - The new user settings (note that these might have been adjusted by the server).

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: SetUserSettingsCommand,
          *,
          settings: User.Settings,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.

## ListUserAuthorizationsCommand Objects

```python
@Message.define("command/user/authorization/list")
class ListUserAuthorizationsCommand(Command)
```

Command to get all granted authorizations of the current user.

**Notes**:

  Requires a ``ListUserAuthorizationsReply`` reply.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## ListUserAuthorizationsReply Objects

```python
@Message.define("command/user/authorization/list/reply")
class ListUserAuthorizationsReply(CommandReply)
```

Reply to ``ListUserAuthorizationsCommand``.

**Arguments**:

- `authorizations` - List of all granted authorizations.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: ListUserAuthorizationsCommand,
          *,
          authorizations: typing.List[str],
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.

