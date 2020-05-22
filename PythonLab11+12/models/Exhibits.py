from abc import ABC


class Exhibits():

    def __init__(self, author: str, weight_in_kg: int, description: str, name_of_exhibit: str, decade: int, age: int):
        self.author = author
        self.weight_in_kg = weight_in_kg
        self.description = description
        self.name_of_exhibit = name_of_exhibit
        self.decade = decade
        self.age = age

    def __str__(self):
        return "Author: " + str(self.author) + "\n" \
               "Weight in kg: " + str(self.weight_in_kg) + "\n" \
               "Description is: " + str(self.description) + "\n" \
               "Name of exhibit: " + str(self.name_of_exhibit) + "\n" \
               "Decade: " + str(self.decade) + "\n" \
               "Age: " + str(self.age) + "\n"
