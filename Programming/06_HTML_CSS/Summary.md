# 19. 01. 14 Summary

## HTML

### 1.index.html

* 문법을 지키지 않아도 error가 발생하지 않음. 

* ```html
  <!DOCTYPE html>  <!-- html은 tree 구조 -->
  <html lang="en"> <!-- lang : triger -->
  <head> <!-- 정보를 담고 있음, 눈에 보이지 않음 -->
      <meta charset="UTF-8"> <!-- mete : 정보 -->
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Ddoromi's Github Page</title>
  </head>
  <body> <!-- 실제 사용자에게 보여지는 정보 -->
      <h1>Comming Soon...</h1>
  </body> 
  </html>
  <!-- body와 h1은 부모자식관계, head와 body는 형제자매 관계-->
  ```

### 2. Tag

* <> : tag, 기본적으로 <여는 태그> 내용 </닫는 태그>
* tag + 내용(content) : element 
  * element의 태그는 'tag'이고 content는 '내용'이다.
* 혼자 열리고 닫히는 태그도 존재함 ex) img
* 태그 용어 : <img src="./animals/cat1.jpg" alt="cat" />
  * src, alt 등 : 속성, " " : 속성 값
  * = 좌우로 띄어쓰기 없음.  " " 사용(' ' X)
* <'header'> , <'nav'> , <'aside'>, <'section'>, <'article'>, <'footer'> 등은 기능이 아니라 역할에 따른 tag임.



## CSS

### 1. Naming

* 명시적이고 구체적으로 짓기
* 어떻게 보여질 지로 정하지 않기
* id는 사용하지 않고, class로 사용하자 // id는 javascript에서 사용

### 2. 우선 순위

* !important : 첫 번째 우선 순위, 쓰지 않음.
* inline 
* media type
* 사용자 정의 (only mine)
* id
* class : class가 중복될 경우 아래 정의된 class가 우선 순위를 가짐.
* class 상속 : 자식 => 부모
* tag를 selector로 썼을 때