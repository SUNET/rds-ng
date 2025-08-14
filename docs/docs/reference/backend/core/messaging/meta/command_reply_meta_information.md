---
sidebar_label: command_reply_meta_information
title: core.messaging.meta.command_reply_meta_information
---

## CommandReplyMetaInformation Objects

```python
@dataclasses.dataclass(frozen=True, kw_only=True)
class CommandReplyMetaInformation(MessageMetaInformation)
```

Message meta information specific to ``CommandReply``.

#### is\_handled\_externally

```python
@property
def is_handled_externally() -> bool
```

Whether the message is handled outside the message bus.

#### set\_handled\_externally

```python
def set_handled_externally(value: bool = True) -> None
```

Sets whether the message is handled outside the message bus.

