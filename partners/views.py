from django.contrib.contenttypes.models import ContentType
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import CustomerSerializer, ManufacturerSerializer
from .models import Customer, Manufacturer


class CustomerViewset(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ManufacturerViewset(ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class GetPartnerContenttype(ListAPIView):
    queryset = ContentType.objects.all()

    def list(self, request, *args, **kwargs):
        rs = []
        contenttypes = ContentType.objects.filter(app_label='partners')
        for item in contenttypes:
            rs.append(item.model)
        return Response(data=rs)
