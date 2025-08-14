---
sidebar_label: callbacks_stack
title: utils.func.callbacks_stack
---

## CallbacksStack Objects

```python
class CallbacksStack()
```

Helper class for running arbitrary callbacks.

#### assign

```python
def assign(key: str, cb: CallbackType) -> typing.Self
```

Assigns a new callback for the specified key.

**Arguments**:

- `key` - The key of the callback stack.
- `cb` - The callback.
  

**Returns**:

  This instance for easy chaining.

#### invoke

```python
def invoke(key: str, *args, **kwargs) -> None
```

Invokes all callbacks for the specified key.

**Arguments**:

- `key` - The key of the callback stack.

#### reset

```python
def reset() -> None
```

Removecs all callbacks.

#### callbacks

```python
def callbacks(key: str) -> typing.List[CallbackType]
```

Gets all callbacks associated with the given key.

**Arguments**:

- `key` - The key of the callback stack.
  

**Returns**:

  List of callbacks.

