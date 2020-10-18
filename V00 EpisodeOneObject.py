class Forest:
    def __init__(self,
                 name,
                 length,
                 width,
                 age,
                 weakness,
                 kind
                 ):
        self.__kind = kind
        self.__age = age
        self.__weakness = weakness
        self.__length = length
        self.__name = name
        self.__width = width

    def forest_info(self):
        return f"name:{self.__name}\n" \
               f"age:{self.__age}\n" \
               f"king:{self.__kind}\n" \
               f"length:{self.__length}\n" \
               f"width:{self.__width}\n" \
               f"weakness:{self.__weakness}\n" \  
               f"that's all buddy"


class FruitTree(Forest):
    def __init__(self,
                 name="unknown",
                 length="3m",
                 width="1m",
                 age="5",
                 weakness="fire,cold and idiot people ",
                 kind="unknown",
                 number_of_trees="200",
                 ):
        super().__init__(name, length, width, age, weakness, kind)
        self.number_of_trees = number_of_trees


trees = FruitTree()
