import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.cannon_rush import CannonRushBot
from zerg.zerg_rush import ZergRushBot
from terran.onebase_battlecruiser import BCRushBot

sc2.run_game(
    sc2.maps.get("BloodBoilLE"),
    [
        Bot(Race.Terran, BCRushBot(), name="BC Rush"),
        Computer(Race.Random, Difficulty.VeryHard),
    ],
    realtime=False,
    save_replay_as="Level_+04.SC2Replay",
)
