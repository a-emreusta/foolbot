import pygsheets
import pandas as pd

class GSpreadsheet():

    def __init__(self):
        self.open_connection()

    def open_connection(self):
        self.pyg_object = pygsheets.authorize(service_account_env_var='GDRIVE_AUTHENTICATION')
        self.sh = self.pyg_object.open('Discord Test')
        self.wks = self.sh[0]

    def get_all_records(self):
        return pd.DataFrame(self.wks.get_all_records())

    def insert_items(self, message_list):
        row_nums = len(self.wks.get_all_records())
        self.wks.insert_rows(row=row_nums+1, number=1, values=message_list)

    def delete_items(self, commands):
        self.wks.delete_rows(index=int(commands[0]), number=int(commands[1]))