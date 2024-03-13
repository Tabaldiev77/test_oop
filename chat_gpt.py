“”” class Elf:
    def __init__(self, name, tribe, eyes=2, hands=2, legs=2, hair_color="green"):
        self.__name = name
        self.__eyes = eyes
        self.__hands = hands
        self.__legs = legs
        self.__hair_color = hair_color
        self.__tribe = tribe
        self.__bow_type = "wooden"
        self.__arrow_count = 20
        self.__master = None
        self.__rank = 1

    def greeting(self):
        if self.__master:
            return f"Greetings, my lord {self.__master}!"
        else:
            return "Greetings, traveler."

    def improve(self):
        if self.__rank < 5:
            self.__rank += 1
            if self.__rank == 5:
                self.__bow_type = "carbon"
            return f"{self.__name} has improved to rank {self.__rank}."
        else:
            return f"{self.__name} has already reached the highest rank."

    def increase_arrow_count(self, amount):
        self.__arrow_count += amount
        return f"{self.__name} has {self.__arrow_count} arrows now."

    def decrease_arrow_count(self, amount):
        if self.__arrow_count >= amount:
            self.__arrow_count -= amount
            return f"{self.__name} has {self.__arrow_count} arrows left."
        else:
            return "Not enough arrows."

    def change_master(self, new_master):
        self.__master = new_master
  ”””
