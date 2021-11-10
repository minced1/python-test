import random

name = str(input("Wen willst du beleidigen?"))
insults = ["Idiot", "Arsch", "Spast", "Diggasagender"]

def insultPerson(name, insultId):
    return(name + ", du " + insults[insultId])
    
print(insultPerson(name, random.randint(0, len(insults)-1)))