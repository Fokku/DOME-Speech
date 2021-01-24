import IdentificationServiceHttpClientHelper
import sys
import time
try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-python for
    installation instructions.
    """)
    sys.exit(1)


# Set up the subscription info for the Speech Service:
# Replace with your own subscription key and service region (e.g., "westus").
speech_key = "bf44683205864acfb4b415fb8585b6ad"
speech_key_westus = "f3aa638bcf6b4f839a153c4cfcfdca68"
service_region = "southeastasia"
event = ""

# Specify the path to an audio file containing speech (mono WAV / PCM with a sampling rate of 16
# kHz).


def speech_recognize_continuous_from_file(filename):
    """performs continuous speech recognition with input from an audio file"""
    # <SpeechContinuousRecognitionWithFile>
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = speechsdk.audio.AudioConfig(filename=filename)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    done = False

    def recognized_cb(evt):
        global event
        if evt.result.text.startswith(event):
            event = evt.result.text
        else:
            event += " {}".format(evt.result.text)

        #print('RECOGNIZED: {}'.format(evt))

    def isstopped(evt):
        global stopped
        stopped = True

    def stop_cb(evt):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        nonlocal done
        done = True

    # Connect callbacks to the events fired by the speech recognizer
    #speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    speech_recognizer.recognized.connect(recognized_cb)
    #speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(isstopped)
    speech_recognizer.canceled.connect(isstopped)
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)
    speech_recognizer.stop_continuous_recognition()
    return event
    # </SpeechContinuousRecognitionWithFile>

def identify_file(file_path, force_short_audio, profile_ids):
    """Identify an audio file on the server.

    Arguments:
    subscription_key -- the subscription key string
    file_path -- the audio file path for identification
    profile_ids -- an array of test profile IDs strings
    force_short_audio -- waive the recommended minimum audio limit needed for enrollment
    """
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        speech_key_westus)

    identification_response = helper.identify_file(
        file_path, profile_ids,
        force_short_audio.lower() == "true")

    print('Identified Speaker = {0}'.format(identification_response.get_identified_profile_id()))
    print('Confidence = {0}'.format(identification_response.get_confidence()))
    print('Profiles Ranking = {0}'.format(identification_response.get_profiles_ranking()))
    return identification_response.get_identified_profile_id()