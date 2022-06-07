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
from rasa_sdk.events import SlotSet
import json

file = open("./json/games.json")
data = json.load(file)

print(data)


class ActionShowTournament(Action):
    def name(self) -> Text:
        return "action_show_tournaments"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Calling {}".format(self.name()))

        tournaments = []
        for tournament in data["games"]:
            tournaments.append({"name": tournament["name"], "date": tournament["date"], "id": tournament["id"]})

        dispatcher.utter_message(text="Tournaments scheduled: {}".format(tournaments))

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
        for tournament in data["games"]:
            if tournament["id"] == tournament_id:
                dispatcher.utter_message(text="Players: {}".format(tournament["players"]))
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
        for tournament in data["games"]:
            if tournament["id"] == tournament_id:
                dispatcher.utter_message(text="Description: {}".format(tournament["description"]))
                found = True
                break

        if not found:
            dispatcher.utter_message(text="Could not find tournament with id: {}".format(tournament_id))

        return []

class ActionAddPlayerWithInfo(Action):
    def name(self) -> Text:
        return "action_add_player_with_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Calling {}".format(self.name()))

        name = next(tracker.get_latest_entity_values('name'))
        age = next(tracker.get_latest_entity_values('age'))
        tournament_id = next(tracker.get_latest_entity_values('kurwa'), "none")

        print(name)
        print(age)
        print(tournament_id)
        print(tracker.get_slot('kurwa'))

        dispatcher.utter_message(text="Adding player to tournament ")

        return []