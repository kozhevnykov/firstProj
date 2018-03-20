import pandas as pd
import xlsxwriter

data = pd.read_excel("All_clients.xlsx")

for manager_name in set(data['Manager_name']):
    temp = data[data["Manager_name"] == manager_name].drop(['Manager_name'], axis = 1)
    file_name = str(manager_name) + ".xlsx"
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    temp.to_excel(writer, index=False, sheet_name='report')
    writer.save()


