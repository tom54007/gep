# Generated by Django 3.0.4 on 2020-06-04 10:46

from django.db import migrations, models
import work.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConstantEg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Raw_coal', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='原煤')),
                ('Clean_coal', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='洗精煤')),
                ('Coke', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='焦炭')),
                ('Briquette', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='型煤')),
                ('Other_coking_products', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='其他焦化产品')),
                ('Crude', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='原油')),
                ('Fuel_oil', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='燃料油')),
                ('Gasoline', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='汽油')),
                ('Diesel', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='柴油')),
                ('Kerosene', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='煤油')),
                ('Liquefied_petroleum_gas', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='液化石油气')),
                ('Refinery_dry_gas', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='炼厂干气')),
                ('Naphtha', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='石脑油')),
                ('Asphalt', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='沥青')),
                ('Lubricating_oil', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='润滑油')),
                ('Petroleum_coke', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='石油焦')),
                ('Natural_gas', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='天然气')),
                ('Cement', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='水泥')),
                ('Steel', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='钢铁')),
                ('Farmland', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='农地')),
                ('Woodland', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='林地')),
                ('Pastureland', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='畜牧地')),
                ('Fishing_ground', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='渔场')),
                ('Construction_land', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='建设用地')),
                ('Raw_coal_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='原煤热值')),
                ('Clean_coal_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='洗精煤热值')),
                ('Coke_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='焦炭热值')),
                ('Briquette_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='型煤热值')),
                ('Other_coking_products_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='其他焦化产品热值')),
                ('Crude_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='原油热值')),
                ('Fuel_oil_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='燃料油热值')),
                ('Gasoline_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='汽油热值')),
                ('Diesel_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='柴油热值')),
                ('Kerosene_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='煤油热值')),
                ('Liquefied_petroleum_gas_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='液化石油气热值')),
                ('Refinery_dry_gas_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='炼厂干气热值')),
                ('Naphtha_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='石脑油热值')),
                ('Asphalt_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='沥青热值')),
                ('Lubricating_oil_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='润滑油热值')),
                ('Petroleum_coke_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='石油焦热值')),
                ('Natural_gas_MJ', models.FloatField(validators=[work.models.can_not_equal_zero], verbose_name='天然气热值')),
            ],
            options={
                'verbose_name': '能源常量',
            },
        ),
        migrations.CreateModel(
            name='Prov_Annual_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=255, verbose_name='省份')),
                ('year', models.IntegerField(verbose_name='年度')),
                ('Consume_Raw_coal', models.FloatField(verbose_name='原煤消耗量')),
                ('Consume_Clean_coal', models.FloatField(verbose_name='洗精煤消耗量')),
                ('Consume_Coke', models.FloatField(verbose_name='焦炭消耗量')),
                ('Consume_Briquette', models.FloatField(verbose_name='型煤消耗量')),
                ('Consume_Other_coking_products', models.FloatField(verbose_name='其他焦化产品消耗量')),
                ('Consume_Crude', models.FloatField(verbose_name='原油消耗量')),
                ('Consume_Fuel_oil', models.FloatField(verbose_name='燃料油消耗量')),
                ('Consume_Gasoline', models.FloatField(verbose_name='汽油消耗量')),
                ('Consume_Diesel', models.FloatField(verbose_name='柴油消耗量')),
                ('Consume_Kerosene', models.FloatField(verbose_name='煤油消耗量')),
                ('Consume_Liquefied_petroleum_gas', models.FloatField(verbose_name='液化石油气消耗量')),
                ('Consume_Refinery_dry_gas', models.FloatField(verbose_name='炼厂干气消耗量')),
                ('Consume_Naphtha', models.FloatField(verbose_name='石脑油消耗量')),
                ('Consume_Asphalt', models.FloatField(verbose_name='沥青消耗量')),
                ('Consume_Lubricating_oil', models.FloatField(verbose_name='润滑油消耗量')),
                ('Consume_Petroleum_coke', models.FloatField(verbose_name='石油焦消耗量')),
                ('Consume_Natural_gas', models.FloatField(verbose_name='天然气消耗量')),
                ('Consume_Cement', models.FloatField(verbose_name='水泥消耗量')),
                ('Consume_Steel', models.FloatField(verbose_name='钢铁消耗量')),
                ('Consume_Farmland', models.FloatField(verbose_name='农地消耗量')),
                ('Consume_Woodland', models.FloatField(verbose_name='林地消耗量')),
                ('Consume_Pastureland', models.FloatField(verbose_name='畜牧地消耗量')),
                ('Consume_Fishing_ground', models.FloatField(verbose_name='渔场消耗量')),
                ('Consume_Construction_land', models.FloatField(verbose_name='建设用地消耗量')),
                ('GDP', models.FloatField(verbose_name='地区当年生产总值')),
                ('Sown_area', models.FloatField(verbose_name='地区当年播种面积')),
                ('Total_population', models.FloatField(verbose_name='地区当年总人口')),
                ('Total_power_generation', models.FloatField(verbose_name='地区当年总发电量')),
                ('Total_energy_consumption', models.FloatField(verbose_name='地区当年能源消费总量')),
                ('Carbon_dioxide_emissions', models.FloatField(verbose_name='地区当年二氧化碳排放量')),
                ('Total_water_consumption', models.FloatField(verbose_name='地区当年用水总量')),
                ('The_total_area', models.FloatField(verbose_name='地区当年总面积')),
                ('Ecological_footprint', models.FloatField(verbose_name='地区当年生态足迹')),
                ('Number_of_employees_in_basic_pension_insurance', models.FloatField(verbose_name='地区当年基本养老保险职工人数')),
                ('Number_of_basic_medical_insurance', models.FloatField(verbose_name='地区当年基本医疗保险人数')),
                ('Number_of_unemployment_insurance', models.FloatField(verbose_name='地区当年失业保险人数')),
                ('Nuclear_power_generation', models.FloatField(verbose_name='地区当年核电发电量')),
                ('Wind_power_generation', models.FloatField(verbose_name='地区当年风电发电量')),
                ('Hydropower_generation', models.FloatField(verbose_name='地区当年水电发电量')),
                ('Photovoltaic_power_generation', models.FloatField(verbose_name='地区当年光伏发电量')),
                ('Primary_school_number', models.FloatField(verbose_name='小学人数')),
                ('Number_of_junior_high_school', models.FloatField(verbose_name='初中人数')),
                ('High_school_number', models.FloatField(verbose_name='高中人数')),
                ('University_and_above', models.FloatField(verbose_name='大学及以上人数')),
            ],
            options={
                'verbose_name': '省级年度原始数据',
                'verbose_name_plural': '省级年度原始数据',
                'ordering': ('-year', 'province'),
            },
        ),
        migrations.CreateModel(
            name='Prov_Calculated_value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=255, verbose_name='省份')),
                ('year', models.IntegerField(verbose_name='年度')),
                ('Cal_Raw_coal', models.FloatField(blank=True, null=True, verbose_name='原煤_年度计算值')),
                ('Cal_Clean_coal', models.FloatField(blank=True, null=True, verbose_name='洗精煤_年度计算值')),
                ('Cal_Coke', models.FloatField(blank=True, null=True, verbose_name='焦炭_年度计算值')),
                ('Cal_Briquette', models.FloatField(blank=True, null=True, verbose_name='型煤_年度计算值')),
                ('Cal_Other_coking_products', models.FloatField(blank=True, null=True, verbose_name='其他焦化产品_年度计算值')),
                ('Cal_Crude', models.FloatField(blank=True, null=True, verbose_name='原油_年度计算值')),
                ('Cal_Fuel_oil', models.FloatField(blank=True, null=True, verbose_name='燃料油_年度计算值')),
                ('Cal_Gasoline', models.FloatField(blank=True, null=True, verbose_name='汽油_年度计算值')),
                ('Cal_Diesel', models.FloatField(blank=True, null=True, verbose_name='柴油_年度计算值')),
                ('Cal_Kerosene', models.FloatField(blank=True, null=True, verbose_name='煤油_年度计算值')),
                ('Cal_Liquefied_petroleum_gas', models.FloatField(blank=True, null=True, verbose_name='液化石油气_年度计算值')),
                ('Cal_Refinery_dry_gas', models.FloatField(blank=True, null=True, verbose_name='炼厂干气_年度计算值')),
                ('Cal_Naphtha', models.FloatField(blank=True, null=True, verbose_name='石脑油_年度计算值')),
                ('Cal_Asphalt', models.FloatField(blank=True, null=True, verbose_name='沥青_年度计算值')),
                ('Cal_Lubricating_oil', models.FloatField(blank=True, null=True, verbose_name='润滑油_年度计算值')),
                ('Cal_Petroleum_coke', models.FloatField(blank=True, null=True, verbose_name='石油焦_年度计算值')),
                ('Cal_Natural_gas', models.FloatField(blank=True, null=True, verbose_name='天然气_年度计算值')),
                ('GHG_Emission_a', models.FloatField(blank=True, null=True, verbose_name='温室气体排放量_年度计算值')),
                ('CO2_Emission_a', models.FloatField(blank=True, null=True, verbose_name='二氧化碳排放量_年度计算值')),
                ('Cal_Cement', models.FloatField(blank=True, null=True, verbose_name='水泥_年度计算值')),
                ('Cal_Steel', models.FloatField(blank=True, null=True, verbose_name='钢铁_年度计算值')),
                ('GHG_Emission_b', models.FloatField(blank=True, null=True, verbose_name='温室气体排放量_年度计算值')),
                ('CO2_Emission_b', models.FloatField(blank=True, null=True, verbose_name='二氧化碳排放量_年度计算值')),
                ('Total_CO2_Emission', models.FloatField(blank=True, null=True, verbose_name='二氧化碳排放总量_年度计算值')),
                ('Cal_EF', models.FloatField(blank=True, null=True, verbose_name='生态足迹_年度计算值')),
                ('per_unit_gdp', models.FloatField(blank=True, null=True, verbose_name='单位GDP能耗')),
                ('co2_per_gdp', models.FloatField(blank=True, null=True, verbose_name='单位GDP二氧化碳排放量')),
                ('water_per_gdp', models.FloatField(blank=True, null=True, verbose_name='单位GDP用水量')),
                ('planting_area', models.FloatField(blank=True, null=True, verbose_name='播种面积占比')),
                ('edu_years', models.FloatField(blank=True, null=True, verbose_name='平均受教育年限')),
                ('ef_per', models.FloatField(blank=True, null=True, verbose_name='人均生态足迹')),
                ('water_per', models.FloatField(blank=True, null=True, verbose_name='人均用水量')),
                ('pension_cov', models.FloatField(blank=True, null=True, verbose_name='养老保险覆盖率')),
                ('medical_cov', models.FloatField(blank=True, null=True, verbose_name='医疗保险覆盖率')),
                ('unemployment_cov', models.FloatField(blank=True, null=True, verbose_name='失业保险覆盖率')),
                ('renewable_energy_per', models.FloatField(blank=True, null=True, verbose_name='可再生能源供给占比(省)')),
            ],
            options={
                'verbose_name': '省级年度计算值',
                'verbose_name_plural': '省级年度计算值',
                'ordering': ('-year', 'province'),
            },
        ),
        migrations.CreateModel(
            name='Calculated_value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=50, verbose_name='省份')),
                ('area', models.CharField(max_length=50, verbose_name='地区')),
                ('year', models.IntegerField(verbose_name='年度')),
                ('Cal_Raw_coal', models.FloatField(blank=True, null=True, verbose_name='原煤_年度计算值')),
                ('Cal_Clean_coal', models.FloatField(blank=True, null=True, verbose_name='洗精煤_年度计算值')),
                ('Cal_Coke', models.FloatField(blank=True, null=True, verbose_name='焦炭_年度计算值')),
                ('Cal_Briquette', models.FloatField(blank=True, null=True, verbose_name='型煤_年度计算值')),
                ('Cal_Other_coking_products', models.FloatField(blank=True, null=True, verbose_name='其他焦化产品_年度计算值')),
                ('Cal_Crude', models.FloatField(blank=True, null=True, verbose_name='原油_年度计算值')),
                ('Cal_Fuel_oil', models.FloatField(blank=True, null=True, verbose_name='燃料油_年度计算值')),
                ('Cal_Gasoline', models.FloatField(blank=True, null=True, verbose_name='汽油_年度计算值')),
                ('Cal_Diesel', models.FloatField(blank=True, null=True, verbose_name='柴油_年度计算值')),
                ('Cal_Kerosene', models.FloatField(blank=True, null=True, verbose_name='煤油_年度计算值')),
                ('Cal_Liquefied_petroleum_gas', models.FloatField(blank=True, null=True, verbose_name='液化石油气_年度计算值')),
                ('Cal_Refinery_dry_gas', models.FloatField(blank=True, null=True, verbose_name='炼厂干气_年度计算值')),
                ('Cal_Naphtha', models.FloatField(blank=True, null=True, verbose_name='石脑油_年度计算值')),
                ('Cal_Asphalt', models.FloatField(blank=True, null=True, verbose_name='沥青_年度计算值')),
                ('Cal_Lubricating_oil', models.FloatField(blank=True, null=True, verbose_name='润滑油_年度计算值')),
                ('Cal_Petroleum_coke', models.FloatField(blank=True, null=True, verbose_name='石油焦_年度计算值')),
                ('Cal_Natural_gas', models.FloatField(blank=True, null=True, verbose_name='天然气_年度计算值')),
                ('GHG_Emission_a', models.FloatField(blank=True, null=True, verbose_name='温室气体排放量_年度计算值')),
                ('CO2_Emission_a', models.FloatField(blank=True, null=True, verbose_name='二氧化碳排放量_年度计算值')),
                ('Cal_Cement', models.FloatField(blank=True, null=True, verbose_name='水泥_年度计算值')),
                ('Cal_Steel', models.FloatField(blank=True, null=True, verbose_name='钢铁_年度计算值')),
                ('GHG_Emission_b', models.FloatField(blank=True, null=True, verbose_name='温室气体排放量_年度计算值')),
                ('CO2_Emission_b', models.FloatField(blank=True, null=True, verbose_name='二氧化碳排放量_年度计算值')),
                ('Total_CO2_Emission', models.FloatField(blank=True, null=True, verbose_name='二氧化碳排放总量_年度计算值')),
                ('Cal_EF', models.FloatField(blank=True, null=True, verbose_name='生态足迹_年度计算值')),
                ('per_unit_gdp', models.FloatField(blank=True, null=True, verbose_name='单位GDP能耗')),
                ('co2_per_gdp', models.FloatField(blank=True, null=True, verbose_name='单位GDP二氧化碳排放量')),
                ('water_per_gdp', models.FloatField(blank=True, null=True, verbose_name='单位GDP用水量')),
                ('planting_area', models.FloatField(blank=True, null=True, verbose_name='播种面积占比')),
                ('edu_years', models.FloatField(blank=True, null=True, verbose_name='平均受教育年限')),
                ('ef_per', models.FloatField(blank=True, null=True, verbose_name='人均生态足迹')),
                ('water_per', models.FloatField(blank=True, null=True, verbose_name='人均用水量')),
                ('pension_cov', models.FloatField(blank=True, null=True, verbose_name='养老保险覆盖率')),
                ('medical_cov', models.FloatField(blank=True, null=True, verbose_name='医疗保险覆盖率')),
                ('unemployment_cov', models.FloatField(blank=True, null=True, verbose_name='失业保险覆盖率')),
                ('renewable_energy_per', models.FloatField(blank=True, null=True, verbose_name='可再生能源供给占比(省)')),
            ],
            options={
                'verbose_name': '地区年度计算值',
                'verbose_name_plural': '地区年度计算值',
                'ordering': ('-year', 'area', 'province'),
                'unique_together': {('province', 'area', 'year')},
            },
        ),
        migrations.CreateModel(
            name='Annual_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=50, verbose_name='省份')),
                ('area', models.CharField(max_length=50, verbose_name='地区')),
                ('year', models.IntegerField(verbose_name='年度')),
                ('Consume_Raw_coal', models.FloatField(verbose_name='原煤消耗量')),
                ('Consume_Clean_coal', models.FloatField(verbose_name='洗精煤消耗量')),
                ('Consume_Coke', models.FloatField(verbose_name='焦炭消耗量')),
                ('Consume_Briquette', models.FloatField(verbose_name='型煤消耗量')),
                ('Consume_Other_coking_products', models.FloatField(verbose_name='其他焦化产品消耗量')),
                ('Consume_Crude', models.FloatField(verbose_name='原油消耗量')),
                ('Consume_Fuel_oil', models.FloatField(verbose_name='燃料油消耗量')),
                ('Consume_Gasoline', models.FloatField(verbose_name='汽油消耗量')),
                ('Consume_Diesel', models.FloatField(verbose_name='柴油消耗量')),
                ('Consume_Kerosene', models.FloatField(verbose_name='煤油消耗量')),
                ('Consume_Liquefied_petroleum_gas', models.FloatField(verbose_name='液化石油气消耗量')),
                ('Consume_Refinery_dry_gas', models.FloatField(verbose_name='炼厂干气消耗量')),
                ('Consume_Naphtha', models.FloatField(verbose_name='石脑油消耗量')),
                ('Consume_Asphalt', models.FloatField(verbose_name='沥青消耗量')),
                ('Consume_Lubricating_oil', models.FloatField(verbose_name='润滑油消耗量')),
                ('Consume_Petroleum_coke', models.FloatField(verbose_name='石油焦消耗量')),
                ('Consume_Natural_gas', models.FloatField(verbose_name='天然气消耗量')),
                ('Consume_Cement', models.FloatField(verbose_name='水泥消耗量')),
                ('Consume_Steel', models.FloatField(verbose_name='钢铁消耗量')),
                ('Consume_Farmland', models.FloatField(verbose_name='农地消耗量')),
                ('Consume_Woodland', models.FloatField(verbose_name='林地消耗量')),
                ('Consume_Pastureland', models.FloatField(verbose_name='畜牧地消耗量')),
                ('Consume_Fishing_ground', models.FloatField(verbose_name='渔场消耗量')),
                ('Consume_Construction_land', models.FloatField(verbose_name='建设用地消耗量')),
                ('GDP', models.FloatField(verbose_name='地区当年生产总值')),
                ('Sown_area', models.FloatField(verbose_name='地区当年播种面积')),
                ('Total_population', models.FloatField(verbose_name='地区当年总人口')),
                ('Total_power_generation', models.FloatField(verbose_name='地区当年总发电量')),
                ('Total_energy_consumption', models.FloatField(verbose_name='地区当年能源消费总量')),
                ('Carbon_dioxide_emissions', models.FloatField(verbose_name='地区当年二氧化碳排放量')),
                ('Total_water_consumption', models.FloatField(verbose_name='地区当年用水总量')),
                ('The_total_area', models.FloatField(verbose_name='地区当年总面积')),
                ('Ecological_footprint', models.FloatField(verbose_name='地区当年生态足迹')),
                ('Number_of_employees_in_basic_pension_insurance', models.FloatField(verbose_name='地区当年基本养老保险职工人数')),
                ('Number_of_basic_medical_insurance', models.FloatField(verbose_name='地区当年基本医疗保险人数')),
                ('Number_of_unemployment_insurance', models.FloatField(verbose_name='地区当年失业保险人数')),
                ('Nuclear_power_generation', models.FloatField(verbose_name='地区当年核电发电量')),
                ('Wind_power_generation', models.FloatField(verbose_name='地区当年风电发电量')),
                ('Hydropower_generation', models.FloatField(verbose_name='地区当年水电发电量')),
                ('Photovoltaic_power_generation', models.FloatField(verbose_name='地区当年光伏发电量')),
                ('Primary_school_number', models.FloatField(verbose_name='小学人数')),
                ('Number_of_junior_high_school', models.FloatField(verbose_name='初中人数')),
                ('High_school_number', models.FloatField(verbose_name='高中人数')),
                ('University_and_above', models.FloatField(verbose_name='大学及以上人数')),
            ],
            options={
                'verbose_name': '地区年度原始数据',
                'verbose_name_plural': '地区年度原始数据',
                'ordering': ('-year', 'area', 'province'),
                'unique_together': {('province', 'area', 'year')},
            },
        ),
    ]
