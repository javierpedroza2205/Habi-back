from django.urls import re_path
from myapp.api import getBuildings, getOwners, getFlats, registerFlat, registerBuilding, deleteBuilding


urlpatterns = [
    re_path(r'^get_buildings/(?P<order>.*)(?P<descending>.*)', getBuildings.getBuildings),
    re_path(r'^get_owners/', getOwners.getOwners),
    re_path(r'^get_flats/', getFlats.getFlats),
    re_path(r'^add_flat/', registerFlat.addFlat),
    re_path(r'^add_building/', registerBuilding.addBuilding),
    re_path(r'^delete_building/', deleteBuilding.deleteBuilding),
]

