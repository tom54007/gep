from django.db import models
from work.models import can_not_equal_zero
# from .caldata import *

# Create your models here.

# 能源常量
class ConstantEg(models.Model):
    # 单位热值
    Raw_coal = models.FloatField(verbose_name='原煤', null=False, blank=False, validators=[can_not_equal_zero])
    Clean_coal = models.FloatField(verbose_name='洗精煤', null=False, blank=False, validators=[can_not_equal_zero])
    Coke = models.FloatField(verbose_name='焦炭', null=False, blank=False, validators=[can_not_equal_zero])
    Briquette = models.FloatField(verbose_name='型煤', null=False, blank=False, validators=[can_not_equal_zero])
    Other_coking_products = models.FloatField(verbose_name='其他焦化产品', null=False, blank=False, validators=[can_not_equal_zero])
    Crude = models.FloatField(verbose_name='原油', null=False, blank=False, validators=[can_not_equal_zero])
    Fuel_oil = models.FloatField(verbose_name='燃料油', null=False, blank=False, validators=[can_not_equal_zero])
    Gasoline = models.FloatField(verbose_name='汽油', null=False, blank=False, validators=[can_not_equal_zero])
    Diesel = models.FloatField(verbose_name='柴油', null=False, blank=False, validators=[can_not_equal_zero])
    Kerosene = models.FloatField(verbose_name='煤油', null=False, blank=False, validators=[can_not_equal_zero])
    Liquefied_petroleum_gas = models.FloatField(verbose_name='液化石油气', null=False, blank=False, validators=[can_not_equal_zero])
    Refinery_dry_gas = models.FloatField(verbose_name='炼厂干气', null=False, blank=False, validators=[can_not_equal_zero])
    Naphtha = models.FloatField(verbose_name='石脑油', null=False, blank=False, validators=[can_not_equal_zero])
    Asphalt = models.FloatField(verbose_name='沥青', null=False, blank=False, validators=[can_not_equal_zero])
    Lubricating_oil = models.FloatField(verbose_name='润滑油', null=False, blank=False, validators=[can_not_equal_zero])
    Petroleum_coke = models.FloatField(verbose_name='石油焦', null=False, blank=False, validators=[can_not_equal_zero])
    Natural_gas = models.FloatField(verbose_name='天然气', null=False, blank=False, validators=[can_not_equal_zero])

    Cement = models.FloatField(verbose_name='水泥', null=False, blank=False, validators=[can_not_equal_zero])
    Steel = models.FloatField(verbose_name='钢铁', null=False, blank=False, validators=[can_not_equal_zero])
    # 产量因子NPP
    Farmland = models.FloatField(verbose_name='农地', null=False, blank=False, validators=[can_not_equal_zero])
    Woodland = models.FloatField(verbose_name='林地', null=False, blank=False, validators=[can_not_equal_zero])
    Pastureland = models.FloatField(verbose_name='畜牧地', null=False, blank=False, validators=[can_not_equal_zero])
    Fishing_ground = models.FloatField(verbose_name='渔场', null=False, blank=False, validators=[can_not_equal_zero])
    Construction_land = models.FloatField(verbose_name='建设用地', null=False, blank=False, validators=[can_not_equal_zero])

    # 能源热值
    Raw_coal_MJ = models.FloatField(verbose_name='原煤热值', null=False, blank=False, validators=[can_not_equal_zero])
    Clean_coal_MJ = models.FloatField(verbose_name='洗精煤热值', null=False, blank=False, validators=[can_not_equal_zero])
    Coke_MJ = models.FloatField(verbose_name='焦炭热值', null=False, blank=False, validators=[can_not_equal_zero])
    Briquette_MJ = models.FloatField(verbose_name='型煤热值', null=False, blank=False, validators=[can_not_equal_zero])
    Other_coking_products_MJ = models.FloatField(verbose_name='其他焦化产品热值', null=False, blank=False, validators=[can_not_equal_zero])
    Crude_MJ = models.FloatField(verbose_name='原油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Fuel_oil_MJ = models.FloatField(verbose_name='燃料油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Gasoline_MJ = models.FloatField(verbose_name='汽油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Diesel_MJ = models.FloatField(verbose_name='柴油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Kerosene_MJ = models.FloatField(verbose_name='煤油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Liquefied_petroleum_gas_MJ = models.FloatField(verbose_name='液化石油气热值', null=False, blank=False, validators=[can_not_equal_zero])
    Refinery_dry_gas_MJ = models.FloatField(verbose_name='炼厂干气热值', null=False, blank=False, validators=[can_not_equal_zero])
    Naphtha_MJ = models.FloatField(verbose_name='石脑油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Asphalt_MJ = models.FloatField(verbose_name='沥青热值', null=False, blank=False, validators=[can_not_equal_zero])
    Lubricating_oil_MJ = models.FloatField(verbose_name='润滑油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Petroleum_coke_MJ = models.FloatField(verbose_name='石油焦热值', null=False, blank=False, validators=[can_not_equal_zero])
    Natural_gas_MJ = models.FloatField(verbose_name='天然气热值', null=False, blank=False, validators=[can_not_equal_zero])

    class Meta:
        verbose_name = '能源常量'


# 地区数据
# 年度数据
class Annual_data(models.Model):
    # province = models.ForeignKey(to=Province, null=False, blank=False, on_delete=models.CASCADE, verbose_name='省份', related_name='data_record_ls')
    # area = models.ForeignKey(to=Area, null=False, blank=False, on_delete=models.CASCADE, verbose_name='地区', related_name='data_record_ls')
    province = models.CharField(max_length=50, verbose_name='省份', null=False, blank=False)
    area = models.CharField(max_length=50, verbose_name='地区', null=False, blank=False)
    year = models.IntegerField(verbose_name='年度', null=False, blank=False)
    # 年度能源消耗量
    Consume_Raw_coal = models.FloatField(verbose_name='原煤消耗量')
    Consume_Clean_coal = models.FloatField(verbose_name='洗精煤消耗量')
    Consume_Coke = models.FloatField(verbose_name='焦炭消耗量')
    Consume_Briquette = models.FloatField(verbose_name='型煤消耗量')
    Consume_Other_coking_products = models.FloatField(verbose_name='其他焦化产品消耗量')
    Consume_Crude = models.FloatField(verbose_name='原油消耗量')
    Consume_Fuel_oil = models.FloatField(verbose_name='燃料油消耗量')
    Consume_Gasoline = models.FloatField(verbose_name='汽油消耗量')
    Consume_Diesel = models.FloatField(verbose_name='柴油消耗量')
    Consume_Kerosene = models.FloatField(verbose_name='煤油消耗量')
    Consume_Liquefied_petroleum_gas = models.FloatField(verbose_name='液化石油气消耗量')
    Consume_Refinery_dry_gas = models.FloatField(verbose_name='炼厂干气消耗量')
    Consume_Naphtha = models.FloatField(verbose_name='石脑油消耗量')
    Consume_Asphalt = models.FloatField(verbose_name='沥青消耗量')
    Consume_Lubricating_oil = models.FloatField(verbose_name='润滑油消耗量')
    Consume_Petroleum_coke = models.FloatField(verbose_name='石油焦消耗量')
    Consume_Natural_gas = models.FloatField(verbose_name='天然气消耗量')

    Consume_Cement = models.FloatField(verbose_name='水泥消耗量')
    Consume_Steel = models.FloatField(verbose_name='钢铁消耗量')
    # 年度土地消耗量
    Consume_Farmland = models.FloatField(verbose_name='农地消耗量')
    Consume_Woodland = models.FloatField(verbose_name='林地消耗量')
    Consume_Pastureland = models.FloatField(verbose_name='畜牧地消耗量')
    Consume_Fishing_ground = models.FloatField(verbose_name='渔场消耗量')
    Consume_Construction_land = models.FloatField(verbose_name='建设用地消耗量')

    # 年度国民经济数据
    GDP = models.FloatField(verbose_name='地区当年生产总值', null=False, blank=False)
    Sown_area = models.FloatField(verbose_name='地区当年播种面积', null=False, blank=False)
    Total_population = models.FloatField(verbose_name='地区当年总人口', null=False, blank=False)
    Total_power_generation = models.FloatField(verbose_name='地区当年总发电量', null=False, blank=False)
    Total_energy_consumption = models.FloatField(verbose_name='地区当年能源消费总量', null=False, blank=False)
    Carbon_dioxide_emissions = models.FloatField(verbose_name='地区当年二氧化碳排放量', null=False, blank=False)
    Total_water_consumption = models.FloatField(verbose_name='地区当年用水总量', null=False, blank=False)
    The_total_area = models.FloatField(verbose_name='地区当年总面积', null=False, blank=False)
    Ecological_footprint = models.FloatField(verbose_name='地区当年生态足迹', null=False, blank=False)
    Number_of_employees_in_basic_pension_insurance = models.FloatField(verbose_name='地区当年基本养老保险职工人数', null=False, blank=False)
    Number_of_basic_medical_insurance = models.FloatField(verbose_name='地区当年基本医疗保险人数', null=False, blank=False)
    Number_of_unemployment_insurance = models.FloatField(verbose_name='地区当年失业保险人数', null=False, blank=False)
    Nuclear_power_generation = models.FloatField(verbose_name='地区当年核电发电量', null=False, blank=False)
    Wind_power_generation = models.FloatField(verbose_name='地区当年风电发电量', null=False, blank=False)
    Hydropower_generation = models.FloatField(verbose_name='地区当年水电发电量', null=False, blank=False)
    Photovoltaic_power_generation = models.FloatField(verbose_name='地区当年光伏发电量', null=False, blank=False)
    Primary_school_number = models.FloatField(verbose_name='小学人数', null=False, blank=False)
    Number_of_junior_high_school = models.FloatField(verbose_name='初中人数', null=False, blank=False)
    High_school_number = models.FloatField(verbose_name='高中人数', null=False, blank=False)
    University_and_above = models.FloatField(verbose_name='大学及以上人数', null=False, blank=False)



    class Meta:
        ordering = '-year', 'area' ,'province'
        verbose_name = '地区年度原始数据'
        verbose_name_plural = verbose_name
        unique_together = [('province', 'area', 'year')]

    def __str__(self):
        return f'{self.province}, {self.area}, {self.year}'


# 计算字段
class Calculated_value(models.Model):
    # province = models.ForeignKey(to=Province, null=False, blank=False, on_delete=models.CASCADE, verbose_name='省份', related_name='data_record_ls')
    # area = models.ForeignKey(to=Area, null=False, blank=False, on_delete=models.CASCADE, verbose_name='地区', related_name='data_record_ls')
    province = models.CharField(max_length=50, verbose_name='省份', null=False, blank=False)
    area = models.CharField(max_length=50, verbose_name='地区', null=False, blank=False)
    year = models.IntegerField(verbose_name='年度', null=False, blank=False)
    
    Cal_Raw_coal = models.FloatField(verbose_name='原煤_年度计算值', null=True, blank=True)
    Cal_Clean_coal = models.FloatField(verbose_name='洗精煤_年度计算值', null=True, blank=True)
    Cal_Coke = models.FloatField(verbose_name='焦炭_年度计算值', null=True, blank=True)
    Cal_Briquette = models.FloatField(verbose_name='型煤_年度计算值', null=True, blank=True)
    Cal_Other_coking_products = models.FloatField(verbose_name='其他焦化产品_年度计算值', null=True, blank=True)
    Cal_Crude = models.FloatField(verbose_name='原油_年度计算值', null=True, blank=True)
    Cal_Fuel_oil = models.FloatField(verbose_name='燃料油_年度计算值', null=True, blank=True)
    Cal_Gasoline = models.FloatField(verbose_name='汽油_年度计算值', null=True, blank=True)
    Cal_Diesel = models.FloatField(verbose_name='柴油_年度计算值', null=True, blank=True)
    Cal_Kerosene = models.FloatField(verbose_name='煤油_年度计算值', null=True, blank=True)
    Cal_Liquefied_petroleum_gas = models.FloatField(verbose_name='液化石油气_年度计算值', null=True, blank=True)
    Cal_Refinery_dry_gas = models.FloatField(verbose_name='炼厂干气_年度计算值', null=True, blank=True)
    Cal_Naphtha = models.FloatField(verbose_name='石脑油_年度计算值', null=True, blank=True)
    Cal_Asphalt = models.FloatField(verbose_name='沥青_年度计算值', null=True, blank=True)
    Cal_Lubricating_oil = models.FloatField(verbose_name='润滑油_年度计算值', null=True, blank=True)
    Cal_Petroleum_coke = models.FloatField(verbose_name='石油焦_年度计算值', null=True, blank=True)
    Cal_Natural_gas = models.FloatField(verbose_name='天然气_年度计算值', null=True, blank=True)
    GHG_Emission_a  = models.FloatField(verbose_name='温室气体排放量_年度计算值', null=True, blank=True)
    CO2_Emission_a = models.FloatField(verbose_name='二氧化碳排放量_年度计算值', null=True, blank=True)
    Cal_Cement = models.FloatField(verbose_name='水泥_年度计算值', null=True, blank=True)
    Cal_Steel = models.FloatField(verbose_name='钢铁_年度计算值', null=True, blank=True)
    GHG_Emission_b  = models.FloatField(verbose_name='温室气体排放量_年度计算值', null=True, blank=True)
    CO2_Emission_b = models.FloatField(verbose_name='二氧化碳排放量_年度计算值', null=True, blank=True)
    Total_CO2_Emission = models.FloatField(verbose_name='二氧化碳排放总量_年度计算值', null=True, blank=True)
    Cal_EF = models.FloatField(verbose_name='生态足迹_年度计算值', null=True, blank=True)

    # 基础指标
    per_unit_gdp = models.FloatField(verbose_name='单位GDP能耗', null=True, blank=True)
    co2_per_gdp = models.FloatField(verbose_name='单位GDP二氧化碳排放量', null=True, blank=True)
    water_per_gdp = models.FloatField(verbose_name='单位GDP用水量', null=True, blank=True)
    planting_area = models.FloatField(verbose_name='播种面积占比', null=True, blank=True)
    edu_years = models.FloatField(verbose_name='平均受教育年限', null=True, blank=True)
    ef_per = models.FloatField(verbose_name='人均生态足迹', null=True, blank=True)
    water_per = models.FloatField(verbose_name='人均用水量', null=True, blank=True)
    pension_cov = models.FloatField(verbose_name='养老保险覆盖率', null=True, blank=True)
    medical_cov = models.FloatField(verbose_name='医疗保险覆盖率', null=True, blank=True)
    unemployment_cov = models.FloatField(verbose_name='失业保险覆盖率', null=True, blank=True)
    renewable_energy_per = models.FloatField(verbose_name='可再生能源供给占比(省)', null=True, blank=True)


    class Meta:
        ordering = '-year', 'area', 'province'
        verbose_name = '地区年度计算值'
        verbose_name_plural = verbose_name
        unique_together = [('province', 'area', 'year')]

    def __str__(self):
        return f'{self.province}, {self.area}, {self.year}'



# 省级数据
# 年度数据
class Prov_Annual_data(models.Model):
    # province = models.ForeignKey(to=Province, null=False, blank=False, on_delete=models.CASCADE, verbose_name='省份', related_name='data_record_ls')
    # area = models.ForeignKey(to=Area, null=False, blank=False, on_delete=models.CASCADE, verbose_name='地区', related_name='data_record_ls')
    province = models.CharField(max_length=255, verbose_name='省份', null=False, blank=False)
    year = models.IntegerField(verbose_name='年度', null=False, blank=False)
    # 年度能源消耗量
    Consume_Raw_coal = models.FloatField(verbose_name='原煤消耗量')
    Consume_Clean_coal = models.FloatField(verbose_name='洗精煤消耗量')
    Consume_Coke = models.FloatField(verbose_name='焦炭消耗量')
    Consume_Briquette = models.FloatField(verbose_name='型煤消耗量')
    Consume_Other_coking_products = models.FloatField(verbose_name='其他焦化产品消耗量')
    Consume_Crude = models.FloatField(verbose_name='原油消耗量')
    Consume_Fuel_oil = models.FloatField(verbose_name='燃料油消耗量')
    Consume_Gasoline = models.FloatField(verbose_name='汽油消耗量')
    Consume_Diesel = models.FloatField(verbose_name='柴油消耗量')
    Consume_Kerosene = models.FloatField(verbose_name='煤油消耗量')
    Consume_Liquefied_petroleum_gas = models.FloatField(verbose_name='液化石油气消耗量')
    Consume_Refinery_dry_gas = models.FloatField(verbose_name='炼厂干气消耗量')
    Consume_Naphtha = models.FloatField(verbose_name='石脑油消耗量')
    Consume_Asphalt = models.FloatField(verbose_name='沥青消耗量')
    Consume_Lubricating_oil = models.FloatField(verbose_name='润滑油消耗量')
    Consume_Petroleum_coke = models.FloatField(verbose_name='石油焦消耗量')
    Consume_Natural_gas = models.FloatField(verbose_name='天然气消耗量')

    Consume_Cement = models.FloatField(verbose_name='水泥消耗量')
    Consume_Steel = models.FloatField(verbose_name='钢铁消耗量')
    # 年度土地消耗量
    Consume_Farmland = models.FloatField(verbose_name='农地消耗量')
    Consume_Woodland = models.FloatField(verbose_name='林地消耗量')
    Consume_Pastureland = models.FloatField(verbose_name='畜牧地消耗量')
    Consume_Fishing_ground = models.FloatField(verbose_name='渔场消耗量')
    Consume_Construction_land = models.FloatField(verbose_name='建设用地消耗量')

    # 年度国民经济数据
    GDP = models.FloatField(verbose_name='地区当年生产总值', null=False, blank=False)
    Sown_area = models.FloatField(verbose_name='地区当年播种面积', null=False, blank=False)
    Total_population = models.FloatField(verbose_name='地区当年总人口', null=False, blank=False)
    Total_power_generation = models.FloatField(verbose_name='地区当年总发电量', null=False, blank=False)
    Total_energy_consumption = models.FloatField(verbose_name='地区当年能源消费总量', null=False, blank=False)
    Carbon_dioxide_emissions = models.FloatField(verbose_name='地区当年二氧化碳排放量', null=False, blank=False)
    Total_water_consumption = models.FloatField(verbose_name='地区当年用水总量', null=False, blank=False)
    The_total_area = models.FloatField(verbose_name='地区当年总面积', null=False, blank=False)
    Ecological_footprint = models.FloatField(verbose_name='地区当年生态足迹', null=False, blank=False)
    Number_of_employees_in_basic_pension_insurance = models.FloatField(verbose_name='地区当年基本养老保险职工人数', null=False, blank=False)
    Number_of_basic_medical_insurance = models.FloatField(verbose_name='地区当年基本医疗保险人数', null=False, blank=False)
    Number_of_unemployment_insurance = models.FloatField(verbose_name='地区当年失业保险人数', null=False, blank=False)
    Nuclear_power_generation = models.FloatField(verbose_name='地区当年核电发电量', null=False, blank=False)
    Wind_power_generation = models.FloatField(verbose_name='地区当年风电发电量', null=False, blank=False)
    Hydropower_generation = models.FloatField(verbose_name='地区当年水电发电量', null=False, blank=False)
    Photovoltaic_power_generation = models.FloatField(verbose_name='地区当年光伏发电量', null=False, blank=False)
    Primary_school_number = models.FloatField(verbose_name='小学人数', null=False, blank=False)
    Number_of_junior_high_school = models.FloatField(verbose_name='初中人数', null=False, blank=False)
    High_school_number = models.FloatField(verbose_name='高中人数', null=False, blank=False)
    University_and_above = models.FloatField(verbose_name='大学及以上人数', null=False, blank=False)

    class Meta:
        ordering = '-year', 'province'
        verbose_name = '省级年度原始数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.province},{self.year}'


# 计算字段
class Prov_Calculated_value(models.Model):
    # province = models.ForeignKey(to=Province, null=False, blank=False, on_delete=models.CASCADE, verbose_name='省份', related_name='data_record_ls')
    # area = models.ForeignKey(to=Area, null=False, blank=False, on_delete=models.CASCADE, verbose_name='地区', related_name='data_record_ls')
    province = models.CharField(max_length=255, verbose_name='省份', null=False, blank=False)
    year = models.IntegerField(verbose_name='年度', null=False, blank=False)
    Cal_Raw_coal = models.FloatField(verbose_name='原煤_年度计算值', null=True, blank=True)
    Cal_Clean_coal = models.FloatField(verbose_name='洗精煤_年度计算值', null=True, blank=True)
    Cal_Coke = models.FloatField(verbose_name='焦炭_年度计算值', null=True, blank=True)
    Cal_Briquette = models.FloatField(verbose_name='型煤_年度计算值', null=True, blank=True)
    Cal_Other_coking_products = models.FloatField(verbose_name='其他焦化产品_年度计算值', null=True, blank=True)
    Cal_Crude = models.FloatField(verbose_name='原油_年度计算值', null=True, blank=True)
    Cal_Fuel_oil = models.FloatField(verbose_name='燃料油_年度计算值', null=True, blank=True)
    Cal_Gasoline = models.FloatField(verbose_name='汽油_年度计算值', null=True, blank=True)
    Cal_Diesel = models.FloatField(verbose_name='柴油_年度计算值', null=True, blank=True)
    Cal_Kerosene = models.FloatField(verbose_name='煤油_年度计算值', null=True, blank=True)
    Cal_Liquefied_petroleum_gas = models.FloatField(verbose_name='液化石油气_年度计算值', null=True, blank=True)
    Cal_Refinery_dry_gas = models.FloatField(verbose_name='炼厂干气_年度计算值', null=True, blank=True)
    Cal_Naphtha = models.FloatField(verbose_name='石脑油_年度计算值', null=True, blank=True)
    Cal_Asphalt = models.FloatField(verbose_name='沥青_年度计算值', null=True, blank=True)
    Cal_Lubricating_oil = models.FloatField(verbose_name='润滑油_年度计算值', null=True, blank=True)
    Cal_Petroleum_coke = models.FloatField(verbose_name='石油焦_年度计算值', null=True, blank=True)
    Cal_Natural_gas = models.FloatField(verbose_name='天然气_年度计算值', null=True, blank=True)
    GHG_Emission_a  = models.FloatField(verbose_name='温室气体排放量_年度计算值', null=True, blank=True)
    CO2_Emission_a = models.FloatField(verbose_name='二氧化碳排放量_年度计算值', null=True, blank=True)
    Cal_Cement = models.FloatField(verbose_name='水泥_年度计算值', null=True, blank=True)
    Cal_Steel = models.FloatField(verbose_name='钢铁_年度计算值', null=True, blank=True)
    GHG_Emission_b  = models.FloatField(verbose_name='温室气体排放量_年度计算值', null=True, blank=True)
    CO2_Emission_b = models.FloatField(verbose_name='二氧化碳排放量_年度计算值', null=True, blank=True)
    Total_CO2_Emission = models.FloatField(verbose_name='二氧化碳排放总量_年度计算值', null=True, blank=True)
    Cal_EF = models.FloatField(verbose_name='生态足迹_年度计算值', null=True, blank=True)

    # 基础指标
    per_unit_gdp = models.FloatField(verbose_name='单位GDP能耗', null=True, blank=True)
    co2_per_gdp = models.FloatField(verbose_name='单位GDP二氧化碳排放量', null=True, blank=True)
    water_per_gdp = models.FloatField(verbose_name='单位GDP用水量', null=True, blank=True)
    planting_area = models.FloatField(verbose_name='播种面积占比', null=True, blank=True)
    edu_years = models.FloatField(verbose_name='平均受教育年限', null=True, blank=True)
    ef_per = models.FloatField(verbose_name='人均生态足迹', null=True, blank=True)
    water_per = models.FloatField(verbose_name='人均用水量', null=True, blank=True)
    pension_cov = models.FloatField(verbose_name='养老保险覆盖率', null=True, blank=True)
    medical_cov = models.FloatField(verbose_name='医疗保险覆盖率', null=True, blank=True)
    unemployment_cov = models.FloatField(verbose_name='失业保险覆盖率', null=True, blank=True)
    renewable_energy_per = models.FloatField(verbose_name='可再生能源供给占比(省)', null=True, blank=True)

    class Meta:
        ordering = '-year', 'province'
        verbose_name = '省级年度计算值'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.province},{self.year}'
