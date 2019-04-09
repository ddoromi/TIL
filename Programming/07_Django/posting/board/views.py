from django.shortcuts import render
from .models import Posting, Comment


def posting_list(request):
    postings = Posting.objects.all()
    return render(request,'board/list.html', {'postings': postings})


def posting_detail(request, id):
    posting = Posting.objects.get(id=id)
    return render(request, 'board/detail.html', {'posting': posting})
