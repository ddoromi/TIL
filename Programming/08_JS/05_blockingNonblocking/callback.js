// function listUsers() {
//     setTimeout(() => {
//         const users = [
//             { id: 1, githubID: 'ryeong' },
//             { id: 2, githubID: 'eduyu' }
//         ];
//     }, 2000)
// }

// 비동기적 요소가 있을 경우 return 값은 쓸 수 없으므로 함수를 인자로 받아 return 해줄 값을 넘겨서 실행해야 함.
function getUser(id, callback) {
    setTimeout(()=>{
        const users = [
            { id: 1, githubID: 'eduyu' },
            { id: 2, githubID: 'edujohn' },
        ];
        const user = users.find(user => user.id === id);
        console.log('Data Loaded!');
        console.log(user);
        callback(user);
    }, 2000)
}

const getRepos = (user, callback) => {
    setTimeout(()=>{
        const repos = [
            'TIL',
            'Workshop_HW',
            'Python',
            'JS'
        ];
        console.log('Data Loaded');
        console.log(repos);
        callback(repos)
    }, 2000)
};

function getCommits (repo, callback) {
    setTimeout(()=>{
        const commits = [
            'Init repo',
            'Make index.html'
        ];
        console.log('Data Loaded!');
        console.log(commits);
        callback(commits);
    }, 2000)
}

getUser(1, user => {
    getRepos(user, repos => {
        getCommits(repos[0], commits => {
            console.log(`${commits.length} 개 커밋을 했네요!`)
        })
    })
});


// user = getUser(1);
// repos = getRepos(user);
// commits = getCommits(repos[0])