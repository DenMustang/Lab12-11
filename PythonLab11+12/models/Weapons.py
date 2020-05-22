from models.Exhibits import Exhibits

class Weapons(Exhibits):
        def __init__(self, author: str, weight_in_kg: int, description: str, name_of_exhibit: str, decade: int, age: int, type_of_weapon: str):
            super().__init__(author, weight_in_kg, description, name_of_exhibit, decade, age)
            self.type_of_weapon = type_of_weapon

        def __str__(self):
            return super.__str__(self) + \
                   "Type of weapon: " + str(self.type_of_weapon) + "\n"
