import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pandas as pd

from validators.document_type_validator import DocumentTypeValidator


def test_valid_document_type():

    data = pd.DataFrame({
        "document_type": ["Passport"]
    })

    validator = DocumentTypeValidator()

    errors = validator.validate(data)

    assert len(errors) == 0


def test_invalid_document_type():

    data = pd.DataFrame({
        "document_type": ["Random Document"]
    })

    validator = DocumentTypeValidator()

    errors = validator.validate(data)

    assert len(errors) > 0