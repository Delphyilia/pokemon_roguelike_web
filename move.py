from basedata import *
from basedata import Pokemon 
from variable_name import *
import math

debug_flag = DEBUG.ON

class TorchSong(Move):
    def __init__(self):
        super().__init__()
        self.power = 80
        self.category = MOVE_CATEGORY.SPECIAL
        self.PP = 10
        self.maxPP = 10
        self.accuracy = 100
        self.move_name = "フレアソング"
        self.type = "ほのお"
        self.explain = ""
    
    def activate(self,move_holder:Pokemon, target_monster: Pokemon,info = None):
        change_rank(move_holder,[0,0,0,1,0,0])

class ScorchingSands(Move):
    def __init__(self):
        super().__init__()
        self.power = 70
        self.category = MOVE_CATEGORY.SPECIAL
        self.PP = 10
        self.maxPP = 10
        self.accuracy = 100
        self.move_name = "ねっさのだいち"
        self.type = "じめん"
        self.explain = ""

class SlackOff(Move):
    def __init__(self):
        super().__init__()
        self.power = 70
        self.category = MOVE_CATEGORY.STATUS
        self.PP = 10
        self.maxPP = 10
        self.accuracy = 100
        self.move_name = "なまける"
        self.type = "ノーマル"
        self.explain = ""
    
    def activate(self, move_holder: Pokemon, target_monster: Pokemon,info = None):
        print(f"{move_holder.position}の{move_holder.monster_name}は怠けた！")
        recover :int = math.floor(move_holder.H / 2) if math.floor(move_holder.H / 2) + move_holder.battleH <= move_holder.H else move_holder.H - move_holder.battleH
        move_holder.battleH += recover
        print(f"HPが{recover}回復した！")
        print("")
        time.sleep(1)

class RainDance(Move):
    def __init__(self):
        super().__init__()
        self.power = 70
        self.category = MOVE_CATEGORY.STATUS
        self.PP = 5
        self.maxPP = 5
        self.accuracy = 100
        self.move_name = "あまごい"
        self.type = "みず"
        self.explain = ""
    
    def activate(self, move_holder: Pokemon, target_monster: Pokemon,info:InfoBattleField = None):
        print(f"{move_holder.position}の{move_holder.monster_name}はあまごいをした！")
        if info.weather == WEATHER.RAINY:
            print("既に雨が降っている！")
        else:
            info.weather = WEATHER.RAINY
            print("雨が降り出した！")
        print("")
        time.sleep(1)

class FireBlast(Move):
    def __init__(self):
        super().__init__()
        self.power = 110
        self.category = MOVE_CATEGORY.SPECIAL
        self.PP = 5
        self.maxPP = 5
        self.accuracy = 85
        self.move_name = "だいもんじ"
        self.type = "ほのお"
        self.explain = ""

class Trailblaze(Move):
    def __init__(self):
        super().__init__()
        self.power = 50
        self.category = MOVE_CATEGORY.PHISICS
        self.PP = 20
        self.maxPP = 20
        self.accuracy = 100
        self.move_name = "くさわけ"
        self.type = "くさ"
        self.explain = ""

    def activate(self, move_holder: Pokemon, target_monster: Pokemon,info = None):
        change_rank(move_holder,[0,0,0,0,0,1])

class Drilling(Move):
    def __init__(self):
        super().__init__()
        self.power = 50
        self.category = MOVE_CATEGORY.PHISICS
        self.PP = 20
        self.maxPP = 20
        self.accuracy = 100
        self.move_name = "くっさく"
        self.type = "じめん"
        self.explain = ""

    def activate(self, move_holder: Pokemon, target_monster: Pokemon,info = None):
        change_rank(move_holder,[0,0,0,0,0,1])

class GunkShot(Move):
    def __init__(self):
        super().__init__()
        self.power = 120
        self.category = MOVE_CATEGORY.PHISICS
        self.PP = 5
        self.maxPP = 5
        self.accuracy = 80
        self.move_name = "ダストシュート"
        self.type = "どく"
        self.explain = ""

class IceBeam(Move):
    def __init__(self):
        super().__init__()
        self.power = 90
        self.category = MOVE_CATEGORY.SPECIAL
        self.PP = 10
        self.maxPP = 10
        self.accuracy = 100
        self.move_name = "れいとうビーム"
        self.type = "こおり"
        self.explain = ""

class SwordsDance(Move):
    def __init__(self):
        super().__init__()
        self.power = 90
        self.category = MOVE_CATEGORY.STATUS
        self.PP = 10
        self.maxPP = 10
        self.accuracy = 100
        self.move_name = "つるぎのまい"
        self.type = "ノーマル"
        self.explain = ""

