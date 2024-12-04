import random
import math
import time
from variable_name import POSITION, ACTIVATE_TIMING, MOVE_CATEGORY ,WEATHER, DEBUG, FIELD

debug_flag = DEBUG.ON

#ポケモンのクラス
class Pokemon:
    def __init__(self, level:int, position:POSITION) -> None:
        self.monster_name :str
        self.level :int = level
        self.type1 :str
        self.type2 :str = ""
        self.PokeDexNo :int
        self.high :int
        self.weight :int
        self.capture_difficulty :int = 255
        self.familiarity :int
        self.baseEXP :int = 255
        self.move1 :Move
        self.move2 :Move
        self.move3 :Move
        self.move4 :Move
        self.ability1 :Ability
        self.ability2 :Ability = None
        self.ability3 :Ability = None
        self.set_individual_value()
        self.set_effort_value()
        self.set_rank_modifiers()
        self.position :POSITION = position
        self.money :int = 339
    
    #種族値の初回設定
    def setBase(self, H, A, B, C, D, S):
        self.baseH = H
        self.baseA = A
        self.baseB = B
        self.baseC = C
        self.baseD = D
        self.baseS = S

        #battleHは戦闘時の体力
        self.battleH = math.floor((self.baseH*2 + self.iH + (self.eH / 4)) * (self.level / 100) + (10 + self.level) * (self.rankH*0.5 + 1))
        
        self.set()
    
    #実数値の再計算
    def set(self):
        #print("実数値の再計算")
        self.H = math.floor((self.baseH*2 + self.iH + (self.eH / 4)) * (self.level / 100) + (10 + self.level) * self.rank_calc(self.rankH))
        self.A = math.floor(((self.baseA*2 + self.iA + (self.eA / 4)) * (self.level / 100) + 5) * self.rank_calc(self.rankA))
        self.B = math.floor(((self.baseB*2 + self.iB + (self.eB / 4)) * (self.level / 100) + 5) * self.rank_calc(self.rankB))
        self.C = math.floor(((self.baseC*2 + self.iC + (self.eC / 4)) * (self.level / 100) + 5) * self.rank_calc(self.rankC))
        self.D = math.floor(((self.baseD*2 + self.iD + (self.eD / 4)) * (self.level / 100) + 5) * self.rank_calc(self.rankD))
        self.S = math.floor(((self.baseS*2 + self.iS + (self.eS / 4)) * (self.level / 100) + 5) * self.rank_calc(self.rankS))

    #戦闘終了時に呼び出し
    def reset(self):
        self.set_rank_modifiers()
        self.set()

    
    #努力値の再計算
    def calc_effort_value(self, H, A, B, C, D, S):
        self.eH = self.eH + H if self.eH + H < 252 else 252
        self.eA = self.eA + A if self.eA + A < 252 else 252
        self.eB = self.eB + B if self.eB + B < 252 else 252
        self.eC = self.eC + C if self.eC + C < 252 else 252
        self.eD = self.eD + D if self.eD + D < 252 else 252
        self.eS = self.eS + S if self.eS + S < 252 else 252
    
    #努力値の初回設定
    def set_effort_value(self):
        self.eH = 0
        self.eA = 0
        self.eB = 0
        self.eC = 0
        self.eD = 0
        self.eS = 0

    #個体値の初回設定
    def set_individual_value(self, H = random.randint(0,31), A = random.randint(0,31), B = random.randint(0,31), C = random.randint(0,31), D = random.randint(0,31), S = random.randint(0,31)):
        self.iH = H
        self.iA = A
        self.iB = B
        self.iC = C
        self.iD = D
        self.iS = S

    #ランク補正の入力と実数値の再計算
    def set_rank_modifiers(self):
        #print("rankの再計算")
        self.rankH = 0
        self.rankA = 0
        self.rankB = 0
        self.rankC = 0
        self.rankD = 0
        self.rankS = 0

    #ランク補正の入力と実数値の再計算
    def calc_rank_modifiers(self, H, A, B, C, D, S):
        #print("rankの再計算")
        self.rankH = self.rankH + H
        self.rankA = self.rankA + A
        self.rankB = self.rankB + B
        self.rankC = self.rankC + C
        self.rankD = self.rankD + D
        self.rankS = self.rankS + S
        self.set()
    
    #ランク補正による実数値の倍率計算
    def rank_calc(self, a) -> float:
        #print("rankCalk")
        return (2 + a)/2 if a >= 0 else 2/(2 - a)

    
    def open(self):
        print(f"レベル{self.level}の{self.name}の個体値：{self.iH} {self.iA} {self.iB} {self.iC} {self.iD} {self.iS}")
        print(f"実数値は：{self.H} {self.A} {self.B} {self.C} {self.D} {self.S}")
        print(f"タイプ1:{self.type1} タイプ2:{self.type2}")
        print(f"現在HP:{self.battleH}")
        print("\n")

    def levelup(self):
        print("レベルアップ！")


