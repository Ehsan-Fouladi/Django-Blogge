from django.template import Library




register = Library()


@register.inclusion_tag("heme_app/index.html")
def how_result(text):
    return {"text": text}