

# =====BEGIN BASIC TYPE DEFINITIONS=====


class Aegis:
    pass


class Stealth:
    pass


class Attack:
    pass


class Modular:
    pass


class AntiAircraft:
    pass


class AntiSubmarine:
    pass


class AntiSurface:
    pass


class GuidedMissile:
    pass


class LandStrike:
    pass


class Littoral:
    pass


class Patrol:
    pass


class FastAttack:
    pass


class Fast:
    pass


# =====BEGIN BASIC CLASS DEFINITIONS=====


class Corvette:
    pass


class Frigate:
    pass


class Destroyer:
    pass


class Cruiser:
    pass


class Carrier:
    pass


class Submarine:
    pass


# =====BEGIN SPECIFIC CLASS DEFINITIONS=====


# ===BEGIN AMERICAN CLASSES===


class Freedom(Littoral, Fast, Modular, Corvette, Frigate):
    pass


class Independence(Littoral, Fast, Modular, Corvette, Frigate):
    pass


class ArleighBurke(Aegis, AntiAircraft, AntiSubmarine, AntiSurface, GuidedMissile, LandStrike, Destroyer):
    pass


class Ticroderoga(Aegis, )
