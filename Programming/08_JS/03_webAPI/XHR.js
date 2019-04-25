const DOMAIN = 'https://jsonplaceholder.typicode.com/';
const RESOURCE = 'posts';
const QUERY_STRING = '';
const URL = DOMAIN + RESOURCE + QUERY_STRING;

// req 대리인 XHR 객체 생성, XHR은 브라우저에만 사용 가능
const XHR = new XMLHttpRequest();

// XHR 요청발사 준비(method, url)

// 요청을 만들고, 정보를 담고, 보내고, 기다리고, 처리한다.
XHR.open('POST', URL);

XHR.setRequestHeader(
    'Content-Type',
    'application/json;charset=UTF-8'
);

// XHR 요청 발사
XHR.send(   // serializing => 받는 쪽에서 읽을 수 있도록 변환하는 과정
    JSON.stringify({"title": "NewPost", "body": "This is New Post", "userId": 1})
);

XHR.addEventListener('load', e => {
    const parseData = JSON.parse(e.target.response);    // 받는 쪽에서 읽기 위해 변환하는 과정
    console.log(parseData);
});

