"""Varaston toimintaa kuvaava moduuli."""


class Varasto:
    """Varasto, joka hallitsee tilavuutta ja saldoa."""

    def __init__(self, tilavuus, alku_saldo=0):
        """Luo uuden varaston annetulla tilavuudella ja alkusaldolla."""
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            self.saldo = alku_saldo
        else:
            self.saldo = tilavuus

    def paljonko_mahtuu(self):
        """Palauttaa varastossa jäljellä olevan vapaan tilan."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Lisää varastoon annetun määrän, enintään varaston täyteen."""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Ottaa varastosta pyydetyn määrän ja palauttaa otetun määrän."""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        """Palauttaa varaston saldon ja vapaan tilan merkkijonona."""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
