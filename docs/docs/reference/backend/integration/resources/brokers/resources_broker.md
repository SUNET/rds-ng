---
sidebar_label: resources_broker
title: integration.resources.brokers.resources_broker
---

## ResourcesBroker Objects

```python
class ResourcesBroker(IntegrationHandler)
```

Base class for all resources brokers.

**Notes**:

  Brokers report errors through raising exceptions (usually *RuntimeError*).

#### \_\_init\_\_

```python
def __init__(comp: BackendComponent,
             svc: Service,
             broker: str,
             *,
             user_token: UserToken,
             auth_token: AuthorizationToken | None = None,
             auth_token_refresh: bool = True,
             default_root: str = "")
```

**Arguments**:

- `comp` - The global component.
- `svc` - The service to use for message sending.
- `broker` - The broker identifier.
- `user_token` - The user token.
- `auth_token` - An optional authorization token.
- `auth_token_refresh` - Whether expired authorization tokens should be refreshed automatically.
- `default_root` - The default root path (overrides the globally configured root).

#### list\_resources

```python
@abc.abstractmethod
def list_resources(root: str,
                   include_folders: bool = True,
                   include_files: bool = True,
                   recursive: bool = True) -> ResourcesList
```

Retrieves a list of all available resources.

**Arguments**:

- `root` - The root path.
- `include_folders` - Whether to include folders.
- `include_files` - Whether to include files.
- `recursive` - Whether to recurse into subdirectories.
  

**Returns**:

  A list of all resources.

#### download\_resource

```python
@abc.abstractmethod
def download_resource(resource: Resource, *,
                      tunnel: ResourcesBrokerTunnel) -> None
```

Downloads the specified resource using the provided tunnel. In case of an error, an exception should be raised.

**Arguments**:

- `resource` - The resource to download.
- `tunnel` - The resources tunnel.

#### broker

```python
@property
def broker() -> str
```

The broker identifier.

#### has\_authorization

```python
@property
def has_authorization() -> bool
```

Whether the broker has valid authorization information.

