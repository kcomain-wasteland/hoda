#  Copyright (c) 2021 kcomain
#
#  This file is part of hwa.
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

import typing


class LocalWeatherForecastPayload(typing.TypedDict):
    generalSituation: str  #: General weather situation
    tcInfo: str  #: Tropical cyclone information
    fireDangerWarning: str  #: Fire danger warning message
    forecastPeriod: str  #: Forecast period
    forecastDesc: str  #: Forecast description
    outlook: str  #: Outlook
    updateTime: str  #: Last update time in ISO format
