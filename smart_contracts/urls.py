from django.urls import path
from .views import ContractAPIView, SmartContractListAPIView

urlpatterns = [
    path('contract', ContractAPIView.as_view({'get': 'list', 'post': 'post'}), name='contract'),
    path('smartcontractlist', SmartContractListAPIView.as_view(), name='smart_contractlist')
]
