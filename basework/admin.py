from django.contrib import admin

from .models import ConstantEg, Annual_data, Prov_Annual_data, Calculated_value, Prov_Calculated_value, \
    ImportFile_excel, area_gep_score, prov_gep_score
from .caldata import *
from work.models import CityDataRecord, ProvinceDataRecord, Province
from .utils import takedata, takedata_lastyear, calc_area_data, calc_prov_data


# Register your models here.

# 常量编辑

class ConstantEgAdmin(admin.ModelAdmin):
    list_display = (
        'Raw_coal', 'Clean_coal', 'Coke', 'Briquette', 'Other_coking_products', 'Crude', 'Fuel_oil', 'Gasoline',
        'Diesel',
        'Kerosene', 'Liquefied_petroleum_gas', 'Refinery_dry_gas', 'Naphtha', 'Asphalt', 'Lubricating_oil',
        'Petroleum_coke', 'Natural_gas', 'Cement', 'Steel', 'Farmland', 'Woodland', 'Pastureland', 'Fishing_ground',
        'Construction_land',)

    fieldsets = (
        ('常量编辑', {
            'fields': (
                (
                    'Raw_coal', 'Raw_coal_MJ', 'Clean_coal', 'Clean_coal_MJ', 'Coke', 'Coke_MJ', 'Briquette',
                    'Briquette_MJ', 'Other_coking_products',
                    'Other_coking_products_MJ', 'Crude', 'Crude_MJ', 'Fuel_oil', 'Fuel_oil_MJ', 'Gasoline',
                    'Gasoline_MJ', 'Diesel', 'Diesel_MJ', 'Kerosene', 'Kerosene_MJ', 'Liquefied_petroleum_gas',
                    'Liquefied_petroleum_gas_MJ', 'Refinery_dry_gas', 'Refinery_dry_gas_MJ', 'Naphtha', 'Naphtha_MJ',
                    'Asphalt', 'Asphalt_MJ', 'Lubricating_oil', 'Lubricating_oil_MJ', 'Petroleum_coke',
                    'Petroleum_coke_MJ', 'Natural_gas', 'Natural_gas_MJ'
                ),
                ('Cement', 'Steel'),
                ('Farmland', 'Woodland', 'Pastureland', 'Fishing_ground', 'Construction_land'),
            )
        }),
    )


