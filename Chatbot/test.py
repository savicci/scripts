import requests
from bs4 import BeautifulSoup

player = "Faker"
link = "https://en.wikipedia.org/wiki/List_of_esports_players"
wiki_link = "https://en.wikipedia.org"

res = requests.get(link)

if res.status_code != 200:
    print("Something broke")

parsed_html = BeautifulSoup(res.text)

## typ 2
wiki_player = parsed_html.body.find("a", string=player)
if wiki_player is None:
    print("Unfortunately {} is not on the list at {}".format(player, link))


player_link = wiki_link + wiki_player.attrs['href']
print("We found {}. Here is some more info about the player: {}".format(player, player_link))
