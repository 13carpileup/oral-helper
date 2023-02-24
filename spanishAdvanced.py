import pyttsx3
import random
import time

###consts###
#the location of the microsoft voice, you need to install them in your settings for it to work (just google install spanish voice package)
spaniards = ["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-TW_HANHAN_11.0"]
#determines the speed of the voice, higher is faster (wpm)
newVoiceRate = 125
#determines the number of questions asked before the program moves onto a new batch of qs
batchSize = 1

engine = pyttsx3.init()
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice', spaniards[0])

#question list, edit the text file and put line breaks between questions to add your own list
f = open("questionList.txt","r",encoding="utf_8_sig")
questions = f.read().split('\n')

#main batch loop
#has a list of x questions which it picks from randomly
#once you say you're confident in it, it will ask it once more then remove it from the list
#batch ends once the list is empty
def batch():
    batch=[questions[random.randint(0,len(questions)-1)] for i in range(batchSize)] #could have multiple of the same q

    confident=[]
    #set to ensure questions aren't added to the text file multiple times
    unconf=set()

    while (len(batch)!=0):
        text=batch[random.randint(0,len(batch)-1)]
        pastTime=time.time() 
        engine.say(text)
        engine.runAndWait()
        store=input("Were you confident in your answer?\n")
        if store.lower()=='y':
            if (text in confident):
                confident.remove(text)
                batch.remove(text)
            else:
                confident.append(text)
        else:
            #any question that is not immediately answered with confidence is added to unconf
            #written to text file at the end of a batch
            unconf.add(text)
        #time in seconds it has taken you to answer, because why not
        print(time.time()-pastTime)
        time.sleep(1)
    
    print("Batch Complete")
    
    f=open("Uncertain_Questions.txt",'a',encoding="utf-8")
    for q in unconf:
        f.write("%s\n"%(q.strip()))
    f.close()

    
loopNumber = int(input("How many batches would you like to do? (-1 for endless)\n"))

if (loopNumber == -1):
    while True:
        batch()
else:
    for i in range(loopNumber):
        batch()

print("All batches completed.")

