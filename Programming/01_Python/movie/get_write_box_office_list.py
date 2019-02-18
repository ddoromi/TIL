import os, requests, csv

key = os.getenv("KOBIS_KEY")

# kobis에서 box_office 순위를 받아오는 함수
def get_box_office_list(key, targetDts):

    # 변수 목록 => movieCd: 영화 대표 코드, movieNm: 영화명(국문), 누적 관객 수: audiAcc, 날짜: targetDt
    box_office_list = []  # 최종으로 저장되는 Movie_data
    box_office_movie = {}  # 새로운 영화의 dictionary
   
    movie_saved = {}  # 영화 대표 코드와 누적 관객수만 저장된 dictionary(key : MovieCd, value : audiAcc)

    for targetDt in targetDts:
        URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0'
        box_office_data = requests.get(URL).json()
        box_office_data = box_office_data['boxOfficeResult']['weeklyBoxOfficeList']

        # 한 주의 Top 10 영화 목록 초기화.
        weekly_list = []

        # 한 주의 Top 10 movieCd를 저장함.
        for i in range(10):
            weekly_list.append(box_office_data[i]['movieCd'])
            
            # movie_saved에 없는 새로운 영화일 경우, box_office_list에 movieCd와 movieNm을 추가하고 다시 초기화 함.
            if box_office_data[i]['movieCd'] not in list(movie_saved.keys()):
                box_office_movie['movieCd'] = box_office_data[i]['movieCd']
                box_office_movie['movieNm'] = box_office_data[i]['movieNm']
                box_office_list.append(box_office_movie)
                box_office_movie = {}

            # movie_saved에 있던 영화의 audiAcc를 최신 data로 바꾸고, 새로운 영화일 경우 movieCd와 audiAcc가 추가됨.
            movie_saved[box_office_data[i]['movieCd']] = box_office_data[i]['audiAcc']

        # box_office_list 영화 중 weekly_list에 있는 영화만 audiAcc와 targetDt를 최신 data로 바꿔줌.
        for j in range(len(box_office_list)):
            if box_office_list[j]['movieCd'] in weekly_list:
                box_office_list[j]['audiAcc'] = movie_saved[box_office_list[j]['movieCd']]
                box_office_list[j]['targetDt'] = targetDt

    return box_office_list


# box_office_list를 받아 파일로 쓰는 함수
def write_box_office_list(box_office_list):
    write_box_office = open('box_office.csv', 'w+', encoding='utf-8', newline='') #w+는 덮어씀, a+는 추가

    # boxoffice.csv의 첫 줄
    writer = csv.writer(write_box_office)
    writer.writerow(['movie_code', 'title', 'audience', 'recoded_at'])

    for i in range(len(box_office_list)):
        writer.writerow(
            [box_office_list[i]['movieCd'], box_office_list[i]['movieNm'], box_office_list[i]['audiAcc'], box_office_list[i]['targetDt']] 
        )
    write_box_office.close()

print(key)
targetDts = ['20181111', '20181118', '20181125', '20181202', '20181209', '20181216', '20181223', '20181230', '20190106', '20190113']
write_box_office_list(get_box_office_list(key, targetDts))