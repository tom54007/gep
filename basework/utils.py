from .models import Annual_data, Prov_Annual_data, ImportFile_excel
from work.models import Province, Area

import pandas as pd
import numpy as np
from pandas import DataFrame
from django.forms.models import model_to_dict
from basework import models

eg_list = [
    ('Consume_Raw_coal', '原煤'),
    ('Consume_Clean_coal', '洗精煤'),
    ('Consume_Coke', '焦炭'),
    ('Consume_Briquette', '型煤'),
    ('Consume_Other_coking_products', '其他焦化产品'),
    ('Consume_Crude', '原油'),
    ('Consume_Fuel_oil', '燃料油'),
    ('Consume_Gasoline', '汽油'),
    ('Consume_Diesel', '柴油'),
    ('Consume_Kerosene', '煤油'),
    ('Consume_Liquefied_petroleum_gas', '液化石油气'),
    ('Consume_Refinery_dry_gas', '炼厂干气'),
    ('Consume_Naphtha', '石脑油'),
    ('Consume_Asphalt', '沥青'),
    ('Consume_Lubricating_oil', '润滑油'),
    ('Consume_Petroleum_coke', '石油焦'),
    ('Consume_Natural_gas', '天然气'),
    ('Consume_Cement', '水泥'),
    ('Consume_Steel', '钢铁'),
    ('Consume_Farmland', '农地'),
    ('Consume_Woodland', '林地'),
    ('Consume_Pastureland', '畜牧地'),
    ('Consume_Fishing_ground', '渔场'),
    ('Consume_Construction_land', '建设用地')
]

economic_list_area = [
    ('GDP', '地区生产总值'),
    ('Sown_area', '地区播种面积'),
    ('Total_population', '地区总人口'),
    ('Total_energy_consumption', '能源消费总量'),
    ('Total_water_consumption', '用水总量'),
    ('The_total_area', '地区总面积'),
    ('Number_of_employees_in_basic_pension_insurance', '基本养老保险职工人数'),
    ('Number_of_basic_medical_insurance', '基本医疗保险人数'),
    ('Number_of_unemployment_insurance', '失业保险人数'),
    ('Primary_school_number', '小学人数'),
    ('Number_of_junior_high_school', '初中人数'),
    ('High_school_number', '高中人数'),
    ('University_and_above', '大学及以上人数')
]
economic_list_prov = [
    ('GDP', '地区生产总值'),
    ('Sown_area', '地区播种面积'),
    ('Total_population', '地区总人口'),
    ('The_total_area', '地区总面积'),
    ('Total_power_generation', '地区总发电量'),
    ('Total_energy_consumption', '能源消费总量'),
    ('Total_water_consumption', '用水总量'),
    ('Number_of_employees_in_basic_pension_insurance', '基本养老保险职工人数'),
    ('Number_of_basic_medical_insurance', '基本医疗保险人数'),
    ('Number_of_unemployment_insurance', '失业保险人数'),
    ('Nuclear_power_generation', '核电发电量'),
    ('Wind_power_generation', '风电发电量'),
    ('Hydropower_generation', '水电发电量'),
    ('Photovoltaic_power_generation', '光伏发电量'),
    ('Primary_school_number', '小学人数'),
    ('Number_of_junior_high_school', '初中人数'),
    ('High_school_number', '高中人数'),
    ('University_and_above', '大学及以上人数')
]
read_items_name = [
    ('r_d', '规模以上工业企业R&D经费'),
    ('rural_urban', '乡-城人均年收入'),
    ('urban_per', '城镇居民可支配收入'),
    ('rural_per', '农村居民可支配收入'),
    ('garbage', '生活垃圾无害化处理率'),
    ('bus_per', '平均每万人拥有公交车辆'),
    ('urban_sewage', '城镇生活污水集中处理率'),
    ('mortality', '死亡率'),
    ('pm25', 'PM2.5年平均浓度'),
    ('so2_emissions', '二氧化硫排放量'),
    ('cod_emissions', '化学需氧量排放量'),
    ('nh_emissions', '氨氮排放量')
]
read_prov_items_name = [
    ('r_d', '企业R&D内部经费支出'),
    ('rural_urban', '乡-城人均年收入'),
    ('urban_per', '城镇居民平均可支配收入'),
    ('rural_per', '农村居民平均可支配收入'),
    ('garbage', '生活垃圾无害化处理率'),
    ('bus_per', '平均每万人拥有公交车辆'),
    ('urban_sewage', '城镇生活污水集中处理率'),
    ('mortality', '死亡率'),
    ('pm25', 'PM2.5年平均浓度'),
    ('so2_emissions', '二氧化硫排放量'),
    ('cod_emissions', '化学需氧量排放量'),
    ('nh_emissions', '氨氮排放量')
]
prov_item_target_name_list = [
    ('renewable_energy_per_target','可再生能源供给占比目标值'),
    ('per_unit_gdp_target','单位GDP能耗目标值'),
    ('water_per_gdp_target','单位GDP用水量目标值'),
    ('water_per_target','人均用水量目标值'),
    ('pension_cov_target','养老保险覆盖率目标值'),
    ('medical_cov_target','医疗保险覆盖率目标值'),
    ('unemployment_cov_target','失业保险覆盖率目标值'),
    ('planting_area_target','播种面积占比目标值'),
    ('edu_years_target','平均受教育年限目标值'),
    ('co2_per_gdp_target','单位GDP二氧化碳排放量目标值'),
    ('ef_per_target','人均生态足迹目标值'),
    ('r_d_target','企业R&D内部经费支出目标值'),
    ('urban_per_target','城镇居民平均可支配收入目标值'),
    ('rural_per_target','农村居民平均可支配收入目标值'),
    ('rural_urban_target','乡-城人均年收入目标值'),
    ('garbage_target','生活垃圾无害化处理率目标值'),
    ('bus_per_target','平均每万人拥有公交车辆目标值'),
    ('urban_sewage_target','城镇生活污水集中处理率目标值'),
    ('mortality_target','死亡率目标值'),
    ('pm25_target','PM2.5年平均浓度目标值'),
    ('so2_emissions_target','二氧化硫排放量目标值'),
    ('cod_emissions_target','化学需氧量排放量目标值'),
    ('nh_emissions_target','氨氮排放量目标值')
]

