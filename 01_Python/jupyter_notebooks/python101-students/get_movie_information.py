import os, requests, csv
os.getenv("KOBIS_KEY")
key = "KOBIS_KEY"

# boxoffice.csv를 읽어 영화 대표 코드만 저장하는 함수
def read_box_office(file_name):
    read_box_office = open(file_name, 'r', encoding='utf-8')
    reader = csv.reader(read_box_office)

    movieCd_list = [] # movieCd(영화 대표 코드)가 저장된 list

    for line in reader:
        movieCd_list.append(line[0])

    movieCd_list.remove('movie_code')
    return movieCd_list

# 영화 대표 코드를 이용해서 kobis에 접속, 영화 상세 정보를 저장하는 함수
def detail_movie_information(key, movieCd_list):
    movies_information = [] # 최종적으로 모든 영화의 정보를 담은 list
    for movieCd in movieCd_list:
        URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={k}&movieCd={movieCd}'
        kobis_data = requests.get(URL).json()
        kobis_data = kobis_data['movieInfoResult']['movieInfo']
        a_movie_information = [] # 하나의 영화 정보를 담은 list
        genres_list = [] # 영화의 장르를 담을 list
    
        a_movie_information.append(kobis_data['movieCd'])     # 영화 대표 코드
        a_movie_information.append(kobis_data['movieNm'])     # 영화명(국문)
        a_movie_information.append(kobis_data['movieNmEn'])   # 영화명(영문)
        a_movie_information.append(kobis_data['movieNmOg'])   # 영화명(원문)
        a_movie_information.append(kobis_data['prdtYear'])    # 개봉연도
        a_movie_information.append(kobis_data['showTm'])      # 상영시간
    
        for genre in kobis_data['genres']:                    # 영화 장르
            genres_list.append(genre['genreNm'])
    
        genres = '/'.join(genres_list)
        a_movie_information.append(genres)
     
        a_movie_information.append(kobis_data['directors'][0]['peopleNm'])  # 감독명
        a_movie_information.append(kobis_data['audits'][0]['watchGradeNm']) # 관람등급
    
        for actor in range(len(kobis_data['actors'])):  # 영화 배우
            if actor == 3:
                break
            a_movie_information.append(kobis_data['actors'][actor]['peopleNm'])
        
        movies_information.append(a_movie_information)

    return movies_information

# 영화 상세 정보를 파일로 쓰는 함수
def write_detail_movie_information(file_name, movies_information):
    write_movies_information = open(file_name, 'w+', encoding='utf-8', newline='')

    # movie.csv의 첫 줄
    writer = csv.writer(write_movies_information)
    writer.writerow(['movie_code', 'movie_name_ko', 'movie_name_en', 'movie_name_og', 'prdt_year', 'show_time', 'genres', 'directors', 'watch_grade_nm', 'actor1', 'actor2', 'actor3'])

    for i in range(len(movies_information)):
        writer.writerow(movies_information[i])

    write_movies_information.close()

write_detail_movie_information('movie.csv', detail_movie_information(key, read_box_office('box_office.csv')))