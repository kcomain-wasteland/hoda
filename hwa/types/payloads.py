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
    """JSON Payload of the Local Weather Forecast Endpoint"""

    generalSituation: str  #: General weather situation
    tcInfo: str  #: Tropical cyclone information
    fireDangerWarning: str  #: Fire danger warning message
    forecastPeriod: str  #: Forecast period
    forecastDesc: str  #: Forecast description
    outlook: str  #: Outlook
    updateTime: str  #: Last update time in ISO format


class SimpleValue(typing.TypedDict):
    value: typing.Union[None, int, float]  #: Value of measurement
    unit: str  #: Unit of the value


class SoilTempPayload(typing.TypedDict):
    """JSON Payload of an item in the ``soilTemp`` list returned by weather forecasts and more.

    It is most likely an error in the weather API as seaTemp, soilTemp and generalSituation
    shouldn't be in the 9 day forecast result.
    """

    place: str  #: Location of the measurement facility
    value: float  #: Temperature of the measured soil
    unit: str  #: Unit of ``value``
    recordTime: str  #: Time of measurement in ISO format
    depth: SimpleValue  #: Depth of the measurement


class ForecastPayload(typing.TypedDict):
    """JSON Payload of a forecast item

    Forecasts can't really be that exact, so text values are returned instead of enums/constants.
    """

    forecastDay: str  #: Day the forecast is about
    week: str  #: Weekday of the forecast
    forecastWind: str  #: Wind forecast
    forecastWeather: str  #: General weather forecast
    forecastMaxtemp: SimpleValue  #: Maximum temperature forecast
    forecastMintemp: SimpleValue  #: Minimum temperature forecast
    forecastMaxrh: SimpleValue  #: Maximum relative humidity forecast
    forecastMinrh: SimpleValue  #: Minimum relative humidity forecast
    ForecastIcon: int  #: weather icons defined at https://fwd.kcomain.dev/urPb

    #: .. important:: Undocumented
    #:     probability of significant rain, see https://fwd.kcomain.dev/hko-psr-post
    PSR: str


class NineDayWeatherForecastPayload(typing.TypedDict):
    """JSON Payload of the 9-Day Weather Forecast Endpoint

    Note that some of the results are undocumented, some are incorrect and in general messy.
    This specification is made according to the API results retrieved at
    ``Fri, 15 Oct 2021 09:31:17 GMT``
    """

    generalSituation: str  #: General weather situation
