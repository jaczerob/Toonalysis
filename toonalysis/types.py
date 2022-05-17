import enum
from typing import Optional


__all__ = ["Toon"]


class Toon:
    def __init__(self, *, id, laff, species, sellbot, cashbot, lawbot, bossbot,
                 toonup, trap, lure, sound, throw, squirt, drop, organic, **_) -> None:
        self.id: int = id
        self.laff: Optional[int] = laff
        self.species = Species(int(species))
        self.sellbot = SellbotSuit(int(sellbot))
        self.cashbot = CashbotSuit(int(cashbot))
        self.lawbot = LawbotSuit(int(lawbot))
        self.bossbot = BossbotSuit(int(bossbot))
        self.toonup = ToonUp(int(toonup))
        self.trap = Trap(int(trap))
        self.lure = Lure(int(lure))
        self.sound = Sound(int(sound))
        self.throw = Throw(int(throw))
        self.squirt = Squirt(int(squirt))
        self.drop = Drop(int(drop))
        self.organic = organic

    def to_document(self) -> dict[str, int | str]:
        return {
            "_id": self.id,
            "laff": self.laff,
            "species": str(self.species),
            "sellbot": str(self.sellbot),
            "cashbot": str(self.cashbot),
            "lawbot": str(self.lawbot),
            "bossbot": str(self.bossbot),
            "toonup": str(self.toonup),
            "trap": str(self.trap),
            "lure": str(self.lure),
            "sound": str(self.sound),
            "throw": str(self.throw),
            "squirt": str(self.squirt),
            "drop": str(self.drop),
            "organic": self.organic,
        }


class Species(enum.Enum):
    Bear = 1
    Cat = 2
    Dog = 3
    Duck = 4
    Horse = 5
    Monkey = 6
    Mouse = 7
    Pig = 8
    Rabbit = 9
    Deer = 10
    Crocodile = 11

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_


class SellbotSuit(enum.Enum):
    NoSuit = 0
    ColdCaller = 1
    Telemarketer = 2
    NameDropper = 3
    GladHander = 4
    MoverAndShaker = 5
    TwoFace = 6
    TheMingler = 7
    MrHollywood = 8
    Maxed = 9

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_


class CashbotSuit(enum.Enum):
    NoSuit = 0
    ShortChange = 1
    PennyPincher = 2
    Tightwad = 3
    BeanCounter = 4
    NumberCruncher = 5
    MoneyBags = 6
    LoanShark = 7
    RobberBaron = 8
    Maxed = 9

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_


class LawbotSuit(enum.Enum):
    NoSuit = 0
    BottomFeeder = 1
    Bloodsucker = 2
    DoubleTalker = 3
    AmbulanceChaser = 4
    BackStabber = 5
    SpinDoctor = 6
    LegalEagle = 7
    BigWig = 8
    Maxed = 9

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_


class BossbotSuit(enum.Enum):
    NoSuit = 0
    Flunky = 1
    PencilPusher = 2
    Yesman = 3
    Micromanager = 4
    Downsizer = 5
    HeadHunter = 6
    CorporateRaider = 7
    TheBigCheese = 8
    Maxed = 9

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_


class ToonUp(enum.Enum):
    NoGag = 0
    Feather = 1
    Megaphone = 2
    Lipstick = 3
    BambooCane = 4
    PixieDust = 5
    JugglingCubes = 6
    HighDive = 7

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_


class Trap(enum.Enum):
    NoGag = 0
    BananaPeel = 1
    Rake = 2
    Marbles = 3
    Quicksand = 4
    Trapdoor = 5
    TNT = 6
    Railroad = 7

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_


class Lure(enum.Enum):
    NoGag = 0
    OneDollarBill = 1
    SmallMagnet = 2
    FiveDollarBill = 3
    BigMagnet = 4
    TenDollarBill = 5
    HypnoGoggles = 6
    Presentation = 7

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_


class Sound(enum.Enum):
    NoGag = 0
    BikeHorn = 1
    Whistle = 2
    Trumpet = 3
    Aoogah = 4
    ElephantTrunk = 5
    FogHorn = 6
    OperaSinger = 7

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_


class Throw(enum.Enum):
    NoGag = 0
    Cupcake = 1
    FruitPieSlice = 2
    CreamPieSlice = 3
    WholeFruitPie = 4
    WholeCreamPie = 5
    BirthdayCake = 6
    WeddingCake = 7

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_


class Squirt(enum.Enum):
    NoGag = 0
    SquirtingFlower = 1
    GlassOfWater = 2
    SquirtGun = 3
    SeltzerBottle = 4
    FireHose = 5
    StormCloud = 6
    Geyser = 7

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_


class Drop(enum.Enum):
    NoGag = 0
    FlowerPot = 1
    Sandbag = 2
    Anvil = 3
    HeavyWeight = 4
    Safe = 5
    GrandPiano = 6
    Toontanic = 7

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_
