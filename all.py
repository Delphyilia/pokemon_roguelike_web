import random
import math
import time
import asyncio


class POSITION:
    WILD   :str = "野生"
    FRIEND :str = "味方"
    ENEMY  :str = "相手"


class ACTIVATE_TIMING:
    PUT_FIELD        :int = 0
    PRIMAL_REVERSION :int = 1   #ゲンシカイキ
    BEGIN_TURN       :int = 2
    MEGA_EVOLUTION   :int = 3
    TERASTAL         :int = 4
    USE_MOVE         :int = 5
    RECEIVE_MOVE     :int = 6
    END_TURN         :int = 7

class MOVE_CATEGORY:
    PHISICS :int = 0
    SPECIAL :int = 1
    STATUS  :int = 2

class ACTION_CATEGORY:
    MOVE1 :int = 0
    MOVE2 :int = 1
    MOVE3 :int = 2
    MOVE4 :int = 3
    
class BATTLE_IDX:
    ACTION_CHOICE  :int = 0
    TRY_ESCAPE     :int = 1
    MONSTER_CHANGE :int = 2
    TRY_CAPTURE    :int = 3
    USE_MOVE       :int = 4
    ENEMY_ONLY_MOVE:int = 5
    END_TURN       :int = 6
    CHANGE_CAUSE_LUSE :int = 7
    ENEMY_CHANGE:int = 8

class BATTLE_RESULT:
    WIN  :int = 0
    LOSE :int = 1
    ESCAPE:int = 2
    GET   :int = 3

class MAIN:
    SEARCHING :int = 0
    BATTLE    :int = 1
    LEVELUP   :int = 2
    NEXT_FLOOR:int = 3
    HP_RECOVER:int = 4
    GATETRAINER:int = 5

class MOVE_RESULT:
    ATTACK_WIN :int = 0


class WEATHER:
    FLAT        :int = 0
    SUNNY       :int = 1
    RAINY       :int = 2
    SANDSTORM   :int = 3
    SNOW        :int = 4

class FIELD:
    FLAT :int = 0
    ELECTRIC :int = 1
    GRASS :int = 2
    PHSYCO :int = 3
    MIST :int = 4

class DEBUG:
    OFF :int = 1
    ON  :int = 1
    OFF :int = 1
    REALON :int = 0




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
        

async def int_input(prompt,min,max):
    while True:
        print(prompt)
        await asyncio.sleep(0.1)
        i = input()
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



debug_flag = DEBUG.ON

class 	intimidate(Ability):
    def __init__(self):
        super().__init__()
        self.abilityName = "威嚇"
        self.abilityType = [1]
        self.explain = "登場したとき、相手の攻撃力を下げる。"
    
    def activate_put_field(self, ability_holder: Pokemon, target_monster: Pokemon = None):
        print(f"{ability_holder.position}の{ability_holder.monster_name}の威嚇！")
        print("")
        change_rank(target_monster, [0,-1,0,0,0,0])
        return True


class 	LightningRod(Ability):
    def __init__(self) -> None:
        super().__init__()
        self.abilityName = "避雷針"
        self.abilityType = [2]
        self.explain = "でんきタイプの技を無効にする。"
        
    def activate_receive_move(self, ability_holder: Pokemon, attack_monster: Pokemon, move_power_ratio: list, move:Move):
        if move.type == "でんき":
            print(f"{ability_holder.position}の{ability_holder.monster_name}の避雷針が発動！")
            print("")
            move_power_ratio.append(0)
            return True
        else:
            return False

class 	MotorDrive(Ability):
    def __init__(self) -> None:
        super().__init__()
        self.abilityName = "でんきエンジン"
        self.abilityType = [2]
        self.explain = "でんきタイプの技を無効化し、素早さを上げる。"
        
    def activate_receive_move(self, ability_holder: Pokemon, attack_monster: Pokemon, move_power_ratio: list, move:Move):
        if move.type == "でんき":
            print(f"{ability_holder.position}の{ability_holder.monster_name}の電気エンジンが発動！")
            move_power_ratio.append(0)
            change_rank(ability_holder, [0,0,0,0,0,1])
            return True
        else:
            return False

class IntrepidSword(Ability):
    def __init__(self) -> None:
        super().__init__()
        self.abilityName = "不撓の剣"
        self.abilityType = []
        self.explain = "登場したとき、攻撃力が上昇する。"
    
    def activate_put_field(self, ability_holder: Pokemon, target_monster: Pokemon = None):
        print(f"{ability_holder.position}の{ability_holder.monster_name}の不撓の剣が発動！")
        print("")
        change_rank(ability_holder, [0,1,0,0,0,0])
        return True

class AsuraZomaAbility(Ability):
    def __init__(self) -> None:
            super().__init__()
            self.abilityName = "阿修羅の力"
            self.explain = "複数の特性を併せ持つ。\nいきなりスカラ：登場したとき、スカラを唱えて防御力を上昇させる。\nいてつくはどう：ターン開始時、しばしば相手の上昇した能力をかき消す。\nデインブレイク：でんきタイプの技の威力が上がる。\n吹雪ブレスブレイク：こおりタイプの技の威力が上がる。"
    
    def activate_begin_turn(self, ability_holder: Pokemon, target_monster:Pokemon):
            if random.randint(1,10) < 6:
                li = [0,0,0,0,0,0]
                li[1] = -1 * target_monster.rankA if target_monster.rankA > 0 else 0
                li[2] = -1 * target_monster.rankB if target_monster.rankB > 0 else 0
                li[3] = -1 * target_monster.rankC if target_monster.rankC > 0 else 0
                li[4] = -1 * target_monster.rankD if target_monster.rankD > 0 else 0
                li[5] = -1 * target_monster.rankS if target_monster.rankS > 0 else 0
                active = False
                for i in li:
                        if i != 0:
                            active = True
                            break
                if active == True:
                        print(f"{ability_holder.position}の{ability_holder.monster_name}のいてつくはどうが発動！")
                        print("")
                        change_rank(target_monster,li)
            
                
            

    def activate_put_field(self, ability_holder: Pokemon, target_monster: Pokemon = None):
        print(f"{ability_holder.position}の{ability_holder.monster_name}のいきなりスカラが発動！")
        change_rank(ability_holder,[0,0,2,0,0,0])
    
    def activate_use_move(self, ability_holder: Pokemon, target_monster: Pokemon, move_power_ratio: list, move: Move = None):
        if move.type == "でんき":
                print(f"{ability_holder.position}の{ability_holder.monster_name}のデインブレイクが発動！")
                print(f"{move.move_name}の威力が上昇した！")
                move_power_ratio.append(1.5)
        elif move.type == "こおり":
            print(f"{ability_holder.position}の{ability_holder.monster_name}の吹雪ブレスブレイクが発動！")
            print(f"{move.move_name}の威力が上昇した！")
            move_power_ratio.append(1.5)

