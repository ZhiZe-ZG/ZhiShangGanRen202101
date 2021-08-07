import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from .zerg.zerg_rush import ZergRushBot
from .terran.mass_reaper import MassReaperBot

sc2.run_game(
    sc2.maps.get("AcolyteLE"),
    [
        Bot(Race.Terran, MassReaperBot(), name="Mass Reaper"),
        Bot(Race.Zerg, ZergRushBot(), name="Zerg Rush"),
    ],
    realtime=False,
    save_replay_as="Level_05.SC2Replay",
)
