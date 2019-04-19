from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Post, Image, Comment
from .forms import PostModelForm, ImageModelForm, CommentModelForm


@login_required
@require_http_methods(['GET', 'POST'])
def create_post(request):
    # POST 방식으로 입력받은 데이터를 저장
    if request.method == 'POST':
        # POST 방식으로 넘어온 데이터를 ModelForm에 넣음
        post_form = PostModelForm(request.POST)
        # data 검증
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect('posts:post_list')

    # get 방식으로 데이터를 입력할 form 요청
    else:
        post_form = PostModelForm()
    image_form = ImageModelForm()
    return render(request, 'posts/form.html', {'post_form': post_form, 'image_form': image_form})


@require_http_methods(['GET'])
def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {'posts': posts, 'comment_form':comment_form})


@login_required
@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:
        if request.method == 'POST':
            post_form = PostModelForm(request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()
                return redirect('posts:post_list')
        else:
            post_form = PostModelForm(instance=post)
        return render(request, 'posts/form.html', {'post_form': post_form})
    else:
        return redirect('posts:post_list')


@login_required
@require_http_methods(['POST'])
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentModelForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'posts/form.html', {'comment_form': comment_form, 'post':post})


@login_required
@require_http_methods(['POST'])
def toggle_like(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    if user in post.like_users.all():  # 찾으면 [value], 없으면 [] // exit() => True or False
        post.like_users.remove(user)
    # if post.like_users.filter(id=user.id).exit():  # 찾으면 [value], 없으면 [] // exit() => True or False
    #     post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('posts:post_list')
