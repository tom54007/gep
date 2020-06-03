from . import models
from openpyxl import load_workbook
import os
from django.core.exceptions import ValidationError


# 二氧化碳排放总量计算
## 能源碳排放 =B5*C5*D5/10^8
def Eg_carbon_emission(co_l: list, mj_l: list, y_l: list):
    if len(mj_l) != len(co_l):
        raise ValueError
    elif len(y_l) != len(co_l):
        raise ValueError
    else:
        k = [co_l[i]*mj_l[i]*y_l[i] for i in range(0, len(co_l))]
        return k

## 工业生产过程碳排放
## 材料生产中的碳排放
def indus_carbon_emission(co_l: list, y_l: list):
    if len(co_l) == len(y_l):
        k = [co_l[i]*y_l[i] for i in range(0, len(co_l))]
        return k
    else:
        raise ValueError


## 温室气体排放量 GHG Emission =SUM(E5:E21)*10
def eg_sum(cal_l: list):
    ghgsum = sum(cal_l)*10
    return ghgsum

## 二氧化碳排放量 CO2 Emission
def co2_emission(eg_sum):
    s = eg_sum*44/12
    return s


## 二氧化碳排放总量 Total CO2 Emission



# 生态足迹计算 =(C4*B4+C5*B5+C7*B7+C8*B8)/1000
## 生态足迹
def ef_sum(co_l: list, y_l: list):
    if len(co_l) == len(y_l):
        k = [co_l[i]*y_l[i] for i in range(0, len(co_l))]
        return sum(k)/1000
    else:
        raise ValueError





# 计算指标计
## 单位GDP能耗	地区当年能源消费总量/地区当年生产总值




## 单位GDP二氧化碳排放量	地区当年二氧化碳排放量/地区当年生产总值



## 单位GDP用水量	地区当年用水总量/地区当年生产总值



## 播种面积占比	地区当年总面积/地区当年播种面积



## 平均受教育年限	（小学人数×6+初中人数×9年+高中人数×12+大学及以上人数×16）/43



## 人均生态足迹	地区当年生态足迹/地区当年总人口



## 人均用水量	地区当年用水总量/地区当年总人口



## 养老保险覆盖率	地区当年基本养老保险职工人数/地区当年总人口



## 医疗保险覆盖率	地区当年基本医疗保险人数/地区当年总人口



## 失业保险覆盖率	地区当年失业保险人数/地区当年总人口



## 可再生能源供给占比	地区当年核电+风电+水电+光伏发电量/地区当年总发电量



