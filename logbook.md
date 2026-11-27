# Logbook — Pac-Man "Ghosts! More ghosts!"

## Team

- jbordelli
- ajeloyan

Task split, agreed at the start after both of us shared our understanding of the subject:

- jbordelli: `config.json` parsing, in-game maze display, ghost AI
- ajeloyan: application window and interface, main menu, in-game gameplay (controls and movement)
- Shared: project setup, structure, MLX constraint review (to confirm)

## Roadmap

Status: **Done**, **In progress**, **To check** (written but not tested yet), **To do**.
Difficulty: **Easy**, **Medium**, **Hard**. This is a rough guide: a Hard task can be simplified if time runs short, and the note column says how.
Owner: jbordelli, ajeloyan, or both. "to confirm" means we still need to agree on it.

### Phase 0 — Setup

| # | Action | Owner | Status | Difficulty | Note |
|---|--------|-------|--------|------------|------|
| 1 | Read the subject and share our understanding | both | Done | Easy | |
| 2 | Split the tasks | both | Done | Easy | |
| 3 | Set up venv, uv, pyproject, Makefile, .gitignore | to confirm | Done | Easy | |
| 4 | Integrate the mazegenerator wheel, unmodified | to confirm | Done | Medium | path in `[tool.uv.sources]` |
| 5 | Keep the logbook up to date | both | In progress | Easy | |

### Phase 1 — Configuration

| # | Action | Owner | Status | Difficulty | Note |
|---|--------|-------|--------|------------|------|
| 6 | Parse `config.json`, skip `#` comment lines | jbordelli | Done | Medium | |
| 7 | Validate values, warn without crashing | jbordelli | Done | Medium | accepts `"42"` |
| 8 | Handle missing or invalid file cleanly | jbordelli | To check | Medium | |
| 9 | Document config keys and defaults in README | to confirm | To do | Easy | |

### Phase 2 — Window and drawing

| # | Action | Owner | Status | Difficulty | Note |
|---|--------|-------|--------|------------|------|
| 10 | Launcher `pac-man.py` and `src/` structure | ajeloyan | Done | Easy | |
| 11 | Application window | ajeloyan | Done | Easy | |
| 12 | Bitmap font and pixel drawing (`canvas.py`, `font.py`) | jbordelli | Done | Medium | no `pygame.font` |
| 13 | Check that every pygame call is MLX-equivalent | both | To check | Medium | list them in README |

### Phase 3 — Menu

| # | Action | Owner | Status | Difficulty | Note |
|---|--------|-------|--------|------------|------|
| 14 | Main menu: START GAME, HIGHSCORES, INSTRUCTIONS, QUIT | ajeloyan | In progress | Medium | |
| 15 | Instructions screen | ajeloyan | To do | Easy | |
| 16 | Highscores screen | ajeloyan | To do | Easy | needs #31 |

### Phase 4 — Level

| # | Action | Owner | Status | Difficulty | Note |
|---|--------|-------|--------|------------|------|
| 17 | Generate and display the maze | jbordelli | Done | Medium | |
| 18 | Show the level number over the maze | jbordelli | Done | Easy | |
| 19 | Pac-gums and super pac-gums on the board | jbordelli | To do | Medium | logic in `game/pellets.py` |
| 20 | Win the level when all pac-gums are eaten | to confirm | To do | Easy | needs #19 |
| 21 | HUD: score, lives, time left | to confirm | To do | Easy | uses the font |
| 22 | Decide what happens when the timer runs out | to confirm | To do | Easy | subject leaves it open |

### Phase 5 — Player

| # | Action | Owner | Status | Difficulty | Note |
|---|--------|-------|--------|------------|------|
| 23 | Player movement and wall collisions | ajeloyan | Done | Medium | to confirm |
| 24 | Smooth movement (interpolation, held keys) | ajeloyan | Done | Hard | |
| 25 | Death, lost life, respawn | ajeloyan | To do | Medium | |

### Phase 6 — Ghosts

| # | Action | Owner | Status | Difficulty | Note |
|---|--------|-------|--------|------------|------|
| 26 | Ghost AI, four personalities | jbordelli | Done | Hard | logic only, tests to add |
| 27 | Draw ghosts, with chase, frightened and eaten modes | jbordelli | To do | Medium | |
| 28 | Collisions between player and ghosts | both | To do | Medium | |
| 29 | BFS pathing around walls | jbordelli | To do | Hard | optional, the limit is documented |

