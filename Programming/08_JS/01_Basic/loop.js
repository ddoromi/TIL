let i = 0;

// while loop
while (i < 10) {
    console.log(i);
    i++;
}

// for loop
for (let j = 0; j < 10; j++) {
    console.log(j)
}

// for - of loop
let sum = 0;
for (let number of [1, 2, 3]) {
    sum += number
}
console.log(sum);
// console.log(number); loop를 나온 number는 잡히지 않음


for (const char of 'Happy') {
    console.log(char)
}