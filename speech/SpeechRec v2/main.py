import os
import time
import recognizer
import socketServer
import json
try:
    #from sense_hat import SenseHat
    pass
except ImportError:
    print("Import Error, try: pip install sense_hat")

server = socketServer.server()

savedSet = set()
nameSet = set()
path = r"C:\Users\19022874\Desktop\C200\C200 Voice System\Audio"
profileids = ["8b126ce5-0281-4b07-b66d-c0a7e576da2e", "daa14ddb-662f-4848-a2c7-1f0eb3dacaf1", "aef0f65d-abf5-4027-bed0-efed96dad93a", 'fc454f21-2c8c-4fc7-afde-00041b3a6255']


for file in os.listdir(path):
    fullpath = os.path.join(path, file)
    if os.path.isfile(fullpath):
        nameSet.add(fullpath)
while True:
    newSet = set()
    for file in os.listdir(path):
        fullpath = os.path.join(path, file)
        if os.path.isfile(fullpath):
            newSet.add(fullpath)
    newnewSet = newSet.difference(nameSet)
    if len(newnewSet) == 0:
        pass
    else:
        for filepath in newnewSet:
            nameSet.add(filepath)
            print("Recognizing from file: {}".format(filepath))
            result = recognizer.speech_recognize_continuous_from_file(filepath)
            print("Recognized text: {}".format(result))
            speaker = recognizer.identify_file(filepath, "true", profileids)
            numbers = []
            for char in list(result):
                if char.isdigit():
                    numbers.append(char)

            if len(numbers) == 1:
                pass
                #SenseHat.show_letter(numbers[0])
                #SenseHat.show_message("Welcome, {}".format(speaker))
                #time.sleep(5)
                server.send(json.dumps([numbers[0], speaker]))
            elif len(numbers) == 0:
                print("No numbers detected")
                #SenseHat.show_message("No numbers detected")
            else:
                print("Multiple numbers detected")
                for i in numbers:
                    server.send(json.dumps([i, speaker]))
                #SenseHat.show_message("Multiple numbers detected")
            #TODO add code for showing numbers on raspi


    time.sleep(2)

