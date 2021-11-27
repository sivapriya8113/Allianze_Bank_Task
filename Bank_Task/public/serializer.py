from rest_framework import serializers
from .models import banks,branches,bank_branches


class bankserializer(serializers.ModelSerializer):
    class Meta:
        model = banks
        fields = '__all__'

class branchserializer(serializers.ModelSerializer):
     branches=bankserializer(many=True, read_only=True)

     class Meta:
         model = branches
         fields = ('ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state','branches')


class bankbranchserializer(serializers.ModelSerializer):
    bankbranches = bankserializer(many=True)

    class Meta:
        model = bank_branches
        fields = ('ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state','bank_name','bankbranches')



