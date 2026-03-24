# ffmpeg-frame-extractor-api

REST API to extract frames at timestamps.

## Overview
This repository is a small but legitimate FFmpeg-focused MVP. It uses local `ffmpeg` / `ffprobe` binaries, keeps defaults conservative, and avoids destructive behavior.

## Features
- Purpose-built CLI/service for this repository's use-case
- Safe-by-default workflow and explicit outputs
- Minimal codebase that is easy to extend
- Uses FFmpeg/ffprobe via subprocess or exec wrappers

## Requirements
- FFmpeg and ffprobe in `PATH`
- Python 3.11+

## Setup
```bash
cd ffmpeg-frame-extractor-api
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

## Usage Examples
```bash
python3 app.py --help
```


## Docker Compose
This repo includes a `compose.yml` setup so you can run the tool with FFmpeg and Python already installed inside the container.

### What the container includes
- Python 3.11
- `ffmpeg` and `ffprobe` from the Debian package
- Project dependencies from `requirements.txt`

### Build
```bash
docker compose build
```

### Default behavior
```bash
docker compose run --rm ffmpeg-tool
```
The default container command prints the tool help, so you can override it with the exact `python app.py ...` command you want.

### Example
```bash
curl -X POST http://localhost:8000/extract -H 'content-type: application/json' -d '{"input_path":"/data/input/sample.mp4","timestamp":"00:00:03"}' --output frame.jpg
```

For API usage, put media under `./data` so it appears inside the container at `/data`.
The API listens on port `8000`.

### Notes
- The container image already provides `ffmpeg` / `ffprobe`, so you do not need them installed on the host.
- Bind-mounted paths in examples use container paths such as `/data/...` and `/output/...`.
- For long-running services, use `docker compose up -d` and `docker compose logs -f`.

## Configuration
- Prefer CLI flags for one-off runs
- Some repos include `config.example.json` for future extension
- Review paths and outputs before long-running jobs

## Output Notes
- Outputs are only written to the files/directories you specify
- Logs go to stdout/stderr unless the tool documents otherwise

## Limitations
- MVP-sized implementation, not a full media platform
- Assumes local FFmpeg availability
- Some advanced workflows are intentionally simplified

## Safety Notes
- Test against sample media first
- Prefer dry-run mode when available
- Validate input URLs and destination paths before long jobs
