# Homework_11

##### 1. 다음은 부트스트랩의 어떤 component이며 아래와 같이 만들려면 어떤 class를 주어야 하는 가.

![1548056789410](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548056789410.png)

=> button

```html
<button type="button" class="btn btn-danger">Danger</button>
```

##### 2. 다음은 부트스트랩의 어떤 component 이며 아래와 동일하게 만들어 보시오.

![1548057009699](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548057009699.png)

=> alert

```html
<div class="alert alert-info" role="alert">
  Hello SSAFY ?!
</div>
```

##### 3. 다음 빈칸을 채우시오.

=> 부트스트랩 그리드 시스템은 레이아웃을 ( 12 )개의 column으로, ( 5 )개의 반응형 사이즈 조건을 사용하여 구축한다.

##### 5. 아래와 같은 분할을 grid system을 활용하여 만들어 보시오.

![1548057112798](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548057112798.png)

```html
<head>
    <style>
        div {
            border: solid 1px black;
        }
        .row {
            background-color: moccasin;
        }
    </style>
</head>

<body>
    <div>
        <div class="row">
    	<div class="col-3">25%</div>
    	<div class="col-6">50%</div>
        <div class="col-3">25%</div>
  	</div>
</body>

        
```