class PyroBall(Move):
    def __init__(self):
        super().__init__()
        self.power = 120
        self.category = MOVE_CATEGORY.PHISICS
        self.PP = 5
        self.maxPP = 5
        self.accuracy = 90
        self.move_name = "かえんボール"
        self.type = "ほのお"
        self.explain = ""

class earthquake(Move):
    def __init__(self):
        super().__init__()
        self.power = 100
        self.category = MOVE_CATEGORY.PHISICS
        self.PP = 10
        self.maxPP = 10
        self.accuracy = 100
        self.move_name = "地震"
        self.type = "じめん"
        self.explain = ""

class surf(Move):
    def __init__(self):
        super().__init__()
        self.power = 90
        self.category = MOVE_CATEGORY.SPECIAL
        self.PP = 15
        self.maxPP = 15
        self.accuracy = 100
        self.move_name = "波乗り"
        self.type = "みず"

class HornAttack(Move):
    def __init__(self):
        super().__init__()
        self.power = 65
        self.category = MOVE_CATEGORY.PHISICS
        self.PP = 25
        self.maxPP = 25
        self.accuracy = 100
        self.move_name = "つのでつく"
        self.type = "ノーマル"

class HydroPump(Move):
    def __init__(self):
        super().__init__()
        self.power = 110
        self.category = MOVE_CATEGORY.SPECIAL
        self.PP = 5
        self.maxPP = 5
        self.accuracy = 80
        self.move_name = "ハイドロポンプ"
        self.type = "みず"

class Thunderbolt(Move):
    def __init__(self):
        super().__init__()
        self.power = 90
        self.category = MOVE_CATEGORY.SPECIAL
        self.PP = 15
        self.maxPP = 15
        self.accuracy = 100
        self.move_name = "10万ボルト"
        self.type = "でんき"

class Judgment(Move):
    def __init__(self):
        super().__init__()
        self.power = 100
        self.category = MOVE_CATEGORY.SPECIAL
        self.PP = 10
        self.maxPP = 10
        self.accuracy = 100
        self.move_name = "裁きの礫"
        self.type = "ノーマル"

class LightThatBurnsTheSky(Move):
    def __init__(self):
        super().__init__()
        self.power = 200
        self.category = MOVE_CATEGORY.SPECIAL
        self.PP = 1
        self.maxPP = 1
        self.accuracy = 100
        self.move_name = "天焦がす滅亡の光"
        self.type = "エスパー"

class IronTail(Move):
    def __init__(self):
        super().__init__()
        self.power = 200
        self.category = MOVE_CATEGORY.PHISICS
        self.PP = 15
        self.maxPP = 15
        self.accuracy = 75
        self.move_name = "アイアンテール"
        self.type = "はがね"

class IronDefense(Move):
    def __init__(self):
        super().__init__()
        self.power = 200
        self.category = MOVE_CATEGORY.STATUS
        self.PP = 15
        self.maxPP = 15
        self.accuracy = 75
        self.move_name = "てっぺき"
        self.type = "はがね"
    
    def activate(self, move_holder: Pokemon, target_monster: Pokemon,info = None):
        print(f"{move_holder.position}の{move_holder.monster_name}はてっぺきを使った！")
        change_rank(target_monster, [0,0,2,0,0,0])


class SkullSplit(Move):
    def __init__(self):
        super().__init__()
        self.power = 80
        self.category = MOVE_CATEGORY.PHISICS
        self.PP = 10
        self.maxPP = 10
        self.accuracy = 100
        self.move_name = "かぶとわり"
        self.type = "かくとう"
    
    def activate(self, move_holder:Pokemon,target_monster :Pokemon,info = None):
        change_rank(target_monster, [0,0,-1,0,0,0])

class GigaCrossBreak(Move):
    def __init__(self):
        super().__init__()
        self.power = 100
        self.category = MOVE_CATEGORY.PHISICS
        self.PP = 5
        self.maxPP = 5
        self.accuracy = 120
        self.move_name = "ギガクロスブレイク"
        self.type = "でんき"

class SheerCold(Move):
    def __init__(self):
        super().__init__()
        self.power = 100
        self.category = MOVE_CATEGORY.PHISICS
        self.PP = 5
        self.maxPP = 5
        self.accuracy = 100
        self.move_name = "絶対零度（ドラクエ）"
        self.type = "こおり"

class ByKilled(Move):
    def __init__(self):
        super().__init__()
        self.power = 0
        self.category = MOVE_CATEGORY.STATUS
        self.PP = 10
        self.maxPP = 10
        self.accuracy = 100
        self.move_name = "バイキルト"
        self.type = "かくとう"
    
    def activate(self, ability_holder:Pokemon,target_monster: Pokemon,info :InfoBattleField= None):
        print(f"{ability_holder.position}の{ability_holder.monster_name}はバイキルトを唱えた！")
        change_rank(ability_holder, [0,2,0,0,0,0])