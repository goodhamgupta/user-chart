from charts import views
from django.conf.urls import url

urlpatterns = [
    url(r'^view/', views.chart),
    url(r'^data/([1-5])$',views.get_data),
    url(r'^insert/',views.insert_data),
]
