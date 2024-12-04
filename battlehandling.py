from basedata import *
from basedata import InfoItems
from variable_name import BATTLE_IDX,POSITION,BATTLE_RESULT,MOVE_RESULT,FIELD
from compatibility import compatibility_ratio

debug_flag = DEBUG.ON



def battle_handling(friend_monsters:list[Pokemon], enemy_monsters:list[Pokemon], info_battle_field :InfoBattleField = None ,info_items :InfoItems = None) -> BATTLE_RESULT:
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
         time.sleep(0.5)
         print(f"味方の LV.{friend.level} {friend.monster_name} を繰り出した！")
         time.sleep(0.5)
         print("")
    else:
         print(f"相手は LV.{enemy.level} {enemy.monster_name} を繰り出した！")
         time.sleep(0.5)
         print(f"味方の LV.{friend.level} {friend.monster_name} を繰り出した！")
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
            action_choice :int = int_input(f"0:逃げる    1:交換    2:捕まえる    3:戦う\n→",0,3)
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
                    action_choice = int_input(f"4:{friend.move1.move_name} {friend.move1.PP}/{friend.move1.maxPP}    5:{friend.move2.move_name} {friend.move2.PP}/{friend.move2.maxPP}    6:{friend.move3.move_name} {friend.move3.PP}/{friend.move3.maxPP}    7:{friend.move4.move_name} {friend.move4.PP}/{friend.move4.maxPP}\n→",4,7)
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
                        delete_choice = int_input("誰を手放しますか？",1,len(friend_monsters))
                        if 1 <= delete_choice <= 12:
                            del_monster =  friend_monsters.pop(delete_choice - 1)
                        print(f"ばいばい、{del_monster.monster_name}！")
                
                    money = math.floor(enemy.baseEXP * (( (2 * enemy.level + 10) / (enemy.level + friends_ave_level + 10)) ** 2.5) + 1)
                    print("勝利！")
                    print(f"{money}円手に入れた！")
                    print("")
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
            move_handling(enemy, friend, info_battle_field)
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
            p = int_input("誰を繰り出しますか？",1,len(friend_monsters))
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
            
            
            if MOVE_RESULT.ATTACK_WIN == move_handling(move_quickness[0], move_quickness[1], info_battle_field,action_choice):
                 if move_quickness[0].position == POSITION.FRIEND and len(enemy_monsters) == 1:
                      reset_status(friend_monsters)
                      money = math.floor(enemy.baseEXP * (( (2 * enemy.level + 10) / (enemy.level + friends_ave_level + 10)) ** 2.5) + 1)
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

            if MOVE_RESULT.ATTACK_WIN == move_handling(move_quickness[1], move_quickness[0], info_battle_field,action_choice):
                 if move_quickness[1].position == POSITION.FRIEND and len(enemy_monsters) == 1:
                      reset_status(friend_monsters)
                      money = math.floor(enemy.baseEXP * (( (2 * enemy.level + 10) / (enemy.level + friends_ave_level + 10)) ** 2.5) + 1)
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

def move_handling(attack_monster :Pokemon, block_monster :Pokemon ,info_battle_field : InfoBattleField,usemove_number = None) -> MOVE_RESULT:
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
            print("タイプ一致ボーナス！") if type_match == True else None
            time.sleep(0.2)
            print(f"{attack_monster.position}の{attack_monster.monster_name}の{move.move_name}！")
            time.sleep(0.2)
            print(compatibility_message)
            time.sleep(0.2)
            print(f"{block_monster.position}の{block_monster.monster_name}に{damage}ダメージ！\n")
            time.sleep(0.2)

            print_debug("倍率補正",move_power_ratio,debug_flag)
            

            if block_monster.battleH - damage < 0:
                 print("オーバーキル！")
                 
            damage = damage if block_monster.battleH - damage >= 0 else block_monster.battleH

            block_monster.battleH = block_monster.battleH - damage

            if block_monster.battleH == 0:
                 print(f"{block_monster.monster_name}のHPが0になった！")
                 print("")
                 time.sleep(0.2)
                 return MOVE_RESULT.ATTACK_WIN
            
            move.activate(attack_monster,block_monster,info_battle_field)
            print_debug(block_monster.rankB,block_monster.B,debug_flag)

        elif move.category == MOVE_CATEGORY.STATUS:
             move.activate(attack_monster,block_monster,info_battle_field)   

        elif skip == True:
             print(f"{block_monster.position}の{block_monster.monster_name}には効果がないようだ…")
        elif skip != True:
         print(f"{attack_monster.position}の{attack_monster.monster_name}の技は外れてしまった！")
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