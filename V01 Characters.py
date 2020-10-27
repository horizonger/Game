#Main class

class Characters:

    def __init__(self,
                 name,
                 lastname,
                 age,
                 hp,
                 title,
                 language,
                 race,
                 weakness
                 ):
        # instance variable unique to each instance
        self.__name = name
        self.__lastname = lastname
        self.__age = age
        self.__hp = hp
        self.__title = title
        self.__race = race
        self.__weakness = weakness
        self.__language = language

    def character_info(self):
        return f"ID:{self.__name} {self.__lastname}\n" \
               f"age:{self.__age}\n" \
               f"Hp:{self.__hp} \n" \
               f"race:{self.__race}\n" \
               f"title:{self.__title}\n" \
               f"weakness:{self.__weakness}\n" \
               f"language:{self.__language}\n" \
               f"that's all buddy"
    
    def attributeone(self):
        return f"{self.__name}"
    
    
    def attributetwo(self):
        return F"{self.__hp}"


class WarriorPerson(Characters):

    def __init__(self,
                 name="none",
                 lastname="none",
                 age="none",
                 hp="150",
                 title="none",
                 language="none",
                 race="human or unknown",
                 weakness="none"):
        super().__init__(name, lastname, age, hp, title, language, race, weakness)


class RegularHumanPerson(Characters):
    def __init__(self,
                 name="none",
                 lastname="",
                 age="none",
                 hp="50",
                 title="The man who be normal",
                 language="English",
                 race="human or unknown",
                 weakness="nearly everything"):
        super().__init__(name, lastname, age, hp, title, language, race, weakness)


class WitchPerson(Characters):
    def __init__(self,
                 name="none",
                 lastname="none",
                 age="none",
                 hp="896",
                 title="none",
                 language="none",
                 race="human or unknown",
                 weakness="none"):
        super().__init__(name, lastname, age, hp, title, language, race, weakness)


class VampirePerson(Characters):
    def __init__(self,
                 name="none",
                 lastname="",
                 age="none",
                 hp="500",
                 title="none",
                 language="none",
                 race="human or unknown",
                 weakness="none"):
        super().__init__(name, lastname, age, hp, title, language, race, weakness)


regular_human = RegularHumanPerson(
    name="john",
    lastname="smith",
    age="45",
    hp="50",
)

regular_humans_sidekick = RegularHumanPerson(
    name="robin",
    age="20",
    hp="32",
)

old_warrior = WarriorPerson(
    name="Berserker",
    lastname="",
    age="345",
    hp="500",
    title="old warrior",
    language="English and old vikings language",
    race="Human",
    weakness="Science"
)

old_which = WitchPerson(
    name="Sarah",
    lastname="",
    age="600",
    hp="659",
    title="Girl of beast",
    language="She knows little bit old english and witch language",
    race="Human",
    weakness="Science and light of angel"
)

young_Vampire = VampirePerson(
    name="Deacon",
    lastname="",
    age="783",
    hp="800",
    language="She knows little bit old english and new english",
    race="vampire",
    weakness="stake"
)
