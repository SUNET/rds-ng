---
sidebar_label: authorization_token_utils
title: data.entities.authorization.authorization_token_utils
---

#### get\_host\_authorization\_token\_id

```python
def get_host_authorization_token_id(user_id: "UserID") -> AuthorizationTokenID
```

Retrieves the authorization token ID for the user host system.

**Arguments**:

- `user_id` - The user ID.
  

**Returns**:

  The authorization token ID.

#### get\_connector\_instance\_authorization\_id

```python
def get_connector_instance_authorization_id(
        instance: "ConnectorInstanceID") -> str
```

Retrieves the authorization ID for a connector instance.

**Arguments**:

- `instance` - The connector instance ID.
  

**Returns**:

  The authorization ID.

#### get\_connector\_instance\_authorization\_token\_id

```python
def get_connector_instance_authorization_token_id(
        user: "User", instance: "ConnectorInstanceID") -> AuthorizationTokenID
```

Retrieves the authorization token ID for a connector instance.

**Arguments**:

- `user` - The user.
- `instance` - The connector instance ID.
  

**Returns**:

  The authorization token ID.

#### has\_authorization\_token\_expired

```python
def has_authorization_token_expired(token: AuthorizationToken) -> bool
```

Checks whether an authorization token has expired and thus should be refreshed.

**Arguments**:

- `token` - The authorization token.

