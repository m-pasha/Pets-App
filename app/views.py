from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views import View
from rest_framework import exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from app.models import Pet
from app.serializers import PetSerializer


class Home(View):

    def get(self, request):
        html = "<h2 align=center>App Pets</h2><hr><br>" \
               "<a href='/api'>API</a><br>" \
               "<a href='/admin'>Django Admin</a>"
        return HttpResponse(html)


class ApiHome(View):

    def get(self, request):
        html = "<h2 align=center>Home API</h2><hr><br><a href='/'>Home</a><br><br>" \
               "<a href='list/'>List</a><br>"
        return HttpResponse(html)


class PetList(ListAPIView):
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'

    def get_queryset(self):
        try:
            return Pet.objects.filter(owner=self.request.user)
        except ObjectDoesNotExist:
            raise exceptions.NotFound('Object NotFound')
