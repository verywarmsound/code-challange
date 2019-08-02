from django.urls import path
from .api import (
    SimulationView
)

urlpatterns = [
    path('api/simulation',
         SimulationView.as_view(), name='location'),

]

