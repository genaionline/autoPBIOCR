from util.pbi_util import UtilPBI

# Ensure the config.ini file has the correct Power BI link
# You can set it programmatically if needed
# config = configparser.ConfigParser()
# config.read('config/config.ini')
# config.set('PowerBI', 'link', 'http://your-valid-power-bi-link')
# with open('config/config.ini', 'w') as configfile:
#     config.write(configfile)



# Connect to Power BI
UtilPBI.connect_pbi()

# Define the dictionary with the specified key-value pairs
filters = {
    "period": "2025-03",
    "market": "SG"
}

# Export the dashboard to a PDF
UtilPBI.export_to_pdf("output.pdf", filters)





