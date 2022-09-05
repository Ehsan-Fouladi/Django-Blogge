from django.shortcuts import redirect


class LoginMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('assets:login')
        return super(LoginMixin, self).dispatch(request, *args, **kwargs)
