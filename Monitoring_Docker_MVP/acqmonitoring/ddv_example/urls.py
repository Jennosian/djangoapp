from django.urls import path
from django.conf.urls import url


from .views import TestModelList, TestModelListJson, firma_vaade

urlpatterns = [

    path('', TestModelList.as_view(), name="testmodel"),
    path('testmodel_data', TestModelListJson.as_view(), name="testmodel_list_json"),
    path('firma/<str:random_id_code>/', firma_vaade, name="firma_vaade"),

]