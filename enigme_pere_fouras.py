import json
from random import*
from time import sleep



def charger_enigmes(fichier):
    with open(fichier, "r", encoding='utf-8') as f:
        question_reponse ={}
        donnees = json.load(f)
        for i in donnees:
            question_reponse[i['question']]=i['reponse']
    return question_reponse




def get_question_reponse(dico_question):
    n=randint(0,len(dico_question)-1)
    question=dico_question.keys()
    reponse=dico_question.values()
    compt=0
    for i in reponse:
        if compt==n:
            reponse_final=i
        compt+=1
    compt=0
    for i in question:
        if compt==n:
            question_final=i
        compt+=1

    reponse=(question_final,reponse_final)
    return reponse

def belle_question(question):
    phrase=question.split("\n")
    for i in phrase:
        print(i,"\n")
        sleep(2)


def enigme_pere_fouras():
    vie=3
    dico_question=charger_enigmes("enigmesPF.json")
    question_reponse=get_question_reponse(dico_question)
    question=question_reponse[0]
    reponse=question_reponse[1].lower()
    #print("réponse",reponse)
    belle_question(question)
    #print(question)
    while vie!=0:
        reponse_rentrer=input("rentrer une réponse: ").lower()
        #print("reponse rentrer",reponse_rentrer,"reponse attendue",reponse)
        if reponse_rentrer==reponse:
            sleep(1)
            print("\nla réponse est correcte")
            return True
        else:
            sleep(1)
            if vie==1:
                print("vous avez perdue")
                print("la réponse etait'", reponse,"'\n")
                return False
            else:
                vie-=1
                print("\nla réponse est incorecte, il vous reste",vie,'essais\n')

enigme_pere_fouras()