import gspread
import time
import datetime
from oauth2client.service_account import ServiceAccountCredentials
from envirophat import light, weather

# Google Drive sheets key
SHEET_ID = '<# ADD KEY #>'

# DO NOT modify lines below this line
# Downloaded service account json file name
CLIENT_JSON_FILENAME = 'client.json'

# Unit for the barometer
BAROMETER_UNIT = 'hPa'

# Minutes between measurements and sync attemps.
MINUTES_BETWEEN_SYNCS = 15

# Authentication scopes. Drive is required to update the document
SCOPES = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Syncs the local measurement with the Google Drive sheet
def sync():
    # Authorize
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CLIENT_JSON_FILENAME, SCOPES)
    gc = gspread.authorize(credentials)

    # Open a worksheet by id
    worksheet = gc.open_by_key(SHEET_ID).sheet1

    # Get new column number
    row_number = len(worksheet.get_all_values()) + 1
    
    # Append row
    # 3. Temp in Degree Celsius
    # 4. Air pressure in hPa
    # 5. Illumination in Lumens
    worksheet.update_cell(row_number, 1, formatted_now_long())
    worksheet.update_cell(row_number, 2, weather.temperature())
    worksheet.update_cell(row_number, 3, weather.pressure(unit=BAROMETER_UNIT))
    worksheet.update_cell(row_number, 4, light.light())

# Gets a long formatted now date as string.
def formatted_now_long():
    now = datetime.datetime.now()
    return (now.strftime("%d.%m.%Y %H:%M"))

# Gets a a short formatted time from now as string.
def formatted_time_now():
    now = datetime.datetime.now()
    return (now.strftime("%H:%M:%S"))

# Main method
if __name__ == '__main__':
    cycle = 1
    while True:
        print("---")
        print("Processing cycle: %s at %s" % (cycle, formatted_time_now()))
        sync()
        time.sleep(MINUTES_BETWEEN_SYNCS * 60)
        cycle += 1