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

import requests


class Earthquake:
    """
    This is a wrapper for the Earthquake Information API as described in the
    HKO Open Data API Documentation.

    As the endpoint support multiple languages, you may specify the desired language with
    the lang parameter on class init, so that you can use the same language for subsequent
    requests without having to specify the language. The default language currently is English.

    :param lang: Language
    """

    BASE: str = "https://data.weather.gov.hk/weatherAPI/opendata/earthquake.php"

    def __init__(self, lang="en") -> None:
        self.lang = lang
        return
