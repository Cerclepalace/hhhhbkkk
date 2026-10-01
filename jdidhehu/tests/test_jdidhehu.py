import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import pytest
from jdidhehu.api import start
from jdidhehu.commission import Commission, CommissionStatus

def test_start():
    result = start(100)
    assert result["target_eur"] == 100
    assert result["discovered"] >= 1
    assert result["qualified"] >= 1

def test_invalid_target():
    with pytest.raises(ValueError):
        start(0)

def test_commission_lifecycle():
    c = Commission("c1", "o1", 25)
    c.transition(CommissionStatus.APPROVED, 20)
    c.transition(CommissionStatus.PAYABLE)
    c.transition(CommissionStatus.PAID, 20)
    assert c.paid_amount == 20
