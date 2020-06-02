# Generated by Django 3.0.4 on 2020-03-13 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityDataRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='年度')),
                ('r_d', models.FloatField(verbose_name='规模以上工业企业R&D经费支出')),
                ('per_unit_gdp', models.FloatField(verbose_name='单位GDP能耗')),
                ('rural_urban', models.FloatField(verbose_name='乡-城人均年收入比')),
                ('urban_per', models.FloatField(verbose_name='城镇居民人均可支配收入')),
                ('rural_per', models.FloatField(verbose_name='农村居民人均可支配收入')),
                ('garbage', models.FloatField(verbose_name='生活垃圾无害化处理率')),
                ('bus_per', models.FloatField(verbose_name='平均万人拥有公共汽车')),
                ('urban_sewage', models.FloatField(verbose_name='城镇生活污水集中处理率')),
                ('edu_years', models.FloatField(verbose_name='平均受教育年限')),
                ('mortality', models.FloatField(verbose_name='死亡率')),
                ('pension_cov', models.FloatField(verbose_name='养老保险覆盖率')),
                ('medical_cov', models.FloatField(verbose_name='医疗保险覆盖率')),
                ('unemployment_cov', models.FloatField(verbose_name='失业保险覆盖率')),
                ('pm25', models.FloatField(verbose_name='PM2.5年平均浓度')),
                ('so2_emissions', models.FloatField(verbose_name='二氧化硫排放量')),
                ('co2_per_gdp', models.FloatField(verbose_name='单位GDP二氧化碳排放量')),
                ('cod_emissions', models.FloatField(verbose_name='化学需氧量排放量')),
                ('nh_emissions', models.FloatField(verbose_name='氨氮排放量')),
                ('water_per', models.FloatField(verbose_name='人均耗水量')),
                ('water_per_gdp', models.FloatField(verbose_name='单位GDP用水量')),
                ('planting_area', models.FloatField(verbose_name='播种面积占比')),
                ('ef_per', models.FloatField(verbose_name='人均生态足迹')),
                ('green_innovation', models.FloatField(blank=True, null=True, verbose_name='绿色创新')),
                ('energy_use', models.FloatField(blank=True, null=True, verbose_name='能源利用')),
                ('parma_ratio', models.FloatField(blank=True, null=True, verbose_name='帕尔玛比率')),
                ('income', models.FloatField(blank=True, null=True, verbose_name='收入')),
                ('infrastructure', models.FloatField(blank=True, null=True, verbose_name='基础设施建设')),
                ('education', models.FloatField(blank=True, null=True, verbose_name='教育')),
                ('life_expectancy', models.FloatField(blank=True, null=True, verbose_name='预期寿命')),
                ('social_security', models.FloatField(blank=True, null=True, verbose_name='社会保障')),
                ('air_pollution', models.FloatField(blank=True, null=True, verbose_name='大气污染')),
                ('greenhouse', models.FloatField(blank=True, null=True, verbose_name='温室气体排放')),
                ('nitrogen', models.FloatField(blank=True, null=True, verbose_name='氮排放')),
                ('water_withdrawal', models.FloatField(blank=True, null=True, verbose_name='取水量')),
                ('land_use', models.FloatField(blank=True, null=True, verbose_name='土地利用')),
                ('EF', models.FloatField(blank=True, null=True, verbose_name='生态足迹')),
                ('city_green_economy', models.FloatField(blank=True, null=True, verbose_name='绿色经济')),
                ('city_sustainable', models.FloatField(blank=True, null=True, verbose_name='可持续发展')),
                ('city_gep_plus', models.FloatField(blank=True, null=True, verbose_name='GEP+')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_record_ls', to='work.Area', verbose_name='地区')),
            ],
        ),
        migrations.CreateModel(
            name='ProvinceDataRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='年度')),
                ('r_d', models.FloatField(verbose_name='规模以上工业企业R&D经费支出')),
                ('per_unit_gdp', models.FloatField(verbose_name='单位GDP能耗')),
                ('rural_urban', models.FloatField(verbose_name='乡-城人均年收入比')),
                ('urban_per', models.FloatField(verbose_name='城镇居民人均可支配收入')),
                ('rural_per', models.FloatField(verbose_name='农村居民人均可支配收入')),
                ('garbage', models.FloatField(verbose_name='生活垃圾无害化处理率')),
                ('bus_per', models.FloatField(verbose_name='平均万人拥有公共汽车')),
                ('urban_sewage', models.FloatField(verbose_name='城镇生活污水集中处理率')),
                ('edu_years', models.FloatField(verbose_name='平均受教育年限')),
                ('mortality', models.FloatField(verbose_name='死亡率')),
                ('pension_cov', models.FloatField(verbose_name='养老保险覆盖率')),
                ('medical_cov', models.FloatField(verbose_name='医疗保险覆盖率')),
                ('unemployment_cov', models.FloatField(verbose_name='失业保险覆盖率')),
                ('pm25', models.FloatField(verbose_name='PM2.5年平均浓度')),
                ('so2_emissions', models.FloatField(verbose_name='二氧化硫排放量')),
                ('co2_per_gdp', models.FloatField(verbose_name='单位GDP二氧化碳排放量')),
                ('cod_emissions', models.FloatField(verbose_name='化学需氧量排放量')),
                ('nh_emissions', models.FloatField(verbose_name='氨氮排放量')),
                ('water_per', models.FloatField(verbose_name='人均耗水量')),
                ('water_per_gdp', models.FloatField(verbose_name='单位GDP用水量')),
                ('planting_area', models.FloatField(verbose_name='播种面积占比')),
                ('ef_per', models.FloatField(verbose_name='人均生态足迹')),
                ('r_d_target', models.FloatField(verbose_name='规模以上工业企业R&D经费支出的目标值')),
                ('per_unit_gdp_target', models.FloatField(verbose_name='单位GDP能耗的目标值')),
                ('rural_urban_target', models.FloatField(verbose_name='乡-城人均年收入比的目标值')),
                ('urban_per_target', models.FloatField(verbose_name='城镇居民人均可支配收入的目标值')),
                ('rural_per_target', models.FloatField(verbose_name='农村居民人均可支配收入的目标值')),
                ('garbage_target', models.FloatField(verbose_name='生活垃圾无害化处理率的目标值')),
                ('bus_per_target', models.FloatField(verbose_name='平均万人拥有公共汽车的目标值')),
                ('urban_sewage_target', models.FloatField(verbose_name='城镇生活污水集中处理率的目标值')),
                ('edu_years_target', models.FloatField(verbose_name='平均受教育年限的目标值')),
                ('mortality_target', models.FloatField(verbose_name='死亡率的目标值')),
                ('pension_cov_target', models.FloatField(verbose_name='养老保险覆盖率的目标值')),
                ('medical_cov_target', models.FloatField(verbose_name='医疗保险覆盖率的目标值')),
                ('unemployment_cov_target', models.FloatField(verbose_name='失业保险覆盖率的目标值')),
                ('pm25_target', models.FloatField(verbose_name='PM2.5年平均浓度的目标值')),
                ('so2_emissions_target', models.FloatField(verbose_name='二氧化硫排放量的目标值')),
                ('co2_per_gdp_target', models.FloatField(verbose_name='单位GDP二氧化碳排放量的目标值')),
                ('cod_emissions_target', models.FloatField(verbose_name='化学需氧量排放量的目标值')),
                ('nh_emissions_target', models.FloatField(verbose_name='氨氮排放量的目标值')),
                ('water_per_target', models.FloatField(verbose_name='人均耗水量的目标值')),
                ('water_per_gdp_target', models.FloatField(verbose_name='单位GDP用水量的目标值')),
                ('planting_area_target', models.FloatField(verbose_name='播种面积占比的目标值')),
                ('ef_per_target', models.FloatField(verbose_name='人均生态足迹的目标值')),
                ('green_innovation', models.FloatField(blank=True, null=True, verbose_name='绿色创新')),
                ('energy_use', models.FloatField(blank=True, null=True, verbose_name='能源利用')),
                ('parma_ratio', models.FloatField(blank=True, null=True, verbose_name='帕尔玛比率')),
                ('income', models.FloatField(blank=True, null=True, verbose_name='收入')),
                ('infrastructure', models.FloatField(blank=True, null=True, verbose_name='基础设施建设')),
                ('education', models.FloatField(blank=True, null=True, verbose_name='教育')),
                ('life_expectancy', models.FloatField(blank=True, null=True, verbose_name='预期寿命')),
                ('social_security', models.FloatField(blank=True, null=True, verbose_name='社会保障')),
                ('air_pollution', models.FloatField(blank=True, null=True, verbose_name='大气污染')),
                ('greenhouse', models.FloatField(blank=True, null=True, verbose_name='温室气体排放')),
                ('nitrogen', models.FloatField(blank=True, null=True, verbose_name='氮排放')),
                ('water_withdrawal', models.FloatField(blank=True, null=True, verbose_name='取水量')),
                ('land_use', models.FloatField(blank=True, null=True, verbose_name='土地利用')),
                ('EF', models.FloatField(blank=True, null=True, verbose_name='生态足迹')),
                ('city_green_economy', models.FloatField(blank=True, null=True, verbose_name='绿色经济')),
                ('city_sustainable', models.FloatField(blank=True, null=True, verbose_name='可持续发展')),
                ('city_gep_plus', models.FloatField(blank=True, null=True, verbose_name='GEP+')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_record_ls', to='work.Province', verbose_name='地区')),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created',), 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.DeleteModel(
            name='DataRecord',
        ),
    ]
