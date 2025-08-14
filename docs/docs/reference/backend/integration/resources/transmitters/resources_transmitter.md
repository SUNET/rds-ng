---
sidebar_label: resources_transmitter
title: integration.resources.transmitters.resources_transmitter
---

## ResourcesTransmitter Objects

```python
class ResourcesTransmitter(AuthorizedExecutor)
```

Main class to transmit resources.

#### \_\_init\_\_

```python
def __init__(comp: BackendComponent,
             svc: Service,
             *,
             auth_channel: Channel,
             tunnel_type: type[ResourcesBrokerTunnelType],
             user_token: UserToken,
             broker_token: ResourcesBrokerToken,
             max_attempts: int = 1,
             attempts_delay: float = 3.0,
             auth_token_refresh: bool = False)
```

**Arguments**:

- `comp` - The global component.
- `svc` - The service used for message sending.
- `auth_channel` - Channel to fetch authorization tokens from.
- `tunnel_type` - The type of the resources broker tunnel that will be created for downloading.
- `user_token` - The user token.
- `broker_token` - The broker token.
- `max_attempts` - The number of attempts for each operation; cannot be less than 1.
- `attempts_delay` - The delay (in seconds) between each attempt.
- `auth_token_refresh` - Whether expired authorization tokens should be refreshed automatically.

#### prepare

```python
def prepare(
    project: Project,
    *,
    callbacks:
    ResourcesTransmitterPrepareCallbacks = ResourcesTransmitterPrepareCallbacks(
    )
) -> None
```

Prepares the transmission of resources; must always be called before any other method.

**Arguments**:

- `project` - The project to work on.
- `callbacks` - Optional execution callbacks.

#### download

```python
def download(
    resource: Resource,
    *,
    callbacks:
    ResourcesTransmitterDownloadCallbacks = ResourcesTransmitterDownloadCallbacks(
    )
) -> None
```

Downloads a resource using the provided tunnel type.

**Arguments**:

- `resource` - The resource to download.
- `callbacks` - Optional execution callbacks.

#### download\_all

```python
def download_all(
    *,
    callbacks:
    ResourcesTransmitterDownloadCallbacks = ResourcesTransmitterDownloadCallbacks(
    ))
```

Downloads all previously listed files.

**Arguments**:

- `callbacks` - Optional execution callbacks.

#### download\_list

```python
def download_list(
    resources: typing.List[Resource],
    *,
    callbacks:
    ResourcesTransmitterDownloadCallbacks = ResourcesTransmitterDownloadCallbacks(
    )
) -> None
```

Downloads an entire list of resources.

**Arguments**:

- `resources` - The resources list.
- `callbacks` - Optional execution callbacks.

