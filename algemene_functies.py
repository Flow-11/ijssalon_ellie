def mijn_functie1(waarde) :
    return waarde**2
print(mijn_functie1(10))

def mijn_functie2(a, b) :
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst

print(mijn_functie2(12,3))