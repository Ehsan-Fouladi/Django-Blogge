from django.shortcuts import render
from post_app.models import post
from django.views.generic.base import TemplateView, RedirectView, View
# from django.views.generic import ListView


# filetr(models django db)
# model
# model Manager and object
# model filter(status=True)

def index(request):
    aurthor = post.objects.all()#Manager_request
    recent_articles = post.objects.all().order_by('-update', '-tima')
    return render(request, "heme_app/index.html", {'aurthor': aurthor, "recent_articles": recent_articles})



def sidebar(request):
    date = {"name": "EhsanFouladi"}
    return render(request, "includes/sidebar.html", context=date)




class HomePageView(TemplateView):

    template_name = "heme_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aurthor'] = post.objects.all()
        return context


class HomePageRedirectView(RedirectView):
    pattern_name = "assets:login"
    permanent = True
    query_string = False
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)

# aurthor = post.published
# aurthor = post.status
# aurthor = post.costom_manger.filter(status=True)
# aurthor = post.costom_manger.all()




