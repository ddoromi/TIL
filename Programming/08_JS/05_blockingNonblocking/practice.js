const cities = [
    {id: 1, name: 'Seoul'},
    {id: 2, name: 'Daegu'},
    {id: 3, name: 'Gyeongju'}
];

const regions = [
    {city: 'Seoul', region: '역삼동'},
    {city: 'Daegu', region: '범어동'},
    {city: 'Gyeongju', region: '황성동'}
];

function getCity(id, callback) {
    setTimeout(() => {
        const city = cities.find(city => city.id === id);
        callback(city)
    }, 2000)
}

getCity(1, city => console.log(regions.find(region => region.city === city.name).region));
