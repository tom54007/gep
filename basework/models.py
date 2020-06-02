from django.db import models
from work.models import Area, Province, can_not_equal_zero

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


