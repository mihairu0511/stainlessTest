# Devices

Types:

```python
from stainlesstest.types import DeviceListResponse
```

Methods:

- <code title="post /devices">client.devices.<a href="./src/stainlesstest/resources/devices.py">create</a>(\*\*<a href="src/stainlesstest/types/device_create_params.py">params</a>) -> None</code>
- <code title="get /devices">client.devices.<a href="./src/stainlesstest/resources/devices.py">list</a>(\*\*<a href="src/stainlesstest/types/device_list_params.py">params</a>) -> <a href="./src/stainlesstest/types/device_list_response.py">DeviceListResponse</a></code>

# Lighting

## Dimmers

Types:

```python
from stainlesstest.types.lighting import APIResponse
```

Methods:

- <code title="post /lighting/dimmers/{deviceId}/{value}">client.lighting.dimmers.<a href="./src/stainlesstest/resources/lighting/dimmers.py">set_value</a>(value, \*, device_id) -> <a href="./src/stainlesstest/types/lighting/api_response.py">APIResponse</a></code>
- <code title="post /lighting/dimmers/{deviceId}/{value}/timer/{timeunit}">client.lighting.dimmers.<a href="./src/stainlesstest/resources/lighting/dimmers.py">set_value_with_timer</a>(timeunit, \*, device_id, value, \*\*<a href="src/stainlesstest/types/lighting/dimmer_set_value_with_timer_params.py">params</a>) -> <a href="./src/stainlesstest/types/lighting/api_response.py">APIResponse</a></code>

## Switches

Types:

```python
from stainlesstest.types.lighting import SwitchRetrieveResponse
```

Methods:

- <code title="get /lighting/switches/{deviceId}">client.lighting.switches.<a href="./src/stainlesstest/resources/lighting/switches.py">retrieve</a>(device_id) -> <a href="./src/stainlesstest/types/lighting/switch_retrieve_response.py">SwitchRetrieveResponse</a></code>
- <code title="post /lighting/switches/{deviceId}/{value}">client.lighting.switches.<a href="./src/stainlesstest/resources/lighting/switches.py">set_value</a>(value, \*, device_id) -> <a href="./src/stainlesstest/types/lighting/api_response.py">APIResponse</a></code>
- <code title="post /lighting/switches/{deviceId}/{value}/timer/{minutes}">client.lighting.switches.<a href="./src/stainlesstest/resources/lighting/switches.py">set_value_with_timer</a>(minutes, \*, device_id, value) -> <a href="./src/stainlesstest/types/lighting/api_response.py">APIResponse</a></code>

# LightingSummary

Types:

```python
from stainlesstest.types import LightingSummaryRetrieveResponse
```

Methods:

- <code title="get /lightingSummary">client.lighting_summary.<a href="./src/stainlesstest/resources/lighting_summary.py">retrieve</a>() -> <a href="./src/stainlesstest/types/lighting_summary_retrieve_response.py">LightingSummaryRetrieveResponse</a></code>

# Temperature

Types:

```python
from stainlesstest.types import (
    TemperatureZoneStatus,
    TemperatureZoneStatusSingleZone,
    TemperatureRetrieveResponse,
    TemperatureForecastResponse,
)
```

Methods:

- <code title="get /temperature">client.temperature.<a href="./src/stainlesstest/resources/temperature/temperature.py">retrieve</a>() -> <a href="./src/stainlesstest/types/temperature_retrieve_response.py">TemperatureRetrieveResponse</a></code>
- <code title="get /temperature/forecast/{days}">client.temperature.<a href="./src/stainlesstest/resources/temperature/temperature.py">forecast</a>(days) -> <a href="./src/stainlesstest/types/temperature_forecast_response.py">TemperatureForecastResponse</a></code>
- <code title="get /temperature/{zoneId}">client.temperature.<a href="./src/stainlesstest/resources/temperature/temperature.py">retrieve_by_zone</a>(zone_id) -> <a href="./src/stainlesstest/types/temperature_zone_status_single_zone.py">TemperatureZoneStatusSingleZone</a></code>

## Heater

Types:

```python
from stainlesstest.types.temperature import HeaterRetrieveStateResponse
```

Methods:

- <code title="get /temperature/{zoneId}/heater">client.temperature.heater.<a href="./src/stainlesstest/resources/temperature/heater.py">retrieve_state</a>(zone_id) -> <a href="./src/stainlesstest/types/temperature/heater_retrieve_state_response.py">HeaterRetrieveStateResponse</a></code>
- <code title="post /temperature/{zoneId}/heater/{state}">client.temperature.heater.<a href="./src/stainlesstest/resources/temperature/heater.py">set_state</a>(state, \*, zone_id) -> <a href="./src/stainlesstest/types/lighting/api_response.py">APIResponse</a></code>

# Zones

Types:

```python
from stainlesstest.types import ZoneListResponse
```

Methods:

- <code title="get /zones">client.zones.<a href="./src/stainlesstest/resources/zones.py">list</a>() -> <a href="./src/stainlesstest/types/zone_list_response.py">ZoneListResponse</a></code>
- <code title="get /zones/{zoneId}/quiet">client.zones.<a href="./src/stainlesstest/resources/zones.py">retrieve_quiet</a>(zone_id) -> None</code>
