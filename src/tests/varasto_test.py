"""Varasto-luokan yksikkötestit."""

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Varasto-luokan toimintaa testaava luokka."""

    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Testaa, että uusi varasto on tyhjä."""
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Testaa uuden varaston tilavuuden."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Testaa, että lisääminen kasvattaa saldoa."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Testaa, että lisääminen pienentää vapaata tilaa."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Testaa, että varastosta ottaminen palauttaa oikean määrän."""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Testaa, että varastosta ottaminen lisää vapaata tilaa."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_nollaa_negatiivisen_tilavuuden(self):
        """Testaa negatiivisen tilavuuden käsittelyn."""
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_nollaa_negatiivisen_alkusaldon(self):
        """Testaa negatiivisen alkusaldon käsittelyn."""
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_konstruktori_tayttaa_varaston_jos_alkusaldo_on_liian_suuri(self):
        """Testaa liian suuren alkusaldon käsittelyn."""
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisays_ei_salli_negatiivista_maaraa(self):
        """Testaa, ettei negatiivista määrää lisätä."""
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_tayttaa_varaston_yli_menevalla_maaralla(self):
        """Testaa, ettei varaston tilavuus ylity lisättäessä."""
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_ei_salli_negatiivista_maaraa(self):
        """Testaa, ettei negatiivista määrää voi ottaa."""
        saatu = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(saatu, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_ei_palauta_enempaa_kuin_varastossa_on(self):
        """Testaa, ettei varastosta voi ottaa saldoa enempää."""
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(saatu, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_merkkijonoesitys(self):
        """Testaa varaston merkkijonoesityksen."""
        self.assertEqual(
            str(self.varasto),
            "saldo = 0, vielä tilaa 10"
        )
