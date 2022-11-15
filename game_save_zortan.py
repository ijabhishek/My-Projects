"""
Zortan is under attack!!! Thanos has arrived!
---------------------------------------------

Since Zortan is under attack, Abhishek calls his Avenger friends from earth.
Avengers receive his call and sends 4 avengers to save Zortan.

1. Ironman
2. Black Widow
3. Spiderman
4. Hulk

Each avenger has its attacking power and they have to fight Thanos
to save Zortan.

Avengers can attack only in pairs and get only 3 chances to kill Thanos,
or else Thanos will kill avengers and we loose the game.
"""
# import the stuff we require
from typing import Final

# Declare our constants
IRONMAN_ATTACK_POWER: Final[int] = 250
BLACKWIDOW_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 300

thanos_life: int = 1500
choice = 0
attack_num = 0

# declare helper messages
WIN_MSG: Final[str] = "You Successfully saved Zortan !!!"
LOST_MSG: Final[str] = "You killed Avengers and captured Zortan!!!"
MSG = """ 
-----------------------------------------------------------------
Zortanis under atteck, choose the pairs no. that will attack Thanos

1) Ironman & Black Widow
2) Black widow & Spiderman
3) Spiderman and Hulk
4) Hulk and Ironman
--------------------------------------------------------------------

"""


# we made some pairs by choices becouse they can fight only in pairs
while True:
    # win / loose 
    if thanos_life <= 0 and attack_num <= 3:
        print(WIN_MSG)
        # win
        break
    elif attack_num >=3 :
        print(LOST_MSG)
        #loose
        break
    print(MSG)
    choice = int(input("Enter your pair of Avengers "))
    if choice == 1:
        print("Ironman & Black widow are attecking Thanos....") 
        thanos_life = thanos_life - IRONMAN_ATTACK_POWER - BLACKWIDOW_ATTACK_POWER
        attack_num = attack_num + 1 
    elif choice == 2 :
        print("Black widow & Spiderman are attecking Thanos....")
        thanos_life = thanos_life - BLACKWIDOW_ATTACK_POWER - SPIDERMAN_ATTACK_POWER
        attack_num = attack_num + 1

    elif choice == 3:
        print("Spiderman and Hulk are attecking Thenos....")
        thanos_life = thanos_life - SPIDERMAN_ATTACK_POWER - HULK_ATTACK_POWER
        attack_num = attack_num + 1
    elif choice == 4: 
        print("Hulk and Ironman are attecking Thenos....")
        thanos_life = thanos_life - HULK_ATTACK_POWER - IRONMAN_ATTACK_POWER
        attack_num = attack_num + 1



