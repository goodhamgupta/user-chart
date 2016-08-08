from charts import views
from django.conf.urls import url

urlpatterns = [
    url(r'^view/', views.chart),
    url(r'^data/([1-6])$',views.get_data)
]
