import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from .zerg.zerg_rush import ZergRushBot
from .protoss.threebase_voidray import ThreebaseVoidrayBot
from .terran.onebase_battlecruiser import BCRushBot

sc2.run_game(
    sc2.maps.get("AcropolisLE"),
    [
        Bot(Race.Terran, BCRushBot(), name="BC Rush"),
        Bot(Race.Protoss, ThreebaseVoidrayBot(), name="Threebase Voidray"),
    ],
    realtime=False,
    save_replay_as="Level_06.SC2Replay",
)
