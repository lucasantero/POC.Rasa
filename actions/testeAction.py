# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionTeste(Action):
    def name(self) -> Text:
        return "action_teste"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = tracker.latest_message['text']

        input_data=tracker.latest_message
        first_name=tracker.latest_message["metadata"]["message"]["from"]["first_name"]
        last_name=tracker.latest_message["metadata"]["message"]["from"]["last_name"]
        username=tracker.latest_message["metadata"]["message"]["from"]["username"]

        #print(str(user_name))

        #response = requests.get("http://localhost:1337/TesteAPI/" + message)

        #dispatcher.utter_message(text=response.text)
        dispatcher.utter_message(text="Primeiro nome: " + str(first_name))
        dispatcher.utter_message(text="Ultimo nome: " + str(last_name))
        dispatcher.utter_message(text="Username: " + str(username))

        return []
