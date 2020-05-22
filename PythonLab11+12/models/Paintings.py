from models.Exhibits import Exhibits

class Paintings(Exhibits):
    def __init__(self,  author: str, weight_in_kg: int, description: str, name_of_exhibit: str, decade: int, age: int,
                 style_of_painting: str):
        super().__init__(author, weight_in_kg, description, name_of_exhibit, decade, age)
        self.style_of_painting = style_of_painting

    def __str__(self):
        return super.__str__(self) + \
               "Style of painting: " + str(self.style_of_painting) + "\n"
