from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField






class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fider_name = models.CharField(max_length=30)
    malecode = models.CharField(max_length=10)
    image = models.ImageField(upload_to="profile/image", blank=True, null=True)


    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = "حساب های کاربری"
        verbose_name_plural = "پروفایل"

class Ticket(models.Model):
    title = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    email = models.EmailField()

    class Meta:
        verbose_name = "تیکت های کاربر"
        verbose_name_plural = "تیکت ها"