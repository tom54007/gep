# Generated by Django 3.0.4 on 2020-03-17 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0012_auto_20200316_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citydatarecord',
            name='province_data',
        ),
        migrations.AlterField(
            model_name='provincedatarecord',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_record_ls', to='work.Province', verbose_name='省份'),
        ),
    ]