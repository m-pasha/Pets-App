from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from rest_framework import exceptions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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
        html = "<h2 align=center>API</h2><hr><br><a href='/'>Home</a><br><br>" \
               "<a href='list/'>List of pets</a><br>" \
               "<a href='create/'>Create a new pet</a><br>" \
               "<a href='edit/1/'>Update or Delete a pet !! be called with a URL keyword argument 'PK'.</a><br>"
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


class PetCreateView(CreateAPIView):
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Pet.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            if request.data:
                user = User.objects.get(username=self.request.user)
                pet = Pet.objects.create(owner=user,
                                         name=request.data['name'],
                                         type_pet=request.data['type_pet'],
                                         birthday=request.data['birthday'])
                serializer = self.get_serializer(pet)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except exceptions.ValidationError:
            raise exceptions.ValidationError('Error data request')


class PetRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return Pet.objects.filter(owner=self.request.user)
        except ObjectDoesNotExist:
            raise exceptions.NotFound('Object Not found.')