class Blaze(Ability):
    def __init__(self) -> None:
        super().__init__()
        self.abilityName = "もうか"
        self.explain = "HPが少ないとき、ほのおタイプの技威力が強化される。"

    def activate_use_move(self, ability_holder: Pokemon, target_monster: Pokemon, move_power_ratio: list, move: Move = None):
        if move.type == "ほのお" and ability_holder.battleH <= ability_holder.H / 3:
            print(f"{ability_holder.position}の{ability_holder.monster_name}のもうかが発動！")
            move_power_ratio.append(1.5)

class Torrent(Ability):
    def __init__(self) -> None:
        super().__init__()
        self.abilityName = "げきりゅう"
        self.explain = "HPが少ないとき、みずタイプの技威力が強化される。"

    def activate_use_move(self, ability_holder: Pokemon, target_monster: Pokemon, move_power_ratio: list, move: Move = None):
        if move.type == "みず" and ability_holder.battleH <= ability_holder.H / 3:
            print(f"{ability_holder.position}の{ability_holder.monster_name}のもうかが発動！")
            move_power_ratio.append(1.5)

class EarthEater(Ability):
    def __init__(self) -> None:
        super().__init__()
        self.abilityName = "どしょく"
        self.explain = "じめんタイプの技を無効化する"
    
    def activate_receive_move(self, ability_holder: Pokemon, attack_monster: Pokemon, move_power_ratio: list, move: Move = None):
        if move.type == "じめん":
            move_power_ratio.append(0)
            recover = math.floor(ability_holder.H / 4) if math.floor(ability_holder.H / 4) + ability_holder.battleH <= ability_holder.H else ability_holder.H - ability_holder.battleH
            print(f"{ability_holder.position}の{ability_holder.monster_name}のどしょくが発動！")
            #print(f"HPが{recover}回復した！")
            print(f"{ability_holder.position}の{ability_holder.monster_name}にじめん技は効果がない！")
            print("")

class WaterAbsorb(Ability):
    def __init__(self) -> None:
        super().__init__()
        self.abilityName = "ちょすい"
        self.explain = "みずタイプの技を無効化する"
    
    def activate_receive_move(self, ability_holder: Pokemon, attack_monster: Pokemon, move_power_ratio: list, move: Move = None):
        if move.type == "みず":
            move_power_ratio.append(0)
            recover = math.floor(ability_holder.H / 4) if math.floor(ability_holder.H / 4) + ability_holder.battleH <= ability_holder.H else ability_holder.H - ability_holder.battleH
            print(f"{ability_holder.position}の{ability_holder.monster_name}のちょすいが発動！")
            #print(f"HPが{recover}回復した！")
            print(f"{ability_holder.position}の{ability_holder.monster_name}にじめん技は効果がない！")
            print("")
        

class Libero(Ability):
    def __init__(self) -> None:
        super().__init__()
        self.abilityName = "リベロ"
        self.explain = "技を出すとき、自分のタイプが技と同じタイプに変化する。"
    
    def activate_use_move(self, ability_holder: Pokemon, target_monster: Pokemon, move_power_ratio: list, move: Move = None):
        print(f"{ability_holder.position}の{ability_holder.monster_name}のリベロが発動！")
        print(f"{move.type}タイプに変化した！")
        print("")
        ability_holder.type1 = move.type
        
class Omnipotent(Ability):
    def __init__(self) -> None:
        super().__init__()
        self.abilityName = "全知全能"
        self.abilityType = [1,2]
        self.explain = "登場したとき、全ての能力が上昇する。体力が満タンのとき、受けるダメージを半減する。たまに敵の攻撃を回避する。ターン終了時にHPを少し回復する。"

    def activate_put_field(self, ability_holder: Pokemon, target_monster: Pokemon = None):
        print(f"\n{ability_holder.position}の{ability_holder.monster_name}の全知全能の力で全能力が上昇する…！\n")
        print("")
        change_rank(ability_holder, [0,1,1,1,1,1])
        return True

    def activate_receive_move(self, ability_holder:Pokemon, attack_monster:Pokemon, li:list = None, move = None):
        if random.randint(1,10) < 3:
                print(f"{ability_holder.position}の{ability_holder.monster_name}の全知全能の力により攻撃を回避した！")
                print("")

                li.append(0)
                return True
        elif ability_holder.battleH == ability_holder.H:
                print(f"{ability_holder.position}の{ability_holder.monster_name}の全知全能の力はダメージを軽減する…！")
                print("")
                li.append(0.5)
                return True
        return False
    
    def activate_end_turn(self, ability_holder: Pokemon, target_monster:Pokemon = None):
        if ability_holder.battleH < ability_holder.H:
            heal = math.floor(ability_holder.H / 8) if  ability_holder.battleH + math.floor(ability_holder.H / 8) <= ability_holder.H else ability_holder.H - ability_holder.battleH
            print(f"{ability_holder.position}の{ability_holder.monster_name}の全知全能の力でキズが回復してゆく…！")
            print(f"HPが{heal}回復した！")
            print("")
            ability_holder.battleH += heal