### Phase 7 — Score and highscores

| # | Action | Owner | Status | Difficulty | Note |
|---|--------|-------|--------|------------|------|
| 30 | Score: pac-gum, super pac-gum, ghost | to confirm | To do | Easy | |
| 31 | Save and load highscores as JSON, robust to file errors | to confirm | To check | Medium | |
| 32 | Name entry: 10 characters max, alphanumeric and spaces | to confirm | To do | Medium | |

### Phase 8 — Game flow

| # | Action | Owner | Status | Difficulty | Note |
|---|--------|-------|--------|------------|------|
| 33 | Next level keeps score and lives | to confirm | To do | Medium | |
| 34 | Game over and win screens | to confirm | To do | Medium | |
| 35 | Pause menu (P): resume or back to menu | to confirm | To do | Easy | |
| 36 | At least 10 levels, first one from seed 42 | to confirm | To do | Easy | |
| 37 | Cheat mode: invincibility, level skip, ghost freeze, extra lives, speed | both | To do | Medium | for peer review |

### Phase 9 — Quality

| # | Action | Owner | Status | Difficulty | Note |
|---|--------|-------|--------|------------|------|
| 38 | pytest tests on the game logic | both | To do | Medium | |
| 39 | flake8 and mypy pass | both | To do | Easy | |
| 40 | Makefile: install, run, debug, clean, lint | to confirm | To check | Easy | |
| 41 | Complete `.gitignore` (`dist/`, `*.egg-info/`, `highscore.json`) | to confirm | To do | Easy | |

### Phase 10 — Documentation and delivery

| # | Action | Owner | Status | Difficulty | Note |
|---|--------|-------|--------|------------|------|
| 42 | README: sections required by the subject, AI usage declared | both | To do | Medium | |
| 43 | Acceptance test plan: features tested, bugs found and fixed | both | To do | Medium | |
| 44 | Packaging script or spec at repo root, unlisted build on Itch.io or Steam | both | To do | Hard | needs a working game first |
| 45 | In-package instructions: controls, options, configuration | both | To do | Easy | |

---

## How to use

One entry per work session, most recent at the bottom. Each entry answers five questions: who did it, what was done, what was decided, what blocked us and how we solved it, what was tested. Dates to be filled in.

Template to copy for each session:

```
## YYYY-MM-DD — short title
- Who:
- Done:
- Decided:
- Blocked / solution:
- Tested:
- Next step:
```

---

## (date to fill in) — Shared understanding and task split
- Who: jbordelli, ajeloyan
- Done: read the subject together, shared our understanding of it, split the tasks (see Team above).
- Decided: split as listed above.
- Blocked / solution: none.
- Tested: not applicable.
- Next step: start the individual tasks.

## (date to fill in) — Configuration parsing
- Who: jbordelli
- Done: full parsing of `config.json`: comment lines (`#`) skipped, values checked against bounds, warnings for non-conforming values without crashing.
- Decided: no `logging` module (project requirement), warnings written with `print(..., file=sys.stderr)`. Identifiers in English. Numeric strings such as `"42"` are accepted.
- Blocked / solution: a typo in a key (`"livse"`) went through silently. Added a check for unknown keys. Several typos and indentation errors in the first drafts, fixed.
- Tested: valid `config.json` loads without warnings; wrong values are reported without crashing.
- Next step: application interface.

## (date to fill in) — Project setup and mazegenerator integration
- Who: (to confirm)
- Done: venv created with `uv`, `pyproject.toml`, `Makefile`, `.gitignore`, `.python-version` (3.14). Wheel `mazegenerator-2.1.0-py3-none-any.whl` placed at the root and declared with `[tool.uv.sources]`. Studied how it works: `maze[y][x]`, walls N=1, E=2, S=4, W=8, "42" pillar = 15.
- Decided: `uv` for dependencies, `pygame-ce` as the graphics library. The wheel is not modified. Its package README is wrong (`width=`/`height=` raises a TypeError), so we follow the actual code.
- Blocked / solution: `uv sync` failed with "Expected a Python module at src/pacman/__init__.py". Solution: `[tool.uv] package = false`, removed `[build-system]` and `[project.scripts]`. Then "Distribution not found at vendor/…": the path in `pyproject.toml` did not match the wheel at the root. Fixed.
- Tested: `uv sync` passes; maze generated from a test script.
- Next step: configuration parsing.