class Annual_dataAdmin(admin.ModelAdmin):
    search_fields = ['area', 'year', 'province']
    list_filter = ['province', 'area', 'year']
    list_display = ('province', 'area', 'year')
    fieldsets = (('地区年度数据', {
        'fields': (
            (
                'province', 'area', 'year',
            ),
            (
                'Consume_Raw_coal', 'Consume_Clean_coal', 'Consume_Coke', 'Consume_Briquette',
                'Consume_Other_coking_products', 'Consume_Crude', 'Consume_Fuel_oil', 'Consume_Gasoline',
                'Consume_Diesel', 'Consume_Kerosene', 'Consume_Liquefied_petroleum_gas', 'Consume_Refinery_dry_gas',
                'Consume_Naphtha', 'Consume_Asphalt', 'Consume_Lubricating_oil', 'Consume_Petroleum_coke',
                'Consume_Natural_gas',
            ),
            (
                'Consume_Cement', 'Consume_Steel',
            ),
            (
                'Consume_Farmland', 'Consume_Woodland', 'Consume_Pastureland', 'Consume_Fishing_ground',
                'Consume_Construction_land',
            ),
            (
                'GDP', 'Sown_area', 'Total_population', 'Total_energy_consumption', 'Total_water_consumption',
                'The_total_area', 'Number_of_employees_in_basic_pension_insurance', 'Number_of_basic_medical_insurance',
                'Number_of_unemployment_insurance', 'Primary_school_number', 'Number_of_junior_high_school',
                'High_school_number', 'University_and_above',
            ),
            (
                'r_d', 'rural_urban', 'urban_per', 'rural_per', 'garbage', 'bus_per', 'urban_sewage', 'mortality',
                'pm25', 'so2_emissions', 'cod_emissions', 'nh_emissions'
            ),
        )
    }),
                 )

    # 数据批量操作
    def get_datas(self, request, queryset):
        # temp = []
        # for d in queryset:
        #     t = [d.job, d.title, str(d.payment), d.person.name]
        #     temp.append(t)
        # f = open('d://data.txt', 'a')
        # for t in temp:
        #     f.write(','.join(t) + '\r\n')
        # f.close()
        # 设置提示信息
        self.message_user(request, '数据导出成功')

    # 设置函数的显示名称
    get_datas.short_description = '导出所选数据'

    def calculate_datas(self, request, queryset):
        temp = []
        con = ConstantEg.objects.all()
        for d in queryset:
            # d = queryset[0]
            # 能源类碳排放计算
            t0 = (d.Consume_Raw_coal * con[0].Raw_coal * con[0].Raw_coal_MJ) / (10 ** 8)
            t1 = (d.Consume_Clean_coal * con[0].Clean_coal * con[0].Clean_coal_MJ) / (10 ** 8)
            t2 = (d.Consume_Coke * con[0].Coke * con[0].Coke_MJ) / (10 ** 8)
            t3 = (d.Consume_Briquette * con[0].Briquette * con[0].Briquette_MJ) / (10 ** 8)
            t4 = (d.Consume_Other_coking_products * con[0].Other_coking_products * con[0].Other_coking_products_MJ) / (
                    10 ** 8)
            t5 = (d.Consume_Crude * con[0].Crude * con[0].Crude_MJ) / (10 ** 8)
            t6 = (d.Consume_Fuel_oil * con[0].Fuel_oil * con[0].Fuel_oil_MJ) / (10 ** 8)
            t7 = (d.Consume_Gasoline * con[0].Gasoline * con[0].Gasoline_MJ) / (10 ** 8)
            t8 = (d.Consume_Diesel * con[0].Diesel * con[0].Diesel_MJ) / (10 ** 8)
            t9 = (d.Consume_Kerosene * con[0].Kerosene * con[0].Kerosene_MJ) / (10 ** 8)
            t10 = (d.Consume_Liquefied_petroleum_gas * con[0].Liquefied_petroleum_gas * con[
                0].Liquefied_petroleum_gas_MJ) / (10 ** 8)
            t11 = (d.Consume_Refinery_dry_gas * con[0].Refinery_dry_gas * con[0].Refinery_dry_gas_MJ) / (10 ** 8)
            t12 = (d.Consume_Naphtha * con[0].Naphtha * con[0].Naphtha_MJ) / (10 ** 8)
            t13 = (d.Consume_Asphalt * con[0].Asphalt * con[0].Asphalt_MJ) / (10 ** 8)
            t14 = (d.Consume_Lubricating_oil * con[0].Lubricating_oil * con[0].Lubricating_oil_MJ) / (10 ** 8)
            t15 = (d.Consume_Petroleum_coke * con[0].Petroleum_coke * con[0].Petroleum_coke_MJ) / (10 ** 8)
            t16 = (d.Consume_Natural_gas * con[0].Natural_gas * con[0].Natural_gas_MJ) / (10 ** 7)
            eg_l = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16]
            ## 温室气体排放量 GHG Emission 
            eg_l_sum = sum(eg_l) * 10
            ## 二氧化碳排放量 CO2 Emission
            eg_l_co2 = eg_l_sum * 44 / 12
            # 工业生产过程碳排放
            t17 = (d.Consume_Cement * con[0].Cement) / 100000
            t18 = (d.Consume_Steel * con[0].Steel) / 100000
            indus_l = [t17, t18]
            ## 温室气体排放量 GHG Emission
            indus_l_sum = sum(indus_l) * 10
            ## 二氧化碳排放量 CO2 Emission
            indus_l_co2 = indus_l_sum * 44 / 12
            # 二氧化碳排放总量 Total CO2 Emission
            total_co2 = eg_l_co2 + indus_l_co2

            # 生态足迹
            t19 = d.Consume_Farmland * con[0].Farmland
            t20 = d.Consume_Woodland * con[0].Woodland
            t21 = d.Consume_Pastureland * con[0].Pastureland
            t22 = d.Consume_Fishing_ground * con[0].Fishing_ground
            t23 = d.Consume_Construction_land * con[0].Construction_land
            ef_l = [t19, t20, t21, t22, t23]
            ef_l_sum = sum(ef_l) / 1000

            # 基础指标计算
            # 地区当年生产总值	GDP
            # 地区当年播种面积	Sown_area
            # 地区当年总人口	Total_population
            # 地区当年总发电量	Total_power_generation
            # 地区当年能源消费总量	Total_energy_consumption
            # 地区当年二氧化碳排放量	Carbon_dioxide_emissions
            # 地区当年用水总量	Total_water_consumption
            # 地区当年总面积	The_total_area
            # 地区当年生态足迹	Ecological_footprint
            # 地区当年基本养老保险职工人数	Number_of_employees_in_basic_pension_insurance
            # 地区当年基本医疗保险人数	Number_of_basic_medical_insurance
            # 地区当年失业保险人数	Number_of_unemployment_insurance
            # 地区当年核电发电量	Nuclear_power_generation
            # 地区当年风电发电量	Wind_power_generation
            # 地区当年水电发电量	Hydropower_generation
            # 地区当年光伏发电量	Photovoltaic_power_generation
            # 小学人数	Primary_school_number
            # 初中人数	Number_of_junior_high_school
            # 高中人数	High_school_number
            # 大学及以上人数	University_and_above

            # 单位GDP能耗	地区当年能源消费总量/地区当年生产总值
            per_unit_gdp = d.Total_energy_consumption / d.GDP
            # 单位GDP二氧化碳排放量	地区当年二氧化碳排放量/地区当年生产总值
            co2_per_gdp = total_co2 / d.GDP * 1000
            # 单位GDP用水量	地区当年用水总量/地区当年生产总值
            water_per_gdp = d.Total_water_consumption / d.GDP
            # 播种面积占比	地区当年播种面积/地区当年总面积
            planting_area = d.Sown_area / d.The_total_area
            # 平均受教育年限	（小学人数×6+初中人数×9+高中人数×12+大学及以上人数×16）/43
            # edu_years = (d.Primary_school_number*6 + d.Number_of_junior_high_school*9 + d.High_school_number*12 + d.University_and_above*16)/43
            # 平均受教育年限 （小学人数×6+初中人数×9年+高中人数×12+大学及以上人数×16）/（小学人数+初中人数+高中人数+大学及以上人数）
            educated_population = d.Primary_school_number + d.Number_of_junior_high_school + d.High_school_number + d.University_and_above
            edu_years = (
                                d.Primary_school_number * 6 + d.Number_of_junior_high_school * 9 + d.High_school_number * 12 + d.University_and_above * 16) / educated_population
            # 人均生态足迹	地区当年生态足迹/地区当年总人口
            ef_per = ef_l_sum / d.Total_population
            # 人均用水量	地区当年用水总量/地区当年总人口
            water_per = d.Total_water_consumption / d.Total_population
            # 养老保险覆盖率	地区当年基本养老保险职工人数/地区当年总人口
            pension_cov = d.Number_of_employees_in_basic_pension_insurance / d.Total_population
            # 医疗保险覆盖率	地区当年基本医疗保险人数/地区当年总人口
            medical_cov = d.Number_of_basic_medical_insurance / d.Total_population
            # 失业保险覆盖率	地区当年失业保险人数/地区当年总人口
            unemployment_cov = d.Number_of_unemployment_insurance / d.Total_population

            # 写入数据表
            ## 判断该条记录是否已经存在
            # w_area = CityDataRecordResource.objects.filter(area=d.area, year=d.year)
            b_area = Calculated_value.objects.filter(province=d.province, area=d.area, year=d.year)
            ## 已存在，更新数据
            ## 不存在，创建数据
            all_base_data = dict(province=d.province, area=d.area, year=d.year, Cal_Raw_coal=t0, Cal_Clean_coal=t1,
                                 Cal_Coke=t2, Cal_Briquette=t3, Cal_Other_coking_products=t4, Cal_Crude=t5,
                                 Cal_Fuel_oil=t6, Cal_Gasoline=t7, Cal_Diesel=t8, Cal_Kerosene=t9,
                                 Cal_Liquefied_petroleum_gas=t10, Cal_Refinery_dry_gas=t11, Cal_Naphtha=t12,
                                 Cal_Asphalt=t13, Cal_Lubricating_oil=t14, Cal_Petroleum_coke=t15, Cal_Natural_gas=t16,
                                 GHG_Emission_a=eg_l_sum, CO2_Emission_a=eg_l_co2, Cal_Cement=t17, Cal_Steel=t18,
                                 GHG_Emission_b=indus_l_sum, CO2_Emission_b=indus_l_co2, Total_CO2_Emission=total_co2,
                                 Cal_EF=ef_l_sum,
                                 r_d=d.r_d, rural_urban=d.rural_urban, urban_per=d.urban_per, rural_per=d.rural_per,
                                 garbage=d.garbage, bus_per=d.bus_per, urban_sewage=d.urban_sewage,
                                 mortality=d.mortality, pm25=d.pm25, so2_emissions=d.so2_emissions,
                                 cod_emissions=d.cod_emissions, nh_emissions=d.nh_emissions, per_unit_gdp=per_unit_gdp,
                                 co2_per_gdp=co2_per_gdp, water_per_gdp=water_per_gdp, planting_area=planting_area,
                                 edu_years=edu_years, ef_per=ef_per, water_per=water_per, pension_cov=pension_cov,
                                 medical_cov=medical_cov, unemployment_cov=unemployment_cov)
            if len(b_area) == 0:
                b_area.create(**all_base_data)
            else:
                b_area.update(**all_base_data)
            ## 保存更改
            info_return = str(len(b_area))

            # 设置提示信息
            self.message_user(request, '数据计算成功')

    # 设置函数的显示名称
    calculate_datas.short_description = '数据计算'
    # 添加到“动作”栏
    actions = ['calculate_datas', 'get_datas']