eg_sheet_name = "二氧化碳和生态足迹的数据"
economic_sheet_name = "地区相关发展数据"
already_item_sheet_name = "无计算所得指标数据"
item_target_sheet_name = "单项指标目标值"


# 定义单项计算公式
# 定义正向指标计算公式

def item_calc_positive(last_value, this_value, maxvalue):
    change_value = this_value - last_value
    weight_value = maxvalue / last_value
    if (maxvalue - last_value) == 0:
        process_value = 1
    else:
        process_value = (this_value - last_value) / (maxvalue - last_value)
    item_score = process_value * weight_value
    return item_score, weight_value


# 定义反向指标计算公式
def item_calc_negative(last_value, this_value, minvalue):
    change_value = last_value - this_value
    weight_value = last_value / minvalue
    if (minvalue - last_value) == 0:
        process_value = 1
    else:
        process_value = (this_value - last_value) / (minvalue - last_value)
    item_score = process_value * weight_value
    return item_score, weight_value


# 定义数据表读取解析函数

def takedata(filename, arealevel, province, year):
    # 解析二氧化碳和生态足迹的数据的数据表
    df = pd.read_excel(filename, sheet_name=eg_sheet_name, header=[0, 1])
    df = df.set_index(df.columns[0])
    df = df.stack(level=0).stack(level=0).reset_index()
    df.columns = list(df.columns[1:].insert(0, 'Resources'))
    this_year = df[df['level_2'] == '当期值']
    last_year = df[df['level_2'] == '前期值']
    print(this_year)
    # 解析地区相关发展数据的数据表
    df_dev = pd.read_excel(filename, sheet_name=economic_sheet_name, header=[0, 1])
    df_dev = df_dev.set_index(df_dev.columns[0])
    df_dev = df_dev.stack(level=0).stack(level=0).reset_index()
    df_dev.columns = list(df_dev.columns[1:].insert(0, 'city'))
    this_year_dev = df_dev[df_dev['level_2'] == '当期值']
    last_year_dev = df_dev[df_dev['level_2'] == '前期值']
    print(this_year_dev)
    # 解析无需计算所得的各项单项基础指标
    df_item = pd.read_excel(filename, sheet_name=already_item_sheet_name, header=[0, 1, 2])
    df_item = df_item.set_index(df_item.columns[0])
    df_item = df_item.stack(level=0).stack(level=0).reset_index()
    df_item.columns = list(df_item.columns[1:].insert(0, 'city'))
    print(df_item)
    # this_year_item = df_item[df_item['city']=='南京'][df_item['level_2']==read_items_name[0][1]]['前期值']
    # this_year_item.values[0]
    # print(this_year_item)
    # 判断数据级别：省级/市级
    # 若为省级，则更新省级数据库数据
    if arealevel == 'province':
        get_database = Prov_Annual_data.objects.filter(province=province, year=year)
        # 加入省份的名称
        k = this_year
        k_dev = this_year_dev
        k_items = df_item
        items = []
        # print(to_database)
        # 获取目标值
        get_target_sheet = pd.read_excel(filename, sheet_name=item_target_sheet_name, header=[0])
        get_target_sheet = get_target_sheet.set_index(get_target_sheet.columns[0])
        get_target_sheet = get_target_sheet.stack(level=0).reset_index()
        get_target_sheet.columns = list(get_target_sheet.columns[1:].insert(0, 'targetvalue'))
        print(get_target_sheet)
        for m in prov_item_target_name_list:
            prov_item_target_each = get_target_sheet[get_target_sheet['targetvalue']==m[1]][0]
            print("目标值",m[1],prov_item_target_each)
            if len(prov_item_target_each) == 0:
                the_each = 0
            else:
                the_each = prov_item_target_each.values[0]
            print("目标值",m[0],the_each)
            items.append([m[0], the_each])
        for m in read_prov_items_name:
            prov_item_each = df_item[df_item['city'] == str(province)][df_item['level_2'] == m[1]]['当期值']
            print(prov_item_each)
            if len(prov_item_each) == 0:
                the_each = 0
            else:
                the_each = prov_item_each.values[0]
            print(the_each)
            items.append([m[0], the_each])
        for m in eg_list:
            area_eg_each = k[k['Resources'] == m[1]]
            if len(area_eg_each) == 0:
                the_each = 0
            else:
                the_each = area_eg_each[0].values[0]
            print(the_each)
            items.append([m[0], the_each])
        for m in economic_list_prov:
            area_dev_each = k_dev[k_dev['level_1'] == m[1]]
            if len(area_dev_each) == 0:
                the_each = 0
            else:
                the_each = area_dev_each[0].values[0]
            print(the_each)
            items.append([m[0], the_each])
        if len(get_database) == 0:
            items.append(['province', province])
            items.append(['year', year])
            updatabase = dict(items)
            Prov_Annual_data.objects.create(**updatabase)
        else:
            updatabase = dict(items)
            Prov_Annual_data.objects.filter(province=province, year=year).update(**updatabase)
    # 若为市级则通过循环更新对应地区的数据库数据
    # this_year_item = df_item[df_item['city']=='南京'][df_item['level_2']==read_items_name[0][1]]['前期值']
    # this_year_item.values[0]
    elif arealevel == 'area':
        get_area = Area.objects.filter(province__name=province)
        get_database = Annual_data.objects.filter(province=province, year=year)
        annual_data = Annual_data()
        area_list = []
        for i in get_area:
            # 加入各个地区的名称
            k = this_year[this_year['level_1'] == i.name]
            k_dev = this_year_dev[this_year_dev['city'] == i.name]
            to_database = get_database.filter(area=i.name)
            items = []
            # print(to_database)
            for m in read_items_name:
                area_item_each = df_item[df_item['city'] == i.name][df_item['level_2'] == m[1]]['当期值']
                if len(area_item_each) == 0:
                    the_each = 0
                else:
                    the_each = area_item_each.values[0]
                print(the_each)
                items.append([m[0], the_each])
            for m in eg_list:
                area_eg_each = k[k['Resources'] == m[1]]
                if len(area_eg_each) == 0:
                    the_each = 0
                else:
                    the_each = area_eg_each[0].values[0]
                print(the_each)
                items.append([m[0], the_each])
            for m in economic_list_area:
                area_dev_each = k_dev[k_dev['level_1'] == m[1]]
                if len(area_dev_each) == 0:
                    the_each = 0
                else:
                    the_each = area_dev_each[0].values[0]
                print(the_each)
                items.append([m[0], the_each])
            if len(to_database) == 0:
                items.append(['province', province])
                items.append(['area', i.name])
                items.append(['year', year])
                updatabase = dict(items)
                Annual_data.objects.create(**updatabase)
            else:
                updatabase = dict(items)
                Annual_data.objects.filter(province=province, area=i.name, year=year).update(**updatabase)


