from django.db import models
from work.models import can_not_equal_zero, Province
import django.utils.timezone as timezone


# from .caldata import *

# Create your models here.

# 能源常量
class ConstantEg(models.Model):
    # 单位热值
    Raw_coal = models.FloatField(verbose_name='原煤', null=False, blank=False, validators=[can_not_equal_zero])
    Clean_coal = models.FloatField(verbose_name='洗精煤', null=False, blank=False, validators=[can_not_equal_zero])
    Coke = models.FloatField(verbose_name='焦炭', null=False, blank=False, validators=[can_not_equal_zero])
    Briquette = models.FloatField(verbose_name='型煤', null=False, blank=False, validators=[can_not_equal_zero])
    Other_coking_products = models.FloatField(verbose_name='其他焦化产品', null=False, blank=False,
                                              validators=[can_not_equal_zero])
    Crude = models.FloatField(verbose_name='原油', null=False, blank=False, validators=[can_not_equal_zero])
    Fuel_oil = models.FloatField(verbose_name='燃料油', null=False, blank=False, validators=[can_not_equal_zero])
    Gasoline = models.FloatField(verbose_name='汽油', null=False, blank=False, validators=[can_not_equal_zero])
    Diesel = models.FloatField(verbose_name='柴油', null=False, blank=False, validators=[can_not_equal_zero])
    Kerosene = models.FloatField(verbose_name='煤油', null=False, blank=False, validators=[can_not_equal_zero])
    Liquefied_petroleum_gas = models.FloatField(verbose_name='液化石油气', null=False, blank=False,
                                                validators=[can_not_equal_zero])
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
    Other_coking_products_MJ = models.FloatField(verbose_name='其他焦化产品热值', null=False, blank=False,
                                                 validators=[can_not_equal_zero])
    Crude_MJ = models.FloatField(verbose_name='原油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Fuel_oil_MJ = models.FloatField(verbose_name='燃料油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Gasoline_MJ = models.FloatField(verbose_name='汽油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Diesel_MJ = models.FloatField(verbose_name='柴油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Kerosene_MJ = models.FloatField(verbose_name='煤油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Liquefied_petroleum_gas_MJ = models.FloatField(verbose_name='液化石油气热值', null=False, blank=False,
                                                   validators=[can_not_equal_zero])
    Refinery_dry_gas_MJ = models.FloatField(verbose_name='炼厂干气热值', null=False, blank=False,
                                            validators=[can_not_equal_zero])
    Naphtha_MJ = models.FloatField(verbose_name='石脑油热值', null=False, blank=False, validators=[can_not_equal_zero])
    Asphalt_MJ = models.FloatField(verbose_name='沥青热值', null=False, blank=False, validators=[can_not_equal_zero])
    Lubricating_oil_MJ = models.FloatField(verbose_name='润滑油热值', null=False, blank=False,
                                           validators=[can_not_equal_zero])
    Petroleum_coke_MJ = models.FloatField(verbose_name='石油焦热值', null=False, blank=False,
                                          validators=[can_not_equal_zero])
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
    Consume_Briquette = models.FloatField(verbose_name='型煤消耗量', default=0)
    Consume_Other_coking_products = models.FloatField(verbose_name='其他焦化产品消耗量')
    Consume_Crude = models.FloatField(verbose_name='原油消耗量')
    Consume_Fuel_oil = models.FloatField(verbose_name='燃料油消耗量')
    Consume_Gasoline = models.FloatField(verbose_name='汽油消耗量')
    Consume_Diesel = models.FloatField(verbose_name='柴油消耗量')
    Consume_Kerosene = models.FloatField(verbose_name='煤油消耗量')
    Consume_Liquefied_petroleum_gas = models.FloatField(verbose_name='液化石油气消耗量')
    Consume_Refinery_dry_gas = models.FloatField(verbose_name='炼厂干气消耗量', default=0)
    Consume_Naphtha = models.FloatField(verbose_name='石脑油消耗量')
    Consume_Asphalt = models.FloatField(verbose_name='沥青消耗量', default=0)
    Consume_Lubricating_oil = models.FloatField(verbose_name='润滑油消耗量')
    Consume_Petroleum_coke = models.FloatField(verbose_name='石油焦消耗量', default=0)
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
    Total_energy_consumption = models.FloatField(verbose_name='地区当年能源消费总量', null=False, blank=False)
    # Carbon_dioxide_emissions = models.FloatField(verbose_name='地区当年二氧化碳排放量', null=False, blank=False)
    Total_water_consumption = models.FloatField(verbose_name='地区当年用水总量', null=False, blank=False)
    The_total_area = models.FloatField(verbose_name='地区当年总面积', null=False, blank=False)
    Number_of_employees_in_basic_pension_insurance = models.FloatField(verbose_name='地区当年基本养老保险职工人数', null=False,
                                                                       blank=False)
    Number_of_basic_medical_insurance = models.FloatField(verbose_name='地区当年基本医疗保险人数', null=False, blank=False)
    Number_of_unemployment_insurance = models.FloatField(verbose_name='地区当年失业保险人数', null=False, blank=False)
    Primary_school_number = models.FloatField(verbose_name='小学人数', null=False, blank=False)
    Number_of_junior_high_school = models.FloatField(verbose_name='初中人数', null=False, blank=False)
    High_school_number = models.FloatField(verbose_name='高中人数', null=False, blank=False)
    University_and_above = models.FloatField(verbose_name='大学及以上人数', null=False, blank=False)

    # 单项基础指标（无需计算所得项）
    r_d = models.FloatField(verbose_name='规模以上工业企业R&D经费支出(万元)', null=False, blank=False)
    rural_urban = models.FloatField(verbose_name='乡-城人均年收入比(/)', null=False, blank=False)
    urban_per = models.FloatField(verbose_name='城镇居民人均可支配收入(元)', null=False, blank=False)
    rural_per = models.FloatField(verbose_name='农村居民人均可支配收入(元)', null=False, blank=False)
    garbage = models.FloatField(verbose_name='生活垃圾无害化处理率(%)', null=False, blank=False)
    bus_per = models.FloatField(verbose_name='平均万人拥有公共汽车(/)', null=False, blank=False)
    urban_sewage = models.FloatField(verbose_name='城镇生活污水集中处理率(%)', null=False, blank=False)
    mortality = models.FloatField(verbose_name='死亡率(%)', null=False, blank=False)
    pm25 = models.FloatField(verbose_name='PM2.5年平均浓度(微克/立方米)', null=False, blank=False)
    so2_emissions = models.FloatField(verbose_name='二氧化硫排放量(万吨)', null=False, blank=False)
    cod_emissions = models.FloatField(verbose_name='化学需氧量排放量(万吨)', null=False, blank=False)
    nh_emissions = models.FloatField(verbose_name='氨氮排放量(万吨)', null=False, blank=False)

    # 单项基础指标

    class Meta:
        ordering = '-year', 'area', 'province'
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

    Cal_Raw_coal = models.FloatField(verbose_name='原煤_年度计算值', null=True)
    Cal_Clean_coal = models.FloatField(verbose_name='洗精煤_年度计算值', null=True)
    Cal_Coke = models.FloatField(verbose_name='焦炭_年度计算值', null=True)
    Cal_Briquette = models.FloatField(verbose_name='型煤_年度计算值', null=True)
    Cal_Other_coking_products = models.FloatField(verbose_name='其他焦化产品_年度计算值', null=True)
    Cal_Crude = models.FloatField(verbose_name='原油_年度计算值', null=True)
    Cal_Fuel_oil = models.FloatField(verbose_name='燃料油_年度计算值', null=True)
    Cal_Gasoline = models.FloatField(verbose_name='汽油_年度计算值', null=True)
    Cal_Diesel = models.FloatField(verbose_name='柴油_年度计算值', null=True)
    Cal_Kerosene = models.FloatField(verbose_name='煤油_年度计算值', null=True)
    Cal_Liquefied_petroleum_gas = models.FloatField(verbose_name='液化石油气_年度计算值', null=True)
    Cal_Refinery_dry_gas = models.FloatField(verbose_name='炼厂干气_年度计算值', null=True)
    Cal_Naphtha = models.FloatField(verbose_name='石脑油_年度计算值', null=True)
    Cal_Asphalt = models.FloatField(verbose_name='沥青_年度计算值', null=True)
    Cal_Lubricating_oil = models.FloatField(verbose_name='润滑油_年度计算值', null=True)
    Cal_Petroleum_coke = models.FloatField(verbose_name='石油焦_年度计算值', null=True)
    Cal_Natural_gas = models.FloatField(verbose_name='天然气_年度计算值', null=True)
    GHG_Emission_a = models.FloatField(verbose_name='温室气体排放量_年度计算值', null=True)
    CO2_Emission_a = models.FloatField(verbose_name='二氧化碳排放量_年度计算值', null=True)
    Cal_Cement = models.FloatField(verbose_name='水泥_年度计算值', null=True)
    Cal_Steel = models.FloatField(verbose_name='钢铁_年度计算值', null=True)
    GHG_Emission_b = models.FloatField(verbose_name='温室气体排放量_年度计算值', null=True)
    CO2_Emission_b = models.FloatField(verbose_name='二氧化碳排放量_年度计算值', null=True)
    Total_CO2_Emission = models.FloatField(verbose_name='二氧化碳排放总量_年度计算值', null=True)
    Cal_EF = models.FloatField(verbose_name='生态足迹_年度计算值', null=True)

    # 基础指标
    per_unit_gdp = models.FloatField(verbose_name='单位GDP能耗', null=True)
    co2_per_gdp = models.FloatField(verbose_name='单位GDP二氧化碳排放量', null=True)
    water_per_gdp = models.FloatField(verbose_name='单位GDP用水量', null=True)
    planting_area = models.FloatField(verbose_name='播种面积占比', null=True)
    edu_years = models.FloatField(verbose_name='平均受教育年限', null=True)
    ef_per = models.FloatField(verbose_name='人均生态足迹', null=True)
    water_per = models.FloatField(verbose_name='人均用水量', null=True)
    pension_cov = models.FloatField(verbose_name='养老保险覆盖率', null=True)
    medical_cov = models.FloatField(verbose_name='医疗保险覆盖率', null=True)
    unemployment_cov = models.FloatField(verbose_name='失业保险覆盖率', null=True)
    # 无需计算所得项
    r_d = models.FloatField(verbose_name='规模以上工业企业R&D经费支出(万元)', null=True)
    rural_urban = models.FloatField(verbose_name='乡-城人均年收入比(/)', null=True)
    urban_per = models.FloatField(verbose_name='城镇居民人均可支配收入(元)', null=True)
    rural_per = models.FloatField(verbose_name='农村居民人均可支配收入(元)', null=True)
    garbage = models.FloatField(verbose_name='生活垃圾无害化处理率(%)', null=True)
    bus_per = models.FloatField(verbose_name='平均万人拥有公共汽车(/)', null=True)
    urban_sewage = models.FloatField(verbose_name='城镇生活污水集中处理率(%)', null=True)
    mortality = models.FloatField(verbose_name='死亡率(%)', null=True)
    pm25 = models.FloatField(verbose_name='PM2.5年平均浓度(微克/立方米)', null=True)
    so2_emissions = models.FloatField(verbose_name='二氧化硫排放量(万吨)', null=True)
    cod_emissions = models.FloatField(verbose_name='化学需氧量排放量(万吨)', null=True)
    nh_emissions = models.FloatField(verbose_name='氨氮排放量(万吨)', null=True)

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
    Consume_Briquette = models.FloatField(verbose_name='型煤消耗量', default=0)
    Consume_Other_coking_products = models.FloatField(verbose_name='其他焦化产品消耗量')
    Consume_Crude = models.FloatField(verbose_name='原油消耗量')
    Consume_Fuel_oil = models.FloatField(verbose_name='燃料油消耗量')
    Consume_Gasoline = models.FloatField(verbose_name='汽油消耗量')
    Consume_Diesel = models.FloatField(verbose_name='柴油消耗量')
    Consume_Kerosene = models.FloatField(verbose_name='煤油消耗量')
    Consume_Liquefied_petroleum_gas = models.FloatField(verbose_name='液化石油气消耗量')
    Consume_Refinery_dry_gas = models.FloatField(verbose_name='炼厂干气消耗量', default=0)
    Consume_Naphtha = models.FloatField(verbose_name='石脑油消耗量')
    Consume_Asphalt = models.FloatField(verbose_name='沥青消耗量', default=0)
    Consume_Lubricating_oil = models.FloatField(verbose_name='润滑油消耗量')
    Consume_Petroleum_coke = models.FloatField(verbose_name='石油焦消耗量', default=0)
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
    # Carbon_dioxide_emissions = models.FloatField(verbose_name='地区当年二氧化碳排放量', null=False, blank=False)
    Total_water_consumption = models.FloatField(verbose_name='地区当年用水总量', null=False, blank=False)
    The_total_area = models.FloatField(verbose_name='地区当年总面积', null=False, blank=False)
    # Ecological_footprint = models.FloatField(verbose_name='地区当年生态足迹', null=False, blank=False)
    Number_of_employees_in_basic_pension_insurance = models.FloatField(verbose_name='地区当年基本养老保险职工人数', null=False,
                                                                       blank=False)
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

    # 单项基础指标（无需计算所得项）
    r_d = models.FloatField(verbose_name='企业R&D内部经费支出', null=False, blank=False)
    rural_urban = models.FloatField(verbose_name='乡-城人均年收入比(/)', null=False, blank=False)
    urban_per = models.FloatField(verbose_name='城镇居民人均可支配收入(元)', null=False, blank=False)
    rural_per = models.FloatField(verbose_name='农村居民人均可支配收入(元)', null=False, blank=False)
    garbage = models.FloatField(verbose_name='生活垃圾无害化处理率(%)', null=False, blank=False)
    bus_per = models.FloatField(verbose_name='平均万人拥有公共汽车(/)', null=False, blank=False)
    urban_sewage = models.FloatField(verbose_name='城镇生活污水集中处理率(%)', null=False, blank=False)
    mortality = models.FloatField(verbose_name='死亡率(%)', null=False, blank=False)
    pm25 = models.FloatField(verbose_name='PM2.5年平均浓度(微克/立方米)', null=False, blank=False)
    so2_emissions = models.FloatField(verbose_name='二氧化硫排放量(万吨)', null=False, blank=False)
    cod_emissions = models.FloatField(verbose_name='化学需氧量排放量(万吨)', null=False, blank=False)
    nh_emissions = models.FloatField(verbose_name='氨氮排放量(万吨)', null=False, blank=False)
    # 指标目标值
    per_unit_gdp_target = models.FloatField(verbose_name='单位GDP能耗目标值', null=True)
    co2_per_gdp_target = models.FloatField(verbose_name='单位GDP二氧化碳排放量目标值', null=True)
    water_per_gdp_target = models.FloatField(verbose_name='单位GDP用水量目标值', null=True)
    planting_area_target = models.FloatField(verbose_name='播种面积占比目标值', null=True)
    edu_years_target = models.FloatField(verbose_name='平均受教育年限目标值', null=True)
    ef_per_target = models.FloatField(verbose_name='人均生态足迹目标值', null=True)
    water_per_target = models.FloatField(verbose_name='人均用水量目标值', null=True)
    pension_cov_target = models.FloatField(verbose_name='养老保险覆盖率目标值', null=True)
    medical_cov_target = models.FloatField(verbose_name='医疗保险覆盖率目标值', null=True)
    unemployment_cov_target = models.FloatField(verbose_name='失业保险覆盖率目标值', null=True)
    renewable_energy_per_target = models.FloatField(verbose_name='可再生能源供给占比目标值', null=True)
    r_d_target = models.FloatField(verbose_name='企业R&D内部经费支出目标值', null=True)
    rural_urban_target = models.FloatField(verbose_name='乡-城人均年收入目标值', null=True)
    urban_per_target = models.FloatField(verbose_name='城镇居民平均可支配收入目标值', null=True)
    rural_per_target = models.FloatField(verbose_name='农村居民平均可支配收入目标值', null=True)
    garbage_target = models.FloatField(verbose_name='生活垃圾无害化处理率目标值', null=True)
    bus_per_target = models.FloatField(verbose_name='平均每万人拥有公交车辆目标值', null=True)
    urban_sewage_target = models.FloatField(verbose_name='城镇生活污水集中处理率目标值', null=True)
    mortality_target = models.FloatField(verbose_name='死亡率目标值', null=True)
    pm25_target = models.FloatField(verbose_name='PM2.5年平均浓度目标值', null=True)
    so2_emissions_target = models.FloatField(verbose_name='二氧化硫排放量目标值', null=True)
    cod_emissions_target = models.FloatField(verbose_name='化学需氧量排放量目标值', null=True)
    nh_emissions_target = models.FloatField(verbose_name='氨氮排放量目标值', null=True)

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
    Cal_Raw_coal = models.FloatField(verbose_name='原煤_年度计算值', null=True)
    Cal_Clean_coal = models.FloatField(verbose_name='洗精煤_年度计算值', null=True)
    Cal_Coke = models.FloatField(verbose_name='焦炭_年度计算值', null=True)
    Cal_Briquette = models.FloatField(verbose_name='型煤_年度计算值', null=True)
    Cal_Other_coking_products = models.FloatField(verbose_name='其他焦化产品_年度计算值', null=True)
    Cal_Crude = models.FloatField(verbose_name='原油_年度计算值', null=True)
    Cal_Fuel_oil = models.FloatField(verbose_name='燃料油_年度计算值', null=True)
    Cal_Gasoline = models.FloatField(verbose_name='汽油_年度计算值', null=True)
    Cal_Diesel = models.FloatField(verbose_name='柴油_年度计算值', null=True)
    Cal_Kerosene = models.FloatField(verbose_name='煤油_年度计算值', null=True)
    Cal_Liquefied_petroleum_gas = models.FloatField(verbose_name='液化石油气_年度计算值', null=True)
    Cal_Refinery_dry_gas = models.FloatField(verbose_name='炼厂干气_年度计算值', null=True)
    Cal_Naphtha = models.FloatField(verbose_name='石脑油_年度计算值', null=True)
    Cal_Asphalt = models.FloatField(verbose_name='沥青_年度计算值', null=True)
    Cal_Lubricating_oil = models.FloatField(verbose_name='润滑油_年度计算值', null=True)
    Cal_Petroleum_coke = models.FloatField(verbose_name='石油焦_年度计算值', null=True)
    Cal_Natural_gas = models.FloatField(verbose_name='天然气_年度计算值', null=True)
    GHG_Emission_a = models.FloatField(verbose_name='温室气体排放量_年度计算值', null=True)
    CO2_Emission_a = models.FloatField(verbose_name='二氧化碳排放量_年度计算值', null=True)
    Cal_Cement = models.FloatField(verbose_name='水泥_年度计算值', null=True)
    Cal_Steel = models.FloatField(verbose_name='钢铁_年度计算值', null=True)
    GHG_Emission_b = models.FloatField(verbose_name='温室气体排放量_年度计算值', null=True)
    CO2_Emission_b = models.FloatField(verbose_name='二氧化碳排放量_年度计算值', null=True)
    Total_CO2_Emission = models.FloatField(verbose_name='二氧化碳排放总量_年度计算值', null=True)
    Cal_EF = models.FloatField(verbose_name='生态足迹_年度计算值', null=True)

    # 基础指标
    per_unit_gdp = models.FloatField(verbose_name='单位GDP能耗', null=True)
    co2_per_gdp = models.FloatField(verbose_name='单位GDP二氧化碳排放量', null=True)
    water_per_gdp = models.FloatField(verbose_name='单位GDP用水量', null=True)
    planting_area = models.FloatField(verbose_name='播种面积占比', null=True)
    edu_years = models.FloatField(verbose_name='平均受教育年限', null=True)
    ef_per = models.FloatField(verbose_name='人均生态足迹', null=True)
    water_per = models.FloatField(verbose_name='人均用水量', null=True)
    pension_cov = models.FloatField(verbose_name='养老保险覆盖率', null=True)
    medical_cov = models.FloatField(verbose_name='医疗保险覆盖率', null=True)
    unemployment_cov = models.FloatField(verbose_name='失业保险覆盖率', null=True)
    renewable_energy_per = models.FloatField(verbose_name='可再生能源供给占比(省)', null=True)
    # 无需计算所得单项指标
    r_d = models.FloatField(verbose_name='企业R&D内部经费支出', null=False, blank=False)
    rural_urban = models.FloatField(verbose_name='乡-城人均年收入比(/)', null=False, blank=False)
    urban_per = models.FloatField(verbose_name='城镇居民人均可支配收入(元)', null=False, blank=False)
    rural_per = models.FloatField(verbose_name='农村居民人均可支配收入(元)', null=False, blank=False)
    garbage = models.FloatField(verbose_name='生活垃圾无害化处理率(%)', null=False, blank=False)
    bus_per = models.FloatField(verbose_name='平均万人拥有公共汽车(/)', null=False, blank=False)
    urban_sewage = models.FloatField(verbose_name='城镇生活污水集中处理率(%)', null=False, blank=False)
    mortality = models.FloatField(verbose_name='死亡率(%)', null=False, blank=False)
    pm25 = models.FloatField(verbose_name='PM2.5年平均浓度(微克/立方米)', null=False, blank=False)
    so2_emissions = models.FloatField(verbose_name='二氧化硫排放量(万吨)', null=False, blank=False)
    cod_emissions = models.FloatField(verbose_name='化学需氧量排放量(万吨)', null=False, blank=False)
    nh_emissions = models.FloatField(verbose_name='氨氮排放量(万吨)', null=False, blank=False)



    class Meta:
        ordering = '-year', 'province'
        verbose_name = '省级年度计算值'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.province},{self.year}'


class area_gep_score(models.Model):
    province = models.CharField(max_length=50, verbose_name='省份', null=False, blank=False)
    area = models.CharField(max_length=50, verbose_name='地区', null=False, blank=False)
    year = models.IntegerField(verbose_name='年度', null=False, blank=False)
    # 单项指标得分
    r_d_score = models.FloatField(verbose_name='规模以上工业企业R&D经费支出(万元)', null=True)
    per_unit_gdp_score = models.FloatField(verbose_name='单位GDP能耗(吨/万元)', null=True)
    rural_urban_score = models.FloatField(verbose_name='乡-城人均年收入比(/)', null=True)
    urban_per_score = models.FloatField(verbose_name='城镇居民人均可支配收入(元)', null=True)
    rural_per_score = models.FloatField(verbose_name='农村居民人均可支配收入(元)', null=True)
    garbage_score = models.FloatField(verbose_name='生活垃圾无害化处理率(%)', null=True)
    bus_per_score = models.FloatField(verbose_name='平均万人拥有公共汽车(/)', null=True)
    urban_sewage_score = models.FloatField(verbose_name='城镇生活污水集中处理率(%)', null=True)
    edu_years_score = models.FloatField(verbose_name='平均受教育年限(年)', null=True)
    mortality_score = models.FloatField(verbose_name='死亡率(%)', null=True)
    pension_cov_score = models.FloatField(verbose_name='养老保险覆盖率(%)', null=True)
    medical_cov_score = models.FloatField(verbose_name='医疗保险覆盖率(%)', null=True)
    unemployment_cov_score = models.FloatField(verbose_name='失业保险覆盖率(%)', null=True)
    pm25_score = models.FloatField(verbose_name='PM2.6年平均浓度(微克/立方米)', null=True)
    so2_emissions_score = models.FloatField(verbose_name='二氧化硫排放量(万吨)', null=True)
    co2_per_gdp_score = models.FloatField(verbose_name='单位GDP二氧化碳排放量(千克/元)', null=True)
    cod_emissions_score = models.FloatField(verbose_name='化学需氧量排放量(万吨)', null=True)
    nh_emissions_score = models.FloatField(verbose_name='氨氮排放量(万吨)', null=True)
    water_per_score = models.FloatField(verbose_name='人均耗水量(立方米)', null=True)
    water_per_gdp_score = models.FloatField(verbose_name='单位GDP用水量(立方米/万元)', null=True)
    planting_area_score = models.FloatField(verbose_name='播种面积占比(%)', null=True)
    ef_per_score = models.FloatField(verbose_name='人均生态足迹(万吨碳/万人)', null=True)
    # GEP框架指标得分
    green_innovation = models.FloatField(verbose_name='绿色创新', null=True)
    energy_use = models.FloatField(verbose_name='能源利用', null=True)
    parma_ratio = models.FloatField(verbose_name='帕尔玛比率', null=True)
    income = models.FloatField(verbose_name='收入', null=True)
    infrastructure = models.FloatField(verbose_name='基础设施建设', null=True)
    education = models.FloatField(verbose_name='教育', null=True)
    life_expectancy = models.FloatField(verbose_name='预期寿命', null=True)
    social_security = models.FloatField(verbose_name='社会保障', null=True)
    air_pollution = models.FloatField(verbose_name='大气污染', null=True)
    greenhouse = models.FloatField(verbose_name='温室气体排放', null=True)
    nitrogen = models.FloatField(verbose_name='氮排放', null=True)
    water_withdrawal = models.FloatField(verbose_name='取水量', null=True)
    land_use = models.FloatField(verbose_name='土地利用', null=True)
    EF = models.FloatField(verbose_name='生态足迹', null=True)
    # GEP+得分
    city_green_economy = models.FloatField(verbose_name='绿色经济', null=True)
    city_sustainable = models.FloatField(verbose_name='可持续发展', null=True)
    city_gep_plus = models.FloatField(verbose_name='GEP+', null=True)

    class Meta:
        ordering = '-year', 'area', 'province'
        verbose_name = '地区年度得分'
        verbose_name_plural = verbose_name
        unique_together = [('province', 'area', 'year')]

    def __str__(self):
        return f'{self.province}, {self.area}, {self.year}'


class prov_gep_score(models.Model):
    province = models.CharField(max_length=50, verbose_name='省份', null=False, blank=False)
    year = models.IntegerField(verbose_name='年度', null=False, blank=False)
    # 单项指标得分
    r_d_score = models.FloatField(verbose_name='企业R&D内部经费支出(万元)', null=True)
    per_unit_gdp_score = models.FloatField(verbose_name='单位GDP能耗(吨/万元)', null=True)
    renewable_energy_per_score = models.FloatField(verbose_name='可再生能源供给占比', null=True)
    rural_urban_score = models.FloatField(verbose_name='乡-城人均年收入比(/)', null=True)
    urban_per_score = models.FloatField(verbose_name='城镇居民人均可支配收入(元)', null=True)
    rural_per_score = models.FloatField(verbose_name='农村居民人均可支配收入(元)', null=True)
    garbage_score = models.FloatField(verbose_name='生活垃圾无害化处理率(%)', null=True)
    bus_per_score = models.FloatField(verbose_name='平均万人拥有公共汽车(/)', null=True)
    urban_sewage_score = models.FloatField(verbose_name='城镇生活污水集中处理率(%)', null=True)
    edu_years_score = models.FloatField(verbose_name='平均受教育年限(年)', null=True)
    mortality_score = models.FloatField(verbose_name='死亡率(%)', null=True)
    pension_cov_score = models.FloatField(verbose_name='养老保险覆盖率(%)', null=True)
    medical_cov_score = models.FloatField(verbose_name='医疗保险覆盖率(%)', null=True)
    unemployment_cov_score = models.FloatField(verbose_name='失业保险覆盖率(%)', null=True)
    pm25_score = models.FloatField(verbose_name='PM2.6年平均浓度(微克/立方米)', null=True)
    so2_emissions_score = models.FloatField(verbose_name='二氧化硫排放量(万吨)', null=True)
    co2_per_gdp_score = models.FloatField(verbose_name='单位GDP二氧化碳排放量(千克/元)', null=True)
    cod_emissions_score = models.FloatField(verbose_name='化学需氧量排放量(万吨)', null=True)
    nh_emissions_score = models.FloatField(verbose_name='氨氮排放量(万吨)', null=True)
    water_per_score = models.FloatField(verbose_name='人均耗水量(立方米)', null=True)
    water_per_gdp_score = models.FloatField(verbose_name='单位GDP用水量(立方米/万元)', null=True)
    planting_area_score = models.FloatField(verbose_name='播种面积占比(%)', null=True)
    ef_per_score = models.FloatField(verbose_name='人均生态足迹(万吨碳/万人)', null=True)
    # GEP框架指标得分
    green_innovation = models.FloatField(verbose_name='绿色创新', null=True)
    energy_use = models.FloatField(verbose_name='能源利用', null=True)
    renewable_energy = models.FloatField(verbose_name='可再生能源供给', null=True)
    parma_ratio = models.FloatField(verbose_name='帕尔玛比率', null=True)
    income = models.FloatField(verbose_name='收入', null=True)
    infrastructure = models.FloatField(verbose_name='基础设施建设', null=True)
    education = models.FloatField(verbose_name='教育', null=True)
    life_expectancy = models.FloatField(verbose_name='预期寿命', null=True)
    social_security = models.FloatField(verbose_name='社会保障', null=True)
    air_pollution = models.FloatField(verbose_name='大气污染', null=True)
    greenhouse = models.FloatField(verbose_name='温室气体排放', null=True)
    nitrogen = models.FloatField(verbose_name='氮排放', null=True)
    water_withdrawal = models.FloatField(verbose_name='取水量', null=True)
    land_use = models.FloatField(verbose_name='土地利用', null=True)
    EF = models.FloatField(verbose_name='生态足迹', null=True)
    # GEP+得分
    city_green_economy = models.FloatField(verbose_name='绿色经济', null=True)
    city_sustainable = models.FloatField(verbose_name='可持续发展', null=True)
    city_gep_plus = models.FloatField(verbose_name='GEP+', null=True)

    class Meta:
        ordering = '-year', 'province'
        verbose_name = '省份年度得分'
        verbose_name_plural = verbose_name
        unique_together = [('province', 'year')]

    def __str__(self):
        return f'{self.province}, {self.year}'


# 文件上传
class ImportFile_excel(models.Model):
    arealevel = models.CharField(verbose_name='数据级别', max_length=50, choices=(('area', '市级'), ('province', '省级')))
    province = models.ForeignKey(to=Province, null=False, blank=False, on_delete=models.CASCADE, verbose_name='省份')
    year = models.IntegerField(verbose_name='年度', null=False, blank=False)
    excelfile = models.FileField(verbose_name='上传', upload_to='data/%Y-%m-%d')
    add_date = models.DateTimeField(verbose_name='上传日期', auto_now=True)

    class Meta:
        verbose_name = '数据导入'

    def __str__(self):
        if self.arealevel == 'area':
            k = '市级'
        else:
            k = '省级'
        return '%s, %s, %s' % (self.province, k, self.year)
