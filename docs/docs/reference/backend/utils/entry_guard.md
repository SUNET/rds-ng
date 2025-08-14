---
sidebar_label: entry_guard
title: utils.entry_guard
---

## EntryGuard Objects

```python
class EntryGuard()
```

A simple context-manager to protect functions from re-entry, usually during asynchronous execution.

In order to check if the function should be executed, query the `can_execute` property.

