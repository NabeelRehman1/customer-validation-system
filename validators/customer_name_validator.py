from validators.validation_strategy import BaseValidator


class CustomerNameValidator(BaseValidator):

    def validate(self, df):

        errors = []

        for index, row in df.iterrows():

            customer_name = str(row["customer_name"])

            if customer_name != customer_name.strip():

                errors.append({
                    "row": index,
                    "column": "customer_name",
                    "error": "Leading or trailing spaces"
                })

            if len(customer_name) < 2:

                errors.append({
                    "row": index,
                    "column": "customer_name",
                    "error": "Customer name too short"
                })

            elif len(customer_name) > 50:

                errors.append({
                    "row": index,
                    "column": "customer_name",
                    "error": "Customer name too long"
                })

        return errors