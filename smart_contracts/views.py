from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .serializers import ContractSerializer, SmartContractSerializer
from .models import Contract


class ContractAPIView(GenericViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(True)
        serializer.save()
        return Response(data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SmartContractListAPIView(ListAPIView):
    serializer_class = SmartContractSerializer
    queryset = Contract.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
