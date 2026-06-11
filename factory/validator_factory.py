from validators.required_column_validator import RequiredColumnValidator
from validators.missing_value_validator import MissingValueValidator
from validators.email_validator import EmailValidator
from validators.phone_validator import PhoneValidator
from validators.customer_id_validator import CustomerIDValidator
from validators.customer_name_validator import CustomerNameValidator
from validators.document_type_validator import DocumentTypeValidator
from validators.duplicate_validator import DuplicateValidator
from validators.document_validator import DocumentValidator


class ValidatorFactory:

    @staticmethod
    def create_validators():

        return [
            RequiredColumnValidator(),
            MissingValueValidator(),
            EmailValidator(),
            PhoneValidator(),
            CustomerIDValidator(),
            CustomerNameValidator(),
            DocumentTypeValidator(),
            DuplicateValidator(),
            DocumentValidator()
        ]