from charts import views
from django.conf.urls import url

urlpatterns = [
    url(r'^view/', views.chart),
    url(r'^detail/', views.detail),
    url(r'^country_data/([1-5])$',views.get_country_data),
    url(r'^continent_data/([1-5])$',views.get_continent_data),
    url(r'^country_detail/([1-5])/([1-5])$',views.get_country_detail),
    url(r'^continent_detail/([1-5])/([1-5])$',views.get_continent_detail),
    url(r'^insert/',views.insert_data),
]
