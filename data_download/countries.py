from pygal_maps_world.i18n import COUNTRIES


for country_code in sorted(i18n.COUNTRIES.keys()):
    print(country_code, i18n.COUNTRIES[country_code])

