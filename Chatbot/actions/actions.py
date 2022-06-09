# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from bs4 import BeautifulSoup
import requests

link = "https://en.wikipedia.org/wiki/List_of_esports_players"
wiki_link = "https://en.wikipedia.org"

games_file = open("./json/games.json")
games_data = json.load(games_file)

links_file = open("./json/links.json")
links_data = json.load(links_file)


class ActionShowTournament(Action):
    def name(self) -> Text:
        return "action_show_tournaments"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Calling {}".format(self.name()))

        tournaments = []
        for tournament in games_data["games"]:
            tournaments.append({"name": tournament["name"], "date": tournament["date"], "id": tournament["id"]})

        dispatcher.utter_message(text="Tournaments scheduled: {}".format(json.dumps(tournaments, indent=2)))

        return []


class ActionShowTournamentPlayers(Action):
    def name(self) -> Text:
        return "action_show_tournament_players"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Calling {}".format(self.name()))
        tournament_id = next(tracker.get_latest_entity_values('tournament_id'), "none")

        found = False
        for tournament in games_data["games"]:
            if tournament["id"] == tournament_id:
                dispatcher.utter_message(text="Players: {}".format(json.dumps(tournament["players"], indent=2)))
                found = True
                break

        if not found:
            dispatcher.utter_message(text="Could not find tournament with id: {}".format(tournament_id))

        return []


class ActionShowTournamentDescription(Action):
    def name(self) -> Text:
        return "action_show_tournament_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Calling {}".format(self.name()))
        tournament_id = next(tracker.get_latest_entity_values('tournament_id'), "none")

        found = False
        for tournament in games_data["games"]:
            if tournament["id"] == tournament_id:
                dispatcher.utter_message(text="Description: {}".format(tournament["description"]))
                found = True
                break

        if not found:
            dispatcher.utter_message(text="Could not find tournament with id: {}".format(tournament_id))

        return []

class ActionShowEsportLinks(Action):
    def name(self) -> Text:
        return "action_show_esport_links"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Calling {}".format(self.name()))

        dispatcher.utter_message(
            text="Cool, here is some e-sport links: {}\n Hope you have fun".format(json.dumps(links_data, indent=2)))

        return []


class ActionShowPlayerOnList(Action):
    def name(self) -> Text:
        return "action_show_player_on_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Calling {}".format(self.name()))

        player_nickname = next(tracker.get_latest_entity_values('player_nickname'), "none")

        res = requests.get(link)

        if res.status_code != 200:
            dispatcher.utter_message(text="Woops, looks like something is broken. Try later")

        parsed_html = BeautifulSoup(res.text)

        dispatcher.utter_message(text="According to {}\n".format(wiki_link))
        wiki_player = parsed_html.body.find("a", string=player_nickname)
        if wiki_player is None:
            dispatcher.utter_message(text="Unfortunately {} is not on the list".format(player_nickname))
            return []

        player_link = wiki_link + wiki_player.attrs['href']
        dispatcher.utter_message(text="We found {}.\nHere is some more info about the player: {}".format(player_nickname, player_link))

        return []
