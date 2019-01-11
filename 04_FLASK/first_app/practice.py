from flask import Flask

app = Flask(__name__)

@app.route('/dictionary/<string:word>')
def dictionary(word):
    my_dictionary = {
        'apple': '사과',
        'banana': '버내너',
        'cat': '고양이',
        'die': '죽다',
        'elephant': '코끼리',
        'father': '아빠'
    }
    if word in my_dictionary.keys():
        return f'{word}는 {my_dictionary[word]}!'
    else:
        return f'{word}는 나만의 단어장에 없는 단어입니다!'

if __name__ == '__main__':
     app.run(debug=True)