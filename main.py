from battlehandling import *
from pokemon import *
import time
import pickle
import os
debug_flag = DEBUG.ON



def main():
    info_items = InfoItems()
    party :list[Pokemon] = [Pokemon]
    
    idx = MAIN.SEARCHING
    info_battle_field = InfoBattleField()
    
    #バイナリデータを読み込むための変数
    data :list[list[Pokemon], InfoItems, InfoBattleField] = []
    file_path = "savedata.pickle"
    
    if not os.path.exists(file_path):
        print("ポケットモンスター(?)の世界へようこそ！")
        print("まずは、最初の仲間を選んでね！")
        n = int_input("1: LV.5 ランターン 2: LV.5 アーボック 3: LV.5 サイドン\n数字を入力:",1,6)
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
   
    else:
        print("セーブデータを読み込んでいます。")
        with open('savedata.pickle',mode='br') as info:
            data = pickle.load(info)
        party.clear()
        party = data[0]
        info_items = data[1]
        info_battle_field = data[2]
        print("読み込みが完了しました！")
        print("")
        

    

    while True:
        while idx == MAIN.SEARCHING:
            if info_items.floor % 10 == 0:
                idx = MAIN.GATETRAINER
                break

        
            print("どうする？")
            action = int_input("1:進む 2:手持ちを確認する 3:セーブする 4:セーブしてゲームを終了 5:パーティの順番を変更\n→",1,5)
            match action:
                case 1:
                    print("探索します…")
                    
                    time.sleep(1)
                    exploration  = random.randint(1,100)
                    if exploration <= 1:
                        print("何もなかった")
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
                        print(f"{i}: Lv.{party[i-1].level} {party[i - 1].monster_name}")
                        i += 1
                    status_open = int_input("誰の情報を見る？",1,len(party))
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
                        i += 1
                    break
                case 3:
                    print("セーブします")
                    if os.path.exists(file_path):
                        os.remove(file_path)
                        print(f"以前のセーブデータを削除しました。")
                    else:
                        pass
                    
                    with open('savedata.pickle',mode='wb') as info:
                        data :list = [party, info_items,info_battle_field]
                        pickle.dump(data, info)
                    print("セーブ完了！")
                    print("")
                    break
                case 4:
                    print("セーブします")
                    if os.path.exists(file_path):
                        os.remove(file_path)
                        print(f"以前のセーブデータを削除しました。")
                    else:
                        pass
                    
                    with open('savedata.pickle',mode='wb') as info:
                        data :list = [party, info_items,info_battle_field]
                        pickle.dump(data, info)
                    print("セーブ完了！")
                    print("")
                    exit()
                case 5:
                    if len(party) == 1:
                        print("パーティは1体しかいないので変更できません。")
                        break

                    print("誰と誰を交換しますか？")
                    i = 1
                    for p in range(len(party)):
                        print(f"{i}: Lv.{party[i-1].level} {party[i - 1].monster_name}")
                        i += 1
                    print("")
                    p1 = int_input("1体目:",1,len(party))
                    p2 = int_input("2体目:",1,len(party))
                    party[p1 - 1],party[p2 - 1] = party[p2 - 1],party[p1 - 1]
                    print("入れ替えが完了しました！")
                    print("")
                    idx = MAIN.SEARCHING
                    break
        
        while idx == MAIN.LEVELUP:
            nessesarry_EXP = 0
            for i in party:
                nessesarry_EXP += i.level ** 3
            nessesarry_EXP  = math.floor(nessesarry_EXP / len(party) / 1.5)
            print("レベルアップチャンス！")
            print(f"お金を{nessesarry_EXP}円支払うことで他の仲間のレベルを1上昇させることができます。")
            print(f"現在の所持金:{info_items.money}円")
            ok = int_input("1:する 2:しない\n:",1,2)
            if ok == 1 and info_items.money >= nessesarry_EXP:
                for i in party:
                    i.level += 1
                    i.set()
                    print(f"{i.monster_name}のレベルが{i.level}に上がった！")
                
                info_items.money = info_items.money - nessesarry_EXP
                idx = MAIN.SEARCHING

            elif ok == 1 and info_items.money < nessesarry_EXP:
                print("お金が足りません")
                print("")
                idx = MAIN.SEARCHING
            else:

                idx = MAIN.SEARCHING
        
        while idx == MAIN.HP_RECOVER:
            print("")
            print("休憩所を発見！")
            time.sleep(0.5)
            print("全員のHPが回復します")
            print("happy…")
            print("")
            time.sleep(2)
            
            i = 0
            for p in range(len(party)):
                party[i].battleH = party[i].H
                i += 1
            idx = MAIN.SEARCHING
        
        while idx == MAIN.BATTLE:
            print("バトル発生！")
            print("")

            enemies = [Pokemon]
            enemy = choice_pokemon(random.randint(info_items.floor, info_items.floor + 5), POSITION.WILD,info_items.type)
            #enemy = Arceus(6,POSITION.WILD)
            enemies[0] = enemy
            
            result = battle_handling(party, enemies, info_battle_field, info_items)
            if result == BATTLE_RESULT.WIN:
                
                
                idx = MAIN.SEARCHING
            elif result == BATTLE_RESULT.LOSE:
                print("負け…")
                print("")
                print(f"あなたは第{info_items.floor}層までたどり着きました。")
                print("")

                exit()
            elif result == BATTLE_RESULT.ESCAPE:
                idx = MAIN.SEARCHING
            elif result == BATTLE_RESULT.GET:
                idx = MAIN.SEARCHING
        

        while idx == MAIN.NEXT_FLOOR:
            print("下層への階段を発見！")
            next = int_input("進みますか？\n1：進む 2：やめておく\n→",1,2)
            if next == 2:
                print("")
                idx = MAIN.SEARCHING
                break
            info_items.floor += 1
            
            print(f"地下{info_items.floor}階に進みます。")
            info_battle_field.field = FIELD.FLAT
            info_battle_field.field = WEATHER.FLAT
            info_items.type = ""
            randomfield = random.randint(1,100)
            if randomfield > 80:
                print("床に電流が流れている！")
                info_battle_field.field = FIELD.ELECTRIC
                info_items.type = "でんき"
            elif randomfield > 60:
                print("日差しが強い！")
                info_battle_field.field = WEATHER.SUNNY
                info_items.type = "ほのお"
            elif randomfield > 40:
                print("雨が降り始めた！")
                info_battle_field.field = WEATHER.RAINY
                info_items.type = "みず"
            idx = MAIN.SEARCHING
        
        while idx == MAIN.GATETRAINER:
            print("トレーナーが佇んでいる…")
            time.sleep(1)
            print("勝負を挑みますか？")
            fight = int_input("1:はい 2:前の階に引き返す\n→",1,2)
            if fight == 2:
                info_items.floor -= 1
                idx = MAIN.SEARCHING
                print(f"第{info_items.floor}階に戻った。")
                print("")
                break

            print(f"ゲートトレーナーが勝負を挑んできた！")
            enemy_party:list[Pokemon] = [Arceus(info_items.floor,POSITION.ENEMY),zacian(info_items.floor,POSITION.ENEMY),UltraNecrozma(info_items.floor,POSITION.ENEMY)]
            result = battle_handling(party, enemy_party, info_battle_field, info_items)
            if result == BATTLE_RESULT.WIN:
                info_items.floor += 1
                print(f"地下{info_items.floor}階に進みます。")
                
                idx = MAIN.SEARCHING
            elif result == BATTLE_RESULT.LOSE:
                print("負け…")
                print("")
                print(f"あなたは第{info_items.floor}層までたどり着きました。")
                print("")

                exit()
            elif result == BATTLE_RESULT.ESCAPE:
                idx = MAIN.SEARCHING
            elif result == BATTLE_RESULT.GET:
                idx = MAIN.SEARCHING





if __name__ == "__main__":
    main()