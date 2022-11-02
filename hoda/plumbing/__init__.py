# hoda.plumbing: lower level api wrapper
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

# this should be the part of the lib that actually interacts with aiohttp and such. if not, i have failed.

from .weather import Weather
from . import http

__all__ = ["Weather", "http"]
