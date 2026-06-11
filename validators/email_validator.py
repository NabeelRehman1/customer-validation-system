from validators.validation_strategy import BaseValidator


class EmailValidator(BaseValidator):

    def validate(self, df):

        errors = []

        for index, row in df.iterrows():

            email = str(row["email"])

            if "@" not in email or "." not in email:

                errors.append({
                    "row": index,
                    "column": "email",
                    "error": "Invalid email format"
                })

        return errors