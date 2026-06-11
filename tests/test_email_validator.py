import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pandas as pd

from validators.email_validator import EmailValidator


def test_valid_email():

    data = pd.DataFrame({
        "email": ["test@gmail.com"]
    })

    validator = EmailValidator()

    errors = validator.validate(data)

    assert len(errors) == 0


def test_invalid_email():

    data = pd.DataFrame({
        "email": ["wrongemail"]
    })

    validator = EmailValidator()

    errors = validator.validate(data)

    assert len(errors) > 0