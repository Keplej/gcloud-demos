from googleapiclient.discovery import build
from google.oauth2 import service_account

class GoogleServices():
    """Parent Class that intergrates Google Cloud Services using different APIs and Services.

    SERVICE_ACCOUNT : Service account json key

    SCOPES : Google Scopes depending on service

    credentials : Service Account Credentials 

    service : Google service build
    """
    def __init__(self, SERVICE_ACCOUNT, SCOPES):
        self.SCOPES = SCOPES
        self.SERVICE_ACCOUNT = SERVICE_ACCOUNT
        self.credentials = self._get_credentials()
        self.service = None
    
    def _get_credentials(self):
        credentials = service_account.Credentials.from_service_account_file(
            self.SERVICE_ACCOUNT, scopes=self.SCOPES)
        print("Credentials obtained successfully.")
        return credentials
    
    def build_service(self, service_name, version):
        """service_name : Google Service you are using e.g. 
        
        sheets=google sheets
        
        gmail=google mail
        """
        self.service = build(service_name, version, credentials=self.credentials)
        return self.service

class GoogleSheets(GoogleServices):
    def __init__(self, SERVICE_ACCOUNT, SCOPES):
        super().__init__(SERVICE_ACCOUNT, SCOPES)
        self.build_service('sheets', 'v4')

    # Add methods specific to Google Sheets
    def read_sheet(self, spreadsheet_id, range_name):
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id, range=range_name).execute()
            return result.get('values', [])
        except Exception as e:
            print(f"An error occurred while reading the sheet: {e}")
            return None
    
    def write_sheet(self, spreadsheet_id, range_name, values):
        """
        Append data to a Google Sheet

        :param values: List of lists representing rows of data to append
        """
        body = {
            "values": values
        }
        try:
            result = self.service.spreadsheets().values().append(spreadsheetId=spreadsheet_id,
                range=range_name, valueInputOption='USER_ENTERED', 
                body=body).execute()
            return result
        except Exception as e:
            print(f"Error has occurred while writing to the sheet: {e}")
            return None
        
    def clear_sheet(self, spreadsheet_id, range_name):
        try:
            result = self.service.spreadsheets().values().clear(
                spreadsheetId=spreadsheet_id,
                range=range_name).execute()
            print(f"Cleared range {range_name} in spreadsheet {spreadsheet_id}")
            return result
        except Exception as e:
            print(f"Error has occurred while clearing the sheet: {e}")
            return None

class GoogleMail(GoogleServices):
    pass