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
        return "action_arquivo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        anexo = {"document": "C:\Produtos\POC.Rasa\data\cidades.txt"}
        #dispatcher.utter_message(text="Username: " + str(username))
        dispatcher.utter_message(json_message=anexo)

        return []
