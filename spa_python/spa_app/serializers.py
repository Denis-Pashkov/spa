from attr import fields
from matplotlib.pyplot import cla
from rest_framework import serializers
from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id', 'date', 'name', 'amount', 'distance')