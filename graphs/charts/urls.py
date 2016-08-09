from charts import views
from django.conf.urls import url

urlpatterns = [
    url(r'^view/', views.chart),
    url(r'^detail/', views.detail),
    url(r'^country_data/([1-5])$',views.get_country_data),
    url(r'^continent_data/([1-5])$',views.get_continent_data),
    url(r'^insert/',views.insert_data),
]