# 写入前期值
def takedata_lastyear(filename, arealevel, province, year):
    year = year - 1
    # 解析二氧化碳和生态足迹的数据的数据表
    df = pd.read_excel(filename, sheet_name=eg_sheet_name, header=[0, 1])
    df = df.set_index(df.columns[0])
    df = df.stack(level=0).stack(level=0).reset_index()
    df.columns = list(df.columns[1:].insert(0, 'Resources'))
    last_year = df[df['level_2'] == '前期值']
    print(last_year)
    # 解析地区相关发展数据的数据表
    df_dev = pd.read_excel(filename, sheet_name=economic_sheet_name, header=[0, 1])
    df_dev = df_dev.set_index(df_dev.columns[0])
    df_dev = df_dev.stack(level=0).stack(level=0).reset_index()
    df_dev.columns = list(df_dev.columns[1:].insert(0, 'city'))
    last_year_dev = df_dev[df_dev['level_2'] == '前期值']
    print(last_year)
    # 解析无需计算所得的各项单项基础指标
    df_item = pd.read_excel(filename, sheet_name=already_item_sheet_name, header=[0, 1, 2])
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
            prov_item_each = df_item[df_item['city'] == str(province)][df_item['level_2'] == m[1]]['前期值']
            print(prov_item_each)
            if len(prov_item_each) == 0:
                the_each = 0
            else:
                the_each = prov_item_each.values[0]
            print(the_each)
            items.append([m[0], the_each])
        for m in eg_list:
            area_eg_each = k[k['Resources'] == m[1]]
            if len(area_eg_each) == 0:
                the_each = 0
            else:
                the_each = area_eg_each[0].values[0]
            print(the_each)
            items.append([m[0], the_each])
        for m in economic_list_prov:
            area_dev_each = k_dev[k_dev['level_1'] == m[1]]
            if len(area_dev_each) == 0:
                the_each = 0
            else:
                the_each = area_dev_each[0].values[0]
            print(the_each)
            items.append([m[0], the_each])
        if len(get_database) == 0:
            items.append(['province', province])
            items.append(['year', year])
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
            k = last_year[last_year['level_1'] == i.name]
            k_dev = last_year_dev[last_year_dev['city'] == i.name]
            to_database = get_database.filter(area=i.name)
            items = []
            # print(to_database)
            for m in read_items_name:
                area_item_each = df_item[df_item['city'] == i.name][df_item['level_2'] == m[1]]['前期值']
                if len(area_item_each) == 0:
                    the_each = 0
                else:
                    the_each = area_item_each.values[0]
                print(the_each)
                items.append([m[0], the_each])
            for m in eg_list:
                area_eg_each = k[k['Resources'] == m[1]]
                if len(area_eg_each) == 0:
                    the_each = 0
                else:
                    the_each = area_eg_each[0].values[0]
                print(the_each)
                items.append([m[0], the_each])
            for m in economic_list_area:
                area_dev_each = k_dev[k_dev['level_1'] == m[1]]
                if len(area_dev_each) == 0:
                    the_each = 0
                else:
                    the_each = area_dev_each[0].values[0]
                print(the_each)
                items.append([m[0], the_each])
            if len(to_database) == 0:
                items.append(['province', province])
                items.append(['area', i.name])
                items.append(['year', year])
                updatabase = dict(items)
                Annual_data.objects.create(**updatabase)
            else:
                updatabase = dict(items)
                Annual_data.objects.filter(province=province, area=i.name, year=year).update(**updatabase)