class UltraAura(Ability):
    def __init__(self) -> None:
        super().__init__()
        self.abilityName = "ウルトラオーラ"
        self.abilityType = [1,2]
        self.explain = "登場したとき、全ての能力が上昇する。体力が満タンのとき、受けるダメージを半減する。たまに敵の攻撃を回避する。ターン終了時に相手のHPを少し減少させる。。"

    def activate_put_field(self, ability_holder: Pokemon, target_monster: Pokemon = None):
        print(f"\n{ability_holder.position}の{ability_holder.monster_name}はオーラを纏い全能力が上昇する…！\n")
        change_rank(ability_holder, [0,1,1,1,1,1])
        return True

    def activate_receive_move(self, ability_holder:Pokemon, attack_monster:Pokemon, li:list = None, move = None):
        if random.randint(1,10) < 3:
                print(f"{ability_holder.position}の{ability_holder.monster_name}のウルトラオーラにより攻撃を回避した！")
                print("")
                li.append(0)
                return True
        elif ability_holder.battleH == ability_holder.H:
                print(f"{ability_holder.position}の{ability_holder.monster_name}のウルトラオーラはダメージを軽減する…！")
                print("")
                li.append(0.5)
                return True
        return False
    
    def activate_end_turn(self, ability_holder: Pokemon, target_monster: Pokemon = None):
        damage = math.floor(target_monster.H / 8) if target_monster.battleH - math.floor(target_monster.H / 8) >= 1 else target_monster.battleH - 1
        if damage != 0:      
            print(f"{ability_holder.position}の{ability_holder.monster_name}のオーラが溢れ出す…")
            time.sleep(0.2)
            print(f"{target_monster.position}の{target_monster.monster_name}に{damage}ダメージ！")
            time.sleep(0.2)
            print("")
            target_monster.battleH -= damage
            return True
        else:
                return False
        


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





#============================
#タイプ相性表 https://vigne-cla.com/9-5/
#============================
typetable = {'':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':1.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':1.0,'フェアリー':1.0},
            'ノーマル':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':1.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':0.5,'ゴースト':0.0,'ドラゴン':1.0,'あく':1.0,'はがね':0.5,'フェアリー':1.0},
            'ほのお':{'':1.0,'ノーマル':1.0,'ほのお':0.5,'みず':0.5,'でんき':1.0,'くさ':2.0,'こおり':2.0,'かくとう':1.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':2.0,'いわ':0.5,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':2.0,'フェアリー':1.0},
            'みず':{'':1.0,'ノーマル':1.0,'ほのお':2.0,'みず':0.5,'でんき':1.0,'くさ':0.5,'こおり':1.0,'かくとう':1.0,'どく':1.0,'じめん':2.0,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':2.0,'ゴースト':1.0,'ドラゴン':0.5,'あく':1.0,'はがね':1.0,'フェアリー':1.0},
            'でんき':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':2.0,'でんき':0.5,'くさ':0.5,'こおり':1.0,'かくとう':1.0,'どく':1.0,'じめん':0.0,'ひこう':2.0,'エスパー':1.0,'むし':1.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':0.5,'あく':1.0,'はがね':1.0,'フェアリー':1.0},
            'くさ':{'':1.0,'ノーマル':1.0,'ほのお':0.5,'みず':2.0,'でんき':1.0,'くさ':0.5,'こおり':1.0,'かくとう':1.0,'どく':0.5,'じめん':2.0,'ひこう':0.5,'エスパー':1.0,'むし':0.5,'いわ':2.0,'ゴースト':1.0,'ドラゴン':0.5,'あく':1.0,'はがね':0.5,'フェアリー':1.0},
            'こおり':{'':1.0,'ノーマル':1.0,'ほのお':0.5,'みず':0.5,'でんき':1.0,'くさ':2.0,'こおり':0.5,'かくとう':1.0,'どく':1.0,'じめん':2.0,'ひこう':2.0,'エスパー':1.0,'むし':1.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':2.0,'あく':1.0,'はがね':0.5,'フェアリー':1.0},
            'かくとう':{'':1.0,'ノーマル':2.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':2.0,'かくとう':1.0,'どく':0.5,'じめん':1.0,'ひこう':0.5,'エスパー':0.5,'むし':0.5,'いわ':2.0,'ゴースト':0.0,'ドラゴン':1.0,'あく':2.0,'はがね':2.0,'フェアリー':0.5},
            'どく':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':2.0,'こおり':1.0,'かくとう':1.0,'どく':0.5,'じめん':0.5,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':0.5,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':0.0,'フェアリー':2.0},
            'じめん':{'':1.0,'ノーマル':1.0,'ほのお':2.0,'みず':1.0,'でんき':2.0,'くさ':0.5,'こおり':1.0,'かくとう':1.0,'どく':2.0,'じめん':1.0,'ひこう':0.0,'エスパー':1.0,'むし':0.5,'いわ':2.0,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':2.0,'フェアリー':1.0},
            'ひこう':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':0.5,'くさ':2.0,'こおり':1.0,'かくとう':2.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':2.0,'いわ':0.5,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':0.5,'フェアリー':1.0},
            'エスパー':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':2.0,'どく':2.0,'じめん':1.0,'ひこう':1.0,'エスパー':0.5,'むし':1.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':1.0,'あく':0.0,'はがね':0.5,'フェアリー':1.0},
            'むし':{'':1.0,'ノーマル':1.0,'ほのお':0.5,'みず':1.0,'でんき':1.0,'くさ':2.0,'こおり':1.0,'かくとう':0.5,'どく':0.5,'じめん':1.0,'ひこう':0.5,'エスパー':2.0,'むし':1.0,'いわ':1.0,'ゴースト':0.5,'ドラゴン':1.0,'あく':2.0,'はがね':0.5,'フェアリー':0.5},
            'いわ':{'':1.0,'ノーマル':1.0,'ほのお':2.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':2.0,'かくとう':0.5,'どく':1.0,'じめん':0.5,'ひこう':2.0,'エスパー':1.0,'むし':2.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':0.5,'フェアリー':1.0},
            'ゴースト':{'':1.0,'ノーマル':0.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':1.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':2.0,'むし':1.0,'いわ':1.0,'ゴースト':2.0,'ドラゴン':1.0,'あく':0.5,'はがね':1.0,'フェアリー':1.0},
            'ドラゴン':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':1.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':2.0,'あく':1.0,'はがね':0.5,'フェアリー':0.0},
            'あく':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':0.5,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':2.0,'むし':1.0,'いわ':1.0,'ゴースト':2.0,'ドラゴン':1.0,'あく':0.5,'はがね':1.0,'フェアリー':0.5},
            'はがね':{'':1.0,'ノーマル':1.0,'ほのお':0.5,'みず':0.5,'でんき':0.5,'くさ':1.0,'こおり':2.0,'かくとう':1.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':2.0,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':0.5,'フェアリー':2.0},
            'フェアリー':{'':1.0,'ノーマル':1.0,'ほのお':0.5,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':2.0,'どく':0.5,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':2.0,'あく':2.0,'はがね':0.5,'フェアリー':1.0}}

