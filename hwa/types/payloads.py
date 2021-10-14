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
    generalSituation: str
    tcInfo: str
    fireDangerWarning: str
    forecastPeriod: str  # why this?????? why not a range of time at least not some tangible text that i have to do natural language processing
    forecastDesc: str
