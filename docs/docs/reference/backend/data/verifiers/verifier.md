---
sidebar_label: verifier
title: data.verifiers.verifier
---

## Verifier Objects

```python
class Verifier(Protocol)
```

Defines the general interface for data verifiers.

#### verify\_create

```python
def verify_create() -> None
```

Verifies a new entity. In case of invalid data, an error is thrown.

**Raises**:

- `VerificationException` - In case of any errors in the entity data.

#### verify\_update

```python
def verify_update() -> None
```

Verifies an updated entity. In case of invalid data, an error is thrown.

**Raises**:

- `VerificationException` - In case of any errors in the entity data.

#### verify\_delete

```python
def verify_delete() -> None
```

Verifies the deletion of an entity. In case of invalid data, an error is thrown.

**Raises**:

- `VerificationException` - In case of any errors in the entity data.