def compatibility_ratio(attack :str, block :str) -> float:
    return typetable[attack][block]



debug_flag = DEBUG.ON



async def battle_handling(friend_monsters:list[Pokemon], enemy_monsters:list[Pokemon], info_battle_field :InfoBattleField = None ,info_items :InfoItems = None) -> BATTLE_RESULT:
    friend :Pokemon = friend_monsters[0]
    enemy :Pokemon = enemy_monsters[0]



    escape_time = 0
    capture_time = 0

    idx = BATTLE_IDX.ACTION_CHOICE
    money:int = 0
    friends_ave_level:int = 0
    i = 1
    for p in friend_monsters:
            friends_ave_level += p.level
            i += 1
    friends_ave_level = math.floor(friends_ave_level / i)
    if enemy.position == POSITION.WILD:
            print(f"野生の LV.{enemy.level} {enemy.monster_name} が出現！")
            await asyncio.sleep(0.1)
            time.sleep(0.5)
            print(f"味方の LV.{friend.level} {friend.monster_name} を繰り出した！")
            await asyncio.sleep(0.1)
            time.sleep(0.5)
            print("")
    else:
            print(f"相手は LV.{enemy.level} {enemy.monster_name} を繰り出した！")
            await asyncio.sleep(0.1)
            time.sleep(0.5)
            print(f"味方の LV.{friend.level} {friend.monster_name} を繰り出した！")
            await asyncio.sleep(0.1)
            time.sleep(0.5)
            print("")

    if friend.S >= enemy.S:
        friend.ability1.activate_put_field(friend, enemy)
        enemy.ability1.activate_put_field(enemy, friend)
    else:
        enemy.ability1.activate_put_field(enemy, friend)
        friend.ability1.activate_put_field(friend, enemy)
    
    print(f"味方の LV.{friend.level} {friend.monster_name}:{friend.battleH}/{friend.H}")
    print(f"{enemy.position}の   LV.{enemy.level}{enemy.monster_name}:{enemy.battleH}/{enemy.H}")


    while True:
        
        while idx == BATTLE_IDX.ACTION_CHOICE:
            print("雨が降り続いている…") if info_battle_field.weather == WEATHER.RAINY else None
            print("日差しが強い…") if info_battle_field.weather == WEATHER.SUNNY else None
            print("床に電流が流れ続けている…") if info_battle_field.field == FIELD.ELECTRIC  else None
            print("")
            print("コマンドを数字で入力しよう！")
            print("0:逃げる    1:交換    2:捕まえる    3:戦う\n→")
            await asyncio.sleep(0.1)
            action_choice :int = await int_input(f"",0,3)
            if 0 == action_choice:
                print("")
                idx = BATTLE_IDX.TRY_ESCAPE

            elif 1 == action_choice:
                print("")
                idx = BATTLE_IDX.MONSTER_CHANGE
            
            elif 2 == action_choice:
                print("")
                idx = BATTLE_IDX.TRY_CAPTURE
            
            elif 3 == action_choice:
                if friend.move1.PP <= 0 and friend.move2.PP <= 0 and friend.move3.PP <= 0 and friend.move4.PP <= 0:
                        print("すべての技のPPがない！")
                        print(f"{friend.position}の{friend.monster_name}はランダムに技を使った！")
                        action_choice = random.randint(4,7)
                        idx = BATTLE_IDX.USE_MOVE

                else:
                    action_choice = await int_input(f"4:{friend.move1.move_name} {friend.move1.PP}/{friend.move1.maxPP}    5:{friend.move2.move_name} {friend.move2.PP}/{friend.move2.maxPP}    6:{friend.move3.move_name} {friend.move3.PP}/{friend.move3.maxPP}    7:{friend.move4.move_name} {friend.move4.PP}/{friend.move4.maxPP}\n→",4,7)
                    if action_choice == 4 and friend.move1.PP <= 0:
                        print("PPが無いので使用できない！")
                        break
                    elif action_choice == 5 and friend.move2.PP <= 0:
                        print("PPが無いので使用できない！")
                        break
                    elif action_choice == 6 and friend.move3.PP <= 0:
                        print("PPが無いので使用できない！")
                        break
                    elif action_choice == 7 and friend.move4.PP <= 0:
                        print("PPが無いので使用できない！")
                        break
                    print("")

                    idx = BATTLE_IDX.USE_MOVE
            else:
                pass
        
        while idx == BATTLE_IDX.TRY_ESCAPE:
            if enemy.position == POSITION.WILD:
                if friend.S >= enemy.S:
                    print("敵から逃走した！")
                    print("")
                    reset_status(friend_monsters)
                    return BATTLE_RESULT.ESCAPE
                else:
                    if ((friend.S * 128 / enemy.S) + 30 * escape_time) % 256 > random.randint(0,255) :
                        print("敵から逃走した！")
                        print("")
                        reset_status(friend_monsters)
                        return BATTLE_RESULT.ESCAPE
                    else:
                        print("逃げられなかった！")
                        print("")
                        print_debug("逃走確率",((friend.S * 128 / enemy.S) + 30 * escape_time) % 256,debug_flag)
                        escape_time += 1
                        idx = BATTLE_IDX.ENEMY_ONLY_MOVE
            else:
                print("勝負から逃げることはできない！")
                idx = BATTLE_IDX.ACTION_CHOICE
        
        while idx == BATTLE_IDX.TRY_CAPTURE:
            if enemy.position == POSITION.WILD:
                if calc_capture_ratio(enemy, capture_time) == True:
                    print(f"{enemy.monster_name}を捕獲した！")
                    enemy.position = POSITION.FRIEND

                    if len(friend_monsters) == info_items.partylength:
                        print(f"連れてゆけるのは{info_items.partylength}匹までです。誰かを手放してください。")
                        i = 1
                        for p in range(len(friend_monsters)):
                            print(f"{i}: Lv.{friend_monsters[i-1].level} {friend_monsters[i - 1].monster_name}")
                            i += 1
                        delete_choice = await int_input("誰を手放しますか？",1,len(friend_monsters))
                        if 1 <= delete_choice <= 12:
                            del_monster =  friend_monsters.pop(delete_choice - 1)
                        print(f"ばいばい、{del_monster.monster_name}！")
                
                    money = math.floor(enemy.baseEXP * (( (2 * enemy.level + 10) / (enemy.level + friends_ave_level + 10)) ** 2.5) + 1)
                    print("勝利！")
                    #print(f"{money}円手に入れた！")
                    print("")
                    money = 0
                    info_items.money += money
                    friend_monsters.append(enemy)
                    reset_status(friend_monsters)
                    return BATTLE_RESULT.GET
                else:
                    print("捕獲に失敗した…")
                    capture_time += 1
                    idx = BATTLE_IDX.ENEMY_ONLY_MOVE
            elif enemy.position == POSITION.ENEMY:
                print("捕獲不可能だ！")
                idx = BATTLE_IDX.ACTION_CHOICE
        
        while idx == BATTLE_IDX.MONSTER_CHANGE:
                print("交換機能は未実装です")
                idx = BATTLE_IDX.ACTION_CHOICE
        
        while idx == BATTLE_IDX.ENEMY_ONLY_MOVE:
            await move_handling(enemy, friend, info_battle_field)
            if friend.battleH != 0:
                idx = BATTLE_IDX.END_TURN
            elif friend.battleH == 0 and len(friend_monsters) == 1:
                    print(f"{friend.monster_name}は倒れた！")
                    print("戦える仲間がいない！")
                    return BATTLE_RESULT.LOSE
            else:
                    idx = BATTLE_IDX.CHANGE_CAUSE_LUSE
                    
        
        while idx == BATTLE_IDX.CHANGE_CAUSE_LUSE:
            friend_monsters.pop(0)
            print(f"{friend.monster_name}は倒れた！")
            print("")

            i = 1
            for p in range(len(friend_monsters)):
                print(f"{i}: Lv.{friend_monsters[i-1].level} {friend_monsters[i - 1].monster_name}")
                i += 1
            print("")
            p = await int_input("誰を繰り出しますか？",1,len(friend_monsters))
            friend_monsters[0],friend_monsters[p-1] = friend_monsters[p-1],friend_monsters[0]
            friend = friend_monsters[0]
            print(f"味方の LV.{friend.level} {friend.monster_name} を繰り出した！")
            friend.ability1.activate_put_field(friend, enemy)
            idx = BATTLE_IDX.ACTION_CHOICE
            

        
        while idx == BATTLE_IDX.USE_MOVE:

            move_quickness :list[Pokemon]
            if friend.S >= enemy.S:
                move_quickness = [friend, enemy]
                friend.ability1.activate_begin_turn(friend, enemy)
                enemy.ability1.activate_begin_turn(enemy, friend)
            else:
                enemy.ability1.activate_begin_turn(enemy, friend)
                friend.ability1.activate_begin_turn(friend, enemy)
                move_quickness = [enemy, friend]
            
            
            if MOVE_RESULT.ATTACK_WIN == await move_handling(move_quickness[0], move_quickness[1], info_battle_field,action_choice):
                    if move_quickness[0].position == POSITION.FRIEND and len(enemy_monsters) == 1:
                        reset_status(friend_monsters)
                        money = math.floor(10* enemy.baseEXP * (( (2 * enemy.level + 10) / (enemy.level + friends_ave_level + 10)) ** 2.5) + 1)
                        print("勝利！")
                        print(f"{money}円手に入れた！")
                        print("")
                        info_items.money += money
                        return BATTLE_RESULT.WIN
                    elif move_quickness[0].position == POSITION.FRIEND and len(enemy_monsters) != 1:
                        money += math.floor(enemy.baseEXP * 2 * (( (2 * enemy.level + 10) / (enemy.level + friends_ave_level + 10)) ** 2.5) + 1)
                        idx = BATTLE_IDX.ENEMY_CHANGE
                        break
                    elif len(friend_monsters) != 1:
                        idx = BATTLE_IDX.CHANGE_CAUSE_LUSE
                        break
                    else :
                        return BATTLE_RESULT.LOSE

            if MOVE_RESULT.ATTACK_WIN == await move_handling(move_quickness[1], move_quickness[0], info_battle_field,action_choice):
                    if move_quickness[1].position == POSITION.FRIEND and len(enemy_monsters) == 1:
                        reset_status(friend_monsters)
                        money = math.floor(10 * enemy.baseEXP * (( (2 * enemy.level + 10) / (enemy.level + friends_ave_level + 10)) ** 2.5) + 1)
                        print("勝利！")
                        print(f"{money}円手に入れた！")
                        print("")
                        info_items.money += money
                        return BATTLE_RESULT.WIN
                    elif  move_quickness[1].position == POSITION.FRIEND and len(enemy_monsters) != 1:
                        money += math.floor(enemy.baseEXP * 2 * (( (2 * enemy.level + 10) / (enemy.level + friends_ave_level + 10)) ** 2.5) + 1)
                        idx = BATTLE_IDX.ENEMY_CHANGE
                        break
                    elif len(friend_monsters) != 1:
                        idx = BATTLE_IDX.CHANGE_CAUSE_LUSE
                        break
                    else:
                        return BATTLE_RESULT.LOSE
            
            idx = BATTLE_IDX.END_TURN
                        

            
        
        while idx == BATTLE_IDX.END_TURN:
            if friend.S >= enemy.S:
                friend.ability1.activate_end_turn(friend, enemy)
                enemy.ability1.activate_end_turn(enemy, friend)
            else:
                enemy.ability1.activate_end_turn(enemy, friend)
                friend.ability1.activate_end_turn(friend, enemy)

            print(f"味方の LV.{friend.level} {friend.monster_name}:{friend.battleH}/{friend.H}")
            print(f"{enemy.position}の   LV.{enemy.level}{enemy.monster_name}:{enemy.battleH}/{enemy.H}")

            idx = BATTLE_IDX.ACTION_CHOICE
        
        while idx == BATTLE_IDX.ENEMY_CHANGE:
            enemy_monsters.pop(0)
            print(f"{enemy.monster_name}は倒れた！")
            enemy = enemy_monsters[0]
            print(f"相手は LV.{enemy.level} {enemy.monster_name} を繰り出した！")
            enemy.ability1.activate_put_field(enemy, friend)
            idx = BATTLE_IDX.ACTION_CHOICE

