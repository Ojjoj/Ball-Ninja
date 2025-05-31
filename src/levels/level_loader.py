from src.levels.level_1 import Level_1
from src.levels.level_2 import Level_2
from src.levels.level_3 import Level_3
from src.levels.level_4 import Level_4
from src.levels.level_5 import Level_5
from src.levels.level_6 import Level_6

def load_levels():
     level_1 = Level_1()
     level_2 = Level_2()
     level_3 = Level_3()
     level_4 = Level_4()
     level_5 = Level_5()
     level_6 = Level_6()
     return [level_1, level_2, level_3, level_4, level_5, level_6]
