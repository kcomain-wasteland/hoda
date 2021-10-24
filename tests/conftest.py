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
import os

import pytest
from xprocess import ProcessStarter


__filedir__ = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def testserver(xprocess):
    class Starter(ProcessStarter):
        # pattern = r"I\* test-server started"
        pattern = r" \* Running on http://127\.0\.0\.1:5000/ \(Press CTRL\+C to quit\)"
        popen_kwargs = {"cwd": __filedir__}

        args = ["flask", "run"]

    logfile = xprocess.ensure("test-server", Starter)
    yield "http://localhost:5000"

    xprocess.getinfo("test-server").terminate()
