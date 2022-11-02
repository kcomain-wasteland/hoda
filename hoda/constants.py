# hoda.constants: constant "variables"
#  Copyright (c) 2021-2022 soopyc
#
#  This file is part of hoda.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import Literal

LANGUAGE = Literal[
    "tc",
    "sc",
    "en",
]
"""Language Types

Available languages:

- ``tc``: Traditional Chinese
- ``sc``: Simplified Chinese
- ``en``: English
"""

WEATHER_DATA_TYPE = Literal[
    "flw",
    "fnd",
    "rhrread",
    "warnsum",
    "warningInfo",
    "swt",
]
"""Weather Data Types

Available items:

- ``flw``: (forecast) local weather
- ``fnd``: (forecast) nine-days
- ``rhrread``: current weather report (anyone have any idea what the "acronym" stands for?)
- ``warnsum``: current warning summary
- ``warningInfo``: weather warning info
- ``swt``: special weather tips
"""

WEATHER_ICON_URL = "https://www.hoda.gov.hk/images/HKOWxIconOutline/pic{id}.png"
"""The icon url for :const:`WEATHER_ICONS`"""

WEATHER_ICONS = {
    50: {"name": "sunny"},
    51: {"name": "sunny_periods"},
    52: {"name": "sunny_intervals"},
    53: {"name": "sunny_periods_few_showers"},
    54: {"name": "sunny_periods_showers"},
    60: {"name": "cloudy"},
    61: {"name": "overcast"},
    62: {"name": "light_rain"},
    63: {"name": "rain"},
    64: {"name": "heavy_rain"},
    65: {"name": "thunderstorm"},
    70: {"name": "fine_night_1"},
    71: {"name": "fine_night_2-6"},
    72: {"name": "fine_night_7-13"},
    73: {"name": "fine_night_14-17"},
    74: {"name": "fine_night_18-24"},
    75: {"name": "fine_night_25-30"},
    76: {"name": "mainly_cloudy_night"},
    77: {"name": "mainly_fine_night"},
    80: {"name": "windy"},
    81: {"name": "dry"},
    82: {"name": "humid"},
    83: {"name": "fog"},
    84: {"name": "mist"},
    85: {"name": "haze"},
    90: {"name": "hot"},
    91: {"name": "warm"},
    92: {"name": "cool"},
    93: {"name": "cold"},
}
"""HKO Weather icons

:meta hide-value:

Reference: https://www.hoda.gov.hk/textonly/v2/explain/wxicon_e.htm

- ``5x``: sunny/sunny with clouds
- ``6x``: cloudy/rain
- ``7x``: nighttime 
- ``8x``: misc/haze
- ``9x``: temperature
"""
