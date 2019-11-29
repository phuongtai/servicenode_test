from django.contrib.contenttypes.models import ContentType
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import CustomerSerializer, ManufacturerSerializer, ContentTypeSerializer
from .models import Customer, Manufacturer


class CustomerViewset(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ManufacturerViewset(ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class GetPartnerContenttype(ListAPIView):
    serializer_class = ContentTypeSerializer
    queryset = ContentType.objects.all()

    def list(self, request, *args, **kwargs):
        contenttypes = ContentType.objects.filter(app_label='partners')
        sers = self.get_serializer(contenttypes, many=True)
        return Response(data=sers.data)
