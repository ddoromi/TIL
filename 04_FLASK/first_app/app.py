import random
from flask import Flask, jsonify # list를 보내줌

app = Flask(__name__) # flask : class, 객체 생성

# /: 루트, 웹에서는 index(domain뒤에 아무것도 없을 때, 가장 상위 페이지)
@app.route('/') # 메서드 http://127.0.0.1:5000/ssafy host = 127.0.0.1, post = 5000 
def index():
    return 'HI'

@app.route('/ssafy') 
def ssafy():
    return 'sssssssafy'

# @app.route('/hi/ksr') #''안의 주소를 그대로 복붙해서 접속해야함.
# def hi():
#     return (f'hi ksr!')

@app.route('/hi/<string:name>') # <string:name> hi/뒤에 오는 변수를 str으로 바꿈
def hi(name):
    return (f'hi {name}!')

@app.route('/pick_lotto')
def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return jsonify(numbers)

if __name__ == '__main__':
     app.run(debug=True) # 기본인자가 **kargs이기 때문에 순서 상관 X

# 개발 환경으로 설정하기 => export FLASK_ENV='development'
# export : 환경 변수 설정
# route('/변수') : 길을 뚫어줌(라우팅), 변수가 있을 경우 => variable routing
# flask에서는 함수 호출을 따로 하지 않아도 호출 됨 => 접속하면 바로 정의된 함수가 실행 됨.
# 라우팅한 코드와 함수 정의 코드는 떨어지면 안됨