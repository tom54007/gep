import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
django.setup()
from work import tasks
from basework import admin, utils, models
from django.forms.models import model_to_dict
import numpy as np

# 省级单项基础指标
prov_item_list_index = [
    ('r_d', '企业R&D内部经费支出(亿元)'),
    ('renewable_energy_per', '可再生能源供给占比(%)'),
    ('per_unit_gdp', '单位GDP能耗(吨/万元)'),
    ('rural_urban', '乡-城人均年收入比(/)'),
    ('urban_per', '城镇居民人均可支配收入(元)'),
    ('rural_per', '农村居民人均可支配收入(元)'),
    ('garbage', '生活垃圾无害化处理率(%)'),
    ('bus_per', '平均万人拥有公共汽车(/)'),
    ('urban_sewage', '城镇生活污水集中处理率(%)'),
    ('edu_years', '平均受教育年限(年)'),
    ('mortality', '死亡率(%)'),
    ('pension_cov', '养老保险覆盖率(%)'),
    ('medical_cov', '医疗保险覆盖率(%)'),
    ('unemployment_cov', '失业保险覆盖率(%)'),
    ('pm25', 'PM2.5年平均浓度(微克/立方米)'),
    ('so2_emissions', '二氧化硫排放量(万吨)'),
    ('co2_per_gdp', '单位GDP二氧化碳排放量(千克/元)'),
    ('cod_emissions', '化学需氧量排放量(万吨)'),
    ('nh_emissions', '氨氮排放量(万吨)'),
    ('water_per', '人均耗水量(立方米)'),
    ('water_per_gdp', '单位GDP用水量(立方米/万元)'),
    ('planting_area', '播种面积占比(%)'),
    ('ef_per', '人均生态足迹(万吨碳/万人)')
]

provdata_this_year = models.Prov_Annual_data.objects.get(province="江苏省",year=2017)
print(provdata_this_year.r_d_target)
provdata_this_year = model_to_dict(provdata_this_year)
print(provdata_this_year['mortality_target'])

item_extremum = []
# for i in prov_item_list_index:
#     item_index = []
#     for m in provdata_this_year.values(i[0]+"_target"):
#         item_index.append(m[i[0]])
#         print(m[i[0]])
    # item_max_each = (i[0] + "_max", max(item_index))
    # item_min_each = (i[0] + "_min", min(item_index))
    # item_extremum.append(item_max_each)
    # item_extremum.append(item_min_each)
# 极值字典
item_extremum = dict(item_extremum)