async def move_handling(attack_monster :Pokemon, block_monster :Pokemon ,info_battle_field : InfoBattleField,usemove_number = None) -> MOVE_RESULT:
    if attack_monster.position == POSITION.WILD:
        usemove_number = random.randint(4,7)
    elif attack_monster.position == POSITION.ENEMY:
        usemove_number = random.randint(4,7)
        #技威力が高いやつを入れたい
    match (usemove_number):
        case 4:
            move :Move = attack_monster.move1
        case 5:
            move :Move = attack_monster.move2
        case 6:
            move :Move = attack_monster.move3
        case 7:
            move :Move = attack_monster.move4
    move.PP -= 1
        
    
    
    move_power_ratio :list[float] = [1.0]
    attack_ability = attack_monster.ability1.activate_use_move(attack_monster, block_monster, move_power_ratio,move)
    block_ability = block_monster.ability1.activate_receive_move(block_monster,attack_monster, move_power_ratio,move)

    skip = False
    for i in move_power_ratio:
        if i == 0:
            skip = True
    if random.randint(0,99) < move.accuracy:
        if skip == False and move.category != MOVE_CATEGORY.STATUS:
            compatibility = float(compatibility_ratio(move.type, block_monster.type1))
            compatibility = float(compatibility * compatibility_ratio(move.type, block_monster.type2))

            if move.type == "ほのお" and info_battle_field.weather == WEATHER.SUNNY:
                    
                    print("晴れ状態でほのお技の威力が上昇した！")
                    move_power_ratio.append(1.5)

            if move.type == "みず" and info_battle_field.weather == WEATHER.RAINY:
                    print("雨状態でみず技の威力が上昇した！")
                    move_power_ratio.append(1.5)
            
            if move.type == "でんき" and info_battle_field.field == FIELD.ELECTRIC:
                    print("エレキフィールドの効果ででんき技の威力が上昇した！")
                    move_power_ratio.append(1.5)

            match compatibility:
                    case 0:
                            compatibility_message = "効果がないようだ…"
                    case 0.25:
                            compatibility_message = "効果は超いまひとつだ…"
                    case 0.5:
                            compatibility_message = "効果はいまひとつだ…"
                    case 1:
                            compatibility_message = "効果は普通のようだ"
                    case 2:
                            compatibility_message = "効果は抜群だ！"
                    case 4:
                            compatibility_message = "効果は超抜群だ！"
            
            if move.category == MOVE_CATEGORY.PHISICS:
                attack_st = attack_monster.A
                block_st = block_monster.B
            elif move.category == MOVE_CATEGORY.SPECIAL:
                attack_st = attack_monster.C
                block_st = block_monster.D

            type_match = False
            if attack_monster.type1 == move.type:
                    move_power_ratio.append(1.5)
                    type_match = True
            if attack_monster.type2 == move.type:
                    move_power_ratio.append(1.5)
                    type_match = True



            ratio = 1.0
            for i in move_power_ratio:
                ratio = ratio * i

            damage = math.floor((((attack_monster.level * 2/5 + 2) * move.power * attack_st / block_st) / 50 + 2) * random.randint(85,100) / 100 * compatibility * ratio)
            damage = 1 if damage == 0 else damage
            damage = 0 if compatibility == 0 else damage

            print("")
            time.sleep(0.2)
            await asyncio.sleep(0.1)
            print("タイプ一致ボーナス！") if type_match == True else None
            time.sleep(0.2)
            await asyncio.sleep(0.1)
            print(f"{attack_monster.position}の{attack_monster.monster_name}の{move.move_name}！")
            time.sleep(0.2)
            await asyncio.sleep(0.1)
            print(compatibility_message)
            time.sleep(0.2)
            await asyncio.sleep(0.1)
            print(f"{block_monster.position}の{block_monster.monster_name}に{damage}ダメージ！\n")
            time.sleep(0.2)
            await asyncio.sleep(0.1)

            print_debug("倍率補正",move_power_ratio,debug_flag)
            

            if block_monster.battleH - damage < 0:
                    print("オーバーキル！")
                    
            damage = damage if block_monster.battleH - damage >= 0 else block_monster.battleH

            block_monster.battleH = block_monster.battleH - damage

            if block_monster.battleH == 0:
                    print(f"{block_monster.monster_name}のHPが0になった！")
                    print("")
                    time.sleep(0.2)
                    await asyncio.sleep(0.1)
                    return MOVE_RESULT.ATTACK_WIN
            
            move.activate(attack_monster,block_monster,info_battle_field)
            print_debug(block_monster.rankB,block_monster.B,debug_flag)

        elif move.category == MOVE_CATEGORY.STATUS:
                move.activate(attack_monster,block_monster,info_battle_field)   

        elif skip == True:
                print(f"{block_monster.position}の{block_monster.monster_name}には効果がないようだ…")
                await asyncio.sleep(0.1)
        elif skip != True:
            print(f"{attack_monster.position}の{attack_monster.monster_name}の技は外れてしまった！")
            await asyncio.sleep(0.1)
            time.sleep(0.2)
            print("")
            

