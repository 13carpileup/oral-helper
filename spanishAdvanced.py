import pyttsx3
import random
import time

#consts
spaniards = ["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-TW_HANHAN_11.0"]
newVoiceRate = 125

engine = pyttsx3.init()

f = open("questionList.txt","r",encoding="utf_8_sig")

questions = f.read().split('\n')

engine.setProperty('rate',newVoiceRate)


engine.setProperty('voice', spaniards[0])
flag=1
while True:
    batch=[questions[random.randint(0,len(questions)-1)] for i in range(4)]
    for q in batch:
        questions.remove(q)
    confident=[]
    unconf=[]

    while (len(batch)!=0):
        text=batch[random.randint(0,len(batch)-1)]
        pastTime=time.time()
        engine.say(text)
        engine.runAndWait()
        store=input("Were you confident in your answer?")
        if store.lower()=='y':
            if (text in confident):
                confident.remove(text)
                batch.remove(text)
            else:
                confident.append(text)
        else:
            unconf.append(text)
        print(time.time()-pastTime)
        time.sleep(1)
    
    print("Batch Complete")
    
    f=open("spanish/RecentlyUncertainQs.txt",'a',encoding="utf-8")
    for q in unconf:
        f.write("%s\n"%(q.strip()))
    f.close()

    

