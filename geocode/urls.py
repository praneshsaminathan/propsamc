from django.urls import path, include
from propsamc.utils.apps import get_api_url

from .views import GeoCodeAPIView

urlpatterns = [

    path(get_api_url(url_name='get-geo-code'), GeoCodeAPIView.as_view(), name='api-get-geo-code'),

]
