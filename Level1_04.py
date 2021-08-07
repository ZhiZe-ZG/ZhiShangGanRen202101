import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from .zerg.hydralisk_push import Hydralisk
from .terran.proxy_rax import ProxyRaxBot

sc2.run_game(
    sc2.maps.get("AcidPlantLE"),
    [
        Bot(Race.Terran, ProxyRaxBot(), name="Proxy Rax"),
        Bot(Race.Random, Difficulty.Easy),
    ],
    realtime=False,
    save_replay_as="Level_04.SC2Replay",
)
