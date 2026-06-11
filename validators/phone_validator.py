from validators.validation_strategy import BaseValidator


class PhoneValidator(BaseValidator):

    def validate(self, df):

        errors = []

        for index, row in df.iterrows():

            phone = str(row["phone"])

            if not phone.isdigit():

                errors.append({
                    "row": index,
                    "column": "phone",
                    "error": "Invalid phone number"
                })

            if len(phone) < 10:

                errors.append({
                    "row": index,
                    "column": "phone",
                    "error": "Phone number too short"
                })

            elif len(phone) > 15:

                errors.append({
                    "row": index,
                    "column": "phone",
                    "error": "Phone number too long"
                })

        return errors