class Prov_Annual_dataAdmin(admin.ModelAdmin):
    search_fields = ['year', 'province']
    list_filter = ['province', 'year']
    list_display = ('province', 'year')
    fieldsets = (('省级年度数据', {
        'fields': (
            (
                'province', 'year',
            ),
            (
                'Consume_Raw_coal', 'Consume_Clean_coal', 'Consume_Coke', 'Consume_Briquette',
                'Consume_Other_coking_products', 'Consume_Crude', 'Consume_Fuel_oil', 'Consume_Gasoline',
                'Consume_Diesel', 'Consume_Kerosene', 'Consume_Liquefied_petroleum_gas', 'Consume_Refinery_dry_gas',
                'Consume_Naphtha', 'Consume_Asphalt', 'Consume_Lubricating_oil', 'Consume_Petroleum_coke',
                'Consume_Natural_gas',
            ),
            (
                'Consume_Cement', 'Consume_Steel',
            ),
            (
                'Consume_Farmland', 'Consume_Woodland', 'Consume_Pastureland', 'Consume_Fishing_ground',
                'Consume_Construction_land',
            ),
            (
                'GDP', 'Sown_area', 'Total_population', 'Total_power_generation', 'Total_energy_consumption',
                'Total_water_consumption', 'The_total_area', 'Number_of_employees_in_basic_pension_insurance',
                'Number_of_basic_medical_insurance', 'Number_of_unemployment_insurance', 'Nuclear_power_generation',
                'Wind_power_generation', 'Hydropower_generation', 'Photovoltaic_power_generation',
                'Primary_school_number', 'Number_of_junior_high_school', 'High_school_number', 'University_and_above',
            ),
            (
                'r_d', 'rural_urban', 'urban_per', 'rural_per', 'garbage', 'bus_per', 'urban_sewage', 'mortality',
                'pm25', 'so2_emissions', 'cod_emissions', 'nh_emissions'
            ),
            (
                'per_unit_gdp_target','co2_per_gdp_target','water_per_gdp_target','planting_area_target','edu_years_target','ef_per_target','water_per_target','pension_cov_target','medical_cov_target','unemployment_cov_target','renewable_energy_per_target','r_d_target','rural_urban_target','urban_per_target','rural_per_target','garbage_target','bus_per_target','urban_sewage_target','mortality_target','pm25_target','so2_emissions_target','cod_emissions_target','nh_emissions_target'
            ),
        )
    }),
                 )

    # 数据批量操作
    def get_datas(self, request, queryset):
        # temp = []
        # for d in queryset:
        #     t = [d.job, d.title, str(d.payment), d.person.name]
        #     temp.append(t)
        # f = open('d://data.txt', 'a')
        # for t in temp:
        #     f.write(','.join(t) + '\r\n')
        # f.close()
        # 设置提示信息
        self.message_user(request, '数据导出成功！')

    # 设置函数的显示名称
    get_datas.short_description = '导出所选数据'

    def prov_calculate_datas(self, request, queryset):
        con = ConstantEg.objects.all()
        for d in queryset:
            # d = queryset[0]
            # 能源类碳排放计算
            t0 = (d.Consume_Raw_coal * con[0].Raw_coal * con[0].Raw_coal_MJ) / (10 ** 8)
            t1 = (d.Consume_Clean_coal * con[0].Clean_coal * con[0].Clean_coal_MJ) / (10 ** 8)
            t2 = (d.Consume_Coke * con[0].Coke * con[0].Coke_MJ) / (10 ** 8)
            t3 = (d.Consume_Briquette * con[0].Briquette * con[0].Briquette_MJ) / (10 ** 8)
            t4 = (d.Consume_Other_coking_products * con[0].Other_coking_products * con[0].Other_coking_products_MJ) / (
                    10 ** 8)
            t5 = (d.Consume_Crude * con[0].Crude * con[0].Crude_MJ) / (10 ** 8)
            t6 = (d.Consume_Fuel_oil * con[0].Fuel_oil * con[0].Fuel_oil_MJ) / (10 ** 8)
            t7 = (d.Consume_Gasoline * con[0].Gasoline * con[0].Gasoline_MJ) / (10 ** 8)
            t8 = (d.Consume_Diesel * con[0].Diesel * con[0].Diesel_MJ) / (10 ** 8)
            t9 = (d.Consume_Kerosene * con[0].Kerosene * con[0].Kerosene_MJ) / (10 ** 8)
            t10 = (d.Consume_Liquefied_petroleum_gas * con[0].Liquefied_petroleum_gas * con[
                0].Liquefied_petroleum_gas_MJ) / (10 ** 8)
            t11 = (d.Consume_Refinery_dry_gas * con[0].Refinery_dry_gas * con[0].Refinery_dry_gas_MJ) / (10 ** 8)
            t12 = (d.Consume_Naphtha * con[0].Naphtha * con[0].Naphtha_MJ) / (10 ** 8)
            t13 = (d.Consume_Asphalt * con[0].Asphalt * con[0].Asphalt_MJ) / (10 ** 8)
            t14 = (d.Consume_Lubricating_oil * con[0].Lubricating_oil * con[0].Lubricating_oil_MJ) / (10 ** 8)
            t15 = (d.Consume_Petroleum_coke * con[0].Petroleum_coke * con[0].Petroleum_coke_MJ) / (10 ** 8)
            t16 = (d.Consume_Natural_gas * con[0].Natural_gas * con[0].Natural_gas_MJ) / (10 ** 7)
            eg_l = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16]
            ## 温室气体排放量 GHG Emission 
            eg_l_sum = sum(eg_l) * 10
            ## 二氧化碳排放量 CO2 Emission
            eg_l_co2 = eg_l_sum * 44 / 12
            # 工业生产过程碳排放
            t17 = (d.Consume_Cement * con[0].Cement) / 100000
            t18 = (d.Consume_Steel * con[0].Steel) / 100000
            indus_l = [t17, t18]
            ## 温室气体排放量 GHG Emission
            indus_l_sum = sum(indus_l) * 10
            ## 二氧化碳排放量 CO2 Emission
            indus_l_co2 = indus_l_sum * 44 / 12
            # 二氧化碳排放总量 Total CO2 Emission
            total_co2 = eg_l_co2 + indus_l_co2

            # 生态足迹
            t19 = d.Consume_Farmland * con[0].Farmland
            t20 = d.Consume_Woodland * con[0].Woodland
            t21 = d.Consume_Pastureland * con[0].Pastureland
            t22 = d.Consume_Fishing_ground * con[0].Fishing_ground
            t23 = d.Consume_Construction_land * con[0].Construction_land
            ef_l = [t19, t20, t21, t22, t23]
            ef_l_sum = sum(ef_l) / 1000

            # 基础指标计算
            # 地区当年生产总值	GDP
            # 地区当年播种面积	Sown_area
            # 地区当年总人口	Total_population
            # 地区当年总发电量	Total_power_generation
            # 地区当年能源消费总量	Total_energy_consumption
            # 地区当年二氧化碳排放量	Carbon_dioxide_emissions
            # 地区当年用水总量	Total_water_consumption
            # 地区当年总面积	The_total_area
            # 地区当年生态足迹	Ecological_footprint
            # 地区当年基本养老保险职工人数	Number_of_employees_in_basic_pension_insurance
            # 地区当年基本医疗保险人数	Number_of_basic_medical_insurance
            # 地区当年失业保险人数	Number_of_unemployment_insurance
            # 地区当年核电发电量	Nuclear_power_generation
            # 地区当年风电发电量	Wind_power_generation
            # 地区当年水电发电量	Hydropower_generation
            # 地区当年光伏发电量	Photovoltaic_power_generation
            # 小学人数	Primary_school_number
            # 初中人数	Number_of_junior_high_school
            # 高中人数	High_school_number
            # 大学及以上人数	University_and_above

            # 单位GDP能耗	地区当年能源消费总量/地区当年生产总值
            per_unit_gdp = d.Total_energy_consumption / d.GDP
            # 单位GDP二氧化碳排放量	地区当年二氧化碳排放量/地区当年生产总值
            co2_per_gdp = total_co2 / d.GDP * 1000
            # 单位GDP用水量	地区当年用水总量/地区当年生产总值
            water_per_gdp = d.Total_water_consumption / d.GDP
            # 播种面积占比	地区当年总面积/地区当年播种面积
            planting_area = d.The_total_area / d.Sown_area
            # 平均受教育年限	（小学人数×6+初中人数×9年+高中人数×12+大学及以上人数×16）/43
            edu_years = (
                                d.Primary_school_number * 6 + d.Number_of_junior_high_school * 9 + d.High_school_number * 12 + d.University_and_above * 16) / 43
            # 人均生态足迹	地区当年生态足迹/地区当年总人口
            ef_per = ef_l_sum / d.Total_population
            # 人均用水量	地区当年用水总量/地区当年总人口
            water_per = d.Total_water_consumption / d.Total_population
            # 养老保险覆盖率	地区当年基本养老保险职工人数/地区当年总人口
            pension_cov = d.Number_of_employees_in_basic_pension_insurance / d.Total_population
            # 医疗保险覆盖率	地区当年基本医疗保险人数/地区当年总人口
            medical_cov = d.Number_of_basic_medical_insurance / d.Total_population
            # 失业保险覆盖率	地区当年失业保险人数/地区当年总人口
            unemployment_cov = d.Number_of_unemployment_insurance / d.Total_population
            # 可再生能源供给占比	地区当年核电+风电+水电+光伏发电量/地区当年总发电量
            renewable_energy_per = (
                                           d.Nuclear_power_generation + d.Wind_power_generation + d.Hydropower_generation + d.Photovoltaic_power_generation) / d.Total_power_generation
            # 写入数据表
            ## 判断该条记录是否已经存在
            # w_area = CityDataRecordResource.objects.filter(area=d.area, year=d.year)
            b_prov = Prov_Calculated_value.objects.filter(province=d.province, year=d.year)
            ## 已存在，更新数据
            ## 不存在，创建数据
            all_base_data = dict(province=d.province, year=d.year, Cal_Raw_coal=t0, Cal_Clean_coal=t1, Cal_Coke=t2,
                                 Cal_Briquette=t3, Cal_Other_coking_products=t4, Cal_Crude=t5, Cal_Fuel_oil=t6,
                                 Cal_Gasoline=t7, Cal_Diesel=t8, Cal_Kerosene=t9, Cal_Liquefied_petroleum_gas=t10,
                                 Cal_Refinery_dry_gas=t11, Cal_Naphtha=t12, Cal_Asphalt=t13, Cal_Lubricating_oil=t14,
                                 Cal_Petroleum_coke=t15, Cal_Natural_gas=t16, GHG_Emission_a=eg_l_sum,
                                 CO2_Emission_a=eg_l_co2, Cal_Cement=t17, Cal_Steel=t18, GHG_Emission_b=indus_l_sum,
                                 CO2_Emission_b=indus_l_co2, Total_CO2_Emission=total_co2, Cal_EF=ef_l_sum, r_d=d.r_d,
                                 rural_urban=d.rural_urban, urban_per=d.urban_per, rural_per=d.rural_per,
                                 garbage=d.garbage, bus_per=d.bus_per, urban_sewage=d.urban_sewage,
                                 mortality=d.mortality, pm25=d.pm25, so2_emissions=d.so2_emissions,
                                 cod_emissions=d.cod_emissions, nh_emissions=d.nh_emissions, per_unit_gdp=per_unit_gdp,
                                 co2_per_gdp=co2_per_gdp, water_per_gdp=water_per_gdp, planting_area=planting_area,
                                 edu_years=edu_years, ef_per=ef_per, water_per=water_per, pension_cov=pension_cov,
                                 medical_cov=medical_cov, unemployment_cov=unemployment_cov,
                                 renewable_energy_per=renewable_energy_per)
            if len(b_prov) == 0:
                b_prov.update_or_create(**all_base_data)
            else:
                b_prov.update(**all_base_data)
            ## 保存更改

            # 设置提示信息
            self.message_user(request, '数据计算成功！')

    # 设置函数的显示名称
    prov_calculate_datas.short_description = '数据计算'
    # 添加到“动作”栏
    actions = ['prov_calculate_datas', 'get_datas']


