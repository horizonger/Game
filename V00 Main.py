# Modules
from GameIGuess import Character
from GameIGuess import Episode1



#Episode function
def episode_one(episode):
    return episode1.welcome(episode)

def first(step_one):
    return episode1.first_choose(step_one)


print("""

WELCOME THE GAME
JUST CHOOSE ONE CHARACTER
Character:
        1:WARRIOR
        2:ORDINARY PERSON
        3:VAMPIRE
        4:WITCH
""")

while True:
    first_Character = int(input(">>>"))

    if first_Character == 1:
        print(Character.old_warrior.character_info())
        character1 = Character.old_warrior.attributes()
        episode_one(character1)
    elif first_Character == 2:
        print(Character.regular_human.character_info())
        character2 = Character.old_warrior.attributes()
        episode_one(character2)

    elif first_Character == 3:
        print(Character.young_Vampire.character_info())
        character3 = Character.old_warrior.attributes()
        episode_one(character3)

    elif first_Character == 4:
        print(Character.old_which.character_info())
        character4 = Character.old_warrior.attributes()
        episode_one(character4)
