import os, csv, requests, time, urllib.request

os.getenv("NAVER_CLIENT_ID")
os.getenv("NAVER_CLIENT_SECRET")
client_id = "NAVER_CLIENT_ID"
client_secret  = "NAVER_CLIENT_SECRET"

# movie.csv를 읽어 영화 대표 코드와 영화명(국문)만을 저장하는 함수
def read_movie(file_name):
    read_movies_information = open(file_name, 'r', encoding='utf-8') #w+는 덮어씀, a+는 추가, r은 읽기만 하기
    reader = csv.reader(read_movies_information)

    movieCd_Nm_list = [] # 영화 대표 코드와 영화명이 저장된 list

    for line in reader:
        movie = [] 
        movie.append(line[0])
        movie.append(line[1])
        movieCd_Nm_list.append(movie)

    movieCd_Nm_list.remove(['movie_code', 'movie_name_ko']) 
    return movieCd_Nm_list

# naver api가 제공하는 영화 정보를 저장하는 함수
def naver_movie_information(movieCd_Nm_list):
    naver_URI = 'https://openapi.naver.com/v1/search/movie.json?query='
    client_id = 'e4rGuROqckKk7FCxM3YZ'
    client_secret = 'e9rKl2agCh'
    headers = { 'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

    naver_movie_information = [] # 최종적으로 저장되는 네이버 영화 정보 list

    for movie in movieCd_Nm_list:
        data_set = requests.get(naver_URI + movie[1], headers=headers).json()
        
        a_movie_info = [] # 하나의 네이버 영화 정보
        a_movie_info.append(movie[0])                           # 영화 대표 코드
        a_movie_info.append(data_set['items'][0]['image'])      # 영화 이미지 URL
        a_movie_info.append(data_set['items'][0]['link'])       # 영화 하이퍼텍스트 링크
        a_movie_info.append(data_set['items'][0]['userRating']) # 유저 평점
        
        naver_movie_information.append(a_movie_info)
        time.sleep(1)

    return naver_movie_information

# naver api가 제공하는 영화 정보를 파일로 쓰는 함수
def write_naver_movie_information(file_name, naver_movie_information):
    write_naver_information = open(file_name, 'w+', encoding='utf-8', newline='') #w+는 덮어씀, a+는 추가

    # movie.csv의 첫 줄
    writer = csv.writer(write_naver_information)
    writer.writerow(['Movie_code', 'Thumb_url', 'Link_url', 'User_rating'])

    for i in range(len(naver_movie_information)):
        writer.writerow(naver_movie_information[i])

    write_naver_information.close()

# 영화 썸네일 이미지의 URL을 통해 이미지를 파일로 저장하는 함수
def save_movie_images(naver_movie_information):
    for i in range(len(naver_movie_information)):
        URL = naver_movie_information[i][1]
        file_name = f'images/{naver_movie_information[i][0]}.jpg'
        urllib.request.urlretrieve(URL, file_name)

write_naver_movie_information('movie_naver.csv', naver_movie_information(read_movie('movie.csv')))
save_movie_images(naver_movie_information(read_movie('movie.csv')))

