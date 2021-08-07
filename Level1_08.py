import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from zerg.expand_everywhere import ExpandEverywhere
from protoss.threebase_voidray import ThreebaseVoidrayBot
from terran.cyclone_push import CyclonePush

sc2.run_game(
    sc2.maps.get("AutomatonLE"),
    [
        Bot(Race.Zerg, ExpandEverywhere(), name="Expand Everywhere"),
        Computer(Race.Random, Difficulty.VeryEasy),
    ],
    realtime=False,
    save_replay_as="Level_08.SC2Replay",
)
