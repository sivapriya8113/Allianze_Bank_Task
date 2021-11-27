from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import bankserializer,bankbranchserializer,branchserializer
from .models import banks,branches,bank_branches
#from rest_framework.permissions import IsAuthenticated
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication




@api_view(['Get'])
def bankdetails(request,pk):
    bankdetails = branches.objects.get(ifsc=pk)
    serializer = branchserializer(bankdetails, many=False)
    return Response(serializer.data)


'''@api_view(['Get'])
def alldetailsofbranches(request):
    branch = request.get('branch')
    city = request.get('city')
    bankbranch = bank_branches.objects.filter(branch= branch,city=city )

    serializer = bankbranchserializer(bankbranch, many=True)
    #authentication_classes = [JSONWebTokenAuthentication, ]
    #permission_classes = [IsAuthenticated, ]
    return Response(serializer.data)'''


'''class BranchListView(generics.ListAPIView):
    serializer_class = branchserializer

    def get_queryset(self):
        print('################',self)
        branch = self.request.query_params.get('branch')
        #city = self.request.query_params.get('city')

        queryset = bank_branches.objects.filter(branch=branch)
        return queryset'''


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
