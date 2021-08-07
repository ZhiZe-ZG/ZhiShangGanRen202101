import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from .zerg.hydralisk_push import Hydralisk
from .terran.ramp_wall import RampWallBot

sc2.run_game(
    sc2.maps.get("AbyssalReefLE"),
    [
        Bot(Race.Terran, RampWallBot(), name="Ramp Wall"),
        Bot(Race.Zerg, Hydralisk(), name="Hydralisk"),
    ],
    realtime=False,
    save_replay_as="Level_03.SC2Replay",
)
