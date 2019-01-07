# # 1. 평균을 구하시오
# my_score = [79, 84, 66, 93]
# my_total = sum(my_score)
# my_average = my_total / len(my_score)
# print(my_average)

# your_score = {
#     '수학': 87,
#     '국어': 83,
#     '영어': 76,
#     '도덕': 100
# }

# your_total = sum(your_score.values())
# your_average = your_total / len(your_score)
# print('당신의 평균은:', your_average)

cities_temp = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5 , 2],
    '광주': [0, -5, 10],
    '구미': [2, -2, 9]
}

# 3: 도시별 온도 평균
for city in cities_temp: # 왼손으로 key 만 꺼내요
    temperatures = cities_temp[city]
    avg_temperature = round(sum(temperatures) / len(temperatures), 2)
    print(city, avg_temperature)
    print(city + ': ' + str(avg_temperature))  
    
for key, value in cities_temp.items(): # 양손으로 key, value 꺼내요
    avg_temperature = round(sum(value) / len(value), 2)
    print(key, avg_temperature)
    print(key + ': ' + str(avg_temperature))   

