# JDIDHEHU

One-Button affiliate orchestration engine.

## Pipeline

CORE -> DISCOVERY -> OFFER -> TRACKING -> COMMISSION -> PAYOUT STATUS -> ONE-BUTTON

## Safety invariants

- No automatic financial transfer.
- No fake clicks.
- No self-referrals.
- No artificial conversions.
- No provider bypass.
- Provider authorization remains external.

## Run

`PYTHONPATH=src python -m pytest -q`

`PYTHONPATH=src python -c "from jdidhehu.api import start; print(start(100))"`