class Calculated_valueAdmin(admin.ModelAdmin):
    search_fields = ['area', 'year', 'province']
    list_filter = ['province', 'area', 'year']
    list_display = ('province', 'area', 'year')
    fieldsets = (('地区年度数据计算', {
        'fields': (
            (
                'province', 'area', 'year',
            ),
            (
                'Cal_Raw_coal', 'Cal_Clean_coal', 'Cal_Coke', 'Cal_Briquette', 'Cal_Other_coking_products', 'Cal_Crude',
                'Cal_Fuel_oil', 'Cal_Gasoline', 'Cal_Diesel', 'Cal_Kerosene', 'Cal_Liquefied_petroleum_gas',
                'Cal_Refinery_dry_gas', 'Cal_Naphtha', 'Cal_Asphalt', 'Cal_Lubricating_oil', 'Cal_Petroleum_coke',
                'Cal_Natural_gas',
            ),
            (
                'GHG_Emission_a', 'CO2_Emission_a',
            ),
            (
                'Cal_Cement', 'Cal_Steel',
            ),
            (
                'GHG_Emission_b', 'CO2_Emission_b',
            ),
            (
                'Total_CO2_Emission',
            ),
            (
                'Cal_EF',
            ),
            (
                'r_d', 'per_unit_gdp', 'rural_urban', 'urban_per', 'rural_per', 'garbage', 'bus_per', 'urban_sewage',
                'edu_years', 'mortality', 'pension_cov', 'medical_cov', 'unemployment_cov', 'pm25', 'so2_emissions',
                'co2_per_gdp', 'cod_emissions', 'nh_emissions', 'water_per', 'water_per_gdp', 'planting_area', 'ef_per',
            ),
        )
    }),
                 )

    def calc_area_gep_score(self, request, queryset):
        for i in queryset:
            calc_area_data(i.province, i.area, i.year)
            self.message_user(request, '数据计算成功！')

    # 设置函数的显示名称
    calc_area_gep_score.short_description = 'GEP得分数据计算'
    # 添加到“动作”栏
    actions = ['calc_area_gep_score']


