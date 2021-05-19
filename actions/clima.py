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

class ActionClima(Action):
    def name(self) -> Text:
        return "action_clima"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        _api_key = "a9d78f0b1aef9609e958646f5c5ae8ab"
        print(tracker.latest_message["entities"])
        city_name = tracker.latest_message["entities"][0]["value"]
        _mainEndpoint = "http://api.openweathermap.org/data/2.5/"
        _cityNameSufix = "weather?q=" + city_name +"&appid=" + _api_key + "&units=metric"

        uri = _mainEndpoint + _cityNameSufix


        response = requests.get(uri)

        dispatcher.utter_message(text="Temperatura de " + str(response.json()["main"]["temp"]) + " graus em " + city_name)

        return []
