import pyttsx3
import random
import time
spaniards = ["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-TW_HANHAN_11.0"]

questions = "¿Cómo es tu zona?]¿Cuáles son las ventajas de vivir en el campo/en la ciudad?]¿Dónde te gustaría vivir en el futuro?]¿Qué cambiarías de tu barrio si fueras el alcalde?]¿Adónde fuiste de vacaciones el año pasado?]¿Qué tipo de vacaciones te gustan?]¿Vas a ir de vacaciones el año que viene?]¿Crees que el turismo puede tener un impacto negativo en tu ciudad?]¿Qué tan importante es el turismo en tu ciudad?]¿Qué diferencias notas entre la vida española y la de tu propio país?]¿Has ido a alguna fiesta hispana? ¿Cómo fue? / ¿Qué fiestas hispanas conoces? ¿Cuál es tu favorita y por qué?]¿Si tuvieras la posibilidad, qué fiesta hispana te gustaría visitar? ¿Por qué?]¿Cuáles tradiciones son importantes en tu cultura? ¿Por qué?]¿Cómo celebraste tu cumpleaños?]¿Qué fiestas similares hay entre el mundo hispanohablante y tu cultura?]¿Qué asignaturas estudias en tu instituto?]	Describe tu día en el insti.]¿Qué hiciste ayer en el insti?]¿Qué cambiarías si fueras el director del instituto?]¿Cuáles son las ventajas y desventajas de llevar uniforme en tu opinión?]¿Qué reglas hay en tu insti?]	¿Crees que los estudiantes deberían usar sus móviles en el insti? ¿Por qué?]¿Qué actividades extraescolares haces?]	¿Prefieres ir de excursión con tu familia o con tus amigos?]Si pudieras organizar un viaje con tu clase ¿dónde te gustaría ir?]¿Qué es más importante: ganar dinero o trabajar en lo que te gusta?]	¿Vale la pena ir a la universidad? ¿Por qué?]¿Por qué muchos jóvenes prefieren pasar un tiempo al extranjero antes de ir a la universidad?]¿Has tenido alguna experiencia de voluntariado? ¿Cómo fue?]¿Qué vas a estudiar el año que viene?]¿Qué trabajo te gustaría hacer en el futuro?]¿Planeas ir a la universidad?]¿Dónde te gustaría estudiar/trabajar en el futuro?]¿Dónde vives?]¿Cómo es tu casa?]¿Cómo sería tu casa ideal?]¿Cómo es tu rutina diaria?]	¿Qué hiciste el fin de semana pasado?]	¿Qué planeas hacer mañana?]¿Cómo ayudas en la casa?]¿Te llevas bien con tu familia?]¿Prefieres salir con tu familia o con tus amigos?]¿Tiene hermanos?]Describe un miembro de tu familia]¿Prefieres cenar en casa o en un restaurante? ¿Por qué (no)?]Háblame de lo que hiciste en un día especial reciente con tus amigos o tu familia?]¿Cuál es la fiesta más importante, en tu opinión?]¿Crees que las fiestas tradicionales son importantes? ¿Por qué (no)?]¿Eres muy deportista? ¿Por qué?]¿Qué haces en tu tiempo libre?]¿Llevas una vida sana?]¿Qué hacías cuando eras niño?]¿Cómo ayudas con las tareas domésticas?]¿Tus padres te dan dinero? ¿Qué haces con la paga?]¿Adónde fuiste de compras la última vez y qué compraste? ¿Qué hiciste?]¿Qué haces para ganar dinero?]¿Cuál es tu comida favorita?]¿Qué come tu familia durante la semana?]¿Has probado la comida española ¿Te gusta? ¿Por qué (no)?]¿Qué vas a comer hoy?"
questions=questions.split(']') 
print(len(questions))     

engine = pyttsx3.init()


newVoiceRate = 125
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

    

