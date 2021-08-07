import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from protoss.cannon_rush import CannonRushBot
from zerg.hydralisk_push import Hydralisk
from terran.cyclone_push import CyclonePush
sc2.run_game(
    sc2.maps.get("DefendersLandingLE"),
    [
        Bot(Race.Protoss, CannonRushBot(), name="Cannon Rush"),
        Bot(Race.Zerg, Hydralisk(), name="Hydralisk"),
    ],
    realtime=False,
    save_replay_as="Level3_01.SC2Replay",
)