# 查询对应省份下的全部地区==》为列表


# 地区待计算指标列表
area_item_this_year = read_items_name
prov_item_last_year = read_prov_items_name
area_item_list_index = [
    # 计算所得单项基础指标
    ('r_d', '规模以上工业企业R&D经费支出(万元)'),
    ('per_unit_gdp', '单位GDP能耗(吨/万元)'),
    ('rural_urban', '乡-城人均年收入比(/)'),
    ('urban_per', '城镇居民人均可支配收入(元)'),
    ('rural_per', '农村居民人均可支配收入(元)'),
    ('garbage', '生活垃圾无害化处理率(%)'),
    ('bus_per', '平均万人拥有公共汽车(/)'),
    ('urban_sewage', '城镇生活污水集中处理率(%)'),
    ('edu_years', '平均受教育年限(年)'),
    ('mortality', '死亡率(%)'),
    ('pension_cov', '养老保险覆盖率(%)'),
    ('medical_cov', '医疗保险覆盖率(%)'),
    ('unemployment_cov', '失业保险覆盖率(%)'),
    ('pm25', 'PM2.6年平均浓度(微克/立方米)'),
    ('so2_emissions', '二氧化硫排放量(万吨)'),
    ('co2_per_gdp', '单位GDP二氧化碳排放量(千克/元)'),
    ('cod_emissions', '化学需氧量排放量(万吨)'),
    ('nh_emissions', '氨氮排放量(万吨)'),
    ('water_per', '人均耗水量(立方米)'),
    ('water_per_gdp', '单位GDP用水量(立方米/万元)'),
    ('planting_area', '播种面积占比(%)'),
    ('ef_per', '人均生态足迹(万吨碳/万人)')
]
# 省级单项基础指标
prov_item_list_index = [
    ('r_d', '企业R&D内部经费支出(亿元)'),
    ('renewable_energy_per', '可再生能源供给占比(%)'),
    ('per_unit_gdp', '单位GDP能耗(吨/万元)'),
    ('rural_urban', '乡-城人均年收入比(/)'),
    ('urban_per', '城镇居民人均可支配收入(元)'),
    ('rural_per', '农村居民人均可支配收入(元)'),
    ('garbage', '生活垃圾无害化处理率(%)'),
    ('bus_per', '平均万人拥有公共汽车(/)'),
    ('urban_sewage', '城镇生活污水集中处理率(%)'),
    ('edu_years', '平均受教育年限(年)'),
    ('mortality', '死亡率(%)'),
    ('pension_cov', '养老保险覆盖率(%)'),
    ('medical_cov', '医疗保险覆盖率(%)'),
    ('unemployment_cov', '失业保险覆盖率(%)'),
    ('pm25', 'PM2.5年平均浓度(微克/立方米)'),
    ('so2_emissions', '二氧化硫排放量(万吨)'),
    ('co2_per_gdp', '单位GDP二氧化碳排放量(千克/元)'),
    ('cod_emissions', '化学需氧量排放量(万吨)'),
    ('nh_emissions', '氨氮排放量(万吨)'),
    ('water_per', '人均耗水量(立方米)'),
    ('water_per_gdp', '单位GDP用水量(立方米/万元)'),
    ('planting_area', '播种面积占比(%)'),
    ('ef_per', '人均生态足迹(万吨碳/万人)')
]
# GEP框架指标计算
area_gep_index = [
    ('green_innovation', '绿色创新'),
    ('energy_use', '能源利用'),
    ('parma_ratio', '帕尔玛比率'),
    ('income', '收入'),
    ('infrastructure', '基础设施建设'),
    ('education', '教育'),
    ('life_expectancy', '预期寿命'),
    ('social_security', '社会保障'),
    ('air_pollution', '大气污染'),
    ('greenhouse', '温室气体排放'),
    ('nitrogen', '氮排放'),
    ('water_withdrawal', '取水量'),
    ('land_use', '土地利用'),
    ('EF', '生态足迹'),
    ('city_green_economy', '绿色经济'),
    ('city_sustainable', '可持续发展'),
    ('city_gep_plus', 'GEP+')
]
prov_gep_index = [
    ('green_innovation', '绿色创新'),
    ('renewable_energy', '可再生能源供给'),
    ('energy_use', '能源利用'),
    ('parma_ratio', '帕尔玛比率'),
    ('income', '收入'),
    ('infrastructure', '基础设施建设'),
    ('education', '教育'),
    ('life_expectancy', '预期寿命'),
    ('social_security', '社会保障'),
    ('air_pollution', '大气污染'),
    ('greenhouse', '温室气体排放'),
    ('nitrogen', '氮排放'),
    ('water_withdrawal', '取水量'),
    ('land_use', '土地利用'),
    ('EF', '生态足迹'),
    ('city_green_economy', '绿色经济'),
    ('city_sustainable', '可持续发展'),
    ('city_gep_plus', 'GEP+')
]


