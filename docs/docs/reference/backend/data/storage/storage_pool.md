---
sidebar_label: storage_pool
title: data.storage.storage_pool
---

## StoragePool Objects

```python
class StoragePool(abc.ABC)
```

A collection of all data storages.

#### prepare

```python
@staticmethod
def prepare(config: Configuration) -> None
```

Performs initial preparation of the storage pool.

**Arguments**:

- `config` - The global configuration.

#### \_\_init\_\_

```python
def __init__(name: str)
```

**Arguments**:

- `name` - The name of the storage pool.

#### begin

```python
def begin() -> None
```

Called initially when a new pool instance is being used.

#### close

```python
def close(save_changes: bool = True) -> None
```

Closes a single pool instance.

#### name

```python
@property
def name() -> str
```

The name of this backend.

#### connector\_storage

```python
@property
@abc.abstractmethod
def connector_storage() -> ConnectorStorage
```

The connector storage.

#### user\_storage

```python
@property
@abc.abstractmethod
def user_storage() -> UserStorage
```

The user storage.

#### project\_storage

```python
@property
@abc.abstractmethod
def project_storage() -> ProjectStorage
```

The project storage.

#### project\_job\_storage

```python
@property
@abc.abstractmethod
def project_job_storage() -> ProjectJobStorage
```

The project job storage.

#### authorization\_token\_storage

```python
@property
@abc.abstractmethod
def authorization_token_storage() -> AuthorizationTokenStorage
```

The authorization token storage.

