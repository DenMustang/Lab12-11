from models.Weapons import Weapons

class ExhibitManager:

    def __init__(self):
        self.weapons_in_arsenal = []

    def add_weapon_to_arsenal(self, *weapons_to_add: Weapons):
        for weapon in weapons_to_add:
            self.weapons_in_arsenal.append(weapon)

    def remove_weapon_from_arsenal(self, *weapons_to_remove: Weapons):
        for weapon in weapons_to_remove:
            self.weapons_in_arsenal.remove(weapon)

    def find_weapons_by_decade(self, decade_to_compare: int):
        """
        >>> first_weapon = Weapons("Unknown author", 12, "Very sharp weapon", "Chamber", 1032, 132, "Spear")
        >>> second_weapon = Weapons("Pablo Belizzi", 20, "Very convenient weapon", "Seditious", 1234, 102, "Sword")
        >>> third_weapon = Weapons("Unknown author", 12, "Really small weapon", "No name", 1489, 92, "Tomahawk")
        >>> exhibit = ExhibitManager()
        >>> exhibit.add_weapon_to_arsenal(first_weapon, second_weapon, third_weapon)
        >>> result = exhibit.find_weapons_by_decade(1300)
        >>> [weapon.decade for weapon in result]
        [1032, 1234]
        """
        result: list = []
        for weapon in self.weapons_in_arsenal:
            if weapon.decade < decade_to_compare:
                result.append(weapon)
        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False, extraglobs={'arsenal': ExhibitManager()})
