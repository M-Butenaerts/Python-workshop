
# MAAK CLASS FACULTEITBAR
class Faculteitbar:

    def __init__(self, naam, faculteit, capaciteit, aanwezigen):
        self.naam = naam
        self.faculteit = faculteit
        self.assortiment = {}
        self.capaciteit = capaciteit
        self.aanwezigen = aanwezigen
        self.wachtrij = 0
        # NAAM
        # FACULTEIT
        # ASSORTIMENT (dictionary)
        # CAPACITEIT
        # HUIDIG AANTAL AANWEZIGEN

    def aanwezigheid_verhogen(self, aantal):
        self.aanwezigen += aantal
        if self.aanwezigen > self.capaciteit:
            diff = 100 - (self.aanwezigen - self.capaciteit)
            print(f"We zitten vol, er kunnen maar {diff} mensen binnen")
            print("Wil de rest wachten tot iedereen binnen kan? (Y/N)")
            answer = input()
            if answer == "Y":
                self.aanwezigen -= aantal
                self.wachtrij = aantal
                print(f'De wachtrij is {self.wachtrij}')
            elif answer == "N":
                self.wachtrij = self.aanwezigen - self.capaciteit
                self.aanwezigen = self.capaciteit
                print(f'De wachtrij is {self.wachtrij}')
            else:
                print(ValueError)

    def aanwezigheid_verlagen(self, aantal):
        self.aanwezigen -= aantal
        if self.wachtrij > 0:
            self.aanwezigheid_verhogen(self.wachtrij)
        if self.aanwezigen < 0:
            print("Error, er zijn minder aanwezigen dan ge wilt verlagen")
        else:
            self.aanwezigen += aantal
    def bier_toevoegen(self, bier, prijs):
        self.assortiment[bier.naam] = prijs



