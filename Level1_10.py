import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from zerg.worker_split import WorkerSplitBot
from protoss.warpgate_push import WarpGateBot
from terran.cyclone_push import CyclonePush

sc2.run_game(
    sc2.maps.get("BattleontheBoardwalkLE"),
    [
        Bot(Race.Zerg, WorkerSplitBot(), name="Worker Split"),
        Computer(Race.Random, Difficulty.Harder),
    ],
    realtime=False,
    save_replay_as="Level_10.SC2Replay",
)
