/* 1. <input> 태그 안의 값을 잡는다. */
const inputArea = document.querySelector('#js-userinput');
const button = document.querySelector('#js-go');
const resultArea = document.querySelector('#result-area');


// inputArea.addEventListener('keydown', e => {
//     if (e.code === 'Enter') {
//         searchAndPush(inputArea.value);
//     }
// });
// button.addEventListener('click', e => {
//     searchAndPush(inputArea.value);
// });


// /* 2. Giphy API 를 통해 data 를 받아서 가공한다. */
// const KEY = 'QWmTtS4LpA2lSE6YNdxxVIxluUMAUyRo';
// let keyword = 'nirvana';
// const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${KEY}`;
// console.log(URL);
//
// /*
// 기존의 요청
// 1. 링크를 누른다
// 2. href로 요청이 간다.
// 3. 브라오다 새로고침 되며, 응답을 render 한다
//
//  AJAX 요청
//  1. 어떤 event가 발생한다.
//  2. 요청을 전송하고, 응답이 도착할 때까지 기다린다. 화면 전환은 없다.
//  3. 응답이 오면, 지금 화면에서 응답 내용을 추가로 render 한다.
//  */
//
// const AJAXCall = new XMLHttpRequest() ;  // AJAX 요청을 보낼 함수
// AJAXCall.open('GET', URL);
// AJAXCall.send();
// AJAXCall.addEventListener('load', e => {
//     const parseData = JSON.parse(e.target.response);
//     pushToDOM(parseData)
// });
//
//
// /* 3. GIF 파일들을 index.html(DOM)에 밀어 넣어서 보여준다. */
// const pushToDOM = data => {
//     const dataArray = data.data;
//     let imgURL;
//     for (const imgData of dataArray) {
//         imgURL = imgData.images.fixed_height.url;
//         resultArea.innerHTML += `<img src="${imgURL}">`
//     }
// };


inputArea.addEventListener('keydown', e => {
    if (e.code === 'Enter') {
        searchAndPush(inputArea.value);
    }
});
button.addEventListener('click', e => {
    searchAndPush(inputArea.value);
});

const searchAndPush = keyword => {
    const KEY = 'pETal56SsBpImEECWh6AcSOUlSZfg7zU';
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${KEY}`;

    const AJAXCall = new XMLHttpRequest(); // AJAX 요청을 보내줄 친구
    AJAXCall.open('GET', URL); // 요청을 발사할 준비
    AJAXCall.send(); // 발사!
    AJAXCall.addEventListener('load', e => { // load 를 기다리며.. res 가 오면,
        const parseData = JSON.parse(e.target.response);
        pushToDOM(parseData);
    });

    const pushToDOM = dataset => {
        resultArea.innerHTML = null;    // 기존의 img 다 날리고 다시 시작한다.
        const dataArray = dataset.data;
        let element, imageURL;

        for (const imgData of dataArray) {
            imageURL = imgData.images.fixed_height.url;
            element = document.createElement('img');   // <img >
            element.classList.add('container-image');             // <img class = "">
            element.src = imageURL;
            resultArea.appendChild(element);
        }
    };
};