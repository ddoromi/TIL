my_score = []

score_sum = 0.0
for score in my_score :
    score_sum += score

my_average = score_sum/len(my_score)
print ( username 'average is ', useraverage)


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