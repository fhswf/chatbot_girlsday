# Demo-Chatbot für den Girls'Day 2021

Dies ist ein kleiner Demo-Chatbot auf Basis von [Rasa](https://rasa.com/). 

Neben einer einfach gehaltenen Begrüßung unterstützt er
- Fragen nach Hauptstädten von Ländern,
- Fragen nach dem Alter von Personen.

Die Erkennung der Entitäten erfolgt dabei mithilfe von [SpaCy](https://spacy.io/).
Die Custom-Actions zur Beantwortung der Wissensfragen können noch ausimplementiert werden (etwa über eine SPARQL Query gegen WikiData).
