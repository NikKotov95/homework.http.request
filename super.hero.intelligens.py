import requests

TOKEN = '2619421814940190'


urls = [
    f'https://superheroapi.com/api.php/{TOKEN}/search/character-id/Hulk',
    f'https://superheroapi.com/api.php/{TOKEN}/search/character-id/Thanos',
    f'https://superheroapi.com/api.php/{TOKEN}/search/character-id/Captain&America',
]

# Функция для принятия списка адресов

def request_get(url_all):
    r = (request_get(url) for url in url_all)
    return r

# Функция для сбора информации о интеллектах супергероев

def parser():
    super_man = []
    for item in request_get(urls):
        intelligence = item.json()
        for power_stats in intelligence['results']:
            super_man.append({
                'name': power_stats['name'],
                'intelligence': power_stats['power_stats']['intelligence']
            })

# Сравниваем игтеллекты героев

intelligence_hero = 0
super_man = {}
for intel_hero in super_man['name']:
    if intelligence_hero < int(intel_hero['intelligence']):
        intelligence_hero = int(intel_hero['intelligence'])
        name = intel_hero['name']
print(f"Самый интеллектуальный {namegit commit .}, интеллект: {intelligence_hero}")

parser()
