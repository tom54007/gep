from .models import Annual_data, Prov_Annual_data, ImportFile_excel
from work.models import Province, Area

import pandas as pd
from pandas import DataFrame

eg_list = ['原煤','洗精煤','焦炭','型煤','其他焦化产品','原油','燃料油','汽油','柴油','煤油','液化石油气','炼厂干气','石脑油','沥青','润滑油','石油焦','天然气','水泥','钢铁','农地','林地','畜牧地','渔场','建设用地']
economic_list_area = ['地区当年生产总值','地区当年播种面积','地区当年总人口','地区当年能源消费总量','地区当年二氧化碳排放量','地区当年用水总量','地区当年总面积','地区当年生态足迹','地区当年基本养老保险职工人数','地区当年基本医疗保险人数','地区当年失业保险人数','小学人数','初中人数','高中人数','大学及以上人数',]
economic_list_prov = ['地区当年生产总值','地区当年播种面积','地区当年总人口','地区当年总发电量','地区当年能源消费总量','地区当年二氧化碳排放量','地区当年用水总量','地区当年总面积','地区当年生态足迹','地区当年基本养老保险职工人数','地区当年基本医疗保险人数','地区当年失业保险人数','地区当年核电发电量','地区当年风电发电量','地区当年水电发电量','地区当年光伏发电量','小学人数','初中人数','高中人数','大学及以上人数',]
eg_sheet_name = "二氧化碳和生态足迹的数据"
economic_sheet_name = "地区相关发展数据"



# 定义数据表读取解析函数
# def takedata(filename, arealevel, province, year):
#     df = pd.read_excel('市级2017原始数据测试.xlsx', sheet_name="二氧化碳和生态足迹的数据", header=[0,1])
#     df = df.set_index(df.columns[0])
#     df = df.stack(level=0).stack(level=0).reset_index()
#     df.columns = list(df.columns[1:].insert(0, 'Resources'))
#     this_year = df[df['level_2']=='当期值']
#     k = this_year[this_year['level_1']=='南京'][this_year['Resources']=='型煤']
#     if len(k)==0:
#         print('none')
#     else:
#         print('有')
def takedata(filename, arealevel, province, year):
# 判断数据级别：省级/市级
    ## 若为省级，则更新省级数据库数据
    if arealevel == 'province':
        print('省级数据'+province)
    ## 若为市级则通过循环更新对应地区的数据库数据
    elif arealevel == 'area':
        get_area = Area.objects.filter(province__name=province)
        area_list = []
        for i in get_area:
            # 加入各个地区的名称
            print(i.name)
        




# 查询对应省份下的全部地区==》为列表
