from Wargame.Ships.Classifications import *
from Wargame.Ships.Types import *


class LosAngeles(Nuclear, FastAttack, LandStrike, Submarine):
    pass


class Seawolf(Nuclear, FastAttack, LandStrike, Submarine):
    pass


class Virginia(Nuclear, FastAttack, LandStrike, Submarine):
    pass


class Ohio(Nuclear, BallisticMissile, Submarine):
    pass


class OhioGM(Nuclear, GuidedMissile, Submarine):
    pass


class Columbia(Nuclear, BallisticMissile, Submarine):
    pass