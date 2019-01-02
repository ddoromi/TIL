import requests
import random
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/push_my_number")
def push_my_number():
    return render_template('push_my_number.html')

@app.route("/get_lotto")
def get_lotto():
    draw_no = request.args.get('draw_no')
    
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'.format(draw_no)
    response = requests.get(url)
    lotto_data = response.json()
    
    real = []
    for key, value in lotto_data.items():
        if "drwtNo" in key:
            real.append(value)
    
    real_numbers = {'real' : real, 'bonus' : lotto_data['bnusNo']}
    my_numbers = [int(request.args.get('one')), int(request.args.get('two')), 
        int(request.args.get('three')), int(request.args.get('four')), int(request.args.get('five')), int(request.args.get('six'))]
    date = lotto_data['drwNoDate']
    
    if len(set(my_numbers) & set(real_numbers['real'])) == 6:
        result = '1등입니다.예~~~~~~~!!!!'
    
    elif len(set(my_numbers) & set(real_numbers['real'])) == 5 & real_numbers['bonus'] in my_numbers:
        result = '2등입니다.예~~~~~~~!!!!'
    
    elif len(set(my_numbers) & set(real_numbers['real'])) == 5:
        result = '3등입니다.예~~~~~~~!!!!'
    
    elif len(set(my_numbers) & set(real_numbers['real'])) == 4:
        result = '4등입니다. 예~~~~~~~~~~!!!!'
    
    else:
        result = '꽝꽈랑꽝꽝꽈랑꽝꽝꽝꽝'
        
    MY_CHAT_ID = '719740732'
    BOT_TOKEN = '750446548:AAHmBtnI9aeuo_YSSmdq844-6HZD3YzY39g'
    url = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, result)

    response = requests.get(url)
        
    return render_template('get_lotto.html', draw_no = draw_no, real_numbers = real_numbers['real'], bonus = real_numbers['bonus'], 
            my_numbers = my_numbers, result = result, date = date)
            
@app.route("/get_number")
def get_number():
    next_number = random.sample(range(1, 46), 6)
    
    MY_CHAT_ID = '719740732'
    BOT_TOKEN = '750446548:AAHmBtnI9aeuo_YSSmdq844-6HZD3YzY39g'
    url = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, next_number)
    response = requests.get(url)
    
    return render_template('get_number.html', next_number = next_number)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
