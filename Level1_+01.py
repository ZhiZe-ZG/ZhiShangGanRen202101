import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.cannon_rush import CannonRushBot
from zerg.onebase_broodlord import BroodlordBot

sc2.run_game(
    sc2.maps.get("AbiogenesisLE"),
    [
        Bot(Race.Zerg, BroodlordBot(), name="Broodlord"),
        Computer(Race.Random, Difficulty.Hard),
    ],
    realtime=False,
    save_replay_as="Level_+01.SC2Replay",
)
