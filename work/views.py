from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models
from . import tasks


def index(request):
    return redirect('/admin')


def province_year_simple(request, province_name, year):
    '''
    /province/<省份>/<年度>
    输出对应省份对应年度所有地级市的“绿色经济”、“可持续发展”、“GEP+”三项指标的得分
    '''
    province_data_record = get_object_or_404(klass=models.ProvinceDataRecord, province__name=province_name, year=year)
    cities = []
    for cdr in models.CityDataRecord.objects.filter(area__province__name=province_name, year=year).all():
        tmp = dict()
        tmp['city_name'] = cdr.area.name
        tmp['year'] = cdr.year
        tmp['city_green_economy'] = cdr.city_green_economy
        tmp['city_sustainable'] = cdr.city_sustainable
        tmp['city_gep_plus'] = cdr.city_gep_plus
        cities.append(tmp)
    return JsonResponse(data=dict(
        province_name=province_name,
        year=year,
        green_economy=province_data_record.city_green_economy,
        sustainable=province_data_record.city_sustainable,
        gep_plus=province_data_record.city_gep_plus,
        cities=cities
        ))


def province_year_all(request, province_name, year):
    '''
    /prov/<省份>/<年度>
    输出对应省份对应年度的全部数据
    '''
    province_data_record = get_object_or_404(klass=models.ProvinceDataRecord, province__name=province_name, year=year)
    return JsonResponse(data=dict(
        province_name=province_name,
        year=year,
        r_d=province_data_record.r_d,
        renewable_energy_per=province_data_record.renewable_energy_per, per_unit_gdp=province_data_record.per_unit_gdp,
        rural_urban=province_data_record.rural_urban, urban_per=province_data_record.urban_per,
        rural_per=province_data_record.rural_per, garbage=province_data_record.garbage,
        bus_per=province_data_record.bus_per, urban_sewage=province_data_record.urban_sewage,
        edu_years=province_data_record.edu_years, mortality=province_data_record.mortality,
        pension_cov=province_data_record.pension_cov, medical_cov=province_data_record.medical_cov,
        unemployment_cov=province_data_record.unemployment_cov, pm25=province_data_record.pm25,
        so2_emissions=province_data_record.so2_emissions, co2_per_gdp=province_data_record.co2_per_gdp,
        cod_emissions=province_data_record.cod_emissions, nh_emissions=province_data_record.nh_emissions,
        water_per=province_data_record.water_per, water_per_gdp=province_data_record.water_per_gdp,
        planting_area=province_data_record.planting_area, ef_per=province_data_record.ef_per,
        r_d_target=province_data_record.r_d_target,
        renewable_energy_per_target=province_data_record.renewable_energy_per_target,
        per_unit_gdp_target=province_data_record.per_unit_gdp_target,
        rural_urban_target=province_data_record.rural_urban_target,
        urban_per_target=province_data_record.urban_per_target, rural_per_target=province_data_record.rural_per_target,
        garbage_target=province_data_record.garbage_target, bus_per_target=province_data_record.bus_per_target,
        urban_sewage_target=province_data_record.urban_sewage_target,
        edu_years_target=province_data_record.edu_years_target, mortality_target=province_data_record.mortality_target,
        pension_cov_target=province_data_record.pension_cov_target,
        medical_cov_target=province_data_record.medical_cov_target,
        unemployment_cov_target=province_data_record.unemployment_cov_target,
        pm25_target=province_data_record.pm25_target, so2_emissions_target=province_data_record.so2_emissions_target,
        co2_per_gdp_target=province_data_record.co2_per_gdp_target,
        cod_emissions_target=province_data_record.cod_emissions_target,
        nh_emissions_target=province_data_record.nh_emissions_target,
        water_per_target=province_data_record.water_per_target,
        water_per_gdp_target=province_data_record.water_per_gdp_target,
        planting_area_target=province_data_record.planting_area_target,
        ef_per_target=province_data_record.ef_per_target, green_innovation=province_data_record.green_innovation,
        renewable_energy=province_data_record.renewable_energy, energy_use=province_data_record.energy_use,
        parma_ratio=province_data_record.parma_ratio, income=province_data_record.income,
        infrastructure=province_data_record.infrastructure, education=province_data_record.education,
        life_expectancy=province_data_record.life_expectancy, social_security=province_data_record.social_security,
        air_pollution=province_data_record.air_pollution, greenhouse=province_data_record.greenhouse,
        nitrogen=province_data_record.nitrogen, water_withdrawal=province_data_record.water_withdrawal,
        land_use=province_data_record.land_use, EF=province_data_record.EF,

        green_economy=province_data_record.city_green_economy,
        sustainable=province_data_record.city_sustainable,
        gep_plus=province_data_record.city_gep_plus,

        ))


