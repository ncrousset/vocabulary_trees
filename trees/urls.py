from django.urls import path

from . import views

urlpatterns = [
    path("trees/", views.TreeList.as_view()),
    path("trees/<int:pk>", views.TreeDetail.as_view),
]
