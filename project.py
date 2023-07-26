import cvprojects
import os
import handgestures
import time
import speechregonition as sr
import aws_services
import text_to_speech as ts



ts.say("Hello guys My name is Mohini , Aatmaa Namaste")


while True:
    ts.say("Tell me  your query")
    
    query = sr.myspeechrecognition(duration=5)
    query.lower()
    if "blur" in query:
        ts.say("oh! you dont want be spotted")
        cvprojects.background_blur()
        time.sleep(8)
        
    if "distance" in query:
        ts.say("You want to check How far you are... cool...")
        cvprojects.face_distance_measure()
        time.sleep(8)
        
        
    if "hand" in query:
        ts.say("Now you can control Amazon services using Hand gestures")
        handgestures.hand()
        time.sleep(15)
        
    if "docker" in query:
        ts.say("Opening Docker As a Service Web Page")
        os.system("start msedge http://192.168.1.38")
        time.sleep(10)
    
    if "chatbot" in query:
        ts.say("Opening AI Psychiatrist chatbot")
        os.system("start msedge http://65.1.111.174")
        time.sleep(10)
           
    if "terminal" in query:
        ts.say("Opening Black Screen as white Screen")
        os.system("start msedge https://192.168.1.38:4200/")
        time.sleep(10)
    if "operating" in query:
        ts.say("opening os in browser")
        os.system("start msedge http://65.1.111.174/os.html")
        time.sleep(10)
    if "notification" in query:
        ts.say("Sending Notifications in 3.. 2... 1...")
        os.system("start msedge https://r85e5zdyid.execute-api.ap-south-1.amazonaws.com/emaill/email")
        
    if "medicine" in query:
        ts.say("opening search for medicine app")
        os.system("start msedge http://easymed.great-site.net/?i=3")
        time.sleep(10)
    
    if "convert" in query:
        aws_services.convert_audio_text()
        time.sleep(10)
    if "shutdown" in query:
        ts.say("Bye Bye See you later, Signing off..")
        ts.stop()
        break
    
    

    
    
    

    
        
