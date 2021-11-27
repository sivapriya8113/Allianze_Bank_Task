from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import bankserializer,bankbranchserializer,branchserializer
from .models import banks,branches,bank_branches




@api_view(['Get'])
def bankdetails(request,pk):
    bankdetails = branches.objects.get(ifsc=pk)
    serializer = branchserializer(bankdetails, many=False)
    return Response(serializer.data)




class BranchListView(generics.ListAPIView):

    serializer_class = branchserializer

    def get_queryset(self):

        bank_name= self.request.query_params.get('bank_name')


        city = self.request.query_params.get('city')

        if city:
            res = bank_branches.objects.filter(city=city)
        if bank_name:
            res = res.filter(bank_name=bank_name)

        return res

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
