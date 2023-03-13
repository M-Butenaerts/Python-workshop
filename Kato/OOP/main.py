from faculteitbar import Faculteitbar
from Bier import Bier


# MAAK FACULTEITSBAR AAN
Bouwpub = Faculteitbar('Bouwpub', 'Bouwkunde', 100)
# MAAK BIER AAN
Jupiler = Bier('Jupiler', 5.2, 33)

# VOEG BIER TOE AAN HET ASSORTIMENT
Bouwpub.bier_toevoegen(Jupiler.naam, '1 Euro')
Bouwpub.bier_toevoegen('HJ', '1.4 Euro')

# VOEG 100 AANWEZIGEN TOE
Bouwpub.aanwezigheid_verhogen(100)
# VERLAAG HET AANTAL LEDEN MET 101
Bouwpub.aanwezigheid_verlagen(101)

print(Bouwpub)
#Print
print(Bouwpub.assortiment)
print(Jupiler.volume)
print(Bouwpub.huidig)
