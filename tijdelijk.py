from helper import decoreer
from algemene_functies import mijn_functie2

def print_aanbieding():
    prijzen = {
        "aardbei": 3,
        "vanille": 4,
        "chocolade": 5,
    }
    aanbieding = prijzen["aardbei"] * 0.8
    print(aanbieding)

    reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter – slechts € {round(aanbieding,2)}"

    lente_tekst = len(reclame_tekst) + 3
    reclame_tekst2 = reclame_tekst[:lente_tekst]
    #print(reclame_tekst2)
    # vraag 6
    reclame_tekst3 = reclame_tekst2.upper()
    
    # vraag 7
    reclame_tekst4 = reclame_tekst3.split(" ")
    #vraag 8,9,10
    for el in reclame_tekst4:   
        lengte = len(el)
        if lengte > 4:
            print(el)
        else :
            print(el.lower())

decoreer("Aanbieding")
print_aanbieding()





    
