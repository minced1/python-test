import random

insults = ["Idiot", "Arsch", "Spast", "Diggasagender"]

def insultPerson(name, insultId):
    return(name + ", du " + insults[insultId])
    
print(insultPerson("Tim", random.randint(0, len(insults)-1)))