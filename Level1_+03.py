import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.cannon_rush import CannonRushBot
from zerg.zerg_rush import ZergRushBot
from terran.ramp_wall import RampWallBot

sc2.run_game(
    sc2.maps.get("BlackpinkLE"),
    [
        Bot(Race.Zerg, ZergRushBot(), name="Zerg Rush"),
        Computer(Race.Random, Difficulty.Harder),
    ],
    realtime=False,
    save_replay_as="Level_+03.SC2Replay",
)
