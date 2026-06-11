import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pandas as pd

from validators.phone_validator import PhoneValidator


def test_valid_phone():

    data = pd.DataFrame({
        "phone": ["07123456789"]
    })

    validator = PhoneValidator()

    errors = validator.validate(data)

    assert len(errors) == 0


def test_invalid_phone():

    data = pd.DataFrame({
        "phone": ["ABC123"]
    })

    validator = PhoneValidator()

    errors = validator.validate(data)

    assert len(errors) > 0