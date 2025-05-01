import os
import sys
from setproctitle import setproctitle

from quack_norris.common.config import read_config


def ui(config=None):
    from quack_norris.ui.app import main as _create_ui

    setproctitle("quack-norris-ui")
    if config is None:
        config = read_config("config.json", overwrites=sys.argv[1:])

    exit_code = _create_ui(config=config)
    sys.exit(exit_code)


def main():
    if sys.argv[1] == "--blocking":
        ui()
    else:
        args = ' '.join(sys.argv[1:])
        if os.name == 'nt':  # Windows
            os.system(f"start /b pythonw -m quack_norris_ui {args}")
        else:  # Linux/Unix/Mac
            os.system(f"python -m quack_norris_ui {args} &")


if __name__ == "__main__":
    ui()
