from django.urls import path
from . import views


app_name = 'heme'
urlpatterns = [
    path("", views.index, name='heme'),
    path("article", views.sidebar, name="sidebar_article"),
    path("homepage/", views.HomePageView.as_view(), name="HomePage"),
    path("red", views.HomePageRedirectView.as_view(), name="Redirect"),
]
# article base view