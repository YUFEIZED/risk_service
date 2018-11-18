from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name='home'),
path('addcustomer', views.add_customer, name='addcustomer'),
path('checkcredit', views.check_credit, name='checkcredit'),
path('updatecredit', views.update_credit, name='updatecredit'),
]