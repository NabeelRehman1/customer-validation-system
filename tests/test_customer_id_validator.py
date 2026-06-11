import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pandas as pd

from validators.customer_id_validator import CustomerIDValidator


def test_valid_customer_id():

    data = pd.DataFrame({
        "customer_id": ["12345678"]
    })

    validator = CustomerIDValidator()

    errors = validator.validate(data)

    assert len(errors) == 0


def test_short_customer_id():

    data = pd.DataFrame({
        "customer_id": ["123"]
    })

    validator = CustomerIDValidator()

    errors = validator.validate(data)

    assert len(errors) > 0