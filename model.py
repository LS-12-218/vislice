import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZMAGA = "w"
PORAZ = "X"

class Igra:
    def __init__(self, geslo, crke = None):
        self.geslo = geslo.upper()
        if crke is None:
            self.crke = []
        else:
            self.crke = [crka.upper() for crka in crke]
    
    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]
    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]
    def stevilo_napak(self):
        return len(self.napacne_crke())
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
    def zmaga(self):
        return False not in [c in self.crke for c in self.geslo]
    def pravilni_del_gesla(self):
        niz = ""
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                niz += crka
            else:
                niz += "_"
        return niz
    def nepravilni_ugibi(self):
        if self.napacne_crke() == []:
            return ""
        else:
            return " ".join(self.napacne_crke())
    def ugibaj(self, crka):
        crko = crka.upper()
        if crko in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crko)
            if self.poraz():
                return PORAZ
            elif self.zmaga():
                return ZMAGA
            elif crko in self.geslo:
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

with open("besede.txt", "r", encoding = "utf-8") as datoteka:
    bazen_besed = [beseda.strip().upper() for beseda in datoteka]

def nova_igra():
    return Igra(random.choice(bazen_besed))