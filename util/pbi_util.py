import configparser
from powerbiclient import (
    Report,
    models,
    PowerBIClient,
    Authentication,
    Uri,
)
from powerbiclient.auth import DeviceCodeAuth

class UtilPBI:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config/config.ini')

    @staticmethod
    def connect_pbi():
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        try:
            link = config.get('PowerBI', 'link')
            # Simulate connection logic
            if not link or link == '<your_power_bi_link_here>':
                raise ValueError("Invalid Power BI link.")
            print(f"Connected to Power BI using link: {link}")

            # Initialize the Power BI client
            pbi_client = PowerBIClient(authentication=Authentication(DeviceCodeAuth()))
            # Authenticate using device code flow
            # A browser window will open, and you will be asked to sign in to Power BI
            pbi_client.auth.authenticate()
        except Exception as e:
            print(f"Error connecting to Power BI: {e}")

    @staticmethod
    def export_to_pdf(pdf_file, filters):
        # Simulate export logic
        print(f"Exporting dashboard to {pdf_file} with filters: {filters}")
        # Here you would add the actual logic to export the dashboard to a PDF
        # This could involve using a library to interact with Power BI and generate a PDF
        # Get a list of all workspaces
        workspaces = pbi_client.workspaces.get_workspaces()
        print("Workspaces:", workspaces)
        # Get all reports in a workspace (replace with your workspace ID)
        workspace_id = "your-workspace-id"
        reports = pbi_client.reports.get_reports(workspace_id)
        print("Reports:", reports)
        # Get data from a report (replace with your report ID)
        report_id = "your-report-id"
        report = pbi_client.reports.get_report(workspace_id, report_id)
        print("Report Details:", report)
        
        print("Export successful.")


    def export_option2(self):
        # Get a list of all workspaces
        workspaces = self.pbi_client.workspaces.get_workspaces()
        print("Workspaces:", workspaces)
        # Get all reports in a workspace (replace with your workspace ID)
        workspace_id = "your-workspace-id"      

        #refer to this link for more details
        #https://learn.microsoft.com/en-us/rest/api/power-bi/reports/export-to-file
        


if __name__ == "__main__":
    UtilPBI.connect_pbi()
    UtilPBI.export_to_pdf("output.pdf", {"filter_key": "filter_value"}) 