# 查地区数据
def calc_area_data(province, area, year):
    areadata_this_year = models.Calculated_value.objects.filter(province=province, year=year)
    areadata_last_year = models.Calculated_value.objects.filter(province=province, year=(year - 1))
    item_extremum = []
    for i in area_item_list_index:
        item_index = []
        for m in areadata_this_year.values(i[0]):
            item_index.append(m[i[0]])
        item_max_each = (i[0] + "_max", max(item_index))
        item_min_each = (i[0] + "_min", min(item_index))
        item_extremum.append(item_max_each)
        item_extremum.append(item_min_each)
    # 极值字典
    item_extremum = dict(item_extremum)
    # 输出极值
    print(item_extremum["mortality" + "_min"])
    # queryset转字典
    area_this_year_datalist = model_to_dict(areadata_this_year.get(area=area))
    area_last_year_datalist = model_to_dict(areadata_last_year.get(area=area))
    print("当期值")
    print(area_this_year_datalist['mortality'])
    print("前期值")
    print(area_last_year_datalist['mortality'])

    r_d = item_calc_positive(area_last_year_datalist['r_d'], area_this_year_datalist['r_d'],
                             item_extremum["r_d_max"])
    per_unit_gdp = item_calc_negative(area_last_year_datalist['per_unit_gdp'],
                                      area_this_year_datalist['per_unit_gdp'], item_extremum["per_unit_gdp_min"])
    rural_urban = item_calc_positive(area_last_year_datalist['rural_urban'],
                                     area_this_year_datalist['rural_urban'], item_extremum["rural_urban_max"])
    urban_per = item_calc_positive(area_last_year_datalist['urban_per'], area_this_year_datalist['urban_per'],
                                   item_extremum["urban_per_max"])
    rural_per = item_calc_positive(area_last_year_datalist['rural_per'], area_this_year_datalist['rural_per'],
                                   item_extremum["rural_per_max"])
    garbage = item_calc_positive(area_last_year_datalist['garbage'], area_this_year_datalist['garbage'],
                                 item_extremum["garbage_max"])
    bus_per = item_calc_positive(area_last_year_datalist['bus_per'], area_this_year_datalist['bus_per'],
                                 item_extremum["bus_per_max"])
    urban_sewage = item_calc_positive(area_last_year_datalist['urban_sewage'],
                                      area_this_year_datalist['urban_sewage'], item_extremum["urban_sewage_max"])
    edu_years = item_calc_positive(area_last_year_datalist['edu_years'], area_this_year_datalist['edu_years'],
                                   item_extremum["edu_years_max"])
    mortality = item_calc_negative(area_last_year_datalist['mortality'], area_this_year_datalist['mortality'],
                                   item_extremum["mortality_min"])
    pension_cov = item_calc_positive(area_last_year_datalist['pension_cov'],
                                     area_this_year_datalist['pension_cov'], item_extremum["pension_cov_max"])
    medical_cov = item_calc_positive(area_last_year_datalist['medical_cov'],
                                     area_this_year_datalist['medical_cov'], item_extremum["medical_cov_max"])
    unemployment_cov = item_calc_positive(area_last_year_datalist['unemployment_cov'],
                                          area_this_year_datalist['unemployment_cov'],
                                          item_extremum["unemployment_cov_max"])
    pm25 = item_calc_negative(area_last_year_datalist['pm25'], area_this_year_datalist['pm25'],
                              item_extremum["pm25_min"])
    so2_emissions = item_calc_negative(area_last_year_datalist['so2_emissions'],
                                       area_this_year_datalist['so2_emissions'],
                                       item_extremum["so2_emissions_min"])
    co2_per_gdp = item_calc_negative(area_last_year_datalist['co2_per_gdp'],
                                     area_this_year_datalist['co2_per_gdp'], item_extremum["co2_per_gdp_min"])
    cod_emissions = item_calc_negative(area_last_year_datalist['cod_emissions'],
                                       area_this_year_datalist['cod_emissions'],
                                       item_extremum["cod_emissions_min"])
    nh_emissions = item_calc_negative(area_last_year_datalist['nh_emissions'],
                                      area_this_year_datalist['nh_emissions'], item_extremum["nh_emissions_min"])
    water_per = item_calc_negative(area_last_year_datalist['water_per'], area_this_year_datalist['water_per'],
                                   item_extremum["water_per_min"])
    water_per_gdp = item_calc_negative(area_last_year_datalist['water_per_gdp'],
                                       area_this_year_datalist['water_per_gdp'],
                                       item_extremum["water_per_gdp_min"])
    planting_area = item_calc_positive(area_last_year_datalist['planting_area'],
                                       area_this_year_datalist['planting_area'],
                                       item_extremum["planting_area_max"])
    ef_per = item_calc_negative(area_last_year_datalist['ef_per'], area_this_year_datalist['ef_per'],
                                item_extremum["ef_per_min"])

    green_innovation = r_d[0]
    # renewable_energy=renewable_energy_per
    energy_use = per_unit_gdp[0]
    parma_ratio = rural_urban[0]
    income = np.average([urban_per[0], rural_per[0]], weights=(urban_per[1], rural_per[1]))
    # garbage,bus_per,urban_sewage
    infrastructure = np.average([garbage[0], bus_per[0], urban_sewage[0]],
                                weights=(garbage[1], bus_per[1], urban_sewage[1]))
    education = edu_years[0]
    life_expectancy = mortality[0]
    # pension_cov,medical_cov,unemployment_cov
    social_security = np.average([pension_cov[0], medical_cov[0], unemployment_cov[0]],
                                 weights=(pension_cov[1], medical_cov[1], unemployment_cov[1]))
    # pm25,so2_emissions
    air_pollution = np.average([pm25[0], so2_emissions[0]], weights=(pm25[1], so2_emissions[1]))
    greenhouse = co2_per_gdp[0]
    # cod_emissions,nh_emissions
    nitrogen = np.average([cod_emissions[0], nh_emissions[0]], weights=(cod_emissions[1], nh_emissions[1]))
    # water_per,water_per_gdp
    water_withdrawal = np.average([water_per[0], water_per_gdp[0]], weights=(water_per[1], water_per_gdp[1]))
    land_use = planting_area[0]
    EF = ef_per[0]

    # （1）绿色经济=（绿色创新*该项权重+能源利用*该项权重+帕尔玛比率*该项权重+收入*该项权重+基础设施建设*该项权重+教育*该项权重+预期寿命*该项权重+社会保障*该项权重+大气污染*该项权重）/（绿色创新权重+能源利用权重+帕尔玛比率权重+收入权重+基础设施建设权重+教育权重+预期寿命权重+社会保障权重+大气污染权重）
    # r_d,per_unit_gdp,rural_urban,urban_per,rural_per,garbage,bus_per,urban_sewage,edu_years,mortality,pension_cov,medical_cov,unemployment_cov,pm25,so2_emissions
    city_green_economy = np.average(
        [r_d[0], per_unit_gdp[0], rural_urban[0], urban_per[0], rural_per[0], garbage[0], bus_per[0], urban_sewage[0],
         edu_years[0], mortality[0], pension_cov[0], medical_cov[0], unemployment_cov[0], pm25[0], so2_emissions[0]],
        weights=(
            r_d[1], per_unit_gdp[1], rural_urban[1], urban_per[1], rural_per[1], garbage[1], bus_per[1],
            urban_sewage[1],
            edu_years[1], mortality[1], pension_cov[1], medical_cov[1], unemployment_cov[1], pm25[1], so2_emissions[1]))
    # （2）可持续发展=（温室气体排放*该项权重+氮排放*该项权重+取水量*该项权重+土地利用*该项权重+生态足迹*该项权重）/（温室气体排放权重+氮排放权重+取水量权重+土地利用权重+生态足迹权重）
    # co2_per_gdp,cod_emissions,nh_emissions,water_per,water_per_gdp,planting_area,ef_per
    city_sustainable = np.average(
        [co2_per_gdp[0], cod_emissions[0], nh_emissions[0], water_per[0], water_per_gdp[0], planting_area[0],
         ef_per[0]], weights=(
            co2_per_gdp[1], cod_emissions[1], nh_emissions[1], water_per[1], water_per_gdp[1], planting_area[1],
            ef_per[1]))
    # （3）GEP+=（绿色经济得分*该项权重+可持续发展得分*该项权重）/（绿色经济权重+可持续发展权重）
    city_gep_plus = np.average(
        [r_d[0], per_unit_gdp[0], rural_urban[0], urban_per[0], rural_per[0], garbage[0], bus_per[0], urban_sewage[0],
         edu_years[0], mortality[0], pension_cov[0], medical_cov[0], unemployment_cov[0], pm25[0], so2_emissions[0],
         co2_per_gdp[0], cod_emissions[0], nh_emissions[0], water_per[0], water_per_gdp[0], planting_area[0],
         ef_per[0]], weights=(
            r_d[1], per_unit_gdp[1], rural_urban[1], urban_per[1], rural_per[1], garbage[1], bus_per[1],
            urban_sewage[1],
            edu_years[1], mortality[1], pension_cov[1], medical_cov[1], unemployment_cov[1], pm25[1], so2_emissions[1],
            co2_per_gdp[1], cod_emissions[1], nh_emissions[1], water_per[1], water_per_gdp[1], planting_area[1],
            ef_per[1]))

    test_dict = dict(province=province, area=area, year=year, r_d_score=r_d[0], per_unit_gdp_score=per_unit_gdp[0],
                     rural_urban_score=rural_urban[0],
                     urban_per_score=urban_per[0], rural_per_score=rural_per[0], garbage_score=garbage[0],
                     bus_per_score=bus_per[0], urban_sewage_score=urban_sewage[0], edu_years_score=edu_years[0],
                     mortality_score=mortality[0], pension_cov_score=pension_cov[0], medical_cov_score=medical_cov[0],
                     unemployment_cov_score=unemployment_cov[0], pm25_score=pm25[0],
                     so2_emissions_score=so2_emissions[0], co2_per_gdp_score=co2_per_gdp[0],
                     cod_emissions_score=cod_emissions[0], nh_emissions_score=nh_emissions[0],
                     water_per_score=water_per[0], water_per_gdp_score=water_per_gdp[0],
                     planting_area_score=planting_area[0], ef_per_score=ef_per[0], green_innovation=green_innovation,
                     energy_use=energy_use, parma_ratio=parma_ratio, income=income, infrastructure=infrastructure,
                     education=education, life_expectancy=life_expectancy, social_security=social_security,
                     air_pollution=air_pollution, greenhouse=greenhouse, nitrogen=nitrogen,
                     water_withdrawal=water_withdrawal, land_use=land_use, EF=EF, city_green_economy=city_green_economy,
                     city_sustainable=city_sustainable, city_gep_plus=city_gep_plus)
    print(test_dict)
    # write_area_database = models.area_gep_score.objects.filter(province=province, year=year, area=area)
    if models.area_gep_score.objects.filter(province=province, year=year, area=area).exists():
        models.area_gep_score.objects.filter(province=province, year=year, area=area).update(**test_dict)
    else:
        models.area_gep_score.objects.filter(province=province, year=year, area=area).create(**test_dict)


