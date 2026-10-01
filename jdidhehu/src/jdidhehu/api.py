from .one_button import OneButtonEngine

_engine = OneButtonEngine()

def start(target_eur: float = 100.0) -> dict:
    result = _engine.start(target_eur)
    return {
        "status": "REVIEW",
        "target_eur": target_eur,
        "discovered": result.discovered,
        "qualified": result.qualified,
        "offers": result.offers,
        "actions_required": result.actions_required,
    }
