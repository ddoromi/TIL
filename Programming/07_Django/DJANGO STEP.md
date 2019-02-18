# DJANGO STEP

### 환경 설정

#### * 가상 환경 만들기

```
mkdir <project_name>
cd <project_name>
pyenv virtualenv 3.6.8 <project_name>
pyenv local <project_name>
pip install django
pip install django-extensions ipython
django-admin startproject <project_name> . (최상단 폴더를 제외하고 생김)
```

#### 1. 프로젝트 만들기 @ terminal

```
django-admin startproject <project_name>
```

#### 2. 최상단 폴더 이름 대문자로 바꾸기 @ terminal

```
mv <project_name> <PROJECT_NAME>
```

#### 3. 앱 만들기 @ terminal

```
django-admin startapp <app_name>
```

#### 4. setting 설정 @ setting.py

```python
ALLOWED_HOST = ['*']
INSTALLED_APPS = ['<app_name>',]
TEMPLATES = [{ 'DIRS': [os.path.join(BASE_DIR, 'templates')] }] # default value
LAGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```

#### 5. 스키마 작성 @ models.py

```
* models.TextField()
* models.CharField(max_length=?)
* models.IntegerField()
* models.DateField()
* models.BooleanField()
* models.FloatField()
* models.ForeignKey(<상단 class>, on_delete=<models.CASCADE, DO_NOTHING>)
=> ()안에 default 값 지정 가능
```

#### 6. migrate @ terminal

```
python manage.py makemigrations <app_name> => 초기화
python manage.py migrate 
```

#### 7. admin 권한 주기 @ admin.py

```python
from .models import <class_name>
admin.site.register(<class_name>)
```

#### 8. superuser 생성 @ terminal

```
python manage.py createsuperuser 
```

#### 

### Code 

#### 1.  url 설정 @ urls.py

```python
# @최상단 urls.py
from django.urls import path, include
path('<app_name>', include('<app_name.urls>'))
```

```python
# @app urls.py
from django.urls import path
from . import views
app_name = '<app_name>'
urlpatterns = [
    path('<url>', view.<function_name>, name='<url_name>')
]
```

#### 2. CRUD 함수 @ views.py

```python
import render, redirect, get_object_or_404 # 에러 
import .models from <class_name>
# list 
def
# create 
def <function_name>(request):
    # class의 모든 객체 
    <변수> = <class_name>.objects.all()
    return render(request, '<>.html', {'변수': 변수})
```





