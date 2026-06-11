from validators.validation_strategy import BaseValidator


class DuplicateValidator(BaseValidator):

    def validate(self, df):

        errors = []

        duplicate_ids = df[df.duplicated("customer_id")]

        for index, row in duplicate_ids.iterrows():

            errors.append({
                "row": index,
                "column": "customer_id",
                "error": "Duplicate customer ID"
            })

        duplicate_emails = df[df.duplicated("email")]

        for index, row in duplicate_emails.iterrows():

            errors.append({
                "row": index,
                "column": "email",
                "error": "Duplicate email"
            })

        return errors