#特性の発動タイミングをジャッジ
def judge_activate_or_pass(abilit:list, condition :ACTIVATE_TIMING):
    for t in abilit:
        if t == condition:
            return True
    return False


class InfoBattleField():
    def __init__(self) -> None:
        self.weather :WEATHER = WEATHER.FLAT
        self.field :FIELD = FIELD.FLAT

#技のクラス
class Move():
    def __init__(self):
        self.power :int
        self.category :MOVE_CATEGORY
        self.PP :int = 0
        self.maxPP :int = 0
        self.accuracy :int
        self.move_name :str
        self.type :str
        self.explain :str

    def activate(self, move_holder:Pokemon ,target_monster:Pokemon,info :InfoBattleField= None):
        pass

#特性のクラス
class Ability():
    def __init__(self) -> None:
        self.abilityName :str = "特性名が設定されていません"
        self.explain :str = "説明文が設定されていません"
        self.abilityType :list[ACTIVATE_TIMING] = []

    
    #特定タイミングで特性が発生しない場合、Falseを返す
    def activate_put_field(self, ability_holder:Pokemon, target_monster :Pokemon = None):
        if judge_activate_or_pass(self.abilityType, ACTIVATE_TIMING.PUT_FIELD) == False:
            return False

    def activate_primal_reversion(self, ability_holder:Pokemon):
        if judge_activate_or_pass(self.abilityType, ACTIVATE_TIMING.PRIMAL_REVERSION) == False:
            return False

    def activate_begin_turn(self, ability_holder:Pokemon, target_monster:Pokemon = None):
        if judge_activate_or_pass(self.abilityType, ACTIVATE_TIMING.BEGIN_TURN) == False:
            return False

    def activate_mega_evolution(self, ability_holder :Pokemon):
        if judge_activate_or_pass(self.abilityType, ACTIVATE_TIMING.MEGA_EVOLUTION) == False:
            return False

    def activate_use_move(self, ability_holder :Pokemon, target_monster:Pokemon, move_power_ratio:list, move :Move = None):
        if judge_activate_or_pass(self.abilityType, ACTIVATE_TIMING.USE_MOVE) == False:
            return False
    
    def activate_receive_move(self, ability_holder :Pokemon , attack_monster :Pokemon,move_power_ratio:list, move:Move = None):
        if judge_activate_or_pass(self.abilityType, ACTIVATE_TIMING.RECEIVE_MOVE) == False:
            return False

    def activate_end_turn(self, ability_holder :Pokemon, target_monster:Pokemon = None):
        if judge_activate_or_pass(self.abilityType, ACTIVATE_TIMING.END_TURN) == False:
            return False
        

class InfoItems():
    def __init__(self) -> None:
        self.money :int = 50
        self.floor :int = 1
        self.partylength :int = 6
        self.type :str = None
        
#捕獲率
def calc_capture_ratio(target_monster :Pokemon, try_capture_time :int) -> bool:
    mode = 2
    if mode ==1:
        A = math.floor((target_monster.H * 3 - target_monster.battleH * 2) * 4096 * target_monster.getHard * 2)
        level_compensation = math.floor((36 - 2 * target_monster.level)/10)
        B = math.floor((A / (target_monster.H * 3)) * level_compensation)
        D = B + 100 * try_capture_time
        print(f"捕獲値:{D}")
        if D > 1044480:
            return True
        else:
            return False
    elif mode == 2:
        A = math.floor( ( ((target_monster.H * 4 - target_monster.battleH * 3) ) * (target_monster.capture_difficulty ) ) * 100  / (target_monster.H) / 255 + 5 * try_capture_time)
        print_debug("捕獲率",A,debug_flag)
        if random.randint(1,99) < A:
            return True
        else:
            return False
        

def int_input(prompt,min,max):
    while True:
        i = input(prompt)
        if i.isdecimal():
            i = int(i)
            if min <= i <= max:
                break
            else:
                print(f"{min}から{max}の間で入力してください")
        #print(f"{i}は数値である必要があります")
    return i



def change_rank(monster:Pokemon, li:list):
    monster.calc_rank_modifiers(int(li[0]), int(li[1]), int(li[2]), int(li[3]), int(li[4]), int(li[5]))
    monster.set()
    i = 0
    time.sleep(0.2)
    for rank in li:
        
        rank = int(rank)
        statusLi = ["HP","こうげき","ぼうぎょ","とくこう","とくぼう","すばやさ"]
        messageLi = ["上がった！","下がった!"]
        
        if rank == 0:
            pass
        elif rank > 0:
            print(f"{monster.position}の{monster.monster_name}の{statusLi[i]}が{messageLi[0]}")
        elif rank < 0:
            print(f"{monster.position}の{monster.monster_name}の{statusLi[i]}が{messageLi[1]}")
        i += 1
        time.sleep(0.2)
    print("")


def print_debug(message:str, variable, flag:DEBUG):
    if flag == DEBUG.REALON:
        print(f"{message}:{variable}")
