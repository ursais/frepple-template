# Copyright (C) 2021 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
"""
This file defines the REST API of our new model
"""

from django_filters import rest_framework as filters
from freppledb.common.api.serializers import ModelSerializer
from freppledb.common.api.views import (  # frePPleRetrieveUpdateDestroyAPIView,
    frePPleListCreateAPIView,
)
from rest_framework_bulk.drf3.serializers import BulkListSerializer, BulkSerializerMixin

from .models import My_Model


class MyModelFilter(filters.FilterSet):
    class Meta:
        model = My_Model
        fields = {
            "name": ["exact", "in", "contains"],
            "charfield": ["exact", "contains"],
            "booleanfield": ["exact"],
            "decimalfield": ["exact", "in", "gt", "gte", "lt", "lte"],
            "source": ["exact", "in"],
            "lastmodified": ["exact", "in", "gt", "gte", "lt", "lte"],
        }
        filter_fields = ("name", "charfield", "booleanfield", "decimalfield")


class MyModelSerializer(BulkSerializerMixin, ModelSerializer):
    class Meta:
        model = My_Model
        fields = ("name", "charfield", "booleanfield", "decimalfield")
        list_serializer_class = BulkListSerializer
        update_lookup_field = "name"
        partial = True


class MyModelSerializerAPI(frePPleListCreateAPIView):
    queryset = My_Model.objects.all()
    serializer_class = MyModelSerializer
    filter_class = MyModelFilter
