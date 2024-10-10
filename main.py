from google_services import GoogleSheets
from dotenv import load_dotenv
import os

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT = os.getenv('SERVICE_ACCOUNT')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

def read_sheet_values(service_account, scopes, spreadhseet_id, range_name):
    """Fetches values from a Google Sheet
    
    :param service_account: Path to the service account JSON file
    :param scopes: List of OAuth 2.0 scopes
    :param spreadsheet_id: ID of the spreadsheet to read from
    :param range_name: Range name (A1 notation) to read
    :return: Values from the specified range
    """
    sheets_service = GoogleSheets(SERVICE_ACCOUNT, SCOPES)
    response = sheets_service.read_sheet(spreadhseet_id, range_name)
    return response

def write_sheet_values(service_account, scopes, spreadhseet_id, range_name, values):
    sheet_service = GoogleSheets(SERVICE_ACCOUNT, SCOPES)
    response = sheet_service.write_sheet(spreadhseet_id, range_name, values)
    return response

def clear_sheet_values(service_account, scopes, spreadhseet_id, range_name):
    sheet_service = GoogleSheets(SERVICE_ACCOUNT, SCOPES)
    response = sheet_service.clear_sheet(spreadhseet_id, range_name)
    return response


if __name__ == "__main__":

    data = [
        ["Mike", "$200.00", "$0.00"],
        ["Eric", "$50.00", "$25.50"]
    ]

    clear_sheet_values(SERVICE_ACCOUNT, SCOPES, SPREADSHEET_ID, 'test!A2:C13')
    write_sheet_values(SERVICE_ACCOUNT, SCOPES, SPREADSHEET_ID, 'test!A1', data)
    # read = read_sheet_values(SERVICE_ACCOUNT, SCOPES, SPREADSHEET_ID, 'test!A1:C3')
    # print(read)