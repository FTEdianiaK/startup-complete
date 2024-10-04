import subprocess
import platform
from alive_progress import alive_bar


LOADED = True

IDLE_TIME = 6
IDLE_LOAD = 20

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
