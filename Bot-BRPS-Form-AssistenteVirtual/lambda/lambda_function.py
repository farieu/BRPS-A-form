# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


PHYSICALHEALTH_QUESTIONS = [
    "Como costuma ser sua saúde física?",
    "Como esteve sua saúde no último ano?",
    "Você está preocupado com algum problema de saúde agora?",
    "Você sente que tem alguma coisa incomum acontecendo com seu corpo ou cabeça?"
]

ANXIETY_QUESTIONS = [
    "Você está preocupado com alguma coisa?",
    "Você tem se sentido tenso ou ansioso a maior parte do tempo?",
    "Quando se sente assim, você consegue saber o porquê?",
    "De que forma suas ansiedades ou preocupações afetam o seu dia a dia?",
    "Existe algo que ajuda a melhorar essa sensação?"
]

SUPERIORITYCOMPLEX_QUESTIONS = [
    "Nos últimos dias você tem se sentido com algum talento ou habilidade que a maioria das pessoas não tem?",
    "Como você sabe disso?",
    "Você acha que as pessoas têm tido inveja de você?", 
    "Você tem acreditado que tenha alguma coisa importante para fazer no mundo?"
]

MOODISSUES_QUESTIONS = [
    "Como tem estado seu humor?",
    "Você acredita que pode melhorar?", 
    "Como esse sentimento tem afetado seu dia a dia?"
]

HOSTILITY_QUESTIONS = [
    "Nos últimos dias você tem estado impaciente ou irritável com as outras pessoas?", 
    "Conseguiu manter o controle?", 
    "Tolerou as provocações?",
    "Chegou a agredir alguém ou quebrar objetos?"
]

MISTRUST_QUESTIONS = [
    "Você tem tido a impressão de que as outras pessoas estão falando ou rindo de você?", 
    "De que forma você percebe isso?", 
    "Você tem achado que tem alguém com más intenções contra você ou se esforçado para lhe causar problemas?",
    "Quem? Por quê? Como você sabe disso?"
]

HALLUCINATIONS_QUESTIONS = [
    "Você tem tido experiências incomuns que a maioria das pessoas não tem?",
    "Você tem escutado coisas que as outras pessoas não podem ouvir?",
    "Você estava acordado nesse momento?", 
    "O que você ouvia - barulhos, cochichos, vozes conversando com você ou conversando entre si?",
    "Com que frequência?" ,
    "Interferem no seu dia a dia?", 
    "Você tem visto coisas que a maioria das pessoas não pode ver?", 
    "Você estava acordado nesse momento?",
    "O que você via - luzes, formas, imagens?",
    "Com que frequência?",
    "Essas coisas interferem no seu dia a dia?"
]

DELUSIONS_QUESTIONS = [
    "Você tem acreditado que alguém ou alguma coisa fora de você esteja controlando seus pensamentos ou suas ações contra a sua vontade?",
    "Você tem a impressão de que o rádio ou a televisão mandam mensagens para você?",
    "Você sente que alguma coisa incomum esteja acontecendo ou está para acontecer?"
]

DISORIENTATION_QUESTIONS = [
    "Qual seu nome completo?",
    "E sua idade?", 
    "Onde você mora?",
    "Está trabalhando atualmente?",
    "Já trabalhou anteriormente?", 
    "Em quê?", 
    "Quanto tempo faz que você está aqui?",
    "Por que motivo você foi internado?", 
    "Quando isso começou?",
    "O que aconteceu depois?",
    "Você pode me dizer que dia é hoje?",
    "Você tem conseguido se concentrar?",
    "Como está sua memória?",
    "Você pode me dizer que dia é hoje?", 
    "Você pode me dizer o que tinha ontem no jantar?"
]

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Bem-vindo ao Virtual Health. Vamos começar! Qual o seu nome?"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class NameIntentRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("InformNameIntent")(handler_input)
    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        name = slots["name"].value if "name" in slots else None
        if name:
            session_attributes = handler_input.attributes_manager.session_attributes
            session_attributes["name"] = name
            handler_input.attributes_manager.session_attributes = session_attributes
            speech_text = f"Olá, {name}! Qual é a sua idade?"
            reprompt_text = "Por favor, diga sua idade."
            handler_input.response_builder.speak(speech_text).ask(reprompt_text)
        else:
            speech_text = "Desculpe, não consegui obter seu nome. Por favor, diga novamente."
            reprompt_text = "Por favor, diga seu nome."
            handler_input.response_builder.speak(speech_text).ask(reprompt_text)
        return handler_input.response_builder.response


class AgeIntentRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("InformAgeIntent")(handler_input)
    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        age = slots["age"].value if "age" in slots else None
        if age:
            session_attributes = handler_input.attributes_manager.session_attributes
            session_attributes["age"] = age
            handler_input.attributes_manager.session_attributes = session_attributes
            speech_text = f"Certo. Vamos falar de saúde física."
            handler_input.response_builder.speak(speech_text).ask(speech_text)
        else:
            speech_text = "Desculpe, não consegui obter sua idade. Por favor, diga novamente."
            handler_input.response_builder.speak(speech_text).ask(speech_text)
        return PhysicalHealthRequestHandler().handle(handler_input)


class PhysicalHealthRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("InformPhysicalHealthIntent")(handler_input)
    def handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        if 'physical_health_index' not in session_attributes:
            session_attributes['physical_health_index'] = 0
        physical_health_index = session_attributes['physical_health_index']
        if physical_health_index < len(PHYSICALHEALTH_QUESTIONS):
            question = PHYSICALHEALTH_QUESTIONS[physical_health_index]
            speech_text = question
            reprompt_text = question
            session_attributes['physical_health_index'] += 1
            handler_input.attributes_manager.session_attributes = session_attributes
            return handler_input.response_builder.speak(speech_text).ask(reprompt_text).response
        return AnxietyRequestHandler().handle(handler_input)

class AnxietyRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("InformAnxietyIntent")(handler_input)
    def handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        if 'anxiety_index' not in session_attributes:
            session_attributes['anxiety_index'] = 0
        anxiety_index = session_attributes['anxiety_index']
        if anxiety_index < len(ANXIETY_QUESTIONS):
            question = ANXIETY_QUESTIONS[anxiety_index]
            speech_text = question
            reprompt_text = question
            session_attributes['anxiety_index'] += 1
            handler_input.attributes_manager.session_attributes = session_attributes
            return handler_input.response_builder.speak(speech_text).ask(reprompt_text).response
        return SuperiorityComplexRequestHandler().handle(handler_input)

class SuperiorityComplexRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        superiority_index = session_attributes.get('superiority_index', 0)
        return ask_utils.is_intent_name("InformSuperiorityIntent")(handler_input) and superiority_index< len(SUPERIORITYCOMPLEX_QUESTIONS)

    def handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        if 'superiority_index' not in session_attributes:
            session_attributes['superiority_index'] = 0
        superiority_index = session_attributes['superiority_index']
        if superiority_index < len(SUPERIORITYCOMPLEX_QUESTIONS):
            question = SUPERIORITYCOMPLEX_QUESTIONS[superiority_index]
            speech_text = question
            reprompt_text = question
            session_attributes['superiority_index'] += 1
            handler_input.attributes_manager.session_attributes = session_attributes
            return handler_input.response_builder.speak(speech_text).ask(reprompt_text).response
        return MoodIssuesRequestHandler().handle(handler_input)

class MoodIssuesRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        mood_index = session_attributes.get('mood_index', 0)
        return ask_utils.is_intent_name("InformMoodIntent")(handler_input) and mood_index < len(MOODISSUES_QUESTIONS)

    def handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        if 'mood_index' not in session_attributes:
            session_attributes['mood_index'] = 0
        mood_index = session_attributes['mood_index']
        if mood_index < len(MOODISSUES_QUESTIONS):
            question = MOODISSUES_QUESTIONS[mood_index]
            speech_text = question
            reprompt_text = question
            session_attributes['mood_index'] += 1
            handler_input.attributes_manager.session_attributes = session_attributes
            return handler_input.response_builder.speak(speech_text).ask(reprompt_text).response
        return HostilityRequestHandler().handle(handler_input)

class HostilityRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        hostility_index = session_attributes.get('hostility_index', 0)
        return ask_utils.is_intent_name("InformHostilityIntent")(handler_input) and hostility_index < len(HOSTILITY_QUESTIONS)

    def handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        if 'hostility_index' not in session_attributes:
            session_attributes['hostility_index'] = 0
        hostility_index = session_attributes['hostility_index']
        if hostility_index < len(HOSTILITY_QUESTIONS):
            question = HOSTILITY_QUESTIONS[hostility_index]
            speech_text = question
            reprompt_text = question
            session_attributes['hostility_index'] += 1
            handler_input.attributes_manager.session_attributes = session_attributes
            return handler_input.response_builder.speak(speech_text).ask(reprompt_text).response
        return MistrustRequestHandler().handle(handler_input)

class MistrustRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        mistrust_index = session_attributes.get('mistrust_index', 0)
        return ask_utils.is_intent_name("InformMistrustIntent")(handler_input) and mistrust_index < len(MISTRUST_QUESTIONS)

    def handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        if 'mistrust_index' not in session_attributes:
            session_attributes['mistrust_index'] = 0
        mistrust_index = session_attributes['mistrust_index']
        if mistrust_index < len(MISTRUST_QUESTIONS):
            question = MISTRUST_QUESTIONS[mistrust_index]
            speech_text = question
            reprompt_text = question
            session_attributes['mistrust_index'] += 1
            handler_input.attributes_manager.session_attributes = session_attributes
            return handler_input.response_builder.speak(speech_text).ask(reprompt_text).response
        return HallucinationsRequestHandler().handle(handler_input)

class HallucinationsRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        hallucinations_index = session_attributes.get('hallucinations_index', 0)
        return ask_utils.is_intent_name("InformHallucinationsIntent")(handler_input) and hallucinations_index < len(HALLUCINATIONS_QUESTIONS)

    def handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        if 'hallucinations_index' not in session_attributes:
            session_attributes['hallucinations_index'] = 0
        hallucinations_index = session_attributes['hallucinations_index']
        if hallucinations_index < len(HALLUCINATIONS_QUESTIONS):
            question = HALLUCINATIONS_QUESTIONS[hallucinations_index]
            speech_text = question
            reprompt_text = question
            session_attributes['hallucinations_index'] += 1
            handler_input.attributes_manager.session_attributes = session_attributes
            return handler_input.response_builder.speak(speech_text).ask(reprompt_text).response
        return DelusionsRequestHandler().handle(handler_input)

class DelusionsRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        delusions_index = session_attributes.get('delusions_index', 0)
        return ask_utils.is_intent_name("InformDelusionsIntent")(handler_input) and delusions_index < len(DELUSIONS_QUESTIONS)

    def handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        if 'delusions_index' not in session_attributes:
            session_attributes['delusions_index'] = 0
        delusions_index = session_attributes['delusions_index']
        if delusions_index < len(DELUSIONS_QUESTIONS):
            question = DELUSIONS_QUESTIONS[delusions_index]
            speech_text = question
            reprompt_text = question
            session_attributes['delusions_index'] += 1
            handler_input.attributes_manager.session_attributes = session_attributes
            return handler_input.response_builder.speak(speech_text).ask(reprompt_text).response
        return DisorientationRequestHandler().handle(handler_input)

class DisorientationRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        disorientation_index = session_attributes.get('disorientation_index', 0)
        return ask_utils.is_intent_name("InformDisorientationIntent")(handler_input) and delusions_index < len(DISORIENTATION_QUESTIONS)

    def handle(self, handler_input):
        session_attributes = handler_input.attributes_manager.session_attributes
        if 'disorientation_index' not in session_attributes:
            session_attributes['disorientation_index'] = 0
        disorientation_index = session_attributes['disorientation_index']
        if disorientation_index < len(DISORIENTATION_QUESTIONS):
            question = DISORIENTATION_QUESTIONS[disorientation_index]
            speech_text = question
            reprompt_text = question
            session_attributes['disorientation_index'] += 1
            handler_input.attributes_manager.session_attributes = session_attributes
            return handler_input.response_builder.speak(speech_text).ask(reprompt_text).response
        return handler_input.response_builder.response

class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(NameIntentRequestHandler())
sb.add_request_handler(AgeIntentRequestHandler())
sb.add_request_handler(PhysicalHealthRequestHandler())
sb.add_request_handler(AnxietyRequestHandler())
sb.add_request_handler(SuperiorityComplexRequestHandler())
sb.add_request_handler(MoodIssuesRequestHandler())
sb.add_request_handler(HostilityRequestHandler())
sb.add_request_handler(MistrustRequestHandler())
sb.add_request_handler(HallucinationsRequestHandler())
sb.add_request_handler(DelusionsRequestHandler())
sb.add_request_handler(DisorientationRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()