from rest_framework import serializers
from .models import Contract
from .fields import (
    PartnerObjectRelatedField,
    ContentTypeField,
    SmartPartnerObjectRelatedField
    )


class ContractSerializer(serializers.ModelSerializer):
    content_type = ContentTypeField(max_length=256)
    entity = PartnerObjectRelatedField(read_only=True, source='content_object')

    class Meta:
        model = Contract
        fields = ('contract_title', 'contract_date', 'content_type', 'object_id', 'entity')


class SmartContractSerializer(serializers.ModelSerializer):
    entity = SmartPartnerObjectRelatedField(read_only=True, source='content_object')

    class Meta:
        model = Contract
        fields = ('contract_title', 'entity')
