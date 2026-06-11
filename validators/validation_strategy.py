class BaseValidator:

    def validate(self, df):
        raise NotImplementedError(
            "Each validator must implement the validate method."
        )