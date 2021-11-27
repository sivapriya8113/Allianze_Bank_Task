from django.conf.urls import url
from django.urls import path

from . import views
#from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import BranchListView

urlpatterns=[

    path('bank_details/<str:pk>/', views.bankdetails, name='bank_details'),
    path('All_details', BranchListView.as_view()),
    #url(r'get_jwt_token/', obtain_jwt_token),  # GET JET TOKEN
    #url(r'refresh_jwt_token/', refresh_jwt_token),  # REFRESH JET TOKEN
    #url(r'verify_jwt_token/', verify_jwt_token),  # VERIFY JET TOKEN

]