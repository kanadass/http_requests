import requests


url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
resp_json = response.json()
most_intelligence = -1
biggest_brain = ''
for hero in resp_json:
    if hero['name'] in ['Hulk', 'Captain America', 'Thanos']:
        if hero['powerstats']['intelligence'] > most_intelligence:
            most_intelligence = hero['powerstats']['intelligence']
            biggest_brain = hero['name']
print(f'Самый умный супергерой: {biggest_brain}')



