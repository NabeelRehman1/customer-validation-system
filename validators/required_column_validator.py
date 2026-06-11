from validators.validation_strategy import BaseValidator


class RequiredColumnValidator(BaseValidator):

    def validate(self, df):

        errors = []

        required_columns = [
            "customer_id",
            "customer_name",
            "email",
            "phone",
            "document_type",
            "document_id",
            "document_name",
            "upload_date"
        ]

        for column in required_columns:

            if column not in df.columns:

                errors.append({
                    "row": "N/A",
                    "column": column,
                    "error": "Required column missing"
                })

        return errors