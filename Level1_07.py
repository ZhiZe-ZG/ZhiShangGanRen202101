import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from .zerg.zerg_rush import ZergRushBot
from .protoss.threebase_voidray import ThreebaseVoidrayBot
from .terran.cyclone_push import CyclonePush

sc2.run_game(
    sc2.maps.get("AscensiontoAiurLE"),
    [
        Bot(Race.Terran, CyclonePush(), name="Cyclone Push"),
        Bot(Race.Random, Difficulty.CheatInsane),
    ],
    realtime=False,
    save_replay_as="Level_07.SC2Replay",
)
