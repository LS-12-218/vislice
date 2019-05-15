STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZMAGA = "w"
PORAZ = "X"

class Igra:
    def __init__(self, geslo, crke = None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke
    
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
        return " ".join(self.napacne_crke)
    def ugibaj(self, crka):
        if crka in self.crke():
            return PONOVLJENA_CRKA
        else:
            self.crke = self.crke + crka
            if self.poraz():
                return PORAZ
            elif self.zmaga():
                return ZMAGA
            elif crka in self.geslo():
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

with open("besede.txt", encoding = "utf-8") as datoteka:
    bazen_besed = [beseda for beseda in datoteka]


t_geslo = "wrerehe"
t_crke = "aeioufeunierh"
igra = Igra(t_geslo, t_crke)
print(igra.napacne_crke())
print(igra.pravilne_crke())
print([igra.stevilo_napak(), igra.poraz(), igra.zmaga(), igra.pravilni_del_gesla(), igra.napacne_crke(), igra.ugibaj("w")])
print(bazen_besed[0:25])