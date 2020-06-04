from django.contrib import admin

from .models import ConstantEg, Annual_data, Prov_Annual_data, Calculated_value, Prov_Calculated_value
from .caldata import *


# Register your models here.

# 常量编辑

class ConstantEgAdmin(admin.ModelAdmin):
    list_display = ('Raw_coal','Clean_coal','Coke','Briquette','Other_coking_products','Crude','Fuel_oil','Gasoline','Diesel','Kerosene','Liquefied_petroleum_gas','Refinery_dry_gas','Naphtha','Asphalt','Lubricating_oil','Petroleum_coke','Natural_gas','Cement','Steel','Farmland','Woodland','Pastureland','Fishing_ground','Construction_land',)

    fieldsets = (
        ('常量编辑', {
            'fields': (
                (
                    'Raw_coal', 'Raw_coal_MJ', 'Clean_coal', 'Clean_coal_MJ', 'Coke', 'Coke_MJ', 'Briquette', 'Briquette_MJ', 'Other_coking_products',
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
    list_display = ('province', 'area', 'year')
    fieldsets = (('地区年度数据', {
            'fields': (
                (
                    'province', 'area', 'year',
                ),
                (
                    'Consume_Raw_coal', 'Consume_Clean_coal','Consume_Coke','Consume_Briquette','Consume_Other_coking_products','Consume_Crude','Consume_Fuel_oil','Consume_Gasoline','Consume_Diesel','Consume_Kerosene','Consume_Liquefied_petroleum_gas','Consume_Refinery_dry_gas','Consume_Naphtha','Consume_Asphalt','Consume_Lubricating_oil','Consume_Petroleum_coke','Consume_Natural_gas',
                ),
                (
                    'Consume_Cement', 'Consume_Steel',
                ),
                (
                    'Consume_Farmland','Consume_Woodland','Consume_Pastureland','Consume_Fishing_ground','Consume_Construction_land',
                ),
                (
                    'GDP','Sown_area','Total_population','Total_power_generation','Total_energy_consumption','Carbon_dioxide_emissions','Total_water_consumption','The_total_area','Ecological_footprint','Number_of_employees_in_basic_pension_insurance','Number_of_basic_medical_insurance','Number_of_unemployment_insurance','Nuclear_power_generation','Wind_power_generation','Hydropower_generation','Photovoltaic_power_generation','Primary_school_number','Number_of_junior_high_school','High_school_number','University_and_above',
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
        # for d in queryset:
        d = queryset[0]
        # 能源类碳排放计算
        t0=(d.Consume_Raw_coal*con[0].Raw_coal*con[0].Raw_coal_MJ)/(10**8)
        t1=(d.Consume_Clean_coal*con[0].Clean_coal*con[0].Clean_coal_MJ)/(10**8)
        t2=(d.Consume_Coke*con[0].Coke*con[0].Coke_MJ)/(10**8)
        t3=(d.Consume_Briquette*con[0].Briquette*con[0].Briquette_MJ)/(10**8)
        t4=(d.Consume_Other_coking_products*con[0].Other_coking_products*con[0].Other_coking_products_MJ)/(10**8)
        t5=(d.Consume_Crude*con[0].Crude*con[0].Crude_MJ)/(10**8)
        t6=(d.Consume_Fuel_oil*con[0].Fuel_oil*con[0].Fuel_oil_MJ)/(10**8)
        t7=(d.Consume_Gasoline*con[0].Gasoline*con[0].Gasoline_MJ)/(10**8)
        t8=(d.Consume_Diesel*con[0].Diesel*con[0].Diesel_MJ)/(10**8)
        t9=(d.Consume_Kerosene*con[0].Kerosene*con[0].Kerosene_MJ)/(10**8)
        t10=(d.Consume_Liquefied_petroleum_gas*con[0].Liquefied_petroleum_gas*con[0].Liquefied_petroleum_gas_MJ)/(10**8)
        t11=(d.Consume_Refinery_dry_gas*con[0].Refinery_dry_gas*con[0].Refinery_dry_gas_MJ)/(10**8)
        t12=(d.Consume_Naphtha*con[0].Naphtha*con[0].Naphtha_MJ)/(10**8)
        t13=(d.Consume_Asphalt*con[0].Asphalt*con[0].Asphalt_MJ)/(10**8)
        t14=(d.Consume_Lubricating_oil*con[0].Lubricating_oil*con[0].Lubricating_oil_MJ)/(10**8)
        t15=(d.Consume_Petroleum_coke*con[0].Petroleum_coke*con[0].Petroleum_coke_MJ)/(10**8)
        t16=(d.Consume_Natural_gas*con[0].Natural_gas*con[0].Natural_gas_MJ)/(10**7)
        eg_l = [t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16]
        ## 温室气体排放量 GHG Emission 
        eg_l_sum = sum(eg_l)*10
        ## 二氧化碳排放量 CO2 Emission
        eg_l_co2 = eg_l_sum*44/12
        # 工业生产过程碳排放
        t17=(d.Consume_Cement*con[0].Cement)/100000
        t18=(d.Consume_Steel*con[0].Steel)/100000
        indus_l = [t17, t18]
        ## 温室气体排放量 GHG Emission
        indus_l_sum = sum(indus_l)*10
        ## 二氧化碳排放量 CO2 Emission
        indus_l_co2 = indus_l_sum*44/12
        # 二氧化碳排放总量 Total CO2 Emission
        total_co2 = eg_l_co2 + indus_l_co2

        self.message_user(request, total_co2)
        # 设置提示信息
        self.message_user(request, '数据计算成功！')

    # 设置函数的显示名称
    calculate_datas.short_description = '数据计算'
    # 添加到“动作”栏
    actions = ['calculate_datas', 'get_datas']

class Prov_Annual_dataAdmin(admin.ModelAdmin):
    list_display = ('province', 'year')
    fieldsets = (('省级年度数据', {
            'fields': (
                (
                    'province', 'year',
                ),
                (
                    'Consume_Raw_coal', 'Consume_Clean_coal','Consume_Coke','Consume_Briquette','Consume_Other_coking_products','Consume_Crude','Consume_Fuel_oil','Consume_Gasoline','Consume_Diesel','Consume_Kerosene','Consume_Liquefied_petroleum_gas','Consume_Refinery_dry_gas','Consume_Naphtha','Consume_Asphalt','Consume_Lubricating_oil','Consume_Petroleum_coke','Consume_Natural_gas',
                ),
                (
                    'Consume_Cement', 'Consume_Steel',
                ),
                (
                    'Consume_Farmland','Consume_Woodland','Consume_Pastureland','Consume_Fishing_ground','Consume_Construction_land',
                ),
                (
                    'per_unit_gdp','co2_per_gdp','water_per_gdp','planting_area','edu_years','ef_per','water_per','pension_cov','medical_cov','unemployment_cov','renewable_energy_per',
                ),
                (
                    'GDP','Sown_area','Total_population','Total_power_generation','Total_energy_consumption','Carbon_dioxide_emissions','Total_water_consumption','The_total_area','Ecological_footprint','Number_of_employees_in_basic_pension_insurance','Number_of_basic_medical_insurance','Number_of_unemployment_insurance','Nuclear_power_generation','Wind_power_generation','Hydropower_generation','Photovoltaic_power_generation','Primary_school_number','Number_of_junior_high_school','High_school_number','University_and_above',
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
    
    def calculate_datas(self, request, queryset):
        # temp = []
        # for d in queryset:
        #     t = [d.job, d.title, str(d.payment), d.person.name]
        #     temp.append(t)
        # f = open('d://data.txt', 'a')
        # for t in temp:
        #     f.write(','.join(t) + '\r\n')
        # f.close()
        # 设置提示信息
        self.message_user(request, '数据计算成功！')

    # 设置函数的显示名称
    calculate_datas.short_description = '数据计算'
    # 添加到“动作”栏
    actions = ['calculate_datas', 'get_datas']


class Calculated_valueAdmin(admin.ModelAdmin):
    list_display = ('province', 'area', 'year')
    fieldsets = (('地区年度数据计算', {
            'fields': (
                (
                    'province', 'area', 'year',
                ),
                (
                    'Cal_Raw_coal', 'Cal_Clean_coal','Cal_Coke','Cal_Briquette','Cal_Other_coking_products','Cal_Crude','Cal_Fuel_oil','Cal_Gasoline','Cal_Diesel','Cal_Kerosene','Cal_Liquefied_petroleum_gas','Cal_Refinery_dry_gas','Cal_Naphtha','Cal_Asphalt','Cal_Lubricating_oil','Cal_Petroleum_coke','Cal_Natural_gas',
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
                    'per_unit_gdp','co2_per_gdp','water_per_gdp','planting_area','edu_years','ef_per','water_per','pension_cov','medical_cov','unemployment_cov','renewable_energy_per',
                ),
            )
        }),
    )


class Prov_Calculated_valueAdmin(admin.ModelAdmin):
    list_display = ('province', 'year')
    fieldsets = (('省级年度数据计算', {
            'fields': (
                (
                    'province', 'year',
                ),
                (
                    'Cal_Raw_coal', 'Cal_Clean_coal','Cal_Coke','Cal_Briquette','Cal_Other_coking_products','Cal_Crude','Cal_Fuel_oil','Cal_Gasoline','Cal_Diesel','Cal_Kerosene','Cal_Liquefied_petroleum_gas','Cal_Refinery_dry_gas','Cal_Naphtha','Cal_Asphalt','Cal_Lubricating_oil','Cal_Petroleum_coke','Cal_Natural_gas',
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
                    'per_unit_gdp','co2_per_gdp','water_per_gdp','planting_area','edu_years','ef_per','water_per','pension_cov','medical_cov','unemployment_cov','renewable_energy_per',
                ),
            )
        }),
    )




admin.site.register(ConstantEg, ConstantEgAdmin)
admin.site.register(Annual_data, Annual_dataAdmin)
admin.site.register(Prov_Annual_data, Prov_Annual_dataAdmin)
admin.site.register(Calculated_value, Calculated_valueAdmin)
admin.site.register(Prov_Calculated_value, Prov_Calculated_valueAdmin)
