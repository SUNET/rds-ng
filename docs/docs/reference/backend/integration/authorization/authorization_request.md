---
sidebar_label: authorization_request
title: integration.authorization.authorization_request
---

## AuthorizationRequestPayload Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class AuthorizationRequestPayload()
```

The payload that is sent with authorization requests.

**Attributes**:

- `auth_id` - The authorization ID.
- `auth_type` - The authorization type.
- `auth_issuer` - The entity that requires the authorization.
- `auth_bearer` - The entity that will be authorized against.
  
- `fingerprint` - The user&#x27;s fingerprint.

