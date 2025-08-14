---
sidebar_label: authorization_token_storage
title: data.storage.authorization_token_storage
---

## AuthorizationTokenStorage Objects

```python
class AuthorizationTokenStorage(Storage[AuthorizationToken,
                                        AuthorizationTokenID], abc.ABC)
```

Storage for authorization tokens.

#### filter\_by\_user

```python
@abc.abstractmethod
def filter_by_user(user_id: UserID) -> typing.List[AuthorizationToken]
```

Returns all tokens belonging to the specified user.

**Arguments**:

- `user_id` - The user ID.
  

**Returns**:

  The matching tokens list.

