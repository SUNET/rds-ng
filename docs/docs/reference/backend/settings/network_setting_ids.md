---
sidebar_label: network_setting_ids
title: settings.network_setting_ids
---

## NetworkSettingIDs Objects

```python
class NetworkSettingIDs()
```

Identifiers for general networking settings.

**Attributes**:

- `API_KEY` - An arbitrary API key to access protected resources (value type: ``string``).
- `VERIFY_SSL` - If enabled, SSL certificates will be verified (value type: ``bool``).
- `TRANSMISSION_CHUNK_SIZE` - The size (in bytes) for network transmissions (value type: ``int``).
- `REGULAR_COMMAND_TIMEOUT` - The timeout (in seconds) for commands (value type: ``float``).
- ``2 - The maximum time (in seconds) for requests to external services; set to 0 to disable (value type: ``float``).

## NetworkServerSettingIDs Objects

```python
class NetworkServerSettingIDs()
```

Identifiers for server-specific networking settings.

**Attributes**:

- `ALLOWED_ORIGINS` - A comma-separated list of allowed origins; use the asterisk (*) to allow all (value type: ``string``).
- `IDLE_TIMEOUT` - The time (in seconds) until idle clients will be disconnected automatically; set to 0 to disable (value type: ``float``).

## NetworkClientSettingIDs Objects

```python
class NetworkClientSettingIDs()
```

Identifiers for client-specific networking settings.

**Attributes**:

- `SERVER_ADDRESS` - The address of the server the client should automatically connect to (value type: ``string``).
- `CONNECTION_TIMEOUT` - The maximum time (in seconds) for connection attempts (value type: ``float``).

