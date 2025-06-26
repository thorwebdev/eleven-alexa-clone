import os
import signal
from eff_word_net.streams import SimpleMicStream
from eff_word_net.engine import HotwordDetector

from eff_word_net.audio_processing import Resnet50_Arc_loss

from eff_word_net import samples_loc

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation, ConversationInitiationData
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

convai_active = False

elevenlabs = ElevenLabs()
agent_id = "agent_01jynq02rjevdv9nr3zrqxa4mw" # os.getenv("AGENT_ID")
# Uncomment the line below if you want to create a new agent with end_call tool
# agent_id = create_agent_with_end_call_tool()
api_key = os.getenv("ELEVENLABS_API_KEY")

dynamic_vars = {
    'user_name': 'Thor',
    'greeting': 'Hey'
}

config = ConversationInitiationData(
    dynamic_variables=dynamic_vars
)

conversation = Conversation(
    # API client and agent ID.
    elevenlabs,
    agent_id,
    config=config,

    # Assume auth is required when API_KEY is set.
    requires_auth=bool(api_key),

    # Use the default audio interface.
    audio_interface=DefaultAudioInterface(),

    # Simple callbacks that print the conversation to the console.
    callback_agent_response=lambda response: print(f"Agent: {response}"),
    callback_agent_response_correction=lambda original, corrected: print(f"Agent: {original} -> {corrected}"),
    callback_user_transcript=lambda transcript: print(f"User: {transcript}"),
    # TODO: how to handle conversation ended by agent end_call system tool?
    
    # Uncomment if you want to see latency measurements.
    # callback_latency_measurement=lambda latency: print(f"Latency: {latency}ms"),
)

base_model = Resnet50_Arc_loss()

mycroft_hw = HotwordDetector(
    hotword="alexa",
    model = base_model,
    reference_file=os.path.join(samples_loc, "alexa_ref.json"),
    threshold=0.7,
    relaxation_time=2
)

mic_stream = SimpleMicStream(
    window_length_secs=1.5,
    sliding_window_secs=0.75,
)

mic_stream.start_stream()

print("Say Alexa ")
while True :
    if not convai_active:
        frame = mic_stream.getFrame()
        result = mycroft_hw.scoreFrame(frame)
        if result==None :
            #no voice activity
            continue
        if(result["match"]):
            print("Wakeword uttered",result["confidence"])
            # Start ConvAI Session
            print("Start ConvAI Session")
            convai_active = True
            conversation.start_session()
            signal.signal(signal.SIGINT, lambda sig, frame: conversation.end_session())
            conversation_id = conversation.wait_for_session_end()
            print(f"Conversation ID: {conversation_id}")
            convai_active = False
            print("Ready for next wake word...")