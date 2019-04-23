// 변수명에 띄어쓰기가 있을 경우 ''로 묶어주지만 그렇지 않은 경우에는 쓰지 않음.
// object 경우, 끝에 ';'를 붙임. cf) for, if, while, function 인 경우에는 붙이지 않음.
const me = {
    name: 'ddorom',
    number: '01029806198',
    product: {
        phone: 'LG G7',
        lapTop: 'Asus',
    }
};

me.name === me['name']; // ddorom
me.product;             // {phone: "LG G7", lapTop: "Asus"}
me.product.phone;       // LG G7

