# 4: 도시중에 최근 3일간 가장 추웠던 곳, 가장 더웠던 곳,
cities_temp = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5 , 2],
    '광주': [0, -5, 10],
    '구미': [2, -2, 10]
}

# all_temp 모든 기온을 모은다
all_temp = []
for key, value in cities_temp.items():
    all_temp += value

# all_temp 에서 highest/lowest 를 찾는다
highest = max(all_temp)
lowest = min(all_temp)
print(highest, lowest)``
# cities_temp 에서 highest/lowest 가 속한 도시를 찾는다.
hottest = []
coldest = []
for key, value in cities_temp.items():
    if highest in value:
        hottest.append(key)

    if lowest in value:
        coldest.append(key)

print(hottest, coldest)