FORBIDDEN_ACTIONS = {
    "fake_clicks",
    "self_referrals",
    "artificial_conversions",
    "provider_bypass",
    "force_payout",
}

def validate_action(action: str) -> None:
    if action in FORBIDDEN_ACTIONS:
        raise PermissionError(f"Blocked action: {action}")
