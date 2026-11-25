"""Entry point: load and check the configuration, then open the app."""

import sys

from src.parsing import load_config
from src.ui.app import App

USAGE = "Usage: python3 pac-man.py config.json"


def main() -> None:
    """Check the arguments, load the configuration and open the window."""
    if len(sys.argv) != 2:
        print(USAGE, file=sys.stderr)
        sys.exit(2)

    config = load_config(sys.argv[1])
    print("Configuration loaded:")
    print(f"  highscore file : {config.highscore_filename}")
    print(f"  lives          : {config.lives}")
    print(f"  level max time : {config.level_max_time}s")
    print(f"  levels         : {len(config.levels)}")
    app = App()
    app.run()


if __name__ == "__main__":
    main()
