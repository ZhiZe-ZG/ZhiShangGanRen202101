import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.warpgate_push import WarpGateBot
from zerg.zerg_rush import ZergRushBot
from terran.cyclone_push import CyclonePush
sc2.run_game(
    sc2.maps.get("DarknessSanctuaryLE"),
    [
        Bot(Race.Zerg, ZergRushBot(), name="Zerg Rush"),
        Computer(Race.Random, Difficulty.MediumHard),
    ],
    realtime=False,
    save_replay_as="Level2_06.SC2Replay",
)
