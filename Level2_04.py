import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.threebase_voidray import ThreebaseVoidrayBot
from zerg.hydralisk_push import Hydralisk
from terran.cyclone_push import CyclonePush
sc2.run_game(
    sc2.maps.get("CeruleanFallLE"),
    [
        Bot(Race.Terran, CyclonePush(), name="Cyclone Push"),
        Computer(Race.Random, Difficulty.VeryEasy),
    ],
    realtime=False,
    save_replay_as="Level2_04.SC2Replay",
)
