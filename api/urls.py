from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name='home'),
    path("autovc/", TemplateView.as_view(template_name="autovc.html"), name='autovc'),
    path("starGan/", TemplateView.as_view(template_name="starGan.html"), name='starGan'),
    path("knn/", TemplateView.as_view(template_name="knn.html"), name='knn'),
    path("results/", TemplateView.as_view(template_name="results.html"), name='results'),


]