# Generated by Django 3.0.4 on 2020-06-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basework', '0013_auto_20200615_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importfile_excel',
            name='excelfile',
            field=models.FileField(upload_to='', verbose_name='上传'),
        ),
    ]
