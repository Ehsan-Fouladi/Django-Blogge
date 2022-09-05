import django.utils.timezone
from django.db.models.fields import related
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify


# name models feld

# null=True
# blank=True
# help_text="hi user"
# unique=True
# db_column="Edit name"
# editable=True
# choices=The parameter detects
# default=The parameter detects
# CHOICES = (
#         ('A', "django"),
#         ('B', "python"),
#         ('C', "ehsan"),
#         ('C', "amir"),
#         ('D', "ail"),
#         ('G', "user"),
#         ('F', "name"),
#         ('H', "admin"),
#     )



class categories(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی ها "
        verbose_name_plural = "دسته ها"

# views
# model manger&
# class manger object all()
# aurthor object

class Manager(models.Manager):
    def get_costum(self):
        return super(Manager, self).get_costum().filter(status=True)


class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="دسته")
    category = models.ManyToManyField(categories, related_name="posts")
    title = models.CharField(max_length=100, unique_for_date="pub_deta", verbose_name="عنوان")
    bode = models.TextField()
    image = models.ImageField(upload_to="image", blank=True, null=True)
    tima = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, verbose_name="تایم اپدیت")
    pub_deta = models.DateField(default=django.utils.timezone.now)
    file_deta = models.FileField(upload_to="file deta", null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name="وضعیت")
    published = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)
    objects = models.Manager()
    costom_manger = Manager()


    def save(
        self, force_insert=False, force_update=False,
            using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(post, self).save()


    def get_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def shoe_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" height="50px" width="60px" >')
        return format_html('<h3 style="color: red">تصویر موجود نیست</h3>')
    shoe_image.short_description = "عکس مقاله"

    def __str__(self):
        return f"{self.title}, {self.bode[:20]}"

    class Meta:
        ordering = ("-tima",)
        verbose_name_plural = "پست ها"
        verbose_name = "پست"

# comment user
class comment(models.Model):
    article = models.ForeignKey(post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]

    class Meta:
        verbose_name = "نظرات"
        verbose_name_plural = "نظرات ها"

class Message_form_user(models.Model):
    name = models.CharField(max_length=100)
    Text = models.TextField(max_length=100)
    Email = models.EmailField()
    Year_time = models.DateTimeField(auto_now_add=True, null=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", verbose_name='کاربر')
    article = models.ForeignKey(post, on_delete=models.CASCADE, related_name="likes", verbose_name='مقاله ')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.article.title}"

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"
        ordering = ('-created_at',)

# name models in objects user
# author = models.ForeignKey(User, on_delete=models.CASCADE)
# author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
# author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="1")
# author = models.ForeignKey(User, on_delete=models.PROTECT)
# author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

