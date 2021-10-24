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
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
import time

from flask import Flask

app = Flask("test-server")
print("I* test-server started")


@app.route("/")
def root():
    text = "<i>Base route: /weatherAPI/opendata/</i>"
    text += "<h1>Available routes</h1>"
    text += '<a href="/weatherAPI/opendata/weather.php">/weather.php</a>'
    return text


@app.route("/test/sleep")
def sleeptest():
    time.sleep(5)
    return "", 204
