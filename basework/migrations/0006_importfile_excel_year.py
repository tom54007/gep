# Generated by Django 3.0.4 on 2020-06-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basework', '0005_auto_20200610_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='importfile_excel',
            name='year',
            field=models.IntegerField(default=2018, verbose_name='年度'),
            preserve_default=False,
        ),
    ]
