from django.views.generic.base import TemplateView
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from blog.forms import CreateUserForm
from django.contrib.auth import login
from django.contrib.auth import forms as auth_forms
from django import forms
from member.models import User
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeDoneView,PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


def home(request):
    if request.user.is_authenticated:
        if request.user.is_manager ==True :
            return redirect('manager_home')
        elif request.user.is_member==True or request.user.is_manager ==True:
            return redirect('blog_home')
    return render(request, 'home.html')

@login_required
def admin_home(request):
    if request.user.is_authenticated:
        if request.user.is_manager ==False or request.user.is_manager ==False :
            error = "로그인 또는 관리자계정으로만 접근가능합니다"
            return HttpResponse(error)
    user_is_member=User.objects.filter(is_member=True,date_joined__lte=timezone.now()).order_by('-date_joined')[:10]
    user_is_manager = User.objects.filter(is_manager=True, date_joined__lte=timezone.now()).order_by('-date_joined')[:10]
    none_user = User.objects.filter(is_member=False,is_manager=False, date_joined__lte=timezone.now()).order_by('-date_joined')[:10]
    return render(request,'manager/home.html', {'user_is_member':user_is_member,'none_user':none_user,'user_is_manager':user_is_manager})

@login_required
def blog_home(request):
    if request.user.is_authenticated:
        if request.user.is_manager ==False or request.user.is_manager ==False :
            error = "로그인 또는 회원계정으로만 접근가능합니다"
            return HttpResponse(error)
    return render(request, 'blog/home.html')


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('home')


class UserPasswordChangeView(PasswordChangeView,):

    success_url = reverse_lazy('password_change_done')
    template_name = 'registration/password_change_form.html'


class UserPasswordDoneView(PasswordChangeDoneView,):
    template_name = 'registration/password_change_done.html'



# get 방식
def validate_username(request):
    # HttpRequest 객체의 GET 과 POST 속성은 django.http.QueryDict 의 인스턴스입니다.
    # get()메서드는 키(여기서는 username)이 없는 경우 기본값 'None'을 반환합니다. https://goo.gl/wtA6KN
    username = request.GET.get('username', None)

    data = {
        # <필드명>__iexact는 대소문자를 구분하지 않고 일치하는 값을 찾는다. https://goo.gl/5XywcT
        # exists()는 쿼리셋에 결과가 있는 경우 True를 반환합니다. https://goo.gl/Vgtr2u
        'is_taken_username':User.objects.filter(username__iexact = username).exists()

    }
    if data['is_taken_username']:
        data['error_message'] = '아이디가 이미 존재합니다. 다른 이름을 입력해 주세요.'

    # data를 Json형식으로 인코딩되도록 합니다.
    return JsonResponse(data)