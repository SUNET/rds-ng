---
sidebar_label: strings
title: utils.strings
---

#### human\_readable\_file\_size

```python
def human_readable_file_size(size: int, suffix="B") -> str
```

Converts a file size to a human-readable string.

**Arguments**:

- `size` - The file size to convert.
- `suffix` - Default suffix.
  

**Returns**:

  The human-readable file size.

#### format\_elapsed\_time

```python
def format_elapsed_time(elapsed: float) -> str
```

Converts a number of seconds into a readable string.

**Arguments**:

- `elapsed` - The elapsed time in seconds.
  

**Returns**:

  The string representation.

#### ensure\_starts\_with

```python
def ensure_starts_with(s: str, start: str) -> str
```

Ensures that a string starts with a given string.

**Arguments**:

- `s` - The string.
- `start` - The start to ensure.
  

**Returns**:

  The new string.

