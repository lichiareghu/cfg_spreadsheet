def calculate_sales(data):
    #print(data)
    total_sales = []
    for row in data:
        if row == 'sales':
            return list(data[row]),data[row].sum()

import pandas as pd
data = pd.read_csv('D:\CFG_Spreadsheet\cfg_spreadsheet\sales.csv')
print(calculate_sales(data))