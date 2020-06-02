from django.db import models
from work.models import can_not_equal_zero

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
        verbose_name = "能源常量"


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

    class Meta:
        ordering = '-year', 'area' ,'province'
        verbose_name = '地区年度资源消耗量'
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
    GHG_Emission  = models.FloatField(verbose_name='温室气体排放量_年度计算值', null=True, blank=True)
    CO2_Emission = models.FloatField(verbose_name='二氧化碳排放量_年度计算值', null=True, blank=True)
    Cal_Cement = models.FloatField(verbose_name='水泥_年度计算值', null=True, blank=True)
    Cal_Steel = models.FloatField(verbose_name='钢铁_年度计算值', null=True, blank=True)
    GHG_Emission  = models.FloatField(verbose_name='温室气体排放量_年度计算值', null=True, blank=True)
    CO2_Emission = models.FloatField(verbose_name='二氧化碳排放量_年度计算值', null=True, blank=True)
    Total_CO2_Emission = models.FloatField(verbose_name='二氧化碳排放总量_年度计算值', null=True, blank=True)
    Cal_EF = models.FloatField(verbose_name='生态足迹_年度计算值', null=True, blank=True)

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

    class Meta:
        ordering = '-year', 'province'
        verbose_name = '省级年度资源消耗量'
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
    GHG_Emission  = models.FloatField(verbose_name='温室气体排放量_年度计算值', null=True, blank=True)
    CO2_Emission = models.FloatField(verbose_name='二氧化碳排放量_年度计算值', null=True, blank=True)
    Cal_Cement = models.FloatField(verbose_name='水泥_年度计算值', null=True, blank=True)
    Cal_Steel = models.FloatField(verbose_name='钢铁_年度计算值', null=True, blank=True)
    GHG_Emission  = models.FloatField(verbose_name='温室气体排放量_年度计算值', null=True, blank=True)
    CO2_Emission = models.FloatField(verbose_name='二氧化碳排放量_年度计算值', null=True, blank=True)
    Total_CO2_Emission = models.FloatField(verbose_name='二氧化碳排放总量_年度计算值', null=True, blank=True)
    Cal_EF = models.FloatField(verbose_name='生态足迹_年度计算值', null=True, blank=True)

    class Meta:
        ordering = '-year', 'province'
        verbose_name = '省级年度计算值'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.province},{self.year}'
