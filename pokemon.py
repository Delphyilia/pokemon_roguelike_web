from basedata import Pokemon
from move import *
from variable_name import *
from ability import *
import sys

debug_flag = DEBUG.ON
pokemon_classes = []


class Arceus(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.monster_name = "アルセウス"
        self.move1 = earthquake()
        self.move2 = surf()
        self.move3 = HydroPump()
        self.move4 = Thunderbolt()
        self.ability1 = Omnipotent()
        self.type1 = "ノーマル"
        self.type2 = ""
        self.capture_difficulty = 1
        super().setBase(120, 120, 120, 120, 120, 120)


class Arboc(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.monster_name = "アーボック"
        self.move1 = earthquake()
        self.move2 = surf()
        self.move3 = HydroPump()
        self.move4 = Thunderbolt()
        self.type1 = "どく"
        self.type2 = ""
        self.ability1 = intimidate()
        self.capture_difficulty = 255
        super().setBase(60, 95, 69, 65, 79, 80)


class Rhydon(Pokemon):
    def __init__(self,newlevel,position):
        super().__init__(newlevel,position)
        self.level = newlevel
        self.monster_name = "サイドン"
        self.move1 = earthquake()
        self.move2 = Thunderbolt()
        self.move3 = HydroPump()
        self.move4 = HornAttack()
        self.type1 = "じめん"
        self.type2 = "いわ"
        self.ability1 = LightningRod()
        self.capture_difficulty = 100
        super().setBase(105, 130, 120, 45, 45, 40)

class Skeledirge(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.level = newlevel
        self.monster_name = "ラウドボーン"
        self.move1 = TorchSong()
        self.move2 = ScorchingSands()
        self.move3 = SlackOff()
        self.move4 = FireBlast()
        self.type1 = "ほのお"
        self.type2 = "ゴースト"
        self.ability1 = Blaze()
        self.capture_difficulty = 100
        super().setBase(104, 75, 100, 110, 75, 66)

class Cinderace(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.level = newlevel
        self.monster_name = "エースバーン"
        self.move1 = PyroBall()
        self.move2 = ScorchingSands()
        self.move3 = Trailblaze()
        self.move4 = GunkShot()
        self.type1 = "ほのお"
        self.type2 = ""
        self.ability1 = Libero()
        self.capture_difficulty = 100
        super().setBase(80, 116, 75, 65, 75, 119)

class Samurott(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.level = newlevel
        self.monster_name = "ダイケンキ"
        self.move1 = IceBeam()
        self.move2 = HydroPump()
        self.move3 = surf()
        self.move4 = SwordsDance()
        self.type1 = "みず"
        self.type2 = ""
        self.ability1 = Torrent()
        self.capture_difficulty = 100
        super().setBase(95, 100, 85, 108, 70, 70)


class zacian(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.level = newlevel
        self.monster_name = "ザシアン"
        self.move1 = earthquake()
        self.move2 = surf()
        self.move3 = HydroPump()
        self.move4 = HornAttack()
        self.type1 = "フェアリー"
        self.type2 = "はがね"
        self.ability1 = IntrepidSword()
        self.capture_difficulty = 3
        super().setBase(92, 170, 115, 80, 115, 148)


class Kartana(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.level = newlevel
        self.monster = "カミツルギ"
        self.move1 = earthquake()
        self.move2 = surf()
        self.move3 = HydroPump()
        self.move4 = HornAttack()
        self.type1 = "くさ"
        self.type2 = "はがね"
        super().setBase(59, 181, 131, 59, 31, 109)

class Gyarados(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.level = newlevel
        self.monster_name = "ギャラドス"
        self.move1 = earthquake()
        self.move2 = surf()
        self.move3 = HydroPump()
        self.move4 = Thunderbolt()
        self.ability1 = intimidate()
        self.type1 = "みず"
        self.type2 = "ひこう"
        self.capture_difficulty = 180
        super().setBase(95, 125, 79, 60, 100, 81)

class UltraNecrozma(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.level = newlevel
        self.monster_name = "ウルトラネクロズマ"
        self.move1 = LightThatBurnsTheSky()
        self.move2 = Thunderbolt()
        self.move3 = HydroPump()
        self.move4 = Thunderbolt()
        self.ability1 = UltraAura()
        self.type1 = "エスパー"
        self.type2 = "ドラゴン"
        self.capture_difficulty = 3
        super().setBase(97, 167, 97, 167, 97, 129)

class Electivire(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.level = newlevel
        self.monster_name = "エレキブル"
        self.move1 = Thunderbolt()
        self.move2 = Thunderbolt()
        self.move3 = Thunderbolt()
        self.move4 = Thunderbolt()
        self.ability1 = MotorDrive()
        self.type1 = "でんき"
        self.type2 = ""
        self.capture_difficulty = 50
        super().setBase(75, 123, 67, 95, 85, 95)

class AsuraZoma(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.level = newlevel
        self.monster_name = "アスラゾーマ"
        self.move1 = GigaCrossBreak()
        self.move2 = SkullSplit()
        self.move3 = SheerCold()
        self.move4 = ByKilled()
        self.ability1 = AsuraZomaAbility()
        self.type1 = "かくとう"
        self.type2 = "あく"
        self.capture_difficulty = 25
        super().setBase(92, 124, 90, 102, 170, 102)

class Orthworm(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.level = newlevel
        self.monster_name = "ミミズズ"
        self.move1 = IronTail()
        self.move2 = earthquake()
        self.move3 = Drilling()
        self.move4 = IronDefense()
        self.ability1 = EarthEater()
        self.type1 = "はがね"
        self.type2 = ""
        self.capture_difficulty = 100
        super().setBase(70, 85, 145, 60, 55, 65)

class Lanturn(Pokemon):
    def __init__(self,newlevel,friendly):
        super().__init__(newlevel, friendly)
        self.level = newlevel
        self.monster_name = "ランターン"
        self.move1 = surf()
        self.move2 = Thunderbolt()
        self.move3 = RainDance()
        self.move4 = HydroPump()
        self.ability1 = WaterAbsorb()
        self.type1 = "みず"
        self.type2 = "でんき"
        self.capture_difficulty = 150
        super().setBase(125, 58, 58, 76, 76, 67)



def choice_pokemon(level, position: POSITION, Ptype=None):
    pokemon_by_type = {
        "ほのお": [Skeledirge, Cinderace],
        "みず": [Samurott, Gyarados, Lanturn],
        "でんき": [Electivire, Lanturn],
    }
    li = [Arboc, Rhydon, Orthworm]
    poke_list = pokemon_by_type.get(Ptype, li)
    poke = random.choice([poke(level, position) for poke in poke_list])
    return poke