class Prov_Calculated_valueAdmin(admin.ModelAdmin):
    search_fields = ['year', 'province']
    list_filter = ['province', 'year']
    list_display = ('province', 'year')
    fieldsets = (('省级年度数据计算', {
        'fields': (
            (
                'province', 'year',
            ),
            (
                'Cal_Raw_coal', 'Cal_Clean_coal', 'Cal_Coke', 'Cal_Briquette', 'Cal_Other_coking_products', 'Cal_Crude',
                'Cal_Fuel_oil', 'Cal_Gasoline', 'Cal_Diesel', 'Cal_Kerosene', 'Cal_Liquefied_petroleum_gas',
                'Cal_Refinery_dry_gas', 'Cal_Naphtha', 'Cal_Asphalt', 'Cal_Lubricating_oil', 'Cal_Petroleum_coke',
                'Cal_Natural_gas',
            ),
            (
                'GHG_Emission_a', 'CO2_Emission_a',
            ),
            (
                'Cal_Cement', 'Cal_Steel',
            ),
            (
                'GHG_Emission_b', 'CO2_Emission_b',
            ),
            (
                'Total_CO2_Emission',
            ),
            (
                'Cal_EF',
            ),
            (
                'r_d', 'renewable_energy_per', 'per_unit_gdp', 'rural_urban', 'urban_per', 'rural_per', 'garbage',
                'bus_per', 'urban_sewage', 'edu_years', 'mortality', 'pension_cov', 'medical_cov', 'unemployment_cov',
                'pm25', 'so2_emissions', 'co2_per_gdp', 'cod_emissions', 'nh_emissions', 'water_per', 'water_per_gdp',
                'planting_area', 'ef_per',
            ),
        )
    }),
                 )

    def calc_prov_gep_score(self, request, queryset):
        for i in queryset:
            calc_prov_data(i.province, i.year)
            self.message_user(request, '数据计算成功！')

    # 设置函数的显示名称
    calc_prov_gep_score.short_description = 'GEP得分数据计算'
    # 添加到“动作”栏
    actions = ['calc_prov_gep_score']


