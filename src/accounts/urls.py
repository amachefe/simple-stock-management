from django.conf.urls import url, include
from rest_framework import routers, permissions
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken import views as authviews

app_name = 'accounts'

"""
set up the url patterns for the functional views and simple class based views
Note: Mapping for actions (used in as_view), are:
    {
    'get': 'retrieve'  # to retrieve one object, as spec by pk passed in url param, e.g. /stock/1
    'get': 'list' # to list all objects, e.g. /stock/
    'get': 'latest' # CUSTOM action (defined in views.StockDataViewSet.latest(), routed /api/v1/stock/latest/ (below)).
    'post': 'create'
    'put': 'update',
    'patch': 'partial_update',
    'patch': 'perform_single_update', # CUSTOM ACTION, routed in /api/v1/stock/<PK> (with path)
    'patch': 'perform_bulk_partial_update',  # CUSTOM ACTION, routed in /api/v1/stock/ (without the ID in the path)
    'delete': 'destroy',
    }
"""
functional_view_urlpatterns = [
    url('^stock/$', views.AccountStockDataViewSet.as_view(
        {'get': 'list', 'patch': 'perform_bulk_partial_update'})),
    url('^stock/(?P<pk>\d+)/$', views.AccountStockDataViewSet.as_view(
         {'get': 'retrieve', 'patch': 'perform_single_update', 'delete': 'destroy', 'put': 'update'})),
    url('^take-stock/$', views.AccountStockDataViewSet.as_view(
         {'get': 'take_stock'})), 
]

"""
add in extra urls to provide option to add content type suffix to requests 
(as handled by the api_view wrapper, in views.py)
"""
urlpatterns = format_suffix_patterns(functional_view_urlpatterns)