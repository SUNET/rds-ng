---
sidebar_label: functional
title: utils.func.functional
---

#### attempt

```python
def attempt(callback: typing.Callable[..., typing.Any],
            *args,
            cb_retry: typing.Callable[..., None] | None = None,
            cb_failed: typing.Callable[[Exception], None] | None = None,
            attempts: int = 1,
            delay: float = 3.0,
            **kwargs) -> (bool, typing.Any)
```

Attempts to execute a callback function up to a certain number of times. If no attempt succeeds either the `fail_callback` is called or the
exception is re-raised.

**Arguments**:

- `callback` - The callback to attempt.
- `cb_retry` - An optional callback called on each retry.
- `cb_failed` - An optional callback in case of a failure.
- `attempts` - The number of attempts.
- `delay` - The delay (in seconds) between attempts.
- `args` - Arbitrary positional arguments, passed to the callback.
- `kwargs` - Arbitrary keyword arguments, passed to the callback.
  

**Returns**:

  A tuple containing the success of the attempt and the return value of the callback.

