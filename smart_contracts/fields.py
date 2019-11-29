from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from partners.models import Manufacturer, Customer
from partners import serializers as sers


class PartnerObjectRelatedField(serializers.DictField):

    def to_representation(self, value):
        if isinstance(value, Manufacturer):
            serializer = sers.ManufacturerSerializer(value)
        elif isinstance(value, Customer):
            serializer = sers.CustomerSerializer(value)
        # TODO: add condition if has more partner
        else:
            raise Exception('Unexpected type of partner object')

        return serializer.data


class SmartPartnerObjectRelatedField(PartnerObjectRelatedField):
    def to_representation(self, value):
        if isinstance(value, Manufacturer):
            serializer = sers.ReprManufacturerSerializer(value)
        elif isinstance(value, Customer):
            serializer = sers.ReprCustomerSerializer(value)
        # TODO: add condition if has more partner
        else:
            raise Exception('Unexpected type of partner object')
        return serializer.data


class ContentTypeField(serializers.Field):
    def to_internal_value(self, data):
        content_type = ContentType.objects.get(model=data)
        if not content_type:
            raise Exception('Your type: {} is not representation in database')
        return content_type

