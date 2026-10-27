# Project Nightfall — Threat Hunting & ATT&CK Investigation Lab

**Investigate the evidence. Map the behaviour. Defend the organisation.**

Project Nightfall is a beginner-friendly, offline-first Streamlit workshop for investigating a fictional incident. It teaches students to distinguish observations from hypotheses, map defensible candidate behaviours to **MITRE ATT&CK Enterprise v15**, test investigation questions, and export an annotated ATT&CK Navigator layer.

> **Safety:** All evidence is synthetic. The application does not connect to real systems, execute log content, send messages, scan targets, or require credentials. It is not production incident-response software.

## Learning objectives

- Build a chronological evidence timeline and identify limitations.
- Formulate testable, evidence-led hypotheses.
- Search and justify ATT&CK v15 candidate mappings without treating them as proof.
- Document alternative explanations and missing telemetry.
- Produce a Navigator-compatible layer and a transparent investigation report.

## Features

The home page and six Streamlit pages cover timeline, evidence search/filter/CSV export, mapping, hypothesis worksheets, D3FEND-oriented recommendations, and report/JSON downloads. Session edits remain in memory for the current browser session.

## Run locally

Prerequisite: Python 3.11+ (tested here with Python 3.12).

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Run tests:

```bash
python -m pytest -q
```

## Student workflow

1. Read the timeline and note which facts are directly observed.
2. Use Evidence Explorer to search records and write observations, alternatives, and missing evidence.
3. In ATT&CK Mapping, select evidence, search the local v15 catalogue, and add a rationale before using `supported`.
4. Test questions in Threat Hunting; leave conclusions blank when unresolved.
5. Add preventive, detective, or response recommendations and link to official [MITRE D3FEND](https://d3fend.mitre.org/).
6. Download the Navigator JSON and report. In [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/), choose **Open Existing Layer** and select the JSON. Verify the layer shows Enterprise ATT&CK version 15.

## Structure

`app.py` is the dashboard; `pages/` contains the workflow; `src/` contains testable business logic; `data/` contains synthetic evidence, hypotheses, and a version-pinned local ATT&CK v15 subset; `tests/` contains offline tests; `docs/` contains workshop guides.

## ATT&CK provenance

The catalogue is explicitly labelled v15 and is a small local subset, not a claim that the complete STIX release is bundled. Its source URL and retrieval metadata are in `data/attack_techniques.json`. This keeps the application usable offline. Technique IDs should be checked against the official [MITRE ATT&CK Enterprise v15](https://attack.mitre.org/versions/v15/techniques/enterprise/) release when extending the catalogue. Navigator export uses the documented layer shape with `domain`, `versions`, `techniques`, scores, colors, and comments.

## Screenshot placeholders

After launch, capture the home timeline, Evidence Explorer, mapping workspace, and export preview and place them in a GitHub README or workshop slides. Screenshots are intentionally not generated in this repository.

## GitHub setup

See [`docs/GITHUB_SETUP.md`](docs/GITHUB_SETUP.md). Do not commit `.env`, virtual environments, caches, or generated exports.

## Troubleshooting

- If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process Bypass`.
- If `streamlit` is not found, activate `.venv` and reinstall requirements with `python -m pip`.
- If a page import fails, launch from the repository root.
- The app requires no network after dependencies are installed; external links are educational references only.

