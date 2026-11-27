Logbook — Pac-Man "Ghosts! More ghosts!"
Team
jbordeli
ajeloyan

Task split, agreed at the start after both of us shared our understanding of the subject:

jbordelli: config.json parsing, in-game maze display, ghost AI
ajeloyan: application window and interface, main menu, in-game gameplay (controls and movement)
Shared: project setup, structure, MLX constraint review (to confirm)
How to use

One entry per work session, most recent at the bottom. Each entry answers five questions: who did it, what was done, what was decided, what blocked us and how we solved it, what was tested. Dates to be filled in.

Shared understanding and task split
Who: jbordeli, ajeloyan
Done: read the subject together, shared our understanding of it, split the tasks (see Team above).
Decided: split as listed above.
Blocked / solution: none.
Tested: not applicable.
Next step: start the individual tasks.

Configuration parsing
Who: jbordeli
Done: full parsing of config.json: comment lines (#) skipped, values checked against bounds, warnings for non-conforming values without crashing.
Decided: no logging module (project requirement), warnings written with print(..., file=sys.stderr). Identifiers in English. Numeric strings such as "42" are accepted.
Blocked / solution: a typo in a key ("livse") went through silently. Added a check for unknown keys. Several typos and indentation errors in the first drafts, fixed.
Tested: valid config.json loads without warnings; wrong values are reported without crashing.
Next step: application interface.

Project setup and mazegenerator integration
Who: ajeloyan
Done: venv created with uv, pyproject.toml, Makefile, .gitignore, .python-version (3.14). Wheel mazegenerator-2.1.0-py3-none-any.whl placed at the root and declared with [tool.uv.sources]. Studied how it works: maze[y][x], walls N=1, E=2, S=4, W=8, "42" pillar = 15.
Decided: uv for dependencies, pygame-ce as the graphics library. The wheel is not modified. Its package README is wrong (width=/height= raises a TypeError), so we follow the actual code.
Blocked / solution: uv sync failed with "Expected a Python module at src/pacman/init.py". Solution: [tool.uv] package = false, removed [build-system] and [project.scripts]. Then "Distribution not found at vendor/…": the path in pyproject.toml did not match the wheel at the root. Fixed.
Tested: uv sync passes; maze generated from a test script.
Next step: configuration parsing.
