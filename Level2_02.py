import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.cannon_rush import CannonRushBot
from zerg.hydralisk_push import Hydralisk
from terran.proxy_rax import ProxyRaxBot
sc2.run_game(
    sc2.maps.get("CactusValleyLE"),
    [
        Bot(Race.Zerg, Hydralisk(), name="Hydralisk"),
        Bot(Race.Terran, ProxyRaxBot(), name="ProxyRaxBot"),
    ],
    realtime=False,
    save_replay_as="Level2_02.SC2Replay",
)
