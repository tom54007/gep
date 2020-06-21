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
economic_list_prov = [
    ('GDP','地区生产总值'),
    ('Sown_area','地区播种面积'),
    ('Total_population','地区总人口'),
    ('The_total_area','地区总面积'),
    ('Total_power_generation','地区总发电量'),
    ('Total_energy_consumption','能源消费总量'),
    ('Total_water_consumption','用水总量'),
    ('Number_of_employees_in_basic_pension_insurance','基本养老保险职工人数'),
    ('Number_of_basic_medical_insurance','基本医疗保险人数'),
    ('Number_of_unemployment_insurance','失业保险人数'),
    ('Nuclear_power_generation','核电发电量'),
    ('Wind_power_generation','风电发电量'),
    ('Hydropower_generation','水电发电量'),
    ('Photovoltaic_power_generation','光伏发电量'),
    ('Primary_school_number','小学人数'),
    ('Number_of_junior_high_school','初中人数'),
    ('High_school_number','高中人数'),
    ('University_and_above','大学及以上人数')
]
read_items_name = [
    ('r_d','规模以上工业企业R&D经费'),
    ('rural_urban','乡-城人均年收入'),
    ('urban_per','城镇居民可支配收入'),
    ('rural_per','农村居民可支配收入'),
    ('garbage','生活垃圾无害化处理率'),
    ('bus_per','平均每万人拥有公交车辆'),
    ('urban_sewage','城镇生活污水集中处理率'),
    ('mortality','死亡率'),
    ('pm25','PM2.5年平均浓度'),
    ('so2_emissions','二氧化硫排放量'),
    ('cod_emissions','化学需氧量排放量'),
    ('nh_emissions','氨氮排放量')
]
read_prov_items_name = [
    ('r_d','企业R&D内部经费支出'),
    ('rural_urban','乡-城人均年收入'),
    ('urban_per','城镇居民平均可支配收入'),
    ('rural_per','农村居民平均可支配收入'),
    ('garbage','生活垃圾无害化处理率'),
    ('bus_per','平均每万人拥有公交车辆'),
    ('urban_sewage','城镇生活污水集中处理率'),
    ('mortality','死亡率'),
    ('pm25','PM2.5年平均浓度'),
    ('so2_emissions','二氧化硫排放量'),
    ('cod_emissions','化学需氧量排放量'),
    ('nh_emissions','氨氮排放量')
]



eg_sheet_name = "二氧化碳和生态足迹的数据"
economic_sheet_name = "地区相关发展数据"
already_item_sheet_name = "无计算所得指标数据"


# 定义单项计算公式
## 定义正向指标计算公式
def item_calc_positive(last_value, this_value, maxvalue):
    change_value = this_value - last_value
    weight_value = maxvalue / last_value
    process_value = (this_value-last_value)/(maxvalue-last_value)
    item_score = process_value * weight_value
    return (item_score, weight_value)

## 定义反向指标计算公式
def item_calc_negative(last_value, this_value, minvalue):
    change_value = last_value - this_value
    weight_value = last_value / minvalue
    process_value = (this_value-last_value)/(minvalue-last_value)
    item_score = process_value * weight_value
    return (item_score, weight_value)


# 定义数据表读取解析函数

def takedata(filename, arealevel, province, year):
    # 解析二氧化碳和生态足迹的数据的数据表
    df = pd.read_excel(filename, sheet_name=eg_sheet_name, header=[0,1])
    df = df.set_index(df.columns[0])
    df = df.stack(level=0).stack(level=0).reset_index()
    df.columns = list(df.columns[1:].insert(0, 'Resources'))
    this_year = df[df['level_2']=='当期值']
    last_year = df[df['level_2']=='前期值']
    print(this_year)
    # 解析地区相关发展数据的数据表
    df_dev = pd.read_excel(filename, sheet_name=economic_sheet_name, header=[0,1])
    df_dev = df_dev.set_index(df_dev.columns[0])
    df_dev = df_dev.stack(level=0).stack(level=0).reset_index()
    df_dev.columns = list(df_dev.columns[1:].insert(0, 'city'))
    this_year_dev = df_dev[df_dev['level_2']=='当期值']
    last_year_dev = df_dev[df_dev['level_2']=='前期值']
    print(this_year_dev)
    # 解析无需计算所得的各项单项基础指标
    df_item = pd.read_excel(filename, sheet_name=already_item_sheet_name, header=[0,1,2])
    df_item = df_item.set_index(df_item.columns[0])
    df_item = df_item.stack(level=0).stack(level=0).reset_index()
    df_item.columns = list(df_item.columns[1:].insert(0, 'city'))
    print(df_item)
    # this_year_item = df_item[df_item['city']=='南京'][df_item['level_2']==read_items_name[0][1]]['前期值']
    # this_year_item.values[0]
    # print(this_year_item)
    # 判断数据级别：省级/市级
    ## 若为省级，则更新省级数据库数据
    if arealevel == 'province':
        get_database = Prov_Annual_data.objects.filter(province=province, year=year)
        # 加入省份的名称
        k = this_year
        k_dev = this_year_dev
        k_items = df_item
        items = []
        print(province)
        print(k)
        # print(to_database)
        for m in read_prov_items_name:
            prov_item_each = df_item[df_item['city']==str(province)][df_item['level_2']==m[1]]['当期值']
            print(prov_item_each)
            if len(prov_item_each)==0:
                the_each = 0
            else:
                the_each = prov_item_each.values[0]
            print(the_each)
            items.append([m[0], the_each])
        for m in eg_list:
            area_eg_each = k[k['Resources']==m[1]]
            if len(area_eg_each)==0:
                the_each = 0
            else:
                the_each = area_eg_each[0].values[0]
            print(the_each)
            items.append([m[0], the_each])
        for m in economic_list_prov:
            area_dev_each = k_dev[k_dev['level_1']==m[1]]
            if len(area_dev_each)==0:
                the_each = 0
            else:
                the_each = area_dev_each[0].values[0]
            print(the_each)
            items.append([m[0], the_each])
        if len(get_database)==0:
            items.append(['province',province])
            items.append(['year',year])
            updatabase = dict(items)
            Prov_Annual_data.objects.create(**updatabase)
        else:
            updatabase = dict(items)
            Prov_Annual_data.objects.filter(province=province, year=year).update(**updatabase)
    ## 若为市级则通过循环更新对应地区的数据库数据
    # this_year_item = df_item[df_item['city']=='南京'][df_item['level_2']==read_items_name[0][1]]['前期值']
    # this_year_item.values[0]
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
            for m in read_items_name:
                area_item_each = df_item[df_item['city']==i.name][df_item['level_2']==m[1]]['当期值']
                if len(area_item_each)==0:
                    the_each = 0
                else:
                    the_each = area_item_each.values[0]
                print(the_each)
                items.append([m[0], the_each])
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

