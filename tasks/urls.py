from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add')
]

# starter_application.settings.urls -> <app>.urls.py -> <app>.views.py -> <app>.templates.html
