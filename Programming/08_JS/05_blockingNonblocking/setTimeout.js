const sleep_3s = () => {
    console.log('Invoke');
    setTimeout(() => {
       console.log('Wake Up!')
    }, 3000);
};

console.log('start');
sleep_3s();
console.log('End of Program');
 