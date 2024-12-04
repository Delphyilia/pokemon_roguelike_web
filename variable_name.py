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