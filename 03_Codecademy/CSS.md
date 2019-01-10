# CSS

## 1.  The . css file

### HTML

* <link> : html의 head 안에 넣어야 함. 
  * href : 연결하는 파일의 주소, type : 연결하는 파일의 타입, rel : html과 연결하는 파일의 관계

​               ex) <link href="./style.css" type="text/css" rel="stylesheet">

### CSS

* element 연결 : html에 있는 tag {  }   ex) h1 { }

* class : html의 class를 불러와서 연결할 수 있음. ex) in html, <h1class = "brand">,  in css  .brand { }

  ​            space를 기준으로 여러  class 연결 가능

* element와 class가 겹칠 경우 class가 오버라이딩 됨.

* id : class를 무시하고 적용. ex) in html, <h1 id="article">,  in css  #article { }

* 특정 element의 class 설정 : element.class { }

### stlye 설정

* 색 => color: 색;
* 대문자로 바꾸기 => text-transform: uppercase;
* 첫 글자는 대문자, 나머지는 소문자 => text-transform: capitalize;
* 폰트 => font-family: 폰트;
* 





