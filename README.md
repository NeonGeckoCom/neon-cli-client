# Neon CLI Client
This is a lightly modified client from [mycroft-core](https://github.com/MycroftAI/mycroft-core/tree/dev/mycroft/client/text).
The CLI can be accessed from a terminal via `neon-cli`.

## CLI Usage
By default, the CLI will use default parameters to connect to a Neon/Mycroft/OVOS
Core instance running on the local host. The following arguments may be passed to
override defaults. This information is also accessible via `neon-cli --help`.

### `--host 0.0.0.0`
The default `0.0.0.0` may be replaced with a different IP address if connecting
to a remote core instance. Note that the messagebus carries unencrypted data, so
enabling remote access is not generally recommended

### `--port 8181`
The default `8181` may be replaced with a different port if the messagebus service
was configured to use a non-default port.

### `--lang en-us`
The language of CLI inputs and expected responses can be set by passing a BCP-47
language code here.

### `--logs-dir ~/.local/state/neon/`
The default log directory is read from configuration, but it may be overridden
here. This is commonly set for Docker connections, where the log path on the host
is not configured for the CLI client.

### `--simple`
This flag will enable a simple text-based CLI showing only inputs and responses.
This can be useful if the default CLI doesn't display properly in a terminal.