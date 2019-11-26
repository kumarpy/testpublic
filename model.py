import datetime
class Breed:
    def __init__(self,id:int,name:str,temperament:str,coat:str):
        self.id = id
        self.name = name
        self.temperament = temperament
        self.coat = coat
    def breed_add(self,name:str,temperament:str,coat:str):
        self.name = name
        self.temperament = temperament
        self.coat = coat

class Pupper:
    def __init__(self,id:int,name:str,sex:str,weight:str,height:str,color:str,birthdate:datetime,breed:Breed):
        self.id = id
        self.name = name
        self.sex = sex
        self.weight = weight
        self.height = height
        self.color = color
        self.birthdate = birthdate
        self.breed = breed
    def pupper_add(self,name:str,sex:str,weight:str,height:str,color:str,birthdate:datetime,breed:Breed):
        self.name = name
        self.sex = sex
        self.weight = weight
        self.height = height
        self.color = color
        self.birthdate = birthdate
        self.breed = breed