class area_gep_scoreAdmin(admin.ModelAdmin):
    search_fields = ['area', 'year', 'province']
    list_filter = ['province', 'area', 'year']
    list_display = ('province', 'area', 'year')
    fieldsets = (
        ('地区', {
            'fields': ('province', 'area', 'year')
        }),
        ('单项指标得分', {
            'fields': ('r_d_score', 'per_unit_gdp_score', 'rural_urban_score', 'urban_per_score', 'rural_per_score',
                       'garbage_score', 'bus_per_score', 'urban_sewage_score', 'edu_years_score', 'mortality_score',
                       'pension_cov_score', 'medical_cov_score', 'unemployment_cov_score', 'pm25_score',
                       'so2_emissions_score', 'co2_per_gdp_score', 'cod_emissions_score', 'nh_emissions_score',
                       'water_per_score', 'water_per_gdp_score', 'planting_area_score', 'ef_per_score')
        }),
        ('单项GEP框架得分', {
            'fields': (
                'green_innovation', 'energy_use', 'parma_ratio', 'income', 'infrastructure', 'education',
                'life_expectancy',
                'social_security', 'air_pollution', 'greenhouse', 'nitrogen', 'water_withdrawal', 'land_use', 'EF')
        }),
        ('GEP+得分', {
            'fields': ('city_green_economy', 'city_sustainable', 'city_gep_plus')
        }),
    )


