from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path("<slug:slug>", views.post_datal, name="detail"),
    path('', views.PostArticleList.as_view(), name="article-list"),
    path("category/<int:pk>", views.category_detail, name="category_detail"),
    path("search/", views.search, name="search"),
    path("contact/", views.MessageView.as_view(), name="contact_article"),
    path("message/edit/<int:pk>", views.MessageList.as_view(), name="message_list"),
    path("message/delete/<int:pk>", views.DeleteMessageView.as_view(), name="message_delete"),
    path("message/<int:pk>", views.MessageUpdateView.as_view(), name="message_update"),
    path("archive/", views.ArchiveArticleView.as_view(), name="time_update"),
    path("archive/<int:year>", views.YearArticleView.as_view(), name="pub_deta"),
    path("like/<slug:slug>/<int:pk>", views.Likes_Detail, name="like"),
]