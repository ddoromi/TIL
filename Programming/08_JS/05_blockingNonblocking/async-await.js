const getUser = id => {
    const users = [{ id: 1, githubID: 'eduyu' }, { id: 2, githubID: 'edujohn' },];
    return new Promise((resolve, reject) => {
        setTimeout(()=>{
            const user = users.find(user => user.id === id);
            user ? resolve(user) : reject(new Error('Can not find'));
        }, 2000)
    });
};

const getRepos = user => {
    const repos = ['TIL', 'Workshop_HW', 'Python', 'JS'];
    return new Promise((resolve, reject) => {
        setTimeout(()=>{
            repos ? resolve(repos) : reject(new Error('Can not find'));
        }, 2000)
    });

};

const getCommits =  repo => {
    const commits = ['Init repo', 'Make index.html'];
    return new Promise((resolve, reject) => {
        setTimeout(()=> {
            if (commits) resolve(commits);
            else reject(new Error('ERRRRRRORRORRRR'));
        }, 2000)
    });
};

getUser(1)
    .then (user => getRepos(user))
    .then(repos => getCommits(repos[0]))
    .then(commits => getCommits(commits.length))
    .catch(error => console.error(error));

