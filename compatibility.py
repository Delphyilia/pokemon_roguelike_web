

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

