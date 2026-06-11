import pandas as pd


class ReportGenerator:

    @staticmethod
    def generate(errors, output_path):

        report_df = pd.DataFrame(errors)

        report_df.to_excel(
            output_path,
            index=False
        )

        return output_path