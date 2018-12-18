import webbrowser #선언은 앞에

keywords = [
    'george',
    'monni'
]

for keyword in keywords:
    url = 'https://www.google.com/search?q=' + keyword
    webbrowser.open_new(url)

