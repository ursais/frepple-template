# Copyright (C) 2021 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
"""
This files defines a URL for your views.
"""

from django.conf.urls import url

from .serializers import MyModelSerializerAPI
from .views import MyModelList

# Automatically add these URLs when the application is installed
autodiscover = True

urlpatterns = [
    # Model list reports, which override standard admin screens
    url(
        r"^data/my_app/my_model/$",
        MyModelList.as_view(),
        name="my_app_my_model_changelist",
    ),
    # URLs for the REST API
    url(r"^api/my_app/my_model/$", MyModelSerializerAPI.as_view()),
]
