from validators.validation_strategy import BaseValidator


class CustomerIDValidator(BaseValidator):

    def validate(self, df):

        errors = []

        for index, row in df.iterrows():

            customer_id = str(row["customer_id"]).strip()

            if len(customer_id) < 8:

                errors.append({
                    "row": index,
                    "column": "customer_id",
                    "error": "Customer ID too short"
                })

            elif len(customer_id) > 12:

                errors.append({
                    "row": index,
                    "column": "customer_id",
                    "error": "Customer ID too long"
                })

            if not customer_id.startswith("CUST"):

                errors.append({
                    "row": index,
                    "column": "customer_id",
                    "error": "Customer ID must start with CUST"
                })

        return errors