from faculteitbar import Faculteitbar
from Bier import Bier


# MAAK FACULTEITSBAR AAN
atmos = Faculteitbar("Atmosfeer", "LR", 60)
# MAAK BIER AAN
jupiler = Bier("jupiler", 5.2, 25)
# VOEG BIER TOE AAN HET ASSORTIMENT
atmos.bier_toevoegen(jupiler.naam, 1.5)
# VOEG 100 AANWEZIGEN TOE
atmos.aanwezigheid_verhogen(100)
# VERLAAG HET AANTAL LEDEN MET 101
atmos.aanwezigheid_verlagen(101)
print(atmos.assortiment)
print(atmos.huidigaantal)

