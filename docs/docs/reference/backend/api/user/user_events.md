---
sidebar_label: user_events
title: api.user.user_events
---

## UserAuthorizationsListEvent Objects

```python
@Message.define("event/user/authorization/list")
class UserAuthorizationsListEvent(Event)
```

Event sent when the user authorizations have changed.

**Arguments**:

- `authorizations` - The new list of all granted authorizations.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          authorizations: typing.List[str],
          chain: Message | None = None) -> EventComposer
```

Helper function to easily build this message.

