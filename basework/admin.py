from django.contrib import admin

from .models import ConstantEg, Annual_data, Prov_Annual_data, Calculated_value, Prov_Calculated_value


# Register your models here.

# 常量编辑

class ConstantEgAdmin(admin.ModelAdmin):
    list_display = ('Raw_coal','Clean_coal','Coke','Briquette','Other_coking_products','Crude','Fuel_oil','Gasoline','Diesel','Kerosene','Liquefied_petroleum_gas','Refinery_dry_gas','Naphtha','Asphalt','Lubricating_oil','Petroleum_coke','Natural_gas','Cement','Steel','Farmland','Woodland','Pastureland','Fishing_ground','Construction_land',)

    fieldsets = (
        ('常量编辑', {
            'fields': (
                (
                    'Raw_coal', 'Raw_coal_MJ', 'Clean_coal', 'Clean_coal_MJ', 'Coke', 'Coke_MJ', 'Briquette', 'Briquette_MJ', 'Other_coking_products',
                    'Other_coking_products_MJ', 'Crude', 'Crude_MJ', 'Fuel_oil', 'Fuel_oil_MJ', 'Gasoline',
                    'Gasoline_MJ', 'Diesel', 'Diesel_MJ', 'Kerosene', 'Kerosene_MJ', 'Liquefied_petroleum_gas',
                    'Liquefied_petroleum_gas_MJ', 'Refinery_dry_gas', 'Refinery_dry_gas_MJ', 'Naphtha', 'Naphtha_MJ',
                    'Asphalt', 'Asphalt_MJ', 'Lubricating_oil', 'Lubricating_oil_MJ', 'Petroleum_coke',
                    'Petroleum_coke_MJ', 'Natural_gas', 'Natural_gas_MJ'
                ),
                ('Cement', 'Steel'),
                ('Farmland', 'Woodland', 'Pastureland', 'Fishing_ground', 'Construction_land'),
            )
        }),
    )

class Annual_dataAdmin(admin.ModelAdmin):
    list_display = ('province', 'area', 'year')
    fieldsets = (('地区年度数据', {
            'fields': (
                (
                    'province', 'area', 'year',
                ),
                (
                    'Consume_Raw_coal', 'Consume_Clean_coal','Consume_Coke','Consume_Briquette','Consume_Other_coking_products','Consume_Crude','Consume_Fuel_oil','Consume_Gasoline','Consume_Diesel','Consume_Kerosene','Consume_Liquefied_petroleum_gas','Consume_Refinery_dry_gas','Consume_Naphtha','Consume_Asphalt','Consume_Lubricating_oil','Consume_Petroleum_coke','Consume_Natural_gas',
                ),
                (
                    'Consume_Cement', 'Consume_Steel',
                ),
                (
                    'Consume_Farmland','Consume_Woodland','Consume_Pastureland','Consume_Fishing_ground','Consume_Construction_land',
                ),
            )
        }),
    )


class Prov_Annual_dataAdmin(admin.ModelAdmin):
    list_display = ('province', 'year')
    fieldsets = (('省级年度数据', {
            'fields': (
                (
                    'province', 'year',
                ),
                (
                    'Consume_Raw_coal', 'Consume_Clean_coal','Consume_Coke','Consume_Briquette','Consume_Other_coking_products','Consume_Crude','Consume_Fuel_oil','Consume_Gasoline','Consume_Diesel','Consume_Kerosene','Consume_Liquefied_petroleum_gas','Consume_Refinery_dry_gas','Consume_Naphtha','Consume_Asphalt','Consume_Lubricating_oil','Consume_Petroleum_coke','Consume_Natural_gas',
                ),
                (
                    'Consume_Cement', 'Consume_Steel',
                ),
                (
                    'Consume_Farmland','Consume_Woodland','Consume_Pastureland','Consume_Fishing_ground','Consume_Construction_land',
                ),
            )
        }),
    )

class Calculated_valueAdmin(admin.ModelAdmin):
    list_display = ('province', 'area', 'year')
    fieldsets = (('地区年度数据计算', {
            'fields': (
                (
                    'province', 'area', 'year',
                ),
                (
                    'Cal_Raw_coal', 'Cal_Clean_coal','Cal_Coke','Cal_Briquette','Cal_Other_coking_products','Cal_Crude','Cal_Fuel_oil','Cal_Gasoline','Cal_Diesel','Cal_Kerosene','Cal_Liquefied_petroleum_gas','Cal_Refinery_dry_gas','Cal_Naphtha','Cal_Asphalt','Cal_Lubricating_oil','Cal_Petroleum_coke','Cal_Natural_gas',
                ),
                (
                    'GHG_Emission_a', 'CO2_Emission_a', 
                ),
                (
                    'Cal_Cement', 'Cal_Steel',
                ),
                (
                    'GHG_Emission_b', 'CO2_Emission_b', 
                ),
                (
                    'Total_CO2_Emission',
                ),
                (
                    'Cal_EF',
                ),
            )
        }),
    )

class Prov_Calculated_valueAdmin(admin.ModelAdmin):
    list_display = ('province', 'year')
    fieldsets = (('省级年度数据计算', {
            'fields': (
                (
                    'province', 'year',
                ),
                (
                    'Cal_Raw_coal', 'Cal_Clean_coal','Cal_Coke','Cal_Briquette','Cal_Other_coking_products','Cal_Crude','Cal_Fuel_oil','Cal_Gasoline','Cal_Diesel','Cal_Kerosene','Cal_Liquefied_petroleum_gas','Cal_Refinery_dry_gas','Cal_Naphtha','Cal_Asphalt','Cal_Lubricating_oil','Cal_Petroleum_coke','Cal_Natural_gas',
                ),
                (
                    'GHG_Emission_a', 'CO2_Emission_a', 
                ),
                (
                    'Cal_Cement', 'Cal_Steel',
                ),
                (
                    'GHG_Emission_b', 'CO2_Emission_b', 
                ),
                (
                    'Total_CO2_Emission',
                ),
                (
                    'Cal_EF',
                ),
            )
        }),
    )



admin.site.register(ConstantEg, ConstantEgAdmin)
admin.site.register(Annual_data, Annual_dataAdmin)
admin.site.register(Prov_Annual_data, Prov_Annual_dataAdmin)
admin.site.register(Calculated_value, Calculated_valueAdmin)