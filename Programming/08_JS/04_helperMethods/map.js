// ES5 for loop
// var numbers = [1, 2, 3];
// var doubleNumbers = [];
//
// for (var i = 0; i < numbers.length; i ++) {
//     doubleNumbers.push(numbers[i] * 2)
// }
// console.log(doubleNumbers);

// ES6+
const numbers = [1, 2, 3];

function double(n) {
    return n * 2
}

const doubleNumbers = numbers.map(double);
const tripleNumbers = numbers.map(number => {
        return number * 3
});
console.log(doubleNumbers);
console.log(tripleNumbers);

const images = [
    {height: 34, width: 39},
    {height: 54, width: 19},
    {height: 34, width: 75},
];
const imageArea = images.map(image => {
    return image.height * image.width
});
console.log(imageArea);

/*
    아래의 pluck 함수를 완성하세요.
    pluck 함수는 배열과 요소 이름의 문자열을 받습니다.
 */

const paints = [
    {color: 'red'},
    {color: 'blue'},
    {color: 'white'},
    {smell: 'ughhhh'}
];
function pluck(array, property) {
    return array.map(arr => {
        if (arr[property]) {
            return arr[property]
        }
    });
}
console.log(pluck(paints, 'color'));
console.log(pluck(paints, 'smell'));
