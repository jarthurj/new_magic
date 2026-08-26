import requests

# Required headers
headers = {
    'User-Agent': 'MagicDeckBuilder/1.0',
    'Accept': 'application/json'
}
url ='https://api.scryfall.com/cards/'
# Search for a card
card_id = "56ebc372-aabd-4174-a943-c7bf59e5028d"
response = requests.get(
    f'https://api.scryfall.com/cards/{card_id}',
    headers=headers
)

data = response.json()
# for x,y in data.items():
#     print(x,y)
print(data['prices'])

