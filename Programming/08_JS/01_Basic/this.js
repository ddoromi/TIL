function hi() {

}

const bye = () => {

};

const me = {
    name: 'seongryeong',
    phone: '01012345678',
    email: '22.ryeong@gmail.com',
    intro: function () {
        return `Hi my name is ${this.name}`
    }
};

const name = 'ryeong';

const you = {
    name: 'seongryeong',
    phone: '01012345678',
    email: '22.ryeong@gmail.com',
    intro: () => {
        return `Hi your name is ${this.name}`
    },
    wait: function () {
        setTimeout(() => {
            console.log(this.email)
        }, 1000)
    }
};
console.log(me.intro());
console.log(you.wait());