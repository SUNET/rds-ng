---
sidebar_label: authorization_strategy
title: integration.authorization.strategies.authorization_strategy
---

## AuthorizationStrategy Objects

```python
class AuthorizationStrategy(IntegrationHandler)
```

Base class for all authorization strategies.

**Notes**:

  Strategies report errors through raising exceptions (usually *RuntimeError*).

## ContentType Objects

```python
class ContentType(Flag)
```

Flags describing what contents the strategy provides.

#### \_\_init\_\_

```python
def __init__(comp: BackendComponent,
             svc: Service,
             strategy: str,
             *,
             contents: ContentType,
             user_token: UserToken | None = None,
             auth_token: AuthorizationToken | None = None,
             auth_private: AuthorizationSettings | None = None)
```

**Arguments**:

- `comp` - The global component.
- `svc` - The service used to send messages through.
- `strategy` - The strategy identifier.
- `contents` - The contents this strategy provides.
- `user_token` - An optional user token.
- `auth_token` - An optional authorization token.
- `auth_private` - Optional private authorization settings.

#### provides\_token\_content

```python
def provides_token_content(content: ContentType) -> bool
```

Checks if a certain content type is provided by this strategy.

**Arguments**:

- `content` - The content type.

#### get\_token\_content

```python
def get_token_content(token: AuthorizationToken,
                      content: ContentType) -> typing.Any
```

Retrieves the token content of the specified type.

**Arguments**:

- `token` - The authorization token.
- `content` - The content type.
  

**Returns**:

  The token content or **None** in case of any errors.

#### strategy

```python
@property
def strategy() -> str
```

The strategy identifier.

#### contents

```python
@property
def contents() -> ContentType
```

The content flags.

