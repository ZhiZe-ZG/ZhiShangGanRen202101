import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.cannon_rush import CannonRushBot
from zerg.onebase_broodlord import BroodlordBot

sc2.run_game(
    sc2.maps.get("BlueshiftLE"),
    [
        Bot(Race.Protoss, CannonRushBot(), name="Cannon Rush"),
        Computer(Race.Random, Difficulty.Hard),
    ],
    realtime=False,
    save_replay_as="Level2_01.SC2Replay",
)
