import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.cannon_rush import CannonRushBot
from zerg.onebase_broodlord import BroodlordBot
from terran.ramp_wall import RampWallBot

sc2.run_game(
    sc2.maps.get("BelShirVestigeLE"),
    [
        Bot(Race.Terran, RampWallBot(), name="Ramp Wall"),
        Computer(Race.Random, Difficulty.VeryEasy),
    ],
    realtime=False,
    save_replay_as="Level_+02.SC2Replay",
)
