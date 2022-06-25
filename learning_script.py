import json
from typing import NoReturn
from dotenv import load_dotenv
from google.cloud import dialogflow
import argparse


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Create new Intent')
    parser.add_argument("--project-id", dest="project_id", help="Project id.Required.", required=True)
    parser.add_argument("--file-path", dest="training_phrases_file_path", help="Path to the file with training phrases.  Required.", required=True)
    args = parser.parse_args()

    training_phrases_file = load_training_phrases_file(args.training_phrases_file_path)
    for training_phrases in training_phrases_file:
        intent_title = training_phrases
        questions = training_phrases_file[training_phrases]['questions']
        answer = training_phrases_file[training_phrases]['answer']
        create_intent(args.project_id, intent_title, questions, answer)


def load_training_phrases_file(training_phrases_file_path: str) -> json:
    with open(training_phrases_file_path, 'r', encoding='utf-8') as file:
        training_phrases_file = json.load(file)
        return training_phrases_file


def create_intent(project_id: str, display_name: str, questions: list, answer: list) -> NoReturn:
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for question in questions:
        part = dialogflow.Intent.TrainingPhrase.Part(text=question)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=answer)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(display_name=display_name, training_phrases=training_phrases, messages=[message])
    request = dialogflow.CreateIntentRequest(parent=parent, intent=intent)
    response = intents_client.create_intent(request)

    print("Intent created: {}".format(response))


if __name__ == "__main__":
    main()
