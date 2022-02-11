from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import DropBoxViewset, UserList
from . import views

router = routers.SimpleRouter()
router.register('accounts',DropBoxViewset )


urlpatterns = [
    path('', include(router.urls)),
    path('userlist/',UserList.as_view(), name="instances")

]
