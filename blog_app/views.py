from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, ArchiveIndexView, YearArchiveView
from django.views.generic.base import View
from post_app.models import post, categories, comment, Message_form_user, Like
from .forms import MassageForm
from .mixins import LoginMixin


# from django.contrib.auth.mixins import LoginRequiredMixin

# comment user body
def post_datal(request, slug):
    aurthor = get_object_or_404(post, slug=slug)
    if request.method == 'POST':
        body = request.POST.get("body")
        parent = request.POST.get("parent_id")
        comment.objects.create(body=body, parent_id=parent, article=aurthor, user=request.user)
    return render(request, "blog_app/post.html", {"aurthor": aurthor})


# def post_list(request):
#     aurthor = post.objects.all()
#     page_number = request.GET.get("page")
#     paginator = Paginator(aurthor, 2)
#     object_list = paginator.get_page(page_number)
#     return render(request, "blog_app/articles_list.html", {"aurthor": object_list})

class PostArticleList(LoginMixin, ListView):
    model = post
    queryset = post.objects.all()
    paginate_by = 2
    # context_object_name = "aurthor"
    # article__slug = self.object_list.slug,
    # like is post and post_list is object_list it is view no article__slug = self.object_list.slug,
    # post_list error QuerySet slug
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.likes.filter(user_id=self.request.user.id).exists():
            context['is_like'] = True
        else:
            context['is_like'] = False
        return context


def category_detail(request, pk=None):
    category = get_object_or_404(categories, id=pk)
    aurthor = category.posts.all()
    return render(request, "blog_app/articles_list.html", {"aurthor": aurthor})


# search box
def search(request):
    q = request.GET.get("q")
    aurthor = post.objects.filter(title__icontains=q)
    page_number = request.GET.get("page")
    paginator = Paginator(aurthor, 1)
    object_list = paginator.get_page(page_number)
    return render(request, "blog_app/articles_list.html", {"aurthor": object_list})


# forms.py
def contact(request):
    if request.method == "POST":
        form = MassageForm(data=request.POST)
        if form.is_valid():
            form.save(commit=True)

            # return redirect("heme:heme")
    else:
        form = MassageForm
    return render(request, "blog_app/contact.html", {"form": form})


# instance = form.save(commit=True)
# instance.bmi = instance.weight * instance.height


# class base viwes articles_list.html

class listview(View):
    queryset = None
    template_name = None

    def get(self, request):
        return render(request, self.template_name, {"object_list": self.queryset})


class Artecle_list(ListView):
    queryset = post.objects.all()
    template_name = "blog_app/articles_list.html"


class Userlist(ListView):
    queryset = post.objects.all()


class ArtecleListView(listview):
    module = post
    template_name = "blog_app/articles_list.html"
    context_object_name = "aurthor"
    paginate_by = 2


class MessageView(CreateView):
    model = Message_form_user
    fields = ('name', 'Text', 'age')
    success_url = reverse_lazy("heme:heme")
    template_name = "blog_app/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Message"] = Message_form_user.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.Email = self.request.user.email
        instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return super(MessageView, self).get_success_url()


# class ArtecleDateilView(DetailView):
#     model = post
#     template_name = "blog_app/post.html"
#     context_object_name = "aurthor"


# class ContactUsView(ListView):
#     template_name = "blog_app/contact.html"
#     form_class = MassageForm
#     queryset = "form"
#     success_url = reverse_lazy("heme:HomePage")
#
#     def form_valid(self, form):
#         from_data = form.cleaned_data
#         Message_form_user.objects.create(**from_data)
#         return super().form_valid(form)

class MessageList(ListView):
    model = Message_form_user


class MessageUpdateView(UpdateView):
    model = Message_form_user
    fields = ('__all__')
    template_name = 'blog_app/message_update_form.html'
    success_url = reverse_lazy("blog:message_list")


class DeleteMessageView(DeleteView):
    model = Message_form_user
    success_url = reverse_lazy("blog:message_list")


class ArchiveArticleView(ArchiveIndexView):
    model = post
    date_field = "update"
    # date_field = "data_times"


class YearArticleView(YearArchiveView):
    model = post
    date_field = "pub_deta"
    make_object_list = True
    allow_future = True


def Likes_Detail(request, slug, pk):
    try:
        likes_list = Like.objects.get(article__slug=slug, user_id=request.user.id)
        likes_list.delete()
        return JsonResponse({'response': 'unlikes'})
    except:
        Like.objects.create(article_id=pk, user_id=request.user.id)
        return JsonResponse({'response': 'likes'})