class Characters:

    def __init__(self,
                 name="none",
                 lastname="none",
                 age="none",
                 hp="50",
                 title="none",
                 language="none",
                 race="human or unknown",
                 weakness="none"
                 ):
        # instance variable unique to each instance
        self.name = name
        self.lastname = lastname
        self.age = age
        self.hp = hp
        self.title = title
        self.race = race
        self.weakness = weakness
        self.language = language

    def character_info(self):
        return f"ID:{self.name} {self.lastname}\n" \
               f"age:{self.age}\n" \
               f"Hp:{self.hp} \n" \
               f"race:{self.race}\n" \
               f"title:{self.title}\n" \
               f"weakness:{self.weakness}\n" \
               f"language:{self.language}\n" \
               f"that's all buddy"


class WarriorPerson(Characters):

    def __init__(self,
                 name="none",
                 lastname="none",
                 age="none",
                 hp="50",
                 title="none",
                 language="none",
                 race="human or unknown",
                 weakness="none"):
        super().__init__(name, lastname, age, hp, title, language, race, weakness)
        self.hp = int(int(self.hp) + 100)


class RegularHumanPerson(Characters):
    def __init__(self,
                 name="none",
                 lastname="none",
                 age="none",
                 hp="50",
                 title="none",
                 language="none",
                 race="human or unknown",
                 weakness="none"):
        super().__init__(name, lastname, age, hp, title, language, race, weakness)
        self.hp = int(int(self.hp) - 30)


class WitchPerson(Characters):
    def __init__(self,
                 name="none",
                 lastname="none",
                 age="none",
                 hp="50",
                 title="none",
                 language="none",
                 race="human or unknown",
                 weakness="none"):
        super().__init__(name, lastname, age, hp, title, language, race, weakness)
        self.hp = int(int(self.hp) - 120)


class VampirePerson(Characters):
    def __init__(self,
                 name="none",
                 lastname="none",
                 age="none",
                 hp="50",
                 title="none",
                 language="none",
                 race="human or unknown",
                 weakness="none"):
        super().__init__(name, lastname, age, hp, title, language, race, weakness)
        self.hp = int(int(self.hp) + 450)


# Characters:
regular_human = RegularHumanPerson(
    name="john",
    lastname="smith",
    age="45",
    title="The man who be normal",
    language="He knows only English",
    race="Human",
    weakness="who knows"
)

old_warrior = WarriorPerson(
    name="Berserker",
    lastname="",
    age="345",
    title="old warrior",
    language="English and old vikings language",
    race="Human",
    weakness="Science"
)

old_which = WitchPerson(
    name="Sarah",
    lastname="",
    age="600",
    title="Girl of beast",
    language="She knows little bit old english and witch language",
    race="Human",
    weakness="Science and light of angel"
)

young_Vampire = VampirePerson(
    name="Deacon",
    lastname="",
    age="783",
    language="She knows little bit old english and new english",
    race="vampire",
    weakness="stake"
)


