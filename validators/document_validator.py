from validators.validation_strategy import BaseValidator


class DocumentValidator(BaseValidator):

    def validate(self, df):

        errors = []

        for index, row in df.iterrows():

            document_id = str(row["document_id"])

            if document_id.strip() == "":

                errors.append({
                    "row": index,
                    "column": "document_id",
                    "error": "Missing document ID"
                })

            document_name = str(row["document_name"])

            if document_name.strip() == "":

                errors.append({
                    "row": index,
                    "column": "document_name",
                    "error": "Missing document name"
                })

        return errors