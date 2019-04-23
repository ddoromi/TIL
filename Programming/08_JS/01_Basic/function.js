/*
    def my_function(arg1, arg2):
        ...
        return value

    func = lambda arg1, arg2: value
 */


// 1. 함수 키워드 정의
function add(num1, num2) {
    return num1 + num2;
}

// 2. 변수에 함수 로직 할당
const sub = function(num1, num2) {
    return num1 - num2;
};

// 3. 함수 표현식 2가지
const multi = function (num1, num2) {
    return num1 * num2;
};

/* step 1: function 키워드를 없앤다.
   step 2: ()와 {} 사이에 => 를 넣는다.
 */
const mul = (num1, num2) => {
    return num1 * num2;
};

/*
    step 1: 인자가 하나라면 괄호가 생략 가능하다.
    step 2: 함수 블록 안에 코드가 return 문 한 줄이라면, {} & return 키워드 삭제 가능하다.
 */
const square = num => num ** 2;
square(3);


let noArgs = () => {
    return 'nothing'
};

noArgs = () => 'nothing';
manyArgs = (a, b, c) => 'many';


// Default Args
function sayHello (name) {
    return `hi, ${name}!`
}

sayHello = name => `hi, ${name}`;

// 익명 함수 실행
(num => num ** 2)(4)