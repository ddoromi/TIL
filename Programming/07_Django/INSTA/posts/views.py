from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Post, Image
from .forms import PostModelForm, ImageModelForm


@login_required
@require_http_methods(['GET', 'POST'])
def create_post(request):
    # POST 방식으로 입력받은 데이터를 저장
    if request.method == 'POST':
        # POST 방식으로 넘어온 데이터를 ModelForm에 넣음
        post_form = PostModelForm(request.POST)
        # data 검증
        if post_form.is_valid():
            post = post_form.save()
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
    return render(request, 'posts/list.html', {'posts': posts})


@login_required
@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostModelForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:post_list')
    else:
        post_form = PostModelForm(instance=post)
    return render(request, 'posts/form.html', {'post_form': post_form})
