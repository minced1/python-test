from random import seed
from random import randint
seed(1)

insults = ["Idiot", "Arsch", "Spast", "Diggasagender"]

def insultPerson(name, insultId):
    return(name + ", du " + insults[insultId])
    
print(insultPerson("Tim", random.randint(0, len(insults))))