Copilotin kooditäydennykset olivat mielestäni hyödyllisiä, koska niiden avulla koodia pystyi kirjoittamaan nopeammin. Kaikkia ehdotuksia ei kuitenkaan voinut hyväksyä suoraan, vaan ne piti ensin lukea ja tarkistaa.

Kokeilin Copilot Chatia pyytämällä sitä selittämään projektin koodia ja Pylintin ilmoituksia. Sain sen avulla paremman käsityksen siitä, mitä koodi tekee ja mitä Pylintin huomautukset tarkoittavat. Huomasin kuitenkin, että myös Copilotin vastaukset kannattaa tarkistaa.

Copilot Agentin avulla lisäsin ohjelmaan toiminnallisuuden, jolla pelaajia voi hakea joukkueen perusteella ja järjestää pisteiden mukaan. Pyysin myös Agentia tekemään yksikkötestejä. Testeissä käytettiin testidataa eikä oikeaa verkkoyhteyttä tarvittu.

Testasin ohjelman komennolla uv run pytest, ja kaikki neljä testiä menivät läpi.

Tarkistin koodin myös Pylintillä. Lopputulokseksi tuli 9,64/10. Jäljelle jäi kaksi R0903-huomautusta, jotka liittyivät luokkien vähäiseen julkisten metodien määrään.

Tehtävästä opin, että Copilotista voi olla paljon apua ohjelmoinnissa, varsinkin jos ei heti ymmärrä jotain koodin kohtaa. Tekoälyn ehdotuksia ei kuitenkaan kannata hyväksyä tarkistamatta niitä. Koodi pitää silti itse ymmärtää ja testata.