# 写入前期值
def takedata_lastyear(filename, arealevel, province, year):
    year = year - 1
    # 解析二氧化碳和生态足迹的数据的数据表
    df = pd.read_excel(filename, sheet_name=eg_sheet_name, header=[0,1])
    df = df.set_index(df.columns[0])
    df = df.stack(level=0).stack(level=0).reset_index()
    df.columns = list(df.columns[1:].insert(0, 'Resources'))
    last_year = df[df['level_2']=='前期值']
    print(last_year)
    # 解析地区相关发展数据的数据表
    df_dev = pd.read_excel(filename, sheet_name=economic_sheet_name, header=[0,1])
    df_dev = df_dev.set_index(df_dev.columns[0])
    df_dev = df_dev.stack(level=0).stack(level=0).reset_index()
    df_dev.columns = list(df_dev.columns[1:].insert(0, 'city'))
    last_year_dev = df_dev[df_dev['level_2']=='前期值']
    print(last_year)
    # 解析无需计算所得的各项单项基础指标
    df_item = pd.read_excel(filename, sheet_name=already_item_sheet_name, header=[0,1,2])
    df_item = df_item.set_index(df_item.columns[0])
    df_item = df_item.stack(level=0).stack(level=0).reset_index()
    df_item.columns = list(df_item.columns[1:].insert(0, 'city'))
    print(df_item)
    # this_year_item = df_item[df_item['city']=='南京'][df_item['level_2']==read_items_name[0][1]]['前期值']
    # this_year_item.values[0]
    # print(this_year_item)
    # 判断数据级别：省级/市级
    ## 若为省级，则更新省级数据库数据
    if arealevel == 'province':
        get_database = Prov_Annual_data.objects.filter(province=province, year=year)
        # 加入省份的名称
        k = last_year
        k_dev = last_year_dev
        k_items = df_item
        items = []
        print(province)
        print(k)
        # print(to_database)
        for m in read_prov_items_name:
            prov_item_each = df_item[df_item['city']==str(province)][df_item['level_2']==m[1]]['前期值']
            print(prov_item_each)
            if len(prov_item_each)==0:
                the_each = 0
            else:
                the_each = prov_item_each.values[0]
            print(the_each)
            items.append([m[0], the_each])
        for m in eg_list:
            area_eg_each = k[k['Resources']==m[1]]
            if len(area_eg_each)==0:
                the_each = 0
            else:
                the_each = area_eg_each[0].values[0]
            print(the_each)
            items.append([m[0], the_each])
        for m in economic_list_prov:
            area_dev_each = k_dev[k_dev['level_1']==m[1]]
            if len(area_dev_each)==0:
                the_each = 0
            else:
                the_each = area_dev_each[0].values[0]
            print(the_each)
            items.append([m[0], the_each])
        if len(get_database)==0:
            items.append(['province',province])
            items.append(['year',year])
            updatabase = dict(items)
            Prov_Annual_data.objects.create(**updatabase)
        else:
            updatabase = dict(items)
            Prov_Annual_data.objects.filter(province=province, year=year).update(**updatabase)
    ## 若为市级则通过循环更新对应地区的数据库数据
    # this_year_item = df_item[df_item['city']=='南京'][df_item['level_2']==read_items_name[0][1]]['前期值']
    # this_year_item.values[0]
    elif arealevel == 'area':
        get_area = Area.objects.filter(province__name=province)
        get_database = Annual_data.objects.filter(province=province, year=year)
        annual_data = Annual_data()
        area_list = []
        for i in get_area:
            # 加入各个地区的名称
            k = last_year[last_year['level_1']==i.name]
            k_dev = last_year_dev[last_year_dev['city']==i.name]
            to_database = get_database.filter(area=i.name)
            items = []
            # print(to_database)
            for m in read_items_name:
                area_item_each = df_item[df_item['city']==i.name][df_item['level_2']==m[1]]['前期值']
                if len(area_item_each)==0:
                    the_each = 0
                else:
                    the_each = area_item_each.values[0]
                print(the_each)
                items.append([m[0], the_each])
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
