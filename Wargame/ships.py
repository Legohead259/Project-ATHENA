

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


class BallisticMissile:
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


class Nuclear:
    pass


class Conventional:
    pass


class AmphibiousAssault:
    pass


class AmphibiousTransport:
    pass


class LandingDock:
    pass


class LandSupport:
    pass


# =====BEGIN BASIC CLASS DEFINITIONS=====


class Corvette:
    pass


class MineCountermeasure:
    pass


class Frigate:
    pass


class Command:
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

# Troop Carriers

class Wasp(AmphibiousAssault, Carrier):
    pass


class America(AmphibiousAssault, Carrier):
    pass


class SanAntonio(AmphibiousTransport):
    pass


class WhidbeyIsland(LandingDock):
    pass


class HarpersFerry(LandingDock):
    pass

# Support Ships


class BlueRidge(Command):
    pass


class Avenger(MineCountermeasure):
    pass


class Cyclone(Patrol):
    pass

# Frigates


class Freedom(Littoral, Fast, Modular, Corvette, Frigate):
    pass


class Independence(Littoral, Fast, Modular, Corvette, Frigate):
    pass

# Destroyers


class ArleighBurke(Aegis, AntiAircraft, AntiSubmarine, AntiSurface, GuidedMissile, LandStrike, Destroyer):
    pass


class Zumwalt(Stealth, LandStrike, AntiSurface, AntiAircraft, LandSupport):
    pass

# Cruisers


class Ticonderoga(Aegis, LandStrike, AntiAircraft, AntiSurface, AntiSubmarine, Cruiser):
    pass

# Carriers


class Nimitz(Nuclear, Carrier):
    pass


class GeraldRFord(Nuclear, Carrier):
    pass

# Submarines


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
