from typing import Union
from typing import NoReturn
from google.cloud import dialogflow


def detect_intent_texts(project_id: str, session_id: str, text, type_bot: str) -> Union[str, NoReturn]:
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code="ru")
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
    if type_bot == "vk":
        if not response.query_result.intent.is_fallback:
            return response.query_result.fulfillment_text
    else:
        return response.query_result.fulfillment_text
