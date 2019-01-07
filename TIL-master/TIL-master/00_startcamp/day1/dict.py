my_info = { 
    'name': 'neo',
    'job': 'hacker',
    'mobile': '01012345678',
    'email': 'neo@hphk.kr' 
}

hphk = [
    {
        'name': 'john',
        'email': 'john@hphk.io'
    },
    {
        'name': 'neo',
        'email': 'neo@hphk.io'
    },
    {
        'name': 'tak',
        'email': 'tak@hphk.io'
        'married': False
    }
]

type(hphk) # list

p = hphk[2]
p['name']

hphk[2]['name']