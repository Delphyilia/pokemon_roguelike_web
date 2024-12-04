from basedata import *
import math
from basedata import Move, Pokemon

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
        self.explain = "じめんタイプの技を無効化し、HPを回復する。"
    
    def activate_receive_move(self, ability_holder: Pokemon, attack_monster: Pokemon, move_power_ratio: list, move: Move = None):
        if move.type == "じめん":
            move_power_ratio.append(0)
            recover = math.floor(ability_holder.H / 4) if math.floor(ability_holder.H / 4) + ability_holder.battleH <= ability_holder.H else ability_holder.H - ability_holder.battleH
            print(f"{ability_holder.position}の{ability_holder.monster_name}のどしょくが発動！")
            print(f"HPが{recover}回復した！")
            print("")

class WaterAbsorb(Ability):
    def __init__(self) -> None:
        super().__init__()
        self.abilityName = "ちょすい"
        self.explain = "みずタイプの技を無効化し、HPを回復する。"
    
    def activate_receive_move(self, ability_holder: Pokemon, attack_monster: Pokemon, move_power_ratio: list, move: Move = None):
        if move.type == "みず":
            move_power_ratio.append(0)
            recover = math.floor(ability_holder.H / 4) if math.floor(ability_holder.H / 4) + ability_holder.battleH <= ability_holder.H else ability_holder.H - ability_holder.battleH
            print(f"{ability_holder.position}の{ability_holder.monster_name}のちょすいが発動！")
            print(f"HPが{recover}回復した！")
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