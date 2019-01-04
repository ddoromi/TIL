# 2019. 01. 04	Summary

## 1.  Workshop

### OS & Command Line Interface

#### Basic

* directory 확인 : dir = ls
* pwd : 현재 위치 확인
* ls : list, ls -a(ls --all) : 숨긴 파일을 포함한 모든 list
* cd : 특정 디렉토리로 이동
* mkdir : 디렉토리 생성, touch : 파일 생성
* vim 파일 이름, 
  * esc : 셀 나가기, dd : 지우기
  * esc -> : i : 내용 입력하기, : w = 저장하기, : q = 나가기
* $ : prompt , 입력을 받을 준비가 됨.
* ^C : 멈춤 ,    ^ : 캐럿(ctrl 키를 뜻함)
* echo : 출력 명령어(= print)
* man 명령어 : 명령어에 대한 설명 -> q를 누르면 나올 수 있음.
* ctrl + p = previous 명령어 (방향키로 접근 가능)
* clear(ctrl + l) : 새로고침
* ctrl + d : 터미널 끄기(파이썬 실행 때에도 나올 수 있음)
* sleep : 터미널 재우기

#### 파일 조작

* echo "문자열" > 파일 이름.확장자 = 파일을 생성하고 문자열을 넣을 수 있음.
* '>' = 덮어씌어버림, '>>' = 내용 추가
* cat 파일 이름 = 파일 안에 있는 내용을 출력 해줌.
* .파일이름 : 숨김 파일
* ls -l : 파일 권한, 날짜,용량 등 파일의 정보를 알려줌 // 여러 옵션을 붙여서 사용할 수 있음(lh : 직관적으로 보여줌)
* rm : 지우기, rm -i : 지우기 전에 물어봄, rm -f : 강제로 지움, *.txt : txt를 다 지움
* ls 파일명 : 파일명이 있는지 알려줌 a* : a로 시작하는 파일을 보여줌
* cp old new: old파일을 복사해서 new 생성

#### 파일 체크

* which 프로그램 : 프로그램이 있는 지 확인
* head : 첫 10줄, tail : 마지막 10줄
* ping : 서버가 살아있는지 확인하는 명령어
* wc : 줄, 단어, 글자
* head sonnets.txt | wc  : |앞에 있는 것을 wc로 넘겨줌
* less : viewer       / 
* grep 찾고자 하는 문자 파일명 (-i : 대문자, 소문자 모두 찾아줌)
* ps aux : process를 알려줌
* / : 최상단 디렉토리(루트)
* ~ : home 디렉토리(컴퓨터가 지정)
* mkdir -p ssafy/ss3/students  : 여러 단계의 폴더 만들기
* rmdir : 디렉토리 지우기   rm -r : 연결된 디렉토리 다 지우기  rm -rf : 파일까지 다 지우기
* cd .. : 한 단계 위 디렉토리로 이동     cd . : 지금 위치(git add . : 지금 있는 위치 add)    cd  - : 한 단계 뒤로 가기
* 

git commi -m ''