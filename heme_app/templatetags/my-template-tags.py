from django.template import Library




register = Library()


@register.inclusion_tag("heme_app/result.html")
def show_result(queryset):
    return {"objects": queryset}