class prov_gep_scoreAdmin(admin.ModelAdmin):
    search_fields = ['year', 'province']
    list_filter = ['province', 'year']
    list_display = ('province', 'year')
    fieldsets = (
        ('地区', {
            'fields': ('province', 'year')
        }),
        ('单项指标得分', {
            'fields': (
                'r_d_score', 'per_unit_gdp_score', 'renewable_energy_per_score', 'rural_urban_score', 'urban_per_score',
                'rural_per_score', 'garbage_score', 'bus_per_score', 'urban_sewage_score', 'edu_years_score',
                'mortality_score', 'pension_cov_score', 'medical_cov_score', 'unemployment_cov_score', 'pm25_score',
                'so2_emissions_score', 'co2_per_gdp_score', 'cod_emissions_score', 'nh_emissions_score',
                'water_per_score',
                'water_per_gdp_score', 'planting_area_score', 'ef_per_score')
        }),
        ('单项GEP框架得分', {
            'fields': ('green_innovation', 'energy_use', 'renewable_energy', 'parma_ratio', 'income', 'infrastructure',
                       'education', 'life_expectancy', 'social_security', 'air_pollution', 'greenhouse', 'nitrogen',
                       'water_withdrawal', 'land_use', 'EF')
        }),
        ('GEP+得分', {
            'fields': ('city_green_economy', 'city_sustainable', 'city_gep_plus')
        }),
    )


