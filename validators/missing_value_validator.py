from validators.validation_strategy import BaseValidator


class MissingValueValidator(BaseValidator):

    def validate(self, df):

        errors = []

        important_columns = [
            "customer_id",
            "customer_name",
            "email"
        ]

        for column in important_columns:

            missing_count = df[column].isnull().sum()

            if missing_count > 0:

                errors.append({
                    "row": "N/A",
                    "column": column,
                    "error": f"{missing_count} missing values found"
                })

        return errors