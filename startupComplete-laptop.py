# Startup Complete: Simple command line tool to let you know
#                   when your PC's ready to go.
# Copyright (C) 2023  Foxie EdianiaK a.k.a. F_TEK

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import subprocess
import platform
from alive_progress import alive_bar

print("""Startup Complete  Copyright (C) 2023  Foxie EdianiaK a.k.a. F_TEK
This program comes with ABSOLUTELY NO WARRANTY. This is free software,
and you are welcome to redistribute it under certain conditions.
For more details refer to the LICENSE file in the GitHub repository."""
      + "\n" * 4)


LOADED = True

IDLE_TIME = 6
IDLE_LOAD = 30

COMPUTER_NAME = platform.node()
if COMPUTER_NAME != "":
    COMPUTER_NAME = "'" + COMPUTER_NAME.upper() + "'"
else:
    COMPUTER_NAME = "COMPUTER"

print(COMPUTER_NAME + " STARTUP IN PROGRESS...")


def get_load() -> int:
    load = subprocess.check_output("wmic cpu get loadpercentage", shell=True)
    try:
        load = int(load.split()[1])
    except IndexError:
        return "NoValueError"
    except ValueError:
        return "NoValueError"
    else:
        return load


def show_load():
    _idle_time = 0
    with alive_bar(IDLE_TIME, theme="classic") as bar:
        while _idle_time < IDLE_TIME:
            _load = get_load()
            if _load == "NoValueError":
                pass
            elif _load <= IDLE_LOAD:
                _idle_time += 1
                bar()
            else:
                return True
        return False


while LOADED:
    LOADED = show_load()

input("\n\nStartup complete!\nPress ENTER to exit...")