## (date to fill in) — Project structure
- Who: (to confirm)
- Done: code moved into `src/`, `pac-man.py` reduced to a three-line launcher, game logic separated from drawing (`game/` and `ui/`).
- Decided: `game/` never imports pygame, only `ui/` does. This lets logic tests run without a window.
- Blocked / solution: `ImportError: attempted relative import with no known parent package` when the code was pasted into `pac-man.py`. Solution: startup code moved into `src/main.py`, and the launcher only calls `main()`.
- Tested: `make run` starts the program.
- Next step: application interface.

## (date to fill in) — Application interface
- Who: ajeloyan
- Done: application window and interface built.
- Decided: window and drawing limited to pygame functions equivalent to the MLX.
- Blocked / solution: (to fill in)
- Tested: (to fill in)
- Next step: main menu.

## (date to fill in) — Main menu
- Who: ajeloyan
- Status: in progress.
- Done: menu being built, with `START GAME`, `HIGHSCORES`, `INSTRUCTIONS`, `QUIT`.
- Decided: (to fill in)
- Blocked / solution: (to fill in)
- Tested: (to fill in)
- Next step: in-game maze display.

## (date to fill in) — In-game maze display
- Who: jbordelli
- Done: maze generated from the configuration and displayed in the game window.
- Decided: walls drawn once into a surface, then copied to the screen each frame.
- Blocked / solution: outer walls were clipped by the window edge. Added a 4-pixel margin.
- Tested: maze fully visible for the first level. (to confirm for the others)
- Next step: in-game gameplay.

## (date to fill in) — In-game gameplay
- Who: ajeloyan
- Done: player movement and keyboard controls.
- Decided: keys tracked with `KEYDOWN` and `KEYUP`, movement drawn with interpolation between cells.
- Blocked / solution: movement was jerky (one cell at a time, key read only on press). Fixed with interpolation and held-key tracking.
- Tested: continuous movement with the keyboard. (to confirm)
- Next step: ghost AI.

## (date to fill in) — Ghost AI
- Who: jbordelli
- Done: four ghosts, each with its own personality. Blinky chases the player, Pinky aims four cells ahead of the player, Inky is computed from Blinky's position, Clyde chases from afar and retreats when close. Modes: chase, frightened, eaten.
- Decided: greedy movement (pick the direction that gets closest to the target). Simple, but it ignores walls.
- Blocked / solution: `TypeError` on `Ghost(... kind=...)` because the `kind` field was missing from the dataclass. Added.
- Known limitation: Manhattan distance ignores walls. A BFS (breadth-first search) would fix this, planned for later.
- Tested: target tests planned in `tests/test_targets.py`. (to confirm)
- Next step: (to fill in)

## (date to fill in) — MLX constraint
- Who: (shared, to confirm)
- Done: the subject allows only pygame functions equivalent to the MLX. Calls replaced: `pygame.draw` by our own pixel drawing functions (`ui/canvas.py`), `pygame.key.get_pressed` by held-key tracking, `pygame.time.Clock` by `time.monotonic`, `pygame.font` by our own bitmap font (`ui/font.py`).
- Decided: pygame-ce kept for the window, surfaces and events, and nothing else.
- Tested: (to fill in, check with the evaluator if needed)

## (date to fill in) — Score, lives, highscores
- Who: (to confirm)
- Done: score, lives and time shown in the HUD (top information bar). Highscores saved as JSON (10 entries maximum, names up to 10 ASCII characters). A ghost collision costs a life.
- Decided: lives reset at each level for now.
- Blocked / solution: (to fill in)
- Tested: (to fill in)
- Next step: (to fill in)

---

## (date to fill in) — Level display in the app
- Who: jbordelli
- Status: in progress.
- Done: (to fill in)
- Decided: (to fill in)
- Blocked / solution: (to fill in)
- Tested: (to fill in)
- Next step: (to fill in)

## Notes
- AI assistance: Claude (Anthropic) was used to explain concepts and draft parts of the code. This must be declared in the README, as the subject requires.

## Old to-do list (replaced by the Roadmap above)
- Win condition: no pac-gums left on the board.
- Level progression keeping lives and score.
- Pause menu (P key).
- BFS for ghosts.
- Logic tests with pytest (`tests/`).
- Fill in `README.md` (sections required by the subject).
- Complete `.gitignore`: `dist/`, `*.egg-info/`, `highscore.json`.
