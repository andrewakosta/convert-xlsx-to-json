import excel2json

# excel2json.convert_from_file('customers.xlsx')

import pandas


def getJsonData(name, sheet):
    data = pandas.read_excel(name, sheet_name=sheet)
    dataAsJson = data.to_json()
    return dataAsJson

    
print(getJsonData("customers.xlsx", "Sheet1"))
