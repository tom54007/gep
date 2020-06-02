from django.contrib import admin
from django.shortcuts import reverse
from django.utils.html import format_html
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from . import models
from . import tasks
from openpyxl import load_workbook
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from tablib import Dataset
from collections import OrderedDict


class ArticleCreateForm(forms.ModelForm):

    class Meta:
        model = models.Article
        fields = 'title', 'author', 'info', 'body', 'pub_date'

        widgets = {
            'body': CKEditorUploadingWidget(),
            'info': CKEditorWidget(),
            }


class ArticleAttachInlineAdmin(admin.TabularInline):
    model = models.Attach
    fields = 'name', 'attach', 'created'
    readonly_fields = 'created',
    extra = 0


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'author', 'pub_date', 'created', 'updated'
    list_display_links = 'title',
    search_fields = 'title', 'author', 'pub_date', 'info', 'body'
    date_hierarchy = 'created'
    readonly_fields = 'id', 'created', 'updated'

    form = ArticleCreateForm

    inlines = ArticleAttachInlineAdmin,


class AreaInlineAdmin(admin.TabularInline):
    model = models.Area
    fields = 'id', 'name',
    readonly_fields = 'id',
    extra = 0


@admin.register(models.Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    list_display_links = 'name',
    search_fields = 'name',

    inlines = AreaInlineAdmin,


class AreaResource(resources.ModelResource):
    province = fields.Field(column_name='province', attribute='province',
                            widget=ForeignKeyWidget(models.Province, 'name'))

    __header_map = {'所属省份': 'province', '区域名称': 'name'}

    class Meta:
        model = models.Area
        exclude = 'id',
        import_id_fields = ('province', 'name')
        clean_model_instances = True

    def get_export_headers(self):
        headers = []
        for field in self.get_export_fields():
            headers.append(self.Meta.model._meta.get_field(field.column_name).verbose_name)
        return headers

    def dehydrate_province(self, obj: models.ProvinceDataRecord):
        return obj.province.name

    def get_or_init_instance(self, instance_loader, row):
        params = {}
        for key in instance_loader.resource.get_import_id_fields():
            field = instance_loader.resource.fields[key]
            params[field.attribute] = field.clean(row)
        try:
            obj = self.get_queryset().get(**params)
            return obj, False
        except models.Area.DoesNotExist:
            headers = [field.column_name for field in self.get_export_fields()]
            for key in headers:
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            obj = models.Area.objects.create(**params)
            return obj, True

    def import_data(self, dataset, dry_run=False, raise_errors=False,
                    use_transactions=None, collect_failed_rows=False, **kwargs):
        headers = []
        for header in dataset.headers:
            if header in self.__header_map:
                headers.append(self.__header_map[header])
            else:
                headers.append(header)

        _dataset = Dataset(headers=headers)
        for row in dataset:
            _dataset.append(row)
        dataset = _dataset
        return super(self.__class__, self).import_data(
            dataset=dataset, dry_run=dry_run, raise_errors=raise_errors,
            use_transactions=use_transactions,
            collect_failed_rows=collect_failed_rows, **kwargs
            )


@admin.register(models.Area)
class AreaAdmin(ImportExportModelAdmin):
    resource_class = AreaResource
    list_display = 'id', 'province', 'name'
    list_display_links = 'name',
    search_fields = 'name', 'province',


city_verbose_to_header_map = OrderedDict([("省份", "province"), ('地区', 'area'), ('年度', 'year'),
        ('规模以上工业企业R&D经费支出(万元)', 'r_d'), ('单位GDP能耗(吨/万元)', 'per_unit_gdp'), ('乡-城人均年收入比(/)', 'rural_urban'),
        ('城镇居民人均可支配收入(元)', 'urban_per'), ('农村居民人均可支配收入(元)', 'rural_per'), ('生活垃圾无害化处理率(%)', 'garbage'),
        ('平均万人拥有公共汽车(/)', 'bus_per'), ('城镇生活污水集中处理率(%)', 'urban_sewage'), ('平均受教育年限(年)', 'edu_years'),
        ('死亡率(%)', 'mortality'), ('养老保险覆盖率(%)', 'pension_cov'), ('医疗保险覆盖率(%)', 'medical_cov'),
        ('失业保险覆盖率(%)', 'unemployment_cov'), ('PM2.5年平均浓度(微克/立方米)', 'pm25'), ('二氧化硫排放量(万吨)', 'so2_emissions'),
        ('单位GDP二氧化碳排放量(千克/元)', 'co2_per_gdp'), ('化学需氧量排放量(万吨)', 'cod_emissions'), ('氨氮排放量(万吨)', 'nh_emissions'),
        ('人均耗水量(立方米)', 'water_per'), ('单位GDP用水量(立方米/万元)', 'water_per_gdp'), ('播种面积占比(%)', 'planting_area'),
        ('人均生态足迹(万吨碳/万人)', 'ef_per'), ('绿色创新', 'green_innovation'), ('能源利用', 'energy_use'), ('帕尔玛比率', 'parma_ratio'),
        ('收入', 'income'), ('基础设施建设', 'infrastructure'), ('教育', 'education'), ('预期寿命', 'life_expectancy'),
        ('社会保障', 'social_security'), ('大气污染', 'air_pollution'), ('温室气体排放', 'greenhouse'), ('氮排放', 'nitrogen'),
        ('取水量', 'water_withdrawal'), ('土地利用', 'land_use'), ('生态足迹', 'EF'), ('绿色经济', 'city_green_economy'),
        ('可持续发展', 'city_sustainable'), ('GEP+', 'city_gep_plus'),
        ])
city_header_to_verbose_map = OrderedDict(
    [('province', '省份'), ('area', '地区'), ('year', '年度'), ('r_d', '规模以上工业企业R&D经费支出(万元)'),
        ('per_unit_gdp', '单位GDP能耗(吨/万元)'), ('rural_urban', '乡-城人均年收入比(/)'), ('urban_per', '城镇居民人均可支配收入(元)'),
        ('rural_per', '农村居民人均可支配收入(元)'), ('garbage', '生活垃圾无害化处理率(%)'), ('bus_per', '平均万人拥有公共汽车(/)'),
        ('urban_sewage', '城镇生活污水集中处理率(%)'), ('edu_years', '平均受教育年限(年)'), ('mortality', '死亡率(%)'),
        ('pension_cov', '养老保险覆盖率(%)'), ('medical_cov', '医疗保险覆盖率(%)'), ('unemployment_cov', '失业保险覆盖率(%)'),
        ('pm25', 'PM2.5年平均浓度(微克/立方米)'), ('so2_emissions', '二氧化硫排放量(万吨)'), ('co2_per_gdp', '单位GDP二氧化碳排放量(千克/元)'),
        ('cod_emissions', '化学需氧量排放量(万吨)'), ('nh_emissions', '氨氮排放量(万吨)'), ('water_per', '人均耗水量(立方米)'),
        ('water_per_gdp', '单位GDP用水量(立方米/万元)'), ('planting_area', '播种面积占比(%)'), ('ef_per', '人均生态足迹(万吨碳/万人)'),
        ('green_innovation', '绿色创新'), ('energy_use', '能源利用'), ('parma_ratio', '帕尔玛比率'), ('income', '收入'),
        ('infrastructure', '基础设施建设'), ('education', '教育'), ('life_expectancy', '预期寿命'), ('social_security', '社会保障'),
        ('air_pollution', '大气污染'), ('greenhouse', '温室气体排放'), ('nitrogen', '氮排放'), ('water_withdrawal', '取水量'),
        ('land_use', '土地利用'), ('EF', '生态足迹'), ('city_green_economy', '绿色经济'), ('city_sustainable', '可持续发展'),
        ('city_gep_plus', 'GEP+')

        ])


models.Area.objects.filter(province__name='', name='')


class AreaForeignWidget(ForeignKeyWidget):

    def clean(self, value, row=None, *args, **kwargs):
        return self.model.objects.get(
            name=row["area"], province__name=row["province"],
        )


class CityDataRecordResource(resources.ModelResource):

    province = fields.Field()
    area = fields.Field(
        column_name='area', attribute='area',
        widget=AreaForeignWidget(models.Area, 'name')
        )

    class Meta:
        model = models.CityDataRecord
        exclude = 'id',
        verbose_name = True
        import_fields = city_header_to_verbose_map.keys()
        export_fields = city_header_to_verbose_map.keys()
        import_id_fields = ('area', 'year')
        clean_model_instances = True

    def dehydrate_province(self, obj: models.CityDataRecord):
        return obj.area.province.name

    def dehydrate_area(self, obj: models.CityDataRecord):
        return obj.area.name

    def get_export_headers(self):
        headers = city_verbose_to_header_map.keys()
        return headers

    def get_or_init_instance(self, instance_loader, row):
        params = {}
        for key in instance_loader.resource.get_import_id_fields():
            field = instance_loader.resource.fields[key]
            params[field.attribute] = field.clean(row)
        try:
            obj = self.get_queryset().get(**params)
            return obj, False
        except models.CityDataRecord.DoesNotExist:
            headers = [field.column_name for field in self.get_export_fields()]
            for key in headers:
                field = instance_loader.resource.fields[key]
                if field.attribute:
                    params[field.attribute] = field.clean(row)
            print(params)
            obj = models.CityDataRecord.objects.create(**params)
            return obj, True

    def import_data(self, dataset, dry_run=False, raise_errors=False,
                    use_transactions=None, collect_failed_rows=False, **kwargs):

        headers = []
        for header in dataset.headers:
            if header in city_verbose_to_header_map:
                headers.append(city_verbose_to_header_map[header])
            else:
                headers.append(header)

        _dataset = Dataset(headers=headers)
        for row in dataset:
            _dataset.append(row)
        dataset = _dataset

        return super(self.__class__, self).import_data(
            dataset=dataset, dry_run=dry_run, raise_errors=raise_errors,
            use_transactions=use_transactions, collect_failed_rows=collect_failed_rows, **kwargs)


@admin.register(models.CityDataRecord)
class CityDataRecordAdmin(ImportExportModelAdmin):
    resource_class = CityDataRecordResource
    list_display = 'id', 'area', 'year',
    list_display_links = 'area', 'year',
    # readonly_fields = 'area', 'year', 'r_d', 'per_unit_gdp', 'rural_urban', 'urban_per', 'rural_per', 'garbage', \
    #                   'bus_per', 'urban_sewage', 'edu_years', 'mortality', 'pension_cov', 'medical_cov',\
    #                   'unemployment_cov', 'pm25', 'so2_emissions', 'co2_per_gdp', 'cod_emissions',\
    #                   'nh_emissions', 'water_per', 'water_per_gdp', 'planting_area', 'ef_per',\
    #                   'green_innovation', 'energy_use', 'parma_ratio', 'income', 'infrastructure', 'education',\
    #                   'life_expectancy', 'social_security', 'air_pollution', 'greenhouse', 'nitrogen', \
    #                   'water_withdrawal', 'land_use', 'EF', 'city_green_economy', 'city_sustainable', 'city_gep_plus'
    autocomplete_fields = 'area',
    search_fields = 'area__province__name', 'area__name', 'year'
    fieldsets = (
        ('地区年份', {
            'fields': (('area',), ('year',), )
            }),
        ('绿色经济基础数据', {
            'fields': (('r_d', ),
                       ('per_unit_gdp',), ('rural_urban', ),
                       ('urban_per', ), ('rural_per', ),
                       ('garbage', ), ('bus_per', ),
                       ('urban_sewage', ), ('edu_years', ),
                       ('mortality', ), ('pension_cov', ),
                       ('medical_cov', ), ('unemployment_cov', ),
                       ('pm25', ), ('so2_emissions', ),)
            }),
        ('可持续发展基础数据', {
            'fields': (('co2_per_gdp', ), ('cod_emissions', ),
                       ('nh_emissions', ), ('water_per', ),
                       ('water_per_gdp', ), ('planting_area', ),
                       ('ef_per', ),
                       )
            }

        ),
        ('高级信息', {
            'classes': ('collapse',),
            'fields': (('green_innovation',), ('energy_use',), ('parma_ratio',), ('income',), ('infrastructure',),
                       ('education',), ('life_expectancy',), ('social_security',), ('air_pollution',), ('greenhouse',),
                       ('nitrogen',), ('water_withdrawal',), ('land_use',), ('EF',), ('city_green_economy',),
                       ('city_sustainable',), ('city_gep_plus',)
            ),

            })

    )


class ProvinceDataRecordCreateForm(forms.ModelForm):

    class Meta:
        model = models.ProvinceDataRecord
        fields = ('province', 'year', 'r_d', 'r_d_target', 'per_unit_gdp', 'per_unit_gdp_target',
                  'rural_urban', 'rural_urban_target', 'urban_per', 'urban_per_target', 'rural_per',
                  'rural_per_target', 'garbage', 'garbage_target', 'bus_per', 'bus_per_target',
                  'urban_sewage', 'urban_sewage_target', 'edu_years', 'edu_years_target', 'mortality',
                  'mortality_target', 'pension_cov', 'pension_cov_target', 'medical_cov',
                  'medical_cov_target', 'unemployment_cov', 'unemployment_cov_target',
                  'pm25', 'pm25_target', 'so2_emissions', 'so2_emissions_target', 'co2_per_gdp',
                  'co2_per_gdp_target', 'cod_emissions', 'cod_emissions_target', 'nh_emissions',
                  'nh_emissions_target', 'water_per', 'water_per_target', 'water_per_gdp',
                  'water_per_gdp_target', 'planting_area', 'planting_area_target', 'ef_per',
                  'ef_per_target',
                  # 'attach'
                  )
        # exclude = ('green_innovation', 'energy_use', 'parma_ratio', 'income',
        #            'infrastructure', 'education', 'life_expectancy', 'social_security',
        #            'air_pollution', 'greenhouse', 'nitrogen', 'water_withdrawal', 'land_use',
        #            'EF', 'city_green_economy', 'city_sustainable', 'city_gep_plus')

    def clean_attach(self):
        attach = self.cleaned_data.get('attach')
        province = self.cleaned_data.get('province')
        if isinstance(province, models.Province):
            models.import_excel_validator(attach, province_obj=province)
        return attach


class ProvinceDataRecordResource(resources.ModelResource):
    province = fields.Field(
        column_name='province', attribute='province', widget=ForeignKeyWidget(models.Province, 'name'))

    __header_map = {
        '省份': 'province', '年度': 'year', '企业 R&D 内部经费支出(亿元)': 'r_d', '可再生能源供给占比(%)':
            'renewable_energy_per', '单位GDP能耗(吨/万元)': 'per_unit_gdp',
        '乡-城人均年收入比(/)': 'rural_urban', '城镇居民人均可支配收入(元)': 'urban_per',
        '农村居民人均可支配收入(元)': 'rural_per', '生活垃圾无害化处理率(%)': 'garbage',
        '平均万人拥有公共汽车(/)': 'bus_per', '城镇生活污水集中处理率(%)': 'urban_sewage',
        '平均受教育年限(年)': 'edu_years', '死亡率(%)': 'mortality', '养老保险覆盖率(%)': 'pension_cov',
        '医疗保险覆盖率(%)': 'medical_cov', '失业保险覆盖率(%)': 'unemployment_cov',
        'PM2.5年平均浓度(微克/立方米)': 'pm25', '二氧化硫排放量(万吨)': 'so2_emissions',
        '单位GDP二氧化碳排放量(千克/元)': 'co2_per_gdp', '化学需氧量排放量(万吨)': 'cod_emissions',
        '氨氮排放量(万吨)': 'nh_emissions', '人均耗水量(立方米)': 'water_per',
        '单位GDP用水量(立方米/万元)': 'water_per_gdp', '播种面积占比(%)': 'planting_area',
        '人均生态足迹(万吨碳/万人)': 'ef_per', '企业 R&D 内部经费支出的目标值': 'r_d_target',
        '可再生能源供给占比的目标值': 'renewable_energy_per_target', '单位GDP能耗的目标值': 'per_unit_gdp_target',
        '乡-城人均年收入比的目标值': 'rural_urban_target', '城镇居民人均可支配收入的目标值': 'urban_per_target',
        '农村居民人均可支配收入的目标值': 'rural_per_target', '生活垃圾无害化处理率的目标值': 'garbage_target',
        '平均万人拥有公共汽车的目标值': 'bus_per_target', '城镇生活污水集中处理率的目标值': 'urban_sewage_target',
        '平均受教育年限的目标值': 'edu_years_target', '死亡率的目标值': 'mortality_target',
        '养老保险覆盖率的目标值': 'pension_cov_target', '医疗保险覆盖率的目标值': 'medical_cov_target',
        '失业保险覆盖率的目标值': 'unemployment_cov_target', 'PM2.5年平均浓度的目标值': 'pm25_target',
        '二氧化硫排放量的目标值': 'so2_emissions_target', '单位GDP二氧化碳排放量的目标值': 'co2_per_gdp_target',
        '化学需氧量排放量的目标值': 'cod_emissions_target', '氨氮排放量的目标值': 'nh_emissions_target',
        '人均耗水量的目标值': 'water_per_target', '单位GDP用水量的目标值': 'water_per_gdp_target',
        '播种面积占比的目标值': 'planting_area_target', '人均生态足迹的目标值': 'ef_per_target',
        '绿色创新': 'green_innovation', '可再生能源供给': 'renewable_energy',
        '能源利用': 'energy_use', '帕尔玛比率': 'parma_ratio', '收入': 'income',
        '基础设施建设': 'infrastructure', '教育': 'education',
        '预期寿命': 'life_expectancy', '社会保障': 'social_security',
        '大气污染': 'air_pollution', '温室气体排放': 'greenhouse', '氮排放': 'nitrogen',
        '取水量': 'water_withdrawal', '土地利用': 'land_use',
        '生态足迹': 'EF',
        '绿色经济': 'city_green_economy', '可持续发展': 'city_sustainable',
        'GEP+': 'city_gep_plus'}

    class Meta:
        model = models.ProvinceDataRecord
        exclude = 'id', 'status'
        verbose_name = True
        import_id_fields = ('province', 'year')
        clean_model_instances = True

    def get_export_headers(self):
        headers = []
        for field in self.get_export_fields():
            headers.append(self.Meta.model._meta.get_field(field.column_name).verbose_name)
        return headers

    def dehydrate_province(self, obj: models.ProvinceDataRecord):
        return obj.province.name

    def get_or_init_instance(self, instance_loader, row):
        params = {}
        for key in instance_loader.resource.get_import_id_fields():
            field = instance_loader.resource.fields[key]
            params[field.attribute] = field.clean(row)
        try:
            obj = self.get_queryset().get(**params)
            return obj, False
        except models.ProvinceDataRecord.DoesNotExist:
            headers = [field.column_name for field in self.get_export_fields()]
            for key in headers:
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            obj = models.ProvinceDataRecord.objects.create(**params)
            return obj, True

    def import_data(self, dataset, dry_run=False, raise_errors=False,
                    use_transactions=None, collect_failed_rows=False, **kwargs):
        headers = []
        for header in dataset.headers:
            if header in self.__header_map:
                headers.append(self.__header_map[header])
            else:
                headers.append(header)

        _dataset = Dataset(headers=headers)
        for row in dataset:
            _dataset.append(row)
        dataset = _dataset
        return super(self.__class__, self).import_data(
            dataset=dataset, dry_run=dry_run, raise_errors=raise_errors,
            use_transactions=use_transactions,
            collect_failed_rows=collect_failed_rows, **kwargs
            )


@admin.register(models.ProvinceDataRecord)
class ProvinceDataRecordAdmin(ImportExportModelAdmin):
    resource_class = ProvinceDataRecordResource
    list_display = 'id', 'province', 'year', 'calc_url'
    list_display_links = 'province', 'year',
    # readonly_fields = 'green_innovation', 'renewable_energy', 'energy_use', 'parma_ratio', 'income', 'infrastructure', 'education',\
    #                   'life_expectancy', 'social_security', 'air_pollution', 'greenhouse', 'nitrogen', \
    #                   'water_withdrawal', 'land_use', 'EF', 'city_green_economy', 'city_sustainable', 'city_gep_plus',\
    #                   'calc_url',

    readonly_fields = 'calc_url',

    def calc_url(self, ins):
        url = reverse('work:process', kwargs=dict(province_name=ins.province.name, year=ins.year))
        html = f'<a href="{url}" target="_blank" title="计算"><i class="fa fa-edit"></i> 计算</a>'
        return format_html(html)

    calc_url.short_description = '执行计算'

    form = ProvinceDataRecordCreateForm
    fieldsets = (
        ('省份年份', {
            'fields': (('province',), ('year',), )
            }),
        ('绿色经济基础数据', {
            'fields': (('r_d', 'r_d_target'), ('renewable_energy_per', 'renewable_energy_per_target'),
                       ('per_unit_gdp', 'per_unit_gdp_target'), ('rural_urban', 'rural_urban_target'),
                       ('urban_per', 'urban_per_target'), ('rural_per', 'rural_per_target'),
                       ('garbage', 'garbage_target'), ('bus_per', 'bus_per_target'),
                       ('urban_sewage', 'urban_sewage_target'), ('edu_years', 'edu_years_target'),
                       ('mortality', 'mortality_target'), ('pension_cov', 'pension_cov_target'),
                       ('medical_cov', 'medical_cov_target'), ('unemployment_cov', 'unemployment_cov_target'),
                       ('pm25', 'pm25_target'), ('so2_emissions', 'so2_emissions_target'),)
            }),
        ('可持续发展基础数据', {
            'fields': (('co2_per_gdp', 'co2_per_gdp_target'), ('cod_emissions', 'cod_emissions_target'),
                       ('nh_emissions', 'nh_emissions_target'), ('water_per', 'water_per_target'),
                       ('water_per_gdp', 'water_per_gdp_target'), ('planting_area', 'planting_area_target'),
                       ('ef_per', 'ef_per_target'),
                       )
            }

        ),
        ('高级信息', {
            'classes': ('collapse',),
            'fields': (('green_innovation',), ('renewable_energy',), ('energy_use',), ('parma_ratio',), ('income',), ('infrastructure',),
                       ('education',), ('life_expectancy',), ('social_security',), ('air_pollution',), ('greenhouse',),
                       ('nitrogen',), ('water_withdrawal',), ('land_use',), ('EF',), ('city_green_economy',),
                       ('city_sustainable',), ('city_gep_plus',)
            ),

            })

    )
    search_fields = 'province',
    autocomplete_fields = 'province',



admin.site.site_header = "数据管理后台"
admin.site.site_title = "数据管理后台"
admin.site.index_title = "欢迎来到数据管理后台"
