---
sidebar_label: execution_callbacks
title: utils.func.execution_callbacks
---

## ExecutionCallbacks Objects

```python
class ExecutionCallbacks(typing.Generic[DoneCallbackType, FailCallbackType],
                         CallbacksStack)
```

Helper class for running &#x27;Done&#x27; and &#x27;Failed&#x27; callbacks during arbitrary executions.

#### done

```python
def done(cb: DoneCallbackType) -> typing.Self
```

Adds a *Done* callback.

**Arguments**:

- `cb` - The callback to add.
  

**Returns**:

  This instance to allow call chaining.

#### failed

```python
def failed(cb: FailCallbackType) -> typing.Self
```

Adds a *Fail* callback.

**Arguments**:

- `cb` - The callback to add.
  

**Returns**:

  This instance to allow call chaining.

#### invoke\_done\_callbacks

```python
def invoke_done_callbacks(*args, **kwargs) -> None
```

Invokes all *Done* callbacks.

#### invoke\_fail\_callbacks

```python
def invoke_fail_callbacks(*args, **kwargs) -> None
```

Invokes all *Fail* callbacks.

#### done\_callbacks

```python
@property
def done_callbacks() -> typing.List[DoneCallbackType]
```

All *Done* callbacks.

#### fail\_callbacks

```python
@property
def fail_callbacks() -> typing.List[FailCallbackType]
```

All *Fail* callbacks.

