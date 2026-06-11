from factory.validator_factory import ValidatorFactory


class ValidationFacade:

    def __init__(self):

        self.validators = ValidatorFactory.create_validators()

    def validate(self, df):

        all_errors = []

        for validator in self.validators:

            errors = validator.validate(df)

            all_errors.extend(errors)

        return all_errors