# 查省份数据
def calc_prov_data(province, year):
    provdata_this_year = models.Prov_Calculated_value.objects.get(province=province, year=year)
    provdata_last_year = models.Prov_Calculated_value.objects.get(province=province, year=(year-1))
    item_extremum = models.Prov_Annual_data.objects.get(province=province,year=year)
    # queryset转字典
    prov_this_year_datalist = provdata_this_year
    prov_last_year_datalist = provdata_last_year

    r_d = item_calc_positive(prov_last_year_datalist.r_d, prov_this_year_datalist.r_d,
                             item_extremum.r_d_target)
    per_unit_gdp = item_calc_negative(prov_last_year_datalist.per_unit_gdp,
                                      prov_this_year_datalist.per_unit_gdp, item_extremum.per_unit_gdp_target)
    renewable_energy_per = item_calc_positive(prov_last_year_datalist.renewable_energy_per,
                                              prov_this_year_datalist.renewable_energy_per,
                                              item_extremum.renewable_energy_per_target)
    rural_urban = item_calc_positive(prov_last_year_datalist.rural_urban,
                                     prov_this_year_datalist.rural_urban, item_extremum.rural_urban_target)
    urban_per = item_calc_positive(prov_last_year_datalist.urban_per, prov_this_year_datalist.urban_per,
                                   item_extremum.urban_per_target)
    rural_per = item_calc_positive(prov_last_year_datalist.rural_per, prov_this_year_datalist.rural_per,
                                   item_extremum.rural_per_target)
    garbage = item_calc_positive(prov_last_year_datalist.garbage, prov_this_year_datalist.garbage,
                                 item_extremum.garbage_target)
    bus_per = item_calc_positive(prov_last_year_datalist.bus_per, prov_this_year_datalist.bus_per,
                                 item_extremum.bus_per_target)
    urban_sewage = item_calc_positive(prov_last_year_datalist.urban_sewage,
                                      prov_this_year_datalist.urban_sewage, item_extremum.urban_sewage_target)
    edu_years = item_calc_positive(prov_last_year_datalist.edu_years, prov_this_year_datalist.edu_years,
                                   item_extremum.edu_years_target)
    mortality = item_calc_negative(prov_last_year_datalist.mortality, prov_this_year_datalist.mortality,
                                   item_extremum.mortality_target)
    pension_cov = item_calc_positive(prov_last_year_datalist.pension_cov,
                                     prov_this_year_datalist.pension_cov, item_extremum.pension_cov_target)
    medical_cov = item_calc_positive(prov_last_year_datalist.medical_cov,
                                     prov_this_year_datalist.medical_cov, item_extremum.medical_cov_target)
    unemployment_cov = item_calc_positive(prov_last_year_datalist.unemployment_cov,
                                          prov_this_year_datalist.unemployment_cov,
                                          item_extremum.unemployment_cov_target)
    pm25 = item_calc_negative(prov_last_year_datalist.pm25, prov_this_year_datalist.pm25,
                              item_extremum.pm25_target)
    so2_emissions = item_calc_negative(prov_last_year_datalist.so2_emissions,
                                       prov_this_year_datalist.so2_emissions,
                                       item_extremum.so2_emissions_target)
    co2_per_gdp = item_calc_negative(prov_last_year_datalist.co2_per_gdp,
                                     prov_this_year_datalist.co2_per_gdp, item_extremum.co2_per_gdp_target)
    cod_emissions = item_calc_negative(prov_last_year_datalist.cod_emissions,
                                       prov_this_year_datalist.cod_emissions,
                                       item_extremum.cod_emissions_target)
    nh_emissions = item_calc_negative(prov_last_year_datalist.nh_emissions,
                                      prov_this_year_datalist.nh_emissions, item_extremum.nh_emissions_target)
    water_per = item_calc_negative(prov_last_year_datalist.water_per, prov_this_year_datalist.water_per,
                                   item_extremum.water_per_target)
    water_per_gdp = item_calc_negative(prov_last_year_datalist.water_per_gdp,
                                       prov_this_year_datalist.water_per_gdp,
                                       item_extremum.water_per_gdp_target)
    planting_area = item_calc_positive(prov_last_year_datalist.planting_area,
                                       prov_this_year_datalist.planting_area,
                                       item_extremum.planting_area_target)
    ef_per = item_calc_negative(prov_last_year_datalist.ef_per, prov_this_year_datalist.ef_per,
                                item_extremum.ef_per_target)

    green_innovation = r_d[0]
    renewable_energy = renewable_energy_per[0]
    # renewable_energy=renewable_energy_per
    energy_use = per_unit_gdp[0]
    parma_ratio = rural_urban[0]
    income = np.average([urban_per[0], rural_per[0]], weights=(urban_per[1], rural_per[1]))
    # garbage,bus_per,urban_sewage
    infrastructure = np.average([garbage[0], bus_per[0], urban_sewage[0]],
                                weights=(garbage[1], bus_per[1], urban_sewage[1]))
    education = edu_years[0]
    life_expectancy = mortality[0]
    # pension_cov,medical_cov,unemployment_cov
    social_security = np.average([pension_cov[0], medical_cov[0], unemployment_cov[0]],
                                 weights=(pension_cov[1], medical_cov[1], unemployment_cov[1]))
    # pm25,so2_emissions
    air_pollution = np.average([pm25[0], so2_emissions[0]], weights=(pm25[1], so2_emissions[1]))
    greenhouse = co2_per_gdp[0]
    # cod_emissions,nh_emissions
    nitrogen = np.average([cod_emissions[0], nh_emissions[0]], weights=(cod_emissions[1], nh_emissions[1]))
    # water_per,water_per_gdp
    water_withdrawal = np.average([water_per[0], water_per_gdp[0]], weights=(water_per[1], water_per_gdp[1]))
    land_use = planting_area[0]
    EF = ef_per[0]

    # （1）绿色经济=（绿色创新*该项权重+能源利用*该项权重+帕尔玛比率*该项权重+收入*该项权重+基础设施建设*该项权重+教育*该项权重+预期寿命*该项权重+社会保障*该项权重+大气污染*该项权重）/（绿色创新权重+能源利用权重+帕尔玛比率权重+收入权重+基础设施建设权重+教育权重+预期寿命权重+社会保障权重+大气污染权重）
    # r_d,per_unit_gdp,rural_urban,urban_per,rural_per,garbage,bus_per,urban_sewage,edu_years,mortality,pension_cov,medical_cov,unemployment_cov,pm25,so2_emissions
    city_green_economy = np.average(
        [r_d[0], per_unit_gdp[0], rural_urban[0], urban_per[0], rural_per[0], garbage[0], bus_per[0], urban_sewage[0],
         edu_years[0], mortality[0], pension_cov[0], medical_cov[0], unemployment_cov[0], pm25[0], so2_emissions[0]],
        weights=(
            r_d[1], per_unit_gdp[1], rural_urban[1], urban_per[1], rural_per[1], garbage[1], bus_per[1],
            urban_sewage[1],
            edu_years[1], mortality[1], pension_cov[1], medical_cov[1], unemployment_cov[1], pm25[1], so2_emissions[1]))
    # （2）可持续发展=（温室气体排放*该项权重+氮排放*该项权重+取水量*该项权重+土地利用*该项权重+生态足迹*该项权重）/（温室气体排放权重+氮排放权重+取水量权重+土地利用权重+生态足迹权重）
    # co2_per_gdp,cod_emissions,nh_emissions,water_per,water_per_gdp,planting_area,ef_per
    city_sustainable = np.average(
        [co2_per_gdp[0], cod_emissions[0], nh_emissions[0], water_per[0], water_per_gdp[0], planting_area[0],
         ef_per[0]], weights=(
            co2_per_gdp[1], cod_emissions[1], nh_emissions[1], water_per[1], water_per_gdp[1], planting_area[1],
            ef_per[1]))
    # （3）GEP+=（绿色经济得分*该项权重+可持续发展得分*该项权重）/（绿色经济权重+可持续发展权重）
    city_gep_plus = np.average(
        [r_d[0], per_unit_gdp[0], rural_urban[0], urban_per[0], rural_per[0], garbage[0], bus_per[0], urban_sewage[0],
         edu_years[0], mortality[0], pension_cov[0], medical_cov[0], unemployment_cov[0], pm25[0], so2_emissions[0],
         co2_per_gdp[0], cod_emissions[0], nh_emissions[0], water_per[0], water_per_gdp[0], planting_area[0],
         ef_per[0]], weights=(
            r_d[1], per_unit_gdp[1], rural_urban[1], urban_per[1], rural_per[1], garbage[1], bus_per[1],
            urban_sewage[1],
            edu_years[1], mortality[1], pension_cov[1], medical_cov[1], unemployment_cov[1], pm25[1], so2_emissions[1],
            co2_per_gdp[1], cod_emissions[1], nh_emissions[1], water_per[1], water_per_gdp[1], planting_area[1],
            ef_per[1]))

    test_dict = dict(province=province, year=year, r_d_score=r_d[0], per_unit_gdp_score=per_unit_gdp[0],
                     renewable_energy_per_score=renewable_energy_per[0], rural_urban_score=rural_urban[0],
                     urban_per_score=urban_per[0], rural_per_score=rural_per[0], garbage_score=garbage[0],
                     bus_per_score=bus_per[0], urban_sewage_score=urban_sewage[0], edu_years_score=edu_years[0],
                     mortality_score=mortality[0], pension_cov_score=pension_cov[0], medical_cov_score=medical_cov[0],
                     unemployment_cov_score=unemployment_cov[0], pm25_score=pm25[0],
                     so2_emissions_score=so2_emissions[0], co2_per_gdp_score=co2_per_gdp[0],
                     cod_emissions_score=cod_emissions[0], nh_emissions_score=nh_emissions[0],
                     water_per_score=water_per[0], water_per_gdp_score=water_per_gdp[0],
                     planting_area_score=planting_area[0], ef_per_score=ef_per[0], green_innovation=green_innovation,
                     renewable_energy=renewable_energy, energy_use=energy_use, parma_ratio=parma_ratio, income=income,
                     infrastructure=infrastructure, education=education, life_expectancy=life_expectancy,
                     social_security=social_security, air_pollution=air_pollution, greenhouse=greenhouse,
                     nitrogen=nitrogen, water_withdrawal=water_withdrawal, land_use=land_use, EF=EF,
                     city_green_economy=city_green_economy, city_sustainable=city_sustainable,
                     city_gep_plus=city_gep_plus)
    if models.prov_gep_score.objects.filter(province=province, year=year).exists():
        models.prov_gep_score.objects.filter(province=province, year=year).update(**test_dict)
    else:
        models.prov_gep_score.objects.filter(province=province, year=year).create(**test_dict)
