import pandas as pd
import json

userInput = "Starlights"

excelPath = "clown_companies.csv"
df = pd.read_csv(excelPath)

companyList = [x for x in df['Company Name']]

index = companyList.index(userInput)

name = df['Company Name'][index]
price = df['Price (per hour)'][index]
min = df['Min Hours'][index]
max = df['Max Hours'][index]

result = {}
result["Name"] = f"{name}"
result["Price"] = f"{price}"
result["Min Hours"] = f"{min}"
result["Max Hours"] = f"{max}"

json_result = json.dump(result)

print(result)