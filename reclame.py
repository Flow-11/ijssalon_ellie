from tijdelijk import print_aanbieding
from algemene_functies import mijn_functie2

#Vraag 5
def aanbieding_1(smaak,prijs,korting):
    korting = prijs * (1 -korting)
    tekst = f"vandaag in de aanbieding: emmertje ijs (1 lister) in de smaak {smaak} van {prijs} euro voor {korting} euro"
    return tekst
print(aanbieding_1("aardbei",4,0.2))

# vraag 6 / 7
def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for x in inkomsten:
        totaal = totaal + x

    bedrag = totaal - (totaal * btw)   
    text =f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {round(bedrag,2)} euro btw betaald dient te worden."
    return text
list = [2,4,6,4]
print(inkomsten_totaal(list,0.8))

#vraag 8
mijn_lijst = [6,8,9,5,3,2,3]
def laag_hoog(mijn_lijst):
    uitvoer = []
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste)
    return uitvoer
print("vraag 8: ",laag_hoog(mijn_lijst))

#vraag9 /10
def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {round(bedrag,2)} euro" 
print(gemiddelde(mijn_lijst))

lijst_11 = [10,5,3,12,4,2,9,2]
#vraag 11
def meervoudig(invoer_lijst) :
    i = 0
    list_hoog = []
    list_laag = []
    
    for x in invoer_lijst:
        gemiddelde = 4
        gemiddelde = sum(invoer_lijst) / len(invoer_lijst)
        if x > gemiddelde :
            list_hoog.insert(i,x)
            i+1
        else :
            list_laag.insert(i,x)
            i+1
    return max(list_hoog),min(list_laag)

meervoudig(lijst_11)

#vraag 12
def combinatie(invoer_lijst2):
       
    korte_lijst =  meervoudig(invoer_lijst2)
    waarde = mijn_functie2(korte_lijst[0],korte_lijst[1])   # mijn_functie2 heeft 2 getallen nodig.

    return print("kortelijst 0 ",korte_lijst[0],"kortelijst 0 ",korte_lijst[1],"korte lijst: ",waarde)

combinatie(lijst_11)
