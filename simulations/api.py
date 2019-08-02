from django.http import  HttpResponseBadRequest,  HttpResponseNotFound
from rest_framework import generics
from .simulator import Simulator
from rest_framework.response import Response


class SimulationView(generics.ListAPIView):
    def get(self, request):
        # get location from URL with coordinates
        location = request.GET.get('location')
        # coordinates must include at least 4 pairs to eliminate Simulator calculating errors
        if location and len(location) >= 8:
            coord_list = location.split(',')
            # converting to numbers
            coordinates = [float(i) for i in coord_list]
            # lat and lng positions are different from FE
            bounding_box = (coordinates[1], coordinates[0], coordinates[3], coordinates[2])
            number_of_requests = 4
            result = Simulator(bounding_box).simulate(number_of_requests)
        else:
            return HttpResponseBadRequest('Please submit two points with coordinates')
        if result:
            return Response(result)
        else:
            return HttpResponseNotFound('Simulator cannot calculate the result with this parameters')
