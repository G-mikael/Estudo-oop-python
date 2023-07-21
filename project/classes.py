from numpy import random

class Student:

    def generate_random_students(n):
        pass

    def __init__(
            self,
            Std_name: str, 
            Std_age: int, 
            Std_gender: str, 
            Ptg_grades: list, 
            Mt_grades: list, 
            Hist_grades: list, 
            Geo_grades : list, 
            Ing_grades: list, 
            Art_grades: list
            ):
        
        self.Std_name = Std_name
        self.Std_age = Std_age
        self.Std_gender = Std_gender
        self.Ptg_grades = Ptg_grades
        self.Mt_grades = Mt_grades
        self.Hist_grades = Hist_grades
        self.Geo_grades = Geo_grades
        self.Ing_grades = Ing_grades
        self.Art_grades = Art_grades


