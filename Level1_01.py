import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from .protoss.cannon_rush import CannonRushBot
from .zerg.onebase_broodlord import BroodlordBot

sc2.run_game(
    sc2.maps.get("16-BitLE"),
    [Bot(Race.Protoss, CannonRushBot()), Bot(Race.Zerg, BroodlordBot())],
    realtime=False,
    save_replay_as="Level_01.SC2Replay"
)