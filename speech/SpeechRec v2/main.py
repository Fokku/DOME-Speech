import os
import time
import recognizer
import json
import databaseConnection as db
try:
    import socketServer
except:
    "Importing SocketServer failed"

debug = False
#attempt to connect to raspi, times out in 15 seconds
try:
    server = socketServer.server()
except:
    print("Connection to RasPi could not be established\nEntering debug mode")
    debug = True

dbcon = db.sqlutil()
savedSet = set()
nameSet = set()
path = r"C:\Users\19022874\Desktop\C200\C200 Voice System\Audio"
profileids = [i[0] for i in dbcon.getlist("SELECT Uid FROM voiceProfile")]
#["8b126ce5-0281-4b07-b66d-c0a7e576da2e", "daa14ddb-662f-4848-a2c7-1f0eb3dacaf1", "aef0f65d-abf5-4027-bed0-efed96dad93a", 'fc454f21-2c8c-4fc7-afde-00041b3a6255']


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
            if speaker != "00000000-0000-0000-0000-000000000000":
                userid = dbcon.getlist("SELECT UserId from voiceProfile WHERE Uid = '{}'".format(speaker))
            print("User ID: {}".format(userid[0][0]))
            numbers = []
            for char in list(result):
                if char.isdigit():
                    numbers.append(char)

            if len(numbers) == 1:
                if debug:
                    print("Number: {}\nSpeaker ID: {}".format(numbers[0], speaker))
                else:
                    server.send(json.dumps([numbers[0], userid]))
            elif len(numbers) == 0:
                print("No numbers detected")
            else:
                print("Multiple numbers detected")
                if debug:
                    print("Numbers: {}\nSpeaker: {}".format(numbers, speaker))
                #for i in numbers:
                #   server.send(json.dumps([i, speaker]))
            if debug:
                print("Sending SQL:\n{}".format("INSERT INTO voiceHistory (Uid, Voicefile, VoiceTxt) VALUES ('{}','{}','{}')".format(speaker, filepath, str(result).replace("'", '"'))))

            try:
                dbcon.execSQL("INSERT INTO voiceHistory (Uid, Voicefile, VoiceTxt) VALUES ('{}','{}','{}')".format(speaker, filepath, str(result).replace("'", '"')))
                print("Successfully uploaded to database")
            except:
                print("Could not upload data to database")

    time.sleep(2)


