# RDS-NG configuration

Below is an overview of all available settings of each RDS-NG component. These settings can either be set in `config.toml` files (located in `src/<component>/.config`) or via environment variables.

## Environment variables

Environment variables are always prefixed with `RDS_` and written in capital letters; all dots need to replaced by underscores. A setting like `authorization.refresh_attempts_limit`, for example, translates to `RDS_AUTHORIZATION_REFRESH_ATTEMPTS_LIMIT`.

To pass environment variables into the containers, `.env` files can be used; these are placed inside the `deployment/env` directory; examples are provided in the `examples` subdirectory.

> **IMPORTANT!**
> Environment variables can only be used in the frontend when running in `develop` mode! If you want to run in `release` mode, frontend settings _must_ be set in its `config.toml`file (located in `src/frontend/static/config`).

## Settings

Most settings have reasonable defaults and usually don't need to be changed. Mandatory settngs are always listed for each component and must be set in order to be able to run RDS-NG.

> **IMPORTANT!**
> Always set all mandatory settings in your configuration! Otherwise, the setup will not run.

### Frontend settings

#### Mandatory settings

- <code>network.client.server_address</code>
- <code>integration.host.api_url</code>
- <code>authorization.oauth2.client.id</code> (1)
- <code>authorization.oauth2.client.redirect_url</code> (1)

_(1)_ If the host uses OAUTH2 authorization.

#### General

| Setting                                    | Description                                                         | Type    | Default value |
|--------------------------------------------|---------------------------------------------------------------------|---------|---------------|
| <code>general.verbose_notifications</code> | Whether to display more verbose notifications (good for debugging). | Boolean | false         |
| <code>general.notification_timeout</code>  | The timeout for overlay notifications in seconds.                   | Number  | 3.0           |
| <code>general.notification_timeout</code>  | The timeout for overlay notifications in seconds.                   | Number  | 3.0           |

#### Theming

| Setting                                | Description                           | Type   | Default value |
|----------------------------------------|---------------------------------------|--------|---------------|
| <code>theme.primary_color</code>       | The primary theme color.              | String | #29833B       |
| <code>theme.light.surface_color</code> | The surface color when in light mode. | String | Slate         |
| <code>theme.dark.surface_color</code>  | The surface color when in dark mode.  | String | White         |

#### Networking

| Setting                                        | Description                                                           | Type   | Default value |
|------------------------------------------------|-----------------------------------------------------------------------|--------|---------------|
| <code>network.regular_command_timeout</code>   | The maximum time (in seconds) for a command-reply to arrive.          | Number | 10.0          |
| <code>network.client.server_address</code>     | The address of the server the client should automatically connect to. | String |               |
| <code>network.client.connection_timeout</code> | The maximum time (in seconds) for connection attempts.                | Number | 10.0          |

#### Integration

| Setting                               | Description                                                                                                                                                                                | Type   | Default value |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------|
| <code>integration.host.api_url</code> | The full URL where the host integration exposes its API; this needs to be in the form of `<APP_URL>/api/v1` (e.g., `http://localhost:8080/apps/rdsng/api/v1` for a local Nextcloud setup). | String |               |

#### Authorization

In order to be properly integrated into its host system, the frontend will authorize against it using OAUTH2. This means that you usually will need to generate a new OAUTH2 client ID and secret for the frontend in your host system.

| Setting                                               | Description                                                                                                                                                                | Type   | Default value |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------|
| <code>authorization.oauth2.client.id</code>           | The OAUTH2 client ID of the frontend.                                                                                                                                      | String |               |
| <code>authorization.oauth2.client.redirect_url</code> | The URL OAUTH2 will redirect to; this needs to be set to the full URL of the host integration (e.g., `http://localhost:8080/apps/rdsng/main` for a local Nextcloud setup). | String |               |
