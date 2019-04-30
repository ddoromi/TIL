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

getUser(1)
    .then (user => getRepos(user))
    .then(repos => getCommits(repos[0]))
    .then(commits => getCommits(commits.length))
    .catch(error => console.error(error));

async function main () {
    try {
        const user = await getUser(1);
        const repos = await getRepos(user);
        const commits =  await getCommits(repos[0]);
        console.log(commits.length)
    } catch (e) {
        console.log(e)
    }
}


