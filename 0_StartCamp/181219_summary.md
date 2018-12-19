# 181219 수업정리

## 1. 명령어(git)

* git add .    => 정지
* git status   => 상태확인
* git commit -m 'commit_name' => 정지
* git push => 업로드



## 2. Code 정리

* Morning Quiz1 : List 평균 구하기

  ```python
  # 1. 평균 구하기
  my_score = [79, 84, 66, 93]
  
  score_sum = 0.0
  for score in my_score :
      score_sum += score
  
  my_average = score_sum/len(my_score)
  #my_average = sum(my_score)/len(my_score)  list values의 합을 구하는 함수 sum()
  print ('My average is ', my_average)
  
  
  your_score = {
      '수학' : 87,
      '국어' : 83,
      '영어' : 76,
      '도덕' : 100
  }
  
  score_sum = 0.0
  your_average = sum(your_score.values())/len(your_score)
  
  # for score in your_score.values():  #dict의 Values를 추출하는 함수 .values()
  #     score_sum += score
  
  # for subject, score in your_score.items():
  #     score_sum += score
  #your_average = score_sum/len(your_score)
  
  print ('Your average is ', your_average)
  
  print (type(your_score.values()))
  print (your_score.values())
  ```

* Morning Quiz2 :  Dict 평균 구하기

  ```python
  cities_temp = {
       '서울' : [-6, -10, 5],
       '대전' : [-3, -5, 2],
       '광주' : [0, -5, 10],
       '구미' : [2, -2, 9]
   }
  
  #도시별 평균 온도
  for city, temp in cities_temp.items() :
      average_temp = sum(temp)/len(temp)
      print(city, '평균 온도 :', round(average_temp, 2))  #pritnt 함수의 형태
      print(city + ': ' + str(average_temp))
      print('{0}: {1}'.format(city, average_temp))
  
  max_temps = {}
  min_temps = {}
  
  # 각 도시별로 최대 온도를 구하여 'max_temps'에 저장
  for city, temps in cities_temp.items() :
      max_temps[city] = max(temps)
  
  # 각 도시별로 최소 온도를 구하여 'min_temps'에 저장
  for city, temps in cities_temp.items() :
      min_temps[city] = min(temps)
  
  print(max_temps)
  print(min_temps)
  
  # 'max_temps'의 최대 온도를 구함(hottest_temp)
  hottest_temp = max(max_temps.values())
  
  # 'max_temps'에서 온도가 최대 온도(hottest_temp)와 같은 경우 city 출력
  for city, max_temp in max_temps.items():
      if max_temp == hottest_temp :
          print('최근 3일간 가장 더웠던 도시는 ', city, max_temp , '도 입니다.')
  
  # 'min_temps'의 최소 온도를 구함(coldest_temp)
  coldest_temp = min(min_temps.values())
  
  # 'min_temps'에서 최소 온도(coldest_temp)와 같은 경우 city 출력
  for city, min_temp in min_temps.items():
      if min_temp == coldest_temp :
          print('최근 3일간 가장 추웠던 도시는 ', city, min_temp, '도 입니다.')
  
          
  #강사님 예시 => list를 더할 수 있음!!!!! 
  #간단한 code로 만들기, 답은 dict나 list로 만들기
  #all_temp에 모든 기온을 모음
  all_temp = []
  for key, value in cities_temp.items() :
      all_temp += value
  print(all_temp)
  
  #all_temp에서 highest/lowest를 찾음
  highest = max(all_temp)
  lowest = min(all_temp)
  
  hottest = []
  coldest = []
  #cities_temp에서 highest/lowest가 속한 도시를 찾음
  #같은 값을 찾아 key 값을 뽑고 싶을 때 in 사용하기
  for key, value in cities_temp.items():
      if highest in value:
          hottest.append(key)
      if lowest in value:
          coldest.append(key)
  print(hottest, coldest)
  ```
