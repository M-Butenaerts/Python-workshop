
# MAAK CLASS FACULTEITBAR
class Faculteitbar:

    def __init__(self, naam, faculteit, capaciteit):
        self.naam = naam
        self.faculteit = faculteit
        self.assortiment = {}           # ASSORTIMENT (dictionary)
        self.capaciteit = capaciteit
        self.huidig = 0    # HUIDIG AANTAL AANWEZIGEN


    def aanwezigheid_verhogen(self, aantal):
        self.huidig += aantal

    def aanwezigheid_verlagen(self, aantal):
        self.huidig -= aantal

    def bier_toevoegen(self, bier, prijs):
        self.assortiment[bier] = prijs





