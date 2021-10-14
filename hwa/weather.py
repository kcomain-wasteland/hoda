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
#  GNU LesserGeneral Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import requests

from .models import LocalWeatherForecast
from .types.params import Language, _LANG


class Weather:
    """
    This is a wrapper for the Weather Information API as described in the
    HKO Open Data API Documentation.

    As the endpoint support multiple languages, you may specify the desired language with
    the lang parameter on class init, so that you can use the same language for subsequent
    requests without having to specify the language.

    The default language is English.

    :param lang: Language, see :class:`hwa.types.Language`
    """

    BASE: str = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
    lang: _LANG = "en"

    def __init__(self, lang: _LANG = "en") -> None:
        self.lang = lang
        return

    def forecast_local(self, lang=None) -> LocalWeatherForecast:
        """
        Get current local weather forecast

        :param lang: Language
        """
