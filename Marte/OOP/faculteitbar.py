
# MAAK CLASS FACULTEITBAR
class Faculteitbar:

    def __init__(self, naam, faculteit, capaciteit):
        # NAAM
        self.naam = naam
        # FACULTEIT
        self.faculteit = faculteit
        # ASSORTIMENT (dictionary)
        self.assortiment = {}
        # CAPACITEIT
        self.capaciteit = capaciteit
        # HUIDIG AANTAL AANWEZIGEN
        self.huidigaantal = 0

    def aanwezigheid_verhogen(self, aantal):
        self.huidigaantal += aantal

    def aanwezigheid_verlagen(self, aantal):
        self.huidigaantal -= aantal

    def bier_toevoegen(self, bier, prijs):
        self.assortiment[bier] = prijs
        # zet in assortiment naam van bier en je krijgt de prijs


