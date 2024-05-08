from django.urls import path
from django.views.generic import TemplateView
from api import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("autovc/", views.AutoVCView.as_view(), name='autovc'),
    path("starGan/", views.StarGanView.as_view(), name='starGan'),
    path("knn/", views.kNNView.as_view(), name='knn'),
    path("results/", views.ResultsView.as_view(), name='results'),


]