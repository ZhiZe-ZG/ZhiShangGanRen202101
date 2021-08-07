import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.threebase_voidray import ThreebaseVoidrayBot
from zerg.hydralisk_push import Hydralisk
from terran.proxy_rax import ProxyRaxBot
from terran.mass_reaper import MassReaperBot
sc2.run_game(
    sc2.maps.get("DreamcatcherLE"),
    [
        Bot(Race.Protoss, ThreebaseVoidrayBot(), name="Threebase Voidray"),
        Computer(Race.Random, Difficulty.VeryEasy),
    ],
    realtime=False,
    save_replay_as="Level3_03.SC2Replay",
)