def city_year_data(request, province_name, city_name, year):
    '''
    '/city/<省份>/<城市>/<年度>'
    输出对应省份对应城市对应年度的全部数据
    '''
    city_data_record = get_object_or_404(
        klass=models.CityDataRecord, area__province__name=province_name, area__name=city_name, year=year)
    return JsonResponse(data=dict(
        province_name=province_name,
        city_name=city_name, year=city_data_record.year, r_d=city_data_record.r_d,
        per_unit_gdp=city_data_record.per_unit_gdp, rural_urban=city_data_record.rural_urban,
        urban_per=city_data_record.urban_per, rural_per=city_data_record.rural_per, garbage=city_data_record.garbage,
        bus_per=city_data_record.bus_per, urban_sewage=city_data_record.urban_sewage,
        edu_years=city_data_record.edu_years, mortality=city_data_record.mortality,
        pension_cov=city_data_record.pension_cov, medical_cov=city_data_record.medical_cov,
        unemployment_cov=city_data_record.unemployment_cov, pm25=city_data_record.pm25,
        so2_emissions=city_data_record.so2_emissions, co2_per_gdp=city_data_record.co2_per_gdp,
        cod_emissions=city_data_record.cod_emissions, nh_emissions=city_data_record.nh_emissions,
        water_per=city_data_record.water_per, water_per_gdp=city_data_record.water_per_gdp,
        planting_area=city_data_record.planting_area, ef_per=city_data_record.ef_per,
        green_innovation=city_data_record.green_innovation, energy_use=city_data_record.energy_use,
        parma_ratio=city_data_record.parma_ratio, income=city_data_record.income,
        infrastructure=city_data_record.infrastructure, education=city_data_record.education,
        life_expectancy=city_data_record.life_expectancy, social_security=city_data_record.social_security,
        air_pollution=city_data_record.air_pollution, greenhouse=city_data_record.greenhouse,
        nitrogen=city_data_record.nitrogen, water_withdrawal=city_data_record.water_withdrawal,
        land_use=city_data_record.land_use, EF=city_data_record.EF,
        city_green_economy=city_data_record.city_green_economy, city_sustainable=city_data_record.city_sustainable,
        city_gep_plus=city_data_record.city_gep_plus,
        ))


@login_required
def process(request, province_name, year):
    year = int(year)
    pdr = get_object_or_404(klass=models.ProvinceDataRecord, province__name=province_name, year=year)
    # cities_num = models.Area.objects.filter(province__name=province_name).count()
    # if pdr.cities_records.count() != cities_num:
    #     messages.warning(request, message=f'{province_name}{year}的地区数据不全，不能开展计算，请重新上传数据')
    try:
        tasks.do_calc(province_name=province_name, year=year)
        messages.success(request, message='计算成功')
    except ValueError:
        messages.error(request, message=f'计算失败，请检查数据，确保该省及该省所辖地区{year}、{year-1}年份的数据')

    return redirect(f'/admin/work/provincedatarecord/{pdr.id}/change/')


def article_json(request, article_id):
    a = models.Article.objects.filter(id=article_id).first()
    if not isinstance(a, models.Article):
        return JsonResponse(data={}, status=404)
    return JsonResponse(data=dict(
        title=a.title,
        author=a.author,
        info=a.info,
        body=a.body,
        pub_date=a.pub_date,
        attach_ls=[{'url': att.attach.url, 'name': att.name} for att in a.attach_ls.all()]
        ))

