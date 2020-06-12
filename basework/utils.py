from .models import Annual_data, Prov_Annual_data, ImportFile_excel

import pandas as pd
from pandas import DataFrame

# 定义数据表读取解析函数
def takedata(filename, arealevel, province, year):
    df = pd.read_excel('市级2017原始数据测试.xlsx', sheet_name="二氧化碳和生态足迹的数据", header=[0,1])
    df = df.set_index(df.columns[0])
    df = df.stack(level=0).stack(level=0).reset_index()
    df.columns = list(df.columns[1:].insert(0, 'Resources'))
    this_year = df[df['level_2']=='当期值']
    k = this_year[this_year['level_1']=='南京'][this_year['Resources']=='型煤']
    if len(k)==0:
        print('none')
    else:
        print('有')