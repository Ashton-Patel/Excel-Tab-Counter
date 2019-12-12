import pandas as pd
import numpy as np
import openpyxl
import os

final_df = pd.DataFrame({'File Name':[],'tabCount':[]})

for i in os.listdir():
    try:
        xl = pd.ExcelFile(i)
        res = len(xl.sheet_names)
    except:
        if i.split(".")[-1] not in ['xlsx','xls','xlsb','csv']:
            res = "Not an Excel"
        else:
            res = "Corrupt or Unsafe"
    final_df = final_df.append({'File Name':i,'tabCount':res}, ignore_index=True)
    print(i," | | ",res)