#
# # tasks.do_calc('江苏省', 2021)
#
# # 地区待计算指标列表
# area_item_this_year = utils.read_items_name
# prov_item_last_year = utils.read_prov_items_name
# area_item_list_index = [
#     # 计算所得单项基础指标
#     ('r_d','规模以上工业企业R&D经费支出(万元)'),
#     ('per_unit_gdp','单位GDP能耗(吨/万元)'),
#     ('rural_urban','乡-城人均年收入比(/)'),
#     ('urban_per','城镇居民人均可支配收入(元)'),
#     ('rural_per','农村居民人均可支配收入(元)'),
#     ('garbage','生活垃圾无害化处理率(%)'),
#     ('bus_per','平均万人拥有公共汽车(/)'),
#     ('urban_sewage','城镇生活污水集中处理率(%)'),
#     ('edu_years','平均受教育年限(年)'),
#     ('mortality','死亡率(%)'),
#     ('pension_cov','养老保险覆盖率(%)'),
#     ('medical_cov','医疗保险覆盖率(%)'),
#     ('unemployment_cov','失业保险覆盖率(%)'),
#     ('pm25','PM2.6年平均浓度(微克/立方米)'),
#     ('so2_emissions','二氧化硫排放量(万吨)'),
#     ('co2_per_gdp','单位GDP二氧化碳排放量(千克/元)'),
#     ('cod_emissions','化学需氧量排放量(万吨)'),
#     ('nh_emissions','氨氮排放量(万吨)'),
#     ('water_per','人均耗水量(立方米)'),
#     ('water_per_gdp','单位GDP用水量(立方米/万元)'),
#     ('planting_area','播种面积占比(%)'),
#     ('ef_per','人均生态足迹(万吨碳/万人)')
# ]
# # 省级单项基础指标
# prov_item_list_index = [
#     ('r_d','企业R&D内部经费支出(亿元)'),
#     ('renewable_energy_per','可再生能源供给占比(%)'),
#     ('per_unit_gdp','单位GDP能耗(吨/万元)'),
#     ('rural_urban','乡-城人均年收入比(/)'),
#     ('urban_per','城镇居民人均可支配收入(元)'),
#     ('rural_per','农村居民人均可支配收入(元)'),
#     ('garbage','生活垃圾无害化处理率(%)'),
#     ('bus_per','平均万人拥有公共汽车(/)'),
#     ('urban_sewage','城镇生活污水集中处理率(%)'),
#     ('edu_years','平均受教育年限(年)'),
#     ('mortality','死亡率(%)'),
#     ('pension_cov','养老保险覆盖率(%)'),
#     ('medical_cov','医疗保险覆盖率(%)'),
#     ('unemployment_cov','失业保险覆盖率(%)'),
#     ('pm25','PM2.5年平均浓度(微克/立方米)'),
#     ('so2_emissions','二氧化硫排放量(万吨)'),
#     ('co2_per_gdp','单位GDP二氧化碳排放量(千克/元)'),
#     ('cod_emissions','化学需氧量排放量(万吨)'),
#     ('nh_emissions','氨氮排放量(万吨)'),
#     ('water_per','人均耗水量(立方米)'),
#     ('water_per_gdp','单位GDP用水量(立方米/万元)'),
#     ('planting_area','播种面积占比(%)'),
#     ('ef_per','人均生态足迹(万吨碳/万人)')
# ]
# # GEP框架指标计算
# area_gep_index = [
#     ('green_innovation','绿色创新'),
#     ('energy_use','能源利用'),
#     ('parma_ratio','帕尔玛比率'),
#     ('income','收入'),
#     ('infrastructure','基础设施建设'),
#     ('education','教育'),
#     ('life_expectancy','预期寿命'),
#     ('social_security','社会保障'),
#     ('air_pollution','大气污染'),
#     ('greenhouse','温室气体排放'),
#     ('nitrogen','氮排放'),
#     ('water_withdrawal','取水量'),
#     ('land_use','土地利用'),
#     ('EF','生态足迹'),
#     ('city_green_economy','绿色经济'),
#     ('city_sustainable','可持续发展'),
#     ('city_gep_plus','GEP+')
# ]
# prov_gep_index = [
#     ('green_innovation','绿色创新'),
#     ('renewable_energy','可再生能源供给'),
#     ('energy_use','能源利用'),
#     ('parma_ratio','帕尔玛比率'),
#     ('income','收入'),
#     ('infrastructure','基础设施建设'),
#     ('education','教育'),
#     ('life_expectancy','预期寿命'),
#     ('social_security','社会保障'),
#     ('air_pollution','大气污染'),
#     ('greenhouse','温室气体排放'),
#     ('nitrogen','氮排放'),
#     ('water_withdrawal','取水量'),
#     ('land_use','土地利用'),
#     ('EF','生态足迹'),
#     ('city_green_economy','绿色经济'),
#     ('city_sustainable','可持续发展'),
#     ('city_gep_plus','GEP+')
# ]
#
#
# # 查地区数据
# def calc_area_data(province, area, year):
#     areadata_this_year = models.Calculated_value.objects.filter(province=province, year=year)
#     areadata_last_year = models.Calculated_value.objects.filter(province=province, year=(year-1))
#     item_extremum = []
#     for i in area_item_list_index:
#         item_index = []
#         for m in areadata_this_year.values(i[0]):
#             item_index.append(m[i[0]])
#         item_max_each = (i[0]+"_max", max(item_index))
#         item_min_each = (i[0]+"_min", min(item_index))
#         item_extremum.append(item_max_each)
#         item_extremum.append(item_min_each)
#     # 极值字典
#     item_extremum = dict(item_extremum)
#     # 输出极值
#     print(item_extremum["mortality"+"_min"])
#     # queryset转字典
#     area_this_year_datalist = model_to_dict(areadata_this_year.get(area=area))
#     area_last_year_datalist = model_to_dict(areadata_last_year.get(area=area))
#     print("当期值")
#     print(area_this_year_datalist['mortality'])
#     print("前期值")
#     print(area_last_year_datalist['mortality'])
#
#     r_d = utils.item_calc_positive(area_last_year_datalist['r_d'], area_this_year_datalist['r_d'], item_extremum["r_d_max"])
#     per_unit_gdp = utils.item_calc_negative(area_last_year_datalist['per_unit_gdp'], area_this_year_datalist['per_unit_gdp'], item_extremum["per_unit_gdp_min"])
#     rural_urban = utils.item_calc_positive(area_last_year_datalist['rural_urban'], area_this_year_datalist['rural_urban'], item_extremum["rural_urban_max"])
#     urban_per = utils.item_calc_positive(area_last_year_datalist['urban_per'], area_this_year_datalist['urban_per'], item_extremum["urban_per_max"])
#     rural_per = utils.item_calc_positive(area_last_year_datalist['rural_per'], area_this_year_datalist['rural_per'], item_extremum["rural_per_max"])
#     garbage = utils.item_calc_positive(area_last_year_datalist['garbage'], area_this_year_datalist['garbage'], item_extremum["garbage_max"])
#     bus_per = utils.item_calc_positive(area_last_year_datalist['bus_per'], area_this_year_datalist['bus_per'], item_extremum["bus_per_max"])
#     urban_sewage = utils.item_calc_positive(area_last_year_datalist['urban_sewage'], area_this_year_datalist['urban_sewage'], item_extremum["urban_sewage_max"])
#     edu_years = utils.item_calc_positive(area_last_year_datalist['edu_years'], area_this_year_datalist['edu_years'], item_extremum["edu_years_max"])
#     mortality = utils.item_calc_negative(area_last_year_datalist['mortality'], area_this_year_datalist['mortality'], item_extremum["mortality_min"])
#     pension_cov = utils.item_calc_positive(area_last_year_datalist['pension_cov'], area_this_year_datalist['pension_cov'], item_extremum["pension_cov_max"])
#     medical_cov = utils.item_calc_positive(area_last_year_datalist['medical_cov'], area_this_year_datalist['medical_cov'], item_extremum["medical_cov_max"])
#     unemployment_cov = utils.item_calc_positive(area_last_year_datalist['unemployment_cov'], area_this_year_datalist['unemployment_cov'], item_extremum["unemployment_cov_max"])
#     pm25 = utils.item_calc_negative(area_last_year_datalist['pm25'], area_this_year_datalist['pm25'], item_extremum["pm25_min"])
#     so2_emissions = utils.item_calc_negative(area_last_year_datalist['so2_emissions'], area_this_year_datalist['so2_emissions'], item_extremum["so2_emissions_min"])
#     co2_per_gdp = utils.item_calc_negative(area_last_year_datalist['co2_per_gdp'], area_this_year_datalist['co2_per_gdp'], item_extremum["co2_per_gdp_min"])
#     cod_emissions = utils.item_calc_negative(area_last_year_datalist['cod_emissions'], area_this_year_datalist['cod_emissions'], item_extremum["cod_emissions_min"])
#     nh_emissions = utils.item_calc_negative(area_last_year_datalist['nh_emissions'], area_this_year_datalist['nh_emissions'], item_extremum["nh_emissions_min"])
#     water_per = utils.item_calc_negative(area_last_year_datalist['water_per'], area_this_year_datalist['water_per'], item_extremum["water_per_min"])
#     water_per_gdp = utils.item_calc_negative(area_last_year_datalist['water_per_gdp'], area_this_year_datalist['water_per_gdp'], item_extremum["water_per_gdp_min"])
#     planting_area = utils.item_calc_positive(area_last_year_datalist['planting_area'], area_this_year_datalist['planting_area'], item_extremum["planting_area_max"])
#     ef_per = utils.item_calc_negative(area_last_year_datalist['ef_per'], area_this_year_datalist['ef_per'], item_extremum["ef_per_min"])
#
#     #     单项框架指标得分计算
#     # 框架指标得分=框架内所有指标得分加权平均
#     # 绿色创新=企业R&D内部经费支出（省级）
#     # 绿色创新=规模以上工业企业R&D经费支出（市级）
#     # （2）可再生能源供给=可再生能源供给占比（省级有市级无）
#     # （3）能源利用=单位GDP能耗
#     # （4）帕尔玛比率=乡-城人均年收入比
#     # （5）收入=（城镇居民人均可支配收入得分*该项权重+农村居民人均可支配收入得分*该项权重）/（镇居民人均可支配收入权重+农村居民人均可支配收入权重）
#     # （6）基础设施建设得分=（生活垃圾无害化处理率得分*该项权重+平均万人拥有公共汽车得分*该项权重+城镇生活污水集中处理率得分*该项权重）/（生活垃圾无害化处理率权重+平均万人拥有公共汽车权重+城镇生活污水集中处理率权重）
#     # （7）教育=平均受教育年限
#     # （8）预期寿命=死亡率
#     # （9）社会保障=（养老保险覆盖率得分*该项权重+医疗保险覆盖率得分*该项权重+失业保险覆盖率得分*该项权重）/（养老保险覆盖率权重+医疗保险覆盖率权重+失业保险覆盖率权重）
#     # （10）大气污染=（PM2.5年平均浓度得分*该项权重+二氧化硫排放量得分*该项权重）/（PM2.5年平均浓度权重+二氧化硫排放量权重）
#     # （11）温室气体排放=单位GDP二氧化碳排放量
#     # （12）氮排放=（化学需氧量排放量得分*该项权重+氨氮排放量得分*该项权重）/（化学需氧量排放量权重+氨氮排放量权重）
#     # （13）取水量=（人均耗水量得分*该项权重+单位GDP用水量得分*该项权重）/（人均耗水量权重+单位GDP用水量权重）
#     # （14）土地利用=播种面积占比
#     # （15）生态足迹=人均生态足迹
#     green_innovation=r_d[0]
#     # renewable_energy=renewable_energy_per
#     energy_use=per_unit_gdp[0]
#     parma_ratio=rural_urban[0]
#     income=np.average([urban_per[0],rural_per[0]], weights=(urban_per[1],rural_per[1]))
#     # garbage,bus_per,urban_sewage
#     infrastructure=np.average([garbage[0],bus_per[0],urban_sewage[0]], weights=(garbage[1],bus_per[1],urban_sewage[1]))
#     education=edu_years[0]
#     life_expectancy=mortality[0]
#     # pension_cov,medical_cov,unemployment_cov
#     social_security=np.average([pension_cov[0],medical_cov[0],unemployment_cov[0]], weights=(pension_cov[1],medical_cov[1],unemployment_cov[1]))
#     # pm25,so2_emissions
#     air_pollution=np.average([pm25[0],so2_emissions[0]], weights=(pm25[1],so2_emissions[1]))
#     greenhouse=co2_per_gdp[0]
#     # cod_emissions,nh_emissions
#     nitrogen=np.average([cod_emissions[0],nh_emissions[0]], weights=(cod_emissions[1],nh_emissions[1]))
#     # water_per,water_per_gdp
#     water_withdrawal=np.average([water_per[0],water_per_gdp[0]], weights=(water_per[1],water_per_gdp[1]))
#     land_use=planting_area[0]
#     EF=ef_per[0]
#
#     # （1）绿色经济=（绿色创新*该项权重+能源利用*该项权重+帕尔玛比率*该项权重+收入*该项权重+基础设施建设*该项权重+教育*该项权重+预期寿命*该项权重+社会保障*该项权重+大气污染*该项权重）/（绿色创新权重+能源利用权重+帕尔玛比率权重+收入权重+基础设施建设权重+教育权重+预期寿命权重+社会保障权重+大气污染权重）
#     # r_d,per_unit_gdp,rural_urban,urban_per,rural_per,garbage,bus_per,urban_sewage,edu_years,mortality,pension_cov,medical_cov,unemployment_cov,pm25,so2_emissions
#     city_green_economy=np.average([r_d[0],per_unit_gdp[0],rural_urban[0],urban_per[0],rural_per[0],garbage[0],bus_per[0],urban_sewage[0],edu_years[0],mortality[0],pension_cov[0],medical_cov[0],unemployment_cov[0],pm25[0],so2_emissions[0]], weights=(r_d[1],per_unit_gdp[1],rural_urban[1],urban_per[1],rural_per[1],garbage[1],bus_per[1],urban_sewage[1],edu_years[1],mortality[1],pension_cov[1],medical_cov[1],unemployment_cov[1],pm25[1],so2_emissions[1]))
#     # （2）可持续发展=（温室气体排放*该项权重+氮排放*该项权重+取水量*该项权重+土地利用*该项权重+生态足迹*该项权重）/（温室气体排放权重+氮排放权重+取水量权重+土地利用权重+生态足迹权重）
#     # co2_per_gdp,cod_emissions,nh_emissions,water_per,water_per_gdp,planting_area,ef_per
#     city_sustainable=np.average([co2_per_gdp[0],cod_emissions[0],nh_emissions[0],water_per[0],water_per_gdp[0],planting_area[0],ef_per[0]], weights=(co2_per_gdp[1],cod_emissions[1],nh_emissions[1],water_per[1],water_per_gdp[1],planting_area[1],ef_per[1]))
#     # （3）GEP+=（绿色经济得分*该项权重+可持续发展得分*该项权重）/（绿色经济权重+可持续发展权重）
#     city_gep_plus=np.average([r_d[0],per_unit_gdp[0],rural_urban[0],urban_per[0],rural_per[0],garbage[0],bus_per[0],urban_sewage[0],edu_years[0],mortality[0],pension_cov[0],medical_cov[0],unemployment_cov[0],pm25[0],so2_emissions[0],co2_per_gdp[0],cod_emissions[0],nh_emissions[0],water_per[0],water_per_gdp[0],planting_area[0],ef_per[0]], weights=(r_d[1],per_unit_gdp[1],rural_urban[1],urban_per[1],rural_per[1],garbage[1],bus_per[1],urban_sewage[1],edu_years[1],mortality[1],pension_cov[1],medical_cov[1],unemployment_cov[1],pm25[1],so2_emissions[1],co2_per_gdp[1],cod_emissions[1],nh_emissions[1],water_per[1],water_per_gdp[1],planting_area[1],ef_per[1]))
#
#     # print(r_d,'规模以上工业企业R&D经费支出(万元)',
#     # (per_unit_gdp,'单位GDP能耗(吨/万元)'),
#     # (rural_urban,'乡-城人均年收入比(/)'),
#     # (urban_per,'城镇居民人均可支配收入(元)'),
#     # (rural_per,'农村居民人均可支配收入(元)'),
#     # (garbage,'生活垃圾无害化处理率(%)'),
#     # (bus_per,'平均万人拥有公共汽车(/)'),
#     # (urban_sewage,'城镇生活污水集中处理率(%)'),
#     # (edu_years,'平均受教育年限(年)'),
#     # (mortality,'死亡率(%)'),
#     # (pension_cov,'养老保险覆盖率(%)'),
#     # (medical_cov,'医疗保险覆盖率(%)'),
#     # (unemployment_cov,'失业保险覆盖率(%)'),
#     # (pm25,'PM2.6年平均浓度(微克/立方米)'),
#     # (so2_emissions,'二氧化硫排放量(万吨)'),
#     # (co2_per_gdp,'单位GDP二氧化碳排放量(千克/元)'),
#     # (cod_emissions,'化学需氧量排放量(万吨)'),
#     # (nh_emissions,'氨氮排放量(万吨)'),
#     # (water_per,'人均耗水量(立方米)'),
#     # (water_per_gdp,'单位GDP用水量(立方米/万元)'),
#     # (planting_area,'播种面积占比(%)'),
#     # (ef_per,'人均生态足迹(万吨碳/万人)'),
#     # (city_green_economy,'绿色经济'),
#     # (energy_use,'能源利用'),
#     # (parma_ratio,'帕尔玛比率'),
#     # (income,'收入'),
#     # (infrastructure,'基础设施建设'),
#     # (education,'教育'),
#     # (life_expectancy,'预期寿命'),
#     # (social_security,'社会保障'),
#     # (air_pollution,'大气污染'),
#     # (greenhouse,'温室气体排放'),
#     # (nitrogen,'氮排放'),
#     # (water_withdrawal,'取水量'),
#     # (land_use,'土地利用'),
#     # (EF,'生态足迹'),
#     # (green_innovation,'绿色创新'),
#     # (city_sustainable,'可持续发展'),
#     # (city_gep_plus, 'GEP+')
#     # )
#     print(r_d[0])
#     for i in areadata_this_year.filter(area=area):
#         print(i.r_d)
#     test_dict = dict(r_d_score=r_d[0],per_unit_gdp_score=per_unit_gdp[0],rural_urban_score=rural_urban[0],urban_per_score=urban_per[0],rural_per_score=rural_per[0],garbage_score=garbage[0],bus_per_score=bus_per[0],urban_sewage_score=urban_sewage[0],edu_years_score=edu_years[0],mortality_score=mortality[0],pension_cov_score=pension_cov[0],medical_cov_score=medical_cov[0],unemployment_cov_score=unemployment_cov[0],pm25_score=pm25[0],so2_emissions_score=so2_emissions[0],co2_per_gdp_score=co2_per_gdp[0],cod_emissions_score=cod_emissions[0],nh_emissions_score=nh_emissions[0],water_per_score=water_per[0],water_per_gdp_score=water_per_gdp[0],planting_area_score=planting_area[0],ef_per_score=ef_per[0],green_innovation=green_innovation,energy_use=energy_use,parma_ratio=parma_ratio,income=income,infrastructure=infrastructure,education=education,life_expectancy=life_expectancy,social_security=social_security,air_pollution=air_pollution,greenhouse=greenhouse,nitrogen=nitrogen,water_withdrawal=water_withdrawal,land_use=land_use,EF=EF,city_green_economy=city_green_economy,city_sustainable=city_sustainable,city_gep_plus=city_gep_plus)
#     print(test_dict)
#     write_area_database = models.Calculated_value.objects.filter(province=province, year=year, area=area)
#     write_area_database.update(**test_dict)
#
#
# # 查省份数据
# def calc_prov_data(province, year):
#     provdata_this_year = models.Prov_Calculated_value.objects.filter(province=province, year=year)
#     provdata_last_year = models.Prov_Calculated_value.objects.filter(province=province, year=(year-1))
#     item_extremum = []
#     for i in area_item_list_index:
#         item_index = []
#         for m in provdata_this_year.values(i[0]):
#             item_index.append(m[i[0]])
#         item_max_each = (i[0]+"_max", max(item_index))
#         item_min_each = (i[0]+"_min", min(item_index))
#         item_extremum.append(item_max_each)
#         item_extremum.append(item_min_each)
#     # 极值字典
#     item_extremum = dict(item_extremum)
#     # 输出极值
#     print(item_extremum["mortality"+"_min"])
#     # queryset转字典
#     prov_this_year_datalist = model_to_dict(provdata_this_year)
#     prov_last_year_datalist = model_to_dict(provdata_last_year)
#     print("当期值")
#     print(prov_this_year_datalist['mortality'])
#     print("前期值")
#     print(prov_last_year_datalist['mortality'])
#
#     r_d = utils.item_calc_positive(prov_last_year_datalist['r_d'], prov_this_year_datalist['r_d'], item_extremum["r_d_max"])
#     per_unit_gdp = utils.item_calc_negative(prov_last_year_datalist['per_unit_gdp'], prov_this_year_datalist['per_unit_gdp'], item_extremum["per_unit_gdp_min"])
#     renewable_energy_per = utils.item_calc_positive(prov_last_year_datalist['renewable_energy_per'], prov_this_year_datalist['renewable_energy_per'], item_extremum["renewable_energy_per_max"])
#     rural_urban = utils.item_calc_positive(prov_last_year_datalist['rural_urban'], prov_this_year_datalist['rural_urban'], item_extremum["rural_urban_max"])
#     urban_per = utils.item_calc_positive(prov_last_year_datalist['urban_per'], prov_this_year_datalist['urban_per'], item_extremum["urban_per_max"])
#     rural_per = utils.item_calc_positive(prov_last_year_datalist['rural_per'], prov_this_year_datalist['rural_per'], item_extremum["rural_per_max"])
#     garbage = utils.item_calc_positive(prov_last_year_datalist['garbage'], prov_this_year_datalist['garbage'], item_extremum["garbage_max"])
#     bus_per = utils.item_calc_positive(prov_last_year_datalist['bus_per'], prov_this_year_datalist['bus_per'], item_extremum["bus_per_max"])
#     urban_sewage = utils.item_calc_positive(prov_last_year_datalist['urban_sewage'], prov_this_year_datalist['urban_sewage'], item_extremum["urban_sewage_max"])
#     edu_years = utils.item_calc_positive(prov_last_year_datalist['edu_years'], prov_this_year_datalist['edu_years'], item_extremum["edu_years_max"])
#     mortality = utils.item_calc_negative(prov_last_year_datalist['mortality'], prov_this_year_datalist['mortality'], item_extremum["mortality_min"])
#     pension_cov = utils.item_calc_positive(prov_last_year_datalist['pension_cov'], prov_this_year_datalist['pension_cov'], item_extremum["pension_cov_max"])
#     medical_cov = utils.item_calc_positive(prov_last_year_datalist['medical_cov'], prov_this_year_datalist['medical_cov'], item_extremum["medical_cov_max"])
#     unemployment_cov = utils.item_calc_positive(prov_last_year_datalist['unemployment_cov'], prov_this_year_datalist['unemployment_cov'], item_extremum["unemployment_cov_max"])
#     pm25 = utils.item_calc_negative(prov_last_year_datalist['pm25'], prov_this_year_datalist['pm25'], item_extremum["pm25_min"])
#     so2_emissions = utils.item_calc_negative(prov_last_year_datalist['so2_emissions'], prov_this_year_datalist['so2_emissions'], item_extremum["so2_emissions_min"])
#     co2_per_gdp = utils.item_calc_negative(prov_last_year_datalist['co2_per_gdp'], prov_this_year_datalist['co2_per_gdp'], item_extremum["co2_per_gdp_min"])
#     cod_emissions = utils.item_calc_negative(prov_last_year_datalist['cod_emissions'], prov_this_year_datalist['cod_emissions'], item_extremum["cod_emissions_min"])
#     nh_emissions = utils.item_calc_negative(prov_last_year_datalist['nh_emissions'], prov_this_year_datalist['nh_emissions'], item_extremum["nh_emissions_min"])
#     water_per = utils.item_calc_negative(prov_last_year_datalist['water_per'], prov_this_year_datalist['water_per'], item_extremum["water_per_min"])
#     water_per_gdp = utils.item_calc_negative(prov_last_year_datalist['water_per_gdp'], prov_this_year_datalist['water_per_gdp'], item_extremum["water_per_gdp_min"])
#     planting_area = utils.item_calc_positive(prov_last_year_datalist['planting_area'], prov_this_year_datalist['planting_area'], item_extremum["planting_area_max"])
#     ef_per = utils.item_calc_negative(prov_last_year_datalist['ef_per'], prov_this_year_datalist['ef_per'], item_extremum["ef_per_min"])
#
#     green_innovation=r_d[0]
#     renewable_energy=renewable_energy_per[0]
#     # renewable_energy=renewable_energy_per
#     energy_use=per_unit_gdp[0]
#     parma_ratio=rural_urban[0]
#     income=np.average([urban_per[0],rural_per[0]], weights=(urban_per[1],rural_per[1]))
#     # garbage,bus_per,urban_sewage
#     infrastructure=np.average([garbage[0],bus_per[0],urban_sewage[0]], weights=(garbage[1],bus_per[1],urban_sewage[1]))
#     education=edu_years[0]
#     life_expectancy=mortality[0]
#     # pension_cov,medical_cov,unemployment_cov
#     social_security=np.average([pension_cov[0],medical_cov[0],unemployment_cov[0]], weights=(pension_cov[1],medical_cov[1],unemployment_cov[1]))
#     # pm25,so2_emissions
#     air_pollution=np.average([pm25[0],so2_emissions[0]], weights=(pm25[1],so2_emissions[1]))
#     greenhouse=co2_per_gdp[0]
#     # cod_emissions,nh_emissions
#     nitrogen=np.average([cod_emissions[0],nh_emissions[0]], weights=(cod_emissions[1],nh_emissions[1]))
#     # water_per,water_per_gdp
#     water_withdrawal=np.average([water_per[0],water_per_gdp[0]], weights=(water_per[1],water_per_gdp[1]))
#     land_use=planting_area[0]
#     EF=ef_per[0]
#
#     # （1）绿色经济=（绿色创新*该项权重+能源利用*该项权重+帕尔玛比率*该项权重+收入*该项权重+基础设施建设*该项权重+教育*该项权重+预期寿命*该项权重+社会保障*该项权重+大气污染*该项权重）/（绿色创新权重+能源利用权重+帕尔玛比率权重+收入权重+基础设施建设权重+教育权重+预期寿命权重+社会保障权重+大气污染权重）
#     # r_d,per_unit_gdp,rural_urban,urban_per,rural_per,garbage,bus_per,urban_sewage,edu_years,mortality,pension_cov,medical_cov,unemployment_cov,pm25,so2_emissions
#     city_green_economy=np.average([r_d[0],per_unit_gdp[0],rural_urban[0],urban_per[0],rural_per[0],garbage[0],bus_per[0],urban_sewage[0],edu_years[0],mortality[0],pension_cov[0],medical_cov[0],unemployment_cov[0],pm25[0],so2_emissions[0]], weights=(r_d[1],per_unit_gdp[1],rural_urban[1],urban_per[1],rural_per[1],garbage[1],bus_per[1],urban_sewage[1],edu_years[1],mortality[1],pension_cov[1],medical_cov[1],unemployment_cov[1],pm25[1],so2_emissions[1]))
#     # （2）可持续发展=（温室气体排放*该项权重+氮排放*该项权重+取水量*该项权重+土地利用*该项权重+生态足迹*该项权重）/（温室气体排放权重+氮排放权重+取水量权重+土地利用权重+生态足迹权重）
#     # co2_per_gdp,cod_emissions,nh_emissions,water_per,water_per_gdp,planting_area,ef_per
#     city_sustainable=np.average([co2_per_gdp[0],cod_emissions[0],nh_emissions[0],water_per[0],water_per_gdp[0],planting_area[0],ef_per[0]], weights=(co2_per_gdp[1],cod_emissions[1],nh_emissions[1],water_per[1],water_per_gdp[1],planting_area[1],ef_per[1]))
#     # （3）GEP+=（绿色经济得分*该项权重+可持续发展得分*该项权重）/（绿色经济权重+可持续发展权重）
#     city_gep_plus=np.average([r_d[0],per_unit_gdp[0],rural_urban[0],urban_per[0],rural_per[0],garbage[0],bus_per[0],urban_sewage[0],edu_years[0],mortality[0],pension_cov[0],medical_cov[0],unemployment_cov[0],pm25[0],so2_emissions[0],co2_per_gdp[0],cod_emissions[0],nh_emissions[0],water_per[0],water_per_gdp[0],planting_area[0],ef_per[0]], weights=(r_d[1],per_unit_gdp[1],rural_urban[1],urban_per[1],rural_per[1],garbage[1],bus_per[1],urban_sewage[1],edu_years[1],mortality[1],pension_cov[1],medical_cov[1],unemployment_cov[1],pm25[1],so2_emissions[1],co2_per_gdp[1],cod_emissions[1],nh_emissions[1],water_per[1],water_per_gdp[1],planting_area[1],ef_per[1]))
#
#     test_dict = dict(r_d_score=r_d[0],per_unit_gdp_score=per_unit_gdp[0],renewable_energy_per_score=renewable_energy_per[0],rural_urban_score=rural_urban[0],urban_per_score=urban_per[0],rural_per_score=rural_per[0],garbage_score=garbage[0],bus_per_score=bus_per[0],urban_sewage_score=urban_sewage[0],edu_years_score=edu_years[0],mortality_score=mortality[0],pension_cov_score=pension_cov[0],medical_cov_score=medical_cov[0],unemployment_cov_score=unemployment_cov[0],pm25_score=pm25[0],so2_emissions_score=so2_emissions[0],co2_per_gdp_score=co2_per_gdp[0],cod_emissions_score=cod_emissions[0],nh_emissions_score=nh_emissions[0],water_per_score=water_per[0],water_per_gdp_score=water_per_gdp[0],planting_area_score=planting_area[0],ef_per_score=ef_per[0],green_innovation=green_innovation,renewable_energy=renewable_energy,energy_use=energy_use,parma_ratio=parma_ratio,income=income,infrastructure=infrastructure,education=education,life_expectancy=life_expectancy,social_security=social_security,air_pollution=air_pollution,greenhouse=greenhouse,nitrogen=nitrogen,water_withdrawal=water_withdrawal,land_use=land_use,EF=EF,city_green_economy=city_green_economy,city_sustainable=city_sustainable,city_gep_plus=city_gep_plus)
#     write_area_database = models.Prov_Calculated_value.objects.filter(province=province, year=year)
#     write_area_database.update(**test_dict)
#
#
#
#
# calc_area_data('江苏省', '南京市', 2017)