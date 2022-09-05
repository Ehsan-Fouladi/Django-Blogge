from django.contrib import admin
from . import models


# admin.site.site_header = "مدیرت وبلاگ"
# admin.site.site_title = "UMSRA Admin Portal"
# admin.site.index_title = "Welcome to UMSRA Researcher Portal"

class FilterByTitle(admin.SimpleListFilter):
    title = " کلید های پرتکرار"
    parameter_name = 'title'
    def lookups(self, request, model_admin):
        return (
            ("python", "پایتون"),
            ("django", "جنگو"),
            ("java", "جاوا"),
        )
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())

class CommentInline(admin.TabularInline):
    model = models.comment



@admin.register(models.post)
class post(admin.ModelAdmin):
    list_display = ("author", "title", "update", "status", "shoe_image")
    list_editable = ("title",)
    list_filter = ("status", "update", FilterByTitle)
    search_fields = ("title", "bode")
    inlines = (CommentInline,)
    # fields =

# admin.site.register(post)
admin.site.register(models.categories)
admin.site.register(models.comment)
admin.site.register(models.Message_form_user)
admin.site.register(models.Like)
