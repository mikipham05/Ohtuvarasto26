# Muutos alkuperäisessä kloonissa
# Muutos toisessa kloonissa
from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))

print(f"{summa(x, y)}")
print(f"{erotus(x, y)}")
print(f"{x} * {y} = {tulo(x, y)}")

logger("lopetetaan ohjelma")
print("goodbye!")
