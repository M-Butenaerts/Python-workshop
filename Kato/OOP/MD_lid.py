# CLASSES

class MD_lid:

    def __init__(self, naam, leeftijd, studie):
        self.naam = naam
        self.leeftijd = leeftijd
        self.studie = studie


class Praesidium_lid(MD_lid):

    def __init__(self, naam, leeftijd, studie, begin_jaar):
        super().__init__(naam, leeftijd, studie)
        self.begin_jaar = begin_jaar

    def roep_silentium(self):
        print(f"SILENTIUM! {self.naam} ")

# RUN


Butti = MD_lid("Mathieu Butenaerts", 22, "EWI")

Sander = Praesidium_lid("Sander Dekeyser", 20, "TBM", 2022)

print(Butti.leeftijd)
Butti.leeftijd = 12

print(Butti.leeftijd)

Sander.roep_silentium()

Butti.roep_silentium()