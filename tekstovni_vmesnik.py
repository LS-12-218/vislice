import model
import random

def izpis_igre(igra):
    return "\nNapačne črke:\n{}\n".format(igra.nepravilni_ugibi()) + 200 * "-" + "\nPreostali poskusi:\n{}\n".format(model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1) + 200 * "-" + "\nTrenutne črke:\n{}\n".format(igra.pravilni_del_gesla()) + 200 * "-" + "\nVnesite naslednjo črko:"
def izpis_zmage(igra):
    return 30 * "\n" + 200 * "-" + "\nUganili ste geslo {}. Čestitamo. Vaš IQ je {}.\n".format(igra.geslo, random.choice([c for c in range(70,140)])) + 200 * "-"
def izpis_poraza(igra):
    return 30 * "\n" + 200 * "-" + "\nIzgubili ste. Geslo je bilo {}. Čestitamo. Vaš IQ je {}.\n".format(igra.geslo, random.choice([c for c in range(70,140)])) + 200 * "-"
def zahtevaj_vnos():
    return input("Naslednji ugib:")
def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        poskus = str(zahtevaj_vnos())
        if len(poskus) != 1 or (poskus.upper() == poskus.lower()):
            print(30 * "\n" + "{} sploh ni črka. Čestitamo. Vaš IQ je {}.".format(poskus, random.choice([c for c in range(60,150)])))
        else:
            print(30 * "\n")
            igra.ugibaj(poskus)
            if igra.poraz():
                print(izpis_poraza(igra))
                break
            elif igra.zmaga():
                print(izpis_zmage(igra))
                break
            else:
                pass
    return

nova = "Y"
while nova == "Y":
    pozeni_vmesnik()
    nova = input("Nova igra [Y/N]:")
    nova = nova.upper()
    if nova not in ["Y", "N"]:
        assert False