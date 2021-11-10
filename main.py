from random import seed
from random import randint

insults = ["Idiot", "Arsch", "Spast", "Diggasagender"]

def insultPerson(name, insultId):
    return(name + ", du " + insults[insultId])

insultPerson()
print(insultPerson("Tim", randint(0, len(insults))))