import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.warpgate_push import WarpGateBot
from zerg.expand_everywhere import ExpandEverywhere
from terran.cyclone_push import CyclonePush
sc2.run_game(
    sc2.maps.get("CyberForestLE"),
    [
        Bot(Race.Protoss, WarpGateBot(), name="Warp Gate"),
        Bot(Race.Zerg, ExpandEverywhere(), name="Expand Everywhere"),
    ],
    realtime=False,
    save_replay_as="Level2_05.SC2Replay",
)
