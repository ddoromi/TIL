// json-server 의 기본 접속 URI 는 아래와 같습니다. 필요에 따라 수정 가능합니다.
const HOST = "http://localhost:3000";

const app = new Vue({
    el: "#app",
    data: {
        logo: 'MO<i class="fab fa-vuejs"></i>IE',
        isMain: true,
        genres: [],
        movies: [],
        search: '', // 검색 기능을 구현할 때, 사용자의 입력 값을 이곳에 쌍방향 바인딩 합니다.
        isDetail: false, // 현재 방식의 목록/상세 화면 전환에 사용되는 flag 입니다.
        movieDetail: {},  // 상세 화면에서 출력할 때 사용할 영화 객체입니다.
        scores: [],
        inputScore: {
            content: '',
            score: null,
            movieId: null
        },
    },
    methods: {
        async getMovies (genreId=null) {
            const URL = genreId ? `${HOST}/genres/${genreId}/movies` : `${HOST}/movies`;
            const res = await axios.get(URL);
            this.movies = res.data;
        },
        async toggleDetail (id = null) {  // 목록 <=> 상세 화면을 전환합니다. 인자로 id 가 들어올 경우, 상세화면을 표시합니다.
            if (id) {
                // 갱신된 데이터 새로 받아서 가져오기
                // const res = await axios.get(`${HOST}/movies/${id}`);
                // this.movieDetail = res.data;
                this.movieDetail = this.movies.find(movie => movie.id === id);
                const res = await axios.get(`${HOST}/movies/${id}/scores`);
                this.scores = res.data;

            }
            this.isDetail = !this.isDetail
        },
        async postScore(movieId) {
            function getAverageScore(scores) {
                const sum = 0;
                const result = scores.reduce((acc, score) => {
                    acc.total += score.score;
                    acc.count++;
                    return acc
                }, {total: 0, count: 0} );
                return (result.total / result.count).toFixed(3)
            }
            if(this.inputScore.score && this.inputScore.content) {
                this.inputScore.movieId = movieId;
                let res = await axios.post(`${HOST}/scores`, this.inputScore);
                const newScore = res.data;
                this.inputScore = { content: '', score: null, };
                this.scores.push(newScore);
                res = await axios.patch(`${HOST}/movies/${movieId}`, { averageScore: getAverageScore(this.scores)});
                this.movieDetail = res.data;
            } else {
                alert('평점을 남겨주세요.')
            }
        },
    },
    computed: {},

    watch: {
        async search(keyword) {
            if (keyword) {
                const res = await axios.get(`${HOST}/movies?q=${keyword}`);
                this.movies = res.data;
            } else {
                this.movies = []
            }
        },
        async movies () {
            this.isDetail = false;
        }
    },
    // Vue instance LIFE CYCLE
    async created() {
        const res = await axios.get(`${HOST}/genres`);
        this.genres = res.data;
    }

});

document.addEventListener('keyup',e => {
    if (e.key === 'Escape') app.$data.isDetail = false
});