"""
def compare_power(enemy :Pokemon, ) -> Move:
    top_move :Move= enemy.move1
    if enemy.move2.power > top_move.power:
        top_move = enemy.move2
    if enemy.move3.power > top_move
"""

        

class InfoDamage:
        def __init__(self) -> None:
            self.move_power_ratio :list[float] = [1.0]
            self.move :Move
            self.compatibility_message :str
            self.attack_st :int
            self.block_st :int
            self.position :POSITION

        


def reset_status(monsters:list[Pokemon], monster:Pokemon = None):
        for m in monsters:
            m.reset()
        if monster != None:
            monster.reset()




debug_flag = DEBUG.ON


async def main():
    info_items = InfoItems()
    party :list[Pokemon] = [Pokemon]
    
    idx = MAIN.SEARCHING
    info_battle_field = InfoBattleField()
    
    #バイナリデータを読み込むための変数
    data :list[list[Pokemon], InfoItems, InfoBattleField] = []
   
    
   
    print("ポケットモンスター(?)の世界へようこそ！")
    print("まずは、最初の仲間を選んでね！")
    print("1: LV.5 ランターン 2: LV.5 アーボック 3: LV.5 サイドン\n数字を入力:")
    await asyncio.sleep(0.1)
    n = await int_input("",1,6)
    await asyncio.sleep(0.1)
    match n:
        case 1:
            party[0] = Lanturn(5, POSITION.FRIEND)
        case 2:
            party[0] = Arboc(5, POSITION.FRIEND)
        case 3:
            party[0] = Rhydon(5, POSITION.FRIEND)
        case 4:
            party[0] = UltraNecrozma(100, POSITION.FRIEND)
        case 5:
            party[0] = AsuraZoma(20, POSITION.FRIEND)
        case 6:
            party[0] = Lanturn(20,POSITION.FRIEND)
    
  
        

    

    while True:
        while idx == MAIN.SEARCHING:
            if info_items.floor % 10 == 0:
                idx = MAIN.GATETRAINER
                break

        
            print("どうする？")
            print("1:進む 2:手持ちを確認する 3:セーブする 4:セーブしてゲームを終了 5:パーティの順番を変更\n→")
            await asyncio.sleep(0.1)
            action = await int_input("",1,5)
            await asyncio.sleep(0.1)
            match action:
                case 1:
                    await asyncio.sleep(0.1)
                    print("探索します…")
                    await asyncio.sleep(0.1)
                    time.sleep(1)
                    exploration  = random.randint(1,100)
                    if exploration <= 1:
                        print("何もなかった")
                        await asyncio.sleep(0.1)
                        print("")
                    elif exploration >= 85:
                        idx = MAIN.LEVELUP
                    elif exploration >= 65:
                        idx = MAIN.HP_RECOVER
                    elif exploration >= 50:
                        idx = MAIN.NEXT_FLOOR
                    else:    
                        idx = MAIN.BATTLE
                    break
                case 2:
                    i = 1
                    for p in range(len(party)):
                        await asyncio.sleep(0.1)
                        print(f"{i}: Lv.{party[i-1].level} {party[i - 1].monster_name}")
                        i += 1
                    print("誰の情報を見る？")
                    await asyncio.sleep(0.1)
                    status_open = await int_input("",1,len(party))
                    i = 1
                    for p in party:
                        if i == status_open:
                            print("")
                            print(f"Lv.{p.level} {p.monster_name}")
                            print(f"タイプ1:{p.type1} タイプ2:{p.type2}")
                            print(f"技1:{p.move1.move_name} 技2:{p.move2.move_name} 技3:{p.move3.move_name} 技4:{p.move4.move_name}")
                            print(f"特性:{p.ability1.abilityName}")
                            print(f"{p.ability1.explain}")
                            print("")
                            await asyncio.sleep(0.1)
                        i += 1
                    break
                case 3:
                    print("セーブ機能はweb版では対応しておりません")
                    await asyncio.sleep(0.1)
                    break
                case 4:
                    print("セーブ機能はweb版では対応しておりません")
                    await asyncio.sleep(0.1)
                    break
                case 5:
                    if len(party) == 1:
                        print("パーティは1体しかいないので変更できません。")
                        await asyncio.sleep(0.1)
                        break

                    print("誰と誰を交換しますか？")
                    await asyncio.sleep(0.1)
                    i = 1
                    for p in range(len(party)):
                        print(f"{i}: Lv.{party[i-1].level} {party[i - 1].monster_name}")
                        await asyncio.sleep(0.1)
                        i += 1
                    print("")
                    p1 = await int_input("1体目:",1,len(party))
                    p2 = await int_input("2体目:",1,len(party))
                    party[p1 - 1],party[p2 - 1] = party[p2 - 1],party[p1 - 1]
                    print("入れ替えが完了しました！")
                    print("")
                    idx = MAIN.SEARCHING
                    await asyncio.sleep(0.1)
                    break
        
        while idx == MAIN.LEVELUP:
            nessesarry_EXP = 0
            for i in party:
                nessesarry_EXP += i.level ** 3
            nessesarry_EXP  = math.floor(nessesarry_EXP / len(party) / 1.5)
            print("レベルアップチャンス！")
            print(f"お金を{nessesarry_EXP}円支払うことで他の仲間のレベルを1上昇させることができます。")
            print(f"現在の所持金:{info_items.money}円")
            print("1:する 2:しない\n:")
            await asyncio.sleep(0.1)
            ok = await int_input("",1,2)
            if ok == 1 and info_items.money >= nessesarry_EXP:
                for i in party:
                    i.level += 1
                    i.set()
                    print(f"{i.monster_name}のレベルが{i.level}に上がった！")
                    await asyncio.sleep(0.1)
                
                info_items.money = info_items.money - nessesarry_EXP
                idx = MAIN.SEARCHING

            elif ok == 1 and info_items.money < nessesarry_EXP:
                print("お金が足りません")
                print("")
                idx = MAIN.SEARCHING
                await asyncio.sleep(0.1)
            else:

                idx = MAIN.SEARCHING
        
        while idx == MAIN.HP_RECOVER:
            print("")
            print("休憩所を発見！")
            await asyncio.sleep(0.1)
            time.sleep(0.2)
            print("全員のHPが回復します")
            print("happy…")
            print("")
            await asyncio.sleep(0.1)
            time.sleep(0.2)
            
            i = 0
            for p in range(len(party)):
                party[i].battleH = party[i].H
                i += 1
            idx = MAIN.SEARCHING
        
        while idx == MAIN.BATTLE:
            print("バトル発生！")
            print("")
            await asyncio.sleep(0.1)

            enemies = [Pokemon]
            enemy = choice_pokemon(random.randint(info_items.floor, info_items.floor + 5), POSITION.WILD,info_items.type)
            #enemy = Arceus(6,POSITION.WILD)
            enemies[0] = enemy
            
            result = await battle_handling(party, enemies, info_battle_field, info_items)
            if result == BATTLE_RESULT.WIN:
                
                
                idx = MAIN.SEARCHING
            elif result == BATTLE_RESULT.LOSE:
                print("負け…")
                print("")
                print(f"あなたは第{info_items.floor}層までたどり着きました。")
                print("")
                await asyncio.sleep(0.1)

                exit()
            elif result == BATTLE_RESULT.ESCAPE:
                idx = MAIN.SEARCHING
            elif result == BATTLE_RESULT.GET:
                idx = MAIN.SEARCHING
        

        while idx == MAIN.NEXT_FLOOR:
            print("下層への階段を発見！")
            await asyncio.sleep(0.1)
            print("進みますか？\n1：進む 2：やめておく\n→")
            await asyncio.sleep(0.1)
            await asyncio.sleep(0.1)
            next = await int_input("",1,2)
            if next == 2:
                print("")
                await asyncio.sleep(0.1)
                idx = MAIN.SEARCHING
                break
            info_items.floor += 1
            
            print(f"地下{info_items.floor}階に進みます。")
            await asyncio.sleep(0.1)
            info_battle_field.field = FIELD.FLAT
            info_battle_field.field = WEATHER.FLAT
            info_items.type = ""
            randomfield = random.randint(1,100)
            if randomfield > 80:
                print("床に電流が流れている！")
                info_battle_field.field = FIELD.ELECTRIC
                info_items.type = "でんき"
                await asyncio.sleep(0.1)
            elif randomfield > 60:
                print("日差しが強い！")
                info_battle_field.field = WEATHER.SUNNY
                info_items.type = "ほのお"
                await asyncio.sleep(0.1)
            elif randomfield > 40:
                print("雨が降り始めた！")
                info_battle_field.field = WEATHER.RAINY
                info_items.type = "みず"
                await asyncio.sleep(0.1)
            idx = MAIN.SEARCHING
        
        while idx == MAIN.GATETRAINER:
            print("トレーナーが佇んでいる…")
            await asyncio.sleep(0.1)
            time.sleep(1)

            print("勝負を挑みますか？")
            print("1:はい 2:前の階に引き返す\n→")
            await asyncio.sleep(0.1)
            fight = await int_input("",1,2)
            if fight == 2:
                info_items.floor -= 1
                idx = MAIN.SEARCHING
                print(f"第{info_items.floor}階に戻った。")
                print("")
                await asyncio.sleep(0.1)
                break

            print(f"ゲートトレーナーが勝負を挑んできた！")
            await asyncio.sleep(0.1)
            enemy_party:list[Pokemon] = [Arceus(info_items.floor,POSITION.ENEMY),zacian(info_items.floor,POSITION.ENEMY),UltraNecrozma(info_items.floor,POSITION.ENEMY)]
            result = await battle_handling(party, enemy_party, info_battle_field, info_items)
            if result == BATTLE_RESULT.WIN:
                info_items.floor += 1
                print(f"地下{info_items.floor}階に進みます。")
                await asyncio.sleep(0.1)
                
                idx = MAIN.SEARCHING
            elif result == BATTLE_RESULT.LOSE:
                print("負け…")
                print("")
                print(f"あなたは第{info_items.floor}層までたどり着きました。")
                print("")
                await asyncio.sleep(0.1)
                exit()
            elif result == BATTLE_RESULT.ESCAPE:
                idx = MAIN.SEARCHING
            elif result == BATTLE_RESULT.GET:
                idx = MAIN.SEARCHING






asyncio.ensure_future(main())