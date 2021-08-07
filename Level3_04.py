import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.warpgate_push import WarpGateBot
from zerg.expand_everywhere import ExpandEverywhere
from terran.onebase_battlecruiser import BCRushBot
from terran.mass_reaper import MassReaperBot
sc2.run_game(
    sc2.maps.get("EastwatchLE"),
    [
        Bot(Race.Protoss, WarpGateBot(), name="Warp Gate"),
        # Bot(Race.Terran, BCRushBot(), name="BC Rush"),
        Computer(Race.Random, Difficulty.MediumHard),
    ],
    realtime=False,
    save_replay_as="Level3_04.SC2Replay",
)
