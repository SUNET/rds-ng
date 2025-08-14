---
sidebar_label: extended_dictionary
title: utils.extended_dictionary
---

## ExtendedDictionary Objects

```python
class ExtendedDictionary()
```

Class to access data from a dictionary through dot notation.

#### value

```python
def value(path: str, default: typing.Any = None) -> typing.Any
```

Gets a value from the dictionary, supporting dot notation.

**Arguments**:

- `path` - The full value path.
- `default` - A default value.
  

**Returns**:

  The value or the default one if none was found.

#### value\_from\_data

```python
def value_from_data(data: typing.Any,
                    path: str,
                    default: typing.Any = None) -> typing.Any
```

Gets a value from a specific data object.

**Arguments**:

- `data` - The data object.
- `path` - The value path.
- `default` - A default value.
  

**Returns**:

  The value or the default one if none was found.

#### data

```python
@property
def data() -> typing.Any
```

The raw data.

