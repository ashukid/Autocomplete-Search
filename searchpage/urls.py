from django.conf.urls import url
from . import views

app_name = 'searchpage'


urlpatterns = [
    url(r'^index/$',views.IndexView.as_view(),name='index'),
    url(r'^query/$',views.search_query,name='search_query'),
] 