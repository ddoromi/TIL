from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth import login, logout
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import User
from posts.forms import CommentModelForm
from django.contrib.auth.decorators import login_required
from IPython import embed
# from django.contrib.auth import get_user_model


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('posts:post_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def log_in(request):
    # 사용자가 로그인 되어 있는 지 확인
    if request.user.is_authenticated:
        return redirect('posts:post_list')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:post_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('posts:post_list')


def user_detail(request, username):
    user_info = User.objects.get(username=username)
    return render(request, 'accounts/user_detail.html', {'user_info': user_info, 'comment_form': CommentModelForm()})


@login_required
@require_POST
def toggle_follow(request, username):
    sender = request.user
    receiver = get_object_or_404(User, username=username)
    # embed()
    if sender != receiver:
        if receiver in sender.followings.all():
            sender.followings.remove(receiver)
        else:
            sender.followings.add(receiver)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))
