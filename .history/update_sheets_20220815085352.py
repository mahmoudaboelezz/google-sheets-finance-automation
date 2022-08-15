import sheets_utility as su
from data_loader import get_data
from spreadsheetid import SPREADSHEET_ID


if __name__ == "__main__":
    service = su.create_authorized_service()
    # su.create_sheet(service)
    try:
        sid = SPREADSHEET_ID
    except:
        sid = "Enter your spreadsheet id here"

    data = get_data()

    su.update_values(service, sid, data)
    su.format_cells(service, sid, 0)
    su.create_pivot_table(service, sid, 0, data)

    print("Created sheets data successfully")
