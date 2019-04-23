// { "a": "A" }
const myObject = {
    coffee: 'Americano',
    iceCream: 'Soft Milk IceCream',
};


const jsonData = JSON.stringify(myObject);  // json object 를 string 으로 바꿔줌
console.log(typeof jsonData);               // string

const parseData = JSON.parse(jsonData);     // json 형식을 갖춘 data 를 string 으로 바꿈
console.log(typeof parseData);             // json