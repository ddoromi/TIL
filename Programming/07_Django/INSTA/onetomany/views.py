from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from .forms import *
from .models import Book, Writer, Chapter


def create(request):
    if request.method == 'POST':
        form = WriterModelForm(request.POST)
        if form.is_valid():     # data 유효성 검사
            form.save()
            return redirect('success')

    elif request.method == 'GET':
        form = WriterModelForm()

    # 유효성 검사 실패할 경우에는 form에 입력한 내용이 담겨있음
    return render(request, 'new.html', {'form': form})


def update(request, id):
    writer = Writer.objects.get(id=id)
    if request.method == 'POST':
        form  = WriterModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

    elif request.method == 'GET':
        form = WriterModelForm(instance=writer)

    # 유효성 검사 실패할 경우에는 form에 입력한 내용이 담겨있음
    return render(request, 'edit.html', {'form': form})
