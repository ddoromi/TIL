// ES5 for loop
// var avengers = [
//     {name: 'Tony Stark'},
//     {name: 'Steve Rogers'},
//     {name: 'Thor'}
// ];
//
// var avenger;
//
// for (var i = 0; i < avengers.length; i ++) {
//     if (avengers[i] === 'Tony Stark') {
//         avenger = avengers[i];
//         break
//     }
// }

// ES6+
const avengers = [
    {name: 'Tony Stark'},
    {name: 'Steve Rogers'},
    {name: 'Thor'}
];
const a = avengers.find(avenger => avenger.name === 'Tony Stark');
console.log(a);