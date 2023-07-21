from numpy import random as rd
import pandas as pd
import numpy as np

def random_grades():
    grades_list = []

    for i in range(0, 4):
        grade = round(np.random.normal(6, 2.5), 2)

        if grade >= 10:
            grade = 10
        elif grade <= 0:
            grade = 0
        else:
            pass

        grades_list.append(grade)
    return grades_list

class Student:

    all = []

    @classmethod
    def generate_random_students(cls, n):
        for i in range(0,n):
            gender = rd.choice(['M', 'F'])

            if gender == 'M':
                boy_names = pd.read_csv('boy_names.csv')
                last_name = pd.read_csv('last_names.csv')
                
                name = str(rd.choice(boy_names['names']) + ' ' + rd.choice(last_name['last_names']))
            else:
                girl_names = pd.read_csv('girl_names.csv')
                last_name = pd.read_csv('last_names.csv')

                name = str(rd.choice(girl_names['names']) + ' ' + rd.choice(last_name['last_names']))
            
            serie = rd.randint(1, 4)

            if serie == 1:
                age = rd.randint(14, 17)
            elif serie == 2:
                age = rd.randint(15, 18)
            elif serie == 3:
                age = rd.randint(16, 19)
            
            ptg_grades = random_grades()
            mt_grades = random_grades()
            hist_grades = random_grades()
            geo_grades = random_grades()
            ing_grades = random_grades()
            art_grades = random_grades()

            student = Student(name, age, gender, serie, ptg_grades, mt_grades, hist_grades, geo_grades, ing_grades, art_grades)



    def __init__(
            self,
            Std_name: str, 
            Std_age: int, 
            Std_gender: str,
            Std_serie: int, 
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
        self.Std_serie = Std_serie
        self.Ptg_grades = Ptg_grades
        self.Mt_grades = Mt_grades
        self.Hist_grades = Hist_grades
        self.Geo_grades = Geo_grades
        self.Ing_grades = Ing_grades
        self.Art_grades = Art_grades

        Student.all.append(self)

Student.generate_random_students(10)

for instance in Student.all:
    print(instance.Ptg_grades)