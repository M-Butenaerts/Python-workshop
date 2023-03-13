from faculteitbar import Faculteitbar
from Bier import Bier


# MAAK FACULTEITSBAR AAN
Bouwpub = Faculteitbar('Bouwpub', 'Bouwkunde', 150, 0)
# MAAK BIER AAN
Jupiler = Bier('Jupiler', 5.2, 0.25)
# VOEG BIER TOE AAN HET ASSORTIMENT
Bouwpub.bier_toevoegen(Jupiler, 1)
# VOEG 100 AANWEZIGEN TOE
Bouwpub.aanwezigheid_verhogen(100)
# VERLAAG HET AANTAL LEDEN MET 101
Bouwpub.aanwezigheid_verlagen(101)
