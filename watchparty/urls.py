"""watchparty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from watchpartyapi.views import check_user, register_user, get_username
from watchpartyapi.views import PartyView
from watchpartyapi.views import PartyAttendeeView
from watchpartyapi.views import ShowGenreView
from watchpartyapi.views import ShowView
from watchpartyapi.views import UserView
from watchpartyapi.views import PartyCommentsView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'parties', PartyView, 'party')
router.register(r'partyattendees', PartyAttendeeView, 'partyattendee')
router.register(r'showgenres', ShowGenreView, 'showgenre')
router.register(r'shows', ShowView, 'show')
router.register(r'users', UserView, 'user')
router.register(r'partycomments', PartyCommentsView, 'partycomment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('checkuser', check_user),
    path('registeruser', register_user),
    path('getusername', get_username),
]
