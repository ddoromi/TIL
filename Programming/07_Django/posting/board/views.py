from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Posting, Comment


@require_http_methods(['GET', 'POST'])
def create_posting(request):
    if request.method == 'POST':
        posting = Posting()
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()
        return redirect('board:posting_detail', posting_id=posting.id)
    else:
        return render(request, 'board/new.html')


@require_http_methods('GET')
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'board/list.html', {'postings': postings})


@require_http_methods('GET')
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.all()
    return render(request, 'board/detail.html', {'posting': posting, 'comments': comments})


@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method == 'POST':
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()
        return redirect('board:posting_detail', posting_id=posting.id)
    else:
        return render(request, 'board/edit.html', {'posting': posting})


@require_http_methods('POST')
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('board:posting_list')


@require_http_methods(['POST'])
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = Comment()
    comment.content = request.POST.get('comment')
    comment.posting = posting
    comment.save()
    return redirect('board:posting_detail', posting_id=posting_id)


@require_http_methods(['POST'])
def delete_comment(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('board:posting_detail', posting_id=posting.id)