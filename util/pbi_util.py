import configparser
import os
from powerbiclient.authentication import DeviceCodeLoginAuthentication
from powerbiclient import Report, models


class UtilPBI:
    def __init__(self):
        self.config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), '../config/config.ini')
        self.config.read(config_path)
        self.client = None

    @staticmethod
    def connect_pbi():
        # Refer to this: https://github.com/microsoft/powerbi-jupyter/blob/main/demo/Embed%20Power%20BI%20report%20demo.ipynb
        
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), '../config/config.ini')
        config.read(config_path)
        try:
            link = config.get('PowerBI', 'link')
            if not link:
                raise ValueError("Invalid Power BI link.")
            print(f"Connected to Power BI using link: {link}")

            device_auth = DeviceCodeLoginAuthentication()
            
            group_id = "e5122c64-1bae-4c59-85ce-35484f92f8df"
            report_id = "2f91863f-3a73-4edf-b74b-f011f0debd4e"

            report = Report(group_id=group_id, report_id=report_id, auth=device_auth)

            if report is not None:
                print("Authentication successful")
            else:
                print(f"Authentication failed.")
                return None

        except Exception as e:
            print(f"Error connecting to Power BI: {e}")
            return None

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
        #https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-url-filters
        
        


if __name__ == "__main__":
    UtilPBI.connect_pbi()
    #UtilPBI.export_to_pdf("output.pdf", {"filter_key": "filter_value"}) 

