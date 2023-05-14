from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .forms import ContactForm1
from .wizards import Destination_WizardView

urlpatterns=[
    path('simple_view/', views.simple_view),
    path('destination/', views.list_destination  ),
    path('destination_add/', login_required(views.destination_view)),
    path('table/', login_required(views.table), name="home"),
    path('table/delete/<int:id>', views.delete, name='delete'),
    path('table/update/<int:id>', views.update, name='update'),
    path('table/update/updaterecord/<int:id>',         views.updaterecord, name='updaterecord'),

    
]