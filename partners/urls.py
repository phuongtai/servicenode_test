
from django.urls import path
from partners import views

urlpatterns = [
    path('customer', views.CustomerViewset.as_view({'get': 'list', 'post': 'create'}), name='customer'),
    path('manufacturer', views.ManufacturerViewset.as_view(({'get': 'list', 'post': 'create'})), name='manufacturer'),
    path('get_partner_type', views.GetPartnerContenttype.as_view(), name='get_contenttype')
]
