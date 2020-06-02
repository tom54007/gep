from django.contrib import admin

from .models import ConstantEg


# Register your models here.

# 常量编辑

class ConstantEgAdmin(admin.ModelAdmin):
    list_display = ('Raw_coal','Clean_coal','Coke','Briquette','Other_coking_products','Crude','Fuel_oil','Gasoline','Diesel','Kerosene','Liquefied_petroleum_gas','Refinery_dry_gas','Naphtha','Asphalt','Lubricating_oil','Petroleum_coke','Natural_gas','Cement','Steel','Farmland','Woodland','Pastureland','Fishing_ground','Construction_land',)

    fieldsets = (
        (None, {
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




admin.site.register(ConstantEg, ConstantEgAdmin)