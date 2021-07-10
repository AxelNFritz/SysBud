from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)



SPREADSHEET_ID = '1tiqsUAUDFrv36zFThLZxIFdOaAQ4UR9_LVmqlB0cPr0'


def main():

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range='A2:G10').execute()   #W20089
  
    values = result.get('values', [])
    print(values)

if __name__ == '__main__':
    main()