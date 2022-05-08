from django.urls import path
from profile_api import views


urlpatterns = [
    path('hello-view', view.HelloApiView.as_view()),
]
