import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer

sc2.run_game(
    sc2.maps.get("AbiogenesisLE"),
    [Bot(Race.Random, Difficulty.Hard), Bot(Race.Random, Difficulty.CheatMoney)],
    realtime=False,
    save_replay_as="Level_02.SC2Replay",
)
