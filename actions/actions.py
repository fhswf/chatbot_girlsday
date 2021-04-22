from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAnswerAge(Action):
    def name(self) -> Text:
        return "action_answer_age"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(f"message: {tracker.latest_message}")
        for ent in tracker.latest_message['entities']:
            if ent['entity'] == 'PER':
                dispatcher.utter_message(text=f"Das Alter von {ent['value']} muss ich nachsehen.")

        return []


CAPITALS = {
    "Deutschland": "Berlin",
    "USA": "Washington",
    "Frankreich": "Paris"
}

class ActionAnswerCapital(Action):
    def name(self) -> Text:
        return "action_answer_capital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(f"message: {tracker.latest_message}")
        for ent in tracker.latest_message['entities']:
            if ent['entity'] == 'LOC':
                country = ent['value']
                if country in CAPITALS:
                    dispatcher.utter_message(text=f"Die Hauptstadt von {country} ist {CAPITALS[country]}.")
                else:    
                    dispatcher.utter_message(text=f"Die Hauptstadt von {country} muss ich nachsehen.")

        return []