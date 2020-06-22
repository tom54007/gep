# Generated by Django 3.0.4 on 2020-06-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basework', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annual_data',
            name='co2_per_gdp',
        ),
        migrations.RemoveField(
            model_name='annual_data',
            name='edu_years',
        ),
        migrations.RemoveField(
            model_name='annual_data',
            name='medical_cov',
        ),
        migrations.RemoveField(
            model_name='annual_data',
            name='pension_cov',
        ),
        migrations.RemoveField(
            model_name='annual_data',
            name='per_unit_gdp',
        ),
        migrations.RemoveField(
            model_name='annual_data',
            name='unemployment_cov',
        ),
        migrations.RemoveField(
            model_name='prov_annual_data',
            name='co2_per_gdp',
        ),
        migrations.RemoveField(
            model_name='prov_annual_data',
            name='edu_years',
        ),
        migrations.RemoveField(
            model_name='prov_annual_data',
            name='medical_cov',
        ),
        migrations.RemoveField(
            model_name='prov_annual_data',
            name='pension_cov',
        ),
        migrations.RemoveField(
            model_name='prov_annual_data',
            name='per_unit_gdp',
        ),
        migrations.RemoveField(
            model_name='prov_annual_data',
            name='unemployment_cov',
        ),
        migrations.AlterField(
            model_name='prov_annual_data',
            name='r_d',
            field=models.FloatField(verbose_name='企业R&D内部经费支出'),
        ),
    ]