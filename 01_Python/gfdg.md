영진위 Key : 35770123d2dc19e6493c29c394b197ed

네이버 Client ID : e4rGuROqckKk7FCxM3YZ

Cilent Secret : e9rKl2agCh



### 1. KOBIS => boxoffice.csv

* 조건 

  * 1 : 주간 데이터 => WeekGb = 0

  *  2 : 10주간, ~20190113 =>  targetDt = 20190113

* 결과

  * 영화 대표 코드 :  movieCd
  * 영화명 (국문) : movieNm
  * 해당일 누적 관객수 : audiAcc
  * 해당일 : targetDt

* 영화 대표코드 결과 : key = key&movieCd=MovieCd
  * 영화명(국문) : movieNm
  * 영화명(영문) : movieNmEn
  * 영화명(원문) : movieOg
  * 개봉연도 : opendDt
  * 상영시간 : showTm
  * 장르 : genreNm
  * 감독명 : peopleNm
  * 관람등급 : watchGradeNm
  * 배우 : actors (최대 3명까지)

### 2. Naver API => movie.csv

* 결과
  * 영진위 영화 대표 코드 : movieCd
  * 영화 썸네일 이미지 URL : 'items''image'
  * 하이퍼텍스트 Link : 'items''link'
  * 유저 평점 : 'items''userRating'





