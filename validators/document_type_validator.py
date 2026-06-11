from validators.validation_strategy import BaseValidator


class DocumentTypeValidator(BaseValidator):

    def validate(self, df):

        errors = []

        allowed_document_types = [
            "Passport",
            "Driving Licence",
            "Utility Bill",
            "Bank Statement"
        ]

        for index, row in df.iterrows():

            document_type = str(row["document_type"])

            if document_type not in allowed_document_types:

                errors.append({
                    "row": index,
                    "column": "document_type",
                    "error": "Invalid document type"
                })

        return errors