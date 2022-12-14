from django.urls import path
from boxerapiApp import views

urlpatterns = [
    path("survivors/",views.ListsurvivorsAPIView.as_view(),name="survivors_list"),
    path("survivors/create/", views.CreateSurvivorsAPIView.as_view(),name="survivors_create"),
    path("location/create/", views.CreateAddressAPIView.as_view(),name="location_create"),
    path("survivors/<int:pk>/",views.UpdateSurvivorAddressAPIViews.as_view(),name="update_survivors"),
]