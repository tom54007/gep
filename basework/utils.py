from .models import Annual_data, Prov_Annual_data, ImportFile_excel
from work.models import Province, Area

import pandas as pd
from pandas import DataFrame

eg_list = [
    ('Consume_Raw_coal','原煤'),
    ('Consume_Clean_coal','洗精煤'),
    ('Consume_Coke','焦炭'),
    ('Consume_Briquette','型煤'),
    ('Consume_Other_coking_products','其他焦化产品'),
    ('Consume_Crude','原油'),
    ('Consume_Fuel_oil','燃料油'),
    ('Consume_Gasoline','汽油'),
    ('Consume_Diesel','柴油'),
    ('Consume_Kerosene','煤油'),
    ('Consume_Liquefied_petroleum_gas','液化石油气'),
    ('Consume_Refinery_dry_gas','炼厂干气'),
    ('Consume_Naphtha','石脑油'),
    ('Consume_Asphalt','沥青'),
    ('Consume_Lubricating_oil','润滑油'),
    ('Consume_Petroleum_coke','石油焦'),
    ('Consume_Natural_gas','天然气'),
    ('Consume_Cement','水泥'),
    ('Consume_Steel','钢铁'),
    ('Consume_Farmland','农地'),
    ('Consume_Woodland','林地'),
    ('Consume_Pastureland','畜牧地'),
    ('Consume_Fishing_ground','渔场'),
    ('Consume_Construction_land','建设用地')
]

economic_list_area = [
    ('GDP','地区生产总值'),
    ('Sown_area','地区播种面积'),
    ('Total_population','地区总人口'),
    ('Total_energy_consumption','能源消费总量'),
    ('Total_water_consumption','用水总量'),
    ('The_total_area','地区总面积'),
    ('Number_of_employees_in_basic_pension_insurance','基本养老保险职工人数'),
    ('Number_of_basic_medical_insurance','基本医疗保险人数'),
    ('Number_of_unemployment_insurance','失业保险人数'),
    ('Primary_school_number','小学人数'),
    ('Number_of_junior_high_school','初中人数'),
    ('High_school_number','高中人数'),
    ('University_and_above','大学及以上人数')
]
economic_list_prov = ['地区当年生产总值','地区当年播种面积','地区当年总人口','地区当年总发电量','地区当年能源消费总量','地区当年用水总量','地区当年总面积','地区当年生态足迹','地区当年基本养老保险职工人数','地区当年基本医疗保险人数','地区当年失业保险人数','地区当年核电发电量','地区当年风电发电量','地区当年水电发电量','地区当年光伏发电量','小学人数','初中人数','高中人数','大学及以上人数',]
eg_sheet_name = "二氧化碳和生态足迹的数据"
economic_sheet_name = "地区相关发展数据"



# 定义数据表读取解析函数

def takedata(filename, arealevel, province, year):
    # 解析二氧化碳和生态足迹的数据的数据表
    df = pd.read_excel(filename, sheet_name=eg_sheet_name, header=[0,1])
    df = df.set_index(df.columns[0])
    df = df.stack(level=0).stack(level=0).reset_index()
    df.columns = list(df.columns[1:].insert(0, 'Resources'))
    this_year = df[df['level_2']=='当期值']
    last_year = df[df['level_2']=='前期值']
    # 解析地区相关发展数据的数据表
    df_dev = pd.read_excel(filename, sheet_name=economic_sheet_name, header=[0,1])
    df_dev = df_dev.set_index(df_dev.columns[0])
    df_dev = df_dev.stack(level=0).stack(level=0).reset_index()
    df_dev.columns = list(df_dev.columns[1:].insert(0, 'city'))
    this_year_dev = df_dev[df_dev['level_2']=='当期值']
    last_year_dev = df_dev[df_dev['level_2']=='前期值']
# 判断数据级别：省级/市级
    ## 若为省级，则更新省级数据库数据
    if arealevel == 'province':
        print('省级数据'+province)
    ## 若为市级则通过循环更新对应地区的数据库数据
    elif arealevel == 'area':
        get_area = Area.objects.filter(province__name=province)
        get_database = Annual_data.objects.filter(province=province, year=year)
        annual_data = Annual_data()
        area_list = []
        for i in get_area:
            # 加入各个地区的名称
            k = this_year[this_year['level_1']==i.name]
            k_dev = this_year_dev[this_year_dev['city']==i.name]
            to_database = get_database.filter(area=i.name)
            items = []
            # print(to_database)
            for m in eg_list:
                area_eg_each = k[k['Resources']==m[1]]
                if len(area_eg_each)==0:
                    the_each = 0
                else:
                    the_each = area_eg_each[0].values[0]
                print(the_each)
                items.append([m[0], the_each])
            for m in economic_list_area:
                area_dev_each = k_dev[k_dev['level_1']==m[1]]
                if len(area_dev_each)==0:
                    the_each = 0
                else:
                    the_each = area_dev_each[0].values[0]
                print(the_each)
                items.append([m[0], the_each])
            if len(to_database)==0:
                items.append(['province',province])
                items.append(['area',i.name])
                items.append(['year',year])
                updatabase = dict(items)
                Annual_data.objects.create(**updatabase)
            else:
                updatabase = dict(items)
                Annual_data.objects.filter(province=province, area=i.name, year=year).update(**updatabase)

        




# 查询对应省份下的全部地区==》为列表