class ImportFile_excelAdmin(admin.ModelAdmin):
    list_display = ('arealevel', 'province', 'year', 'excelfile', 'add_date')

    def gotfile(self, request, queryset):
        d = ImportFile_excel.objects.all()
        self.message_user(request, str(queryset[0].excelfile))

    def save_model(self, request, obj, form, change):
        self.message_user(request, str(obj.excelfile))
        # 输出文件路径
        print(obj.excelfile.path)
        # 输出数据级别
        print(obj.arealevel)
        # 输出省份
        print(obj.province)
        # 输出年度
        print(obj.year)
        print('*' * 30)
        obj.save()
        takedata(obj.excelfile.path, obj.arealevel, obj.province, obj.year)
        takedata_lastyear(obj.excelfile.path, obj.arealevel, obj.province, obj.year)
        return super().save_model(request, obj, form, change)

    # 设置函数的显示名称
    gotfile.short_description = '反馈文件名'
    # 添加到“动作”栏
    actions = ['gotfile']


admin.site.register(ConstantEg, ConstantEgAdmin)
admin.site.register(Annual_data, Annual_dataAdmin)
admin.site.register(Prov_Annual_data, Prov_Annual_dataAdmin)
admin.site.register(Calculated_value, Calculated_valueAdmin)
admin.site.register(Prov_Calculated_value, Prov_Calculated_valueAdmin)
admin.site.register(ImportFile_excel, ImportFile_excelAdmin)
admin.site.register(area_gep_score, area_gep_scoreAdmin)
admin.site.register(prov_gep_score, prov_gep_scoreAdmin)
