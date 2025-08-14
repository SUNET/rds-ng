---
sidebar_label: resources_transmitter_callbacks
title: integration.resources.transmitters.resources_transmitter_callbacks
---

## ResourcesTransmitterPrepareCallbacks Objects

```python
class ResourcesTransmitterPrepareCallbacks(
        ExecutionCallbacks[typing.Callable[[ResourcesList], None],
                           typing.Callable[[Exception], None]])
```

Callbacks used for transmitter preparation.

## ResourcesTransmitterDownloadCallbacks Objects

```python
class ResourcesTransmitterDownloadCallbacks(ExecutionCallbacks[
        typing.Callable[[Resource, ResourceBuffer], None],
        typing.Callable[[Resource, Exception], None],
])
```

Callbacks used for transmitter downloads.

#### progress

```python
def progress(cb: typing.Callable[[Resource, int, int], None]) -> typing.Self
```

Adds a *Progress* callback.

**Arguments**:

- `cb` - The callback to add.
  

**Returns**:

  This instance to allow call chaining.

#### all\_done

```python
def all_done(cb: typing.Callable[[bool], None]) -> typing.Self
```

Adds a *All Done* callback.

**Arguments**:

- `cb` - The callback to add.
  

**Returns**:

  This instance to allow call chaining.

#### invoke\_progress\_callbacks

```python
def invoke_progress_callbacks(*args, **kwargs) -> None
```

Invokes all *Progress* callbacks.

#### invoke\_all\_done\_callbacks

```python
def invoke_all_done_callbacks(*args, **kwargs) -> None
```

Invokes all *All Done* callbacks.

