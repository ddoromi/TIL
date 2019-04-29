// ES5 for loop
// var products = [
//     {name: 'cucumber', type: 'vege',},
//     {name: 'banana', type: 'fruit',},
//     {name: 'carrot', type: 'vege',},
//     {name: 'melon', type: 'fruit',},
// ];
// var friuts = [];
//
// for (var i = 0; i < products.length; i ++) {
//     if (products[i].type === 'fruit') {
//         fruits.push(products[i])
//     }
// }


// ES6+
const products = [
    {name: 'cucumber', type: 'vege',},
    {name: 'banana', type: 'fruit',},
    {name: 'carrot', type: 'vege',},
    {name: 'melon', type: 'fruit',},
];

const fruits = products
    .filter(product => product.type === 'fruit')
    .map(wowthis => wowthis.name);
console.log(fruits);

const users = [
    { id: 1, admin: true },
    { id: 2, admin: false },
    { id: 3, admin: false },
    { id: 4, admin: true },
    { id: 5, admin: false }
];

const adminUsers = users
    .filter(user => user.admin)
    .map(user => user.id);
console.log(adminUsers);
