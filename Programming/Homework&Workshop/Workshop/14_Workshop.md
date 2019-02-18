# 14_Workshop

### 1. https://<your-server-url>/info 의경로로 들어갔을 때 다음과 같이반 정보를 보여주는 페이지를 만들어 주세요.

![1548307342690](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548307342690.png)

### 2. https://<your-server-url>/student/<학생이름>의 경로로 들어갔을 때 다음과 같이 학생의 이름과 나이를 보여주는 페이지를 만들어 주세요.

![1548307718751](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548307718751.png)

##### first_workshop/url.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.ss3_info),
    path('student/<name>/', views.student_age),
]
```

##### first_workshop/views.py

```python
from django.shortcuts import render

# Create your views here.
def ss3_info(request):
    teacher = '유태영'
    student = ['지상현', '이원진', '이지선', '이상주', '권성령', '장재영']
    return render(request, 'ss3_info.html', {'teacher': teacher, 'student': student})
    
def student_age(request, name):
    student_age = {
        '지상현': 25, '이원진': 28, '이지선': 27, '이상주': 27, '권성령': 26, '장재영': 30
    }
    return render(request, 'student_age.html', { 'name': name, 'student_age': student_age[name]})
```

##### first_workshop/templates/workshop_base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>First Workshop {% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

##### first_workshop/templates/ss3_info.html

```html
{% extends 'workshop_base.html' %}

{% block title %} SS3_INFORMATION {% endblock %}

{% block content %}

    <h1>우리반 정보</h1>
    <h2>Teacher</h2>
    <ul>{{ teacher }}</ul>
    <h2>Student</h2>
    <ul>
        {% for student in student %}
        <li>{{ student }}</li>
        {% endfor %}
    </ul>
    
{% endblock %}
```

##### first_workshop/templates/student_age.html

```html
{% extends 'workshop_base.html' %}

{% block title %} Student Age {% endblock %}

{% block content%}
    <h1>이름: {{ name }}</h1>
    <h2>나이: {{ student_age }}</h2>
{% endblock %}
```

