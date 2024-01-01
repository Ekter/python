from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()

to_write = """Sophiast
PNSrobocup
Polytech Team NS
PolyBotRiviera
PolyBot
FC Farming
Pascal's squad
FireFlies16
R3D3
PolyTechBots
Poly Cup Bot
SophiaTech Bot Team
Les PolyBots de Nice-Sophia
azur bots cup
SKBots
Azur Bots Builders
Polybot Crew
Polybot Squad
Bots In Group"""

sleep(5)

for s in to_write.split("\n"):
    print(s)
    keyboard.type(s)
    sleep(1)
    keyboard.press(Key.tab)
    sleep(2)
    keyboard.release(Key.tab)
    sleep(1)
    keyboard.press(Key.tab)
    sleep(2)
    keyboard.release(Key.tab)
    sleep(5)
