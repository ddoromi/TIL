from django import forms
from .models import Movie


class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    title_en = forms.CharField(max_length=100)
    audience = forms.IntegerField()
    open_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )
    genre = forms.CharField(max_length=100)
    watch_grade = forms.CharField(max_length=100)
    score = forms.FloatField()
    poster_url = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'  # ['title', 'title_en'] 리스트로 특정 컬럼만 받아올 수 있음
        widgets = {
            'open_date': forms.DateInput(attrs={'type': 'date'})
        }
