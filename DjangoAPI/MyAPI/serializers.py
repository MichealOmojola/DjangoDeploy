from dataclasses import field
from rest_framework import serializers
from .models import approvals

class approvalSerializers(serializers.ModelSerializer):
    class Meta:
        model=approvals
        field = '__all__'