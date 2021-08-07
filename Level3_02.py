import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.cannon_rush import CannonRushBot
from zerg.hydralisk_push import Hydralisk
from terran.proxy_rax import ProxyRaxBot
from terran.mass_reaper import MassReaperBot
sc2.run_game(
    sc2.maps.get("DiscoBloodbathLE"),
    [
        Bot(Race.Terran, ProxyRaxBot(), name="Proxy Rax"),
        Bot(Race.Terran, MassReaperBot(), name="Mass Reaper"),
    ],
    realtime=False,
    save_replay_as="Level3_02.SC2Replay",
)
