import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from .zerg.expand_everywhere import ExpandEverywhere
from .protoss.warpgate_push import WarpGateBot
from .terran.cyclone_push import CyclonePush

sc2.run_game(
    sc2.maps.get("BackwaterLE"),
    [
        Bot(Race.Protoss, WarpGateBot(), name="Warp Gate"),
        Bot(Race.Random, Difficulty.Medium),
    ],
    realtime=False,
    save_replay_as="Level_09.SC2Replay",
)
