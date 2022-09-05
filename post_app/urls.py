from django.urls import path
from admin_notification.views import check_notification_view

urlpatterns = [
    path('notification/', check_notification_view, name="check_notifications"),
]