from django.conf.urls import url

from app import views


urlpatterns = [
    url(r'^$', views.ApiHome.as_view()),
    url(r'^list/$', views.PetList.as_view()),
    url(r'^create/$', views.PetCreateView.as_view()),
    url(r'^edit/(?P<pk>.+)/$', views.PetRetrieveUpdateDestroyView.as_view()),
]
