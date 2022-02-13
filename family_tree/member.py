from enum import Enum, auto

class Gender(Enum):
     MALE = auto()
     FEMALE = auto()


class Member:
    def __init__(self, id, name, gender):
        self.id = id
        self.name = name
        self.gender = Gender(gender)
        self.mother = None
        self.father = None
        self.spouse = None
        self.children = []
    
    def set_mother(self, mother):
        if not isinstance(mother, Member):
            raise ValueError('Invalid value for mother')
        if mother.gender != Gender.FEMALE:
            raise ValueError("Mother can't be a male, she must be a FEMALE")
        self.mother = mother
        
    def set_father(self, father):
        if not isinstance(father, Member):
            raise ValueError('Invalid value for father')
        if father.gender != Gender.MALE:
            raise ValueError("Father can't be a female, she must be a MALE")
        self.father = father
        
    def set_spouse(self, spouse):
        if not isinstance(spouse, Member):
            raise ValueError('Invalid value for spouse')
        if self.gender == spouse.gender:
            raise ValueError("Invalid gender value for spouse."
            "Spouse and member cannot have the same gender")
        self.spouse = spouse

    def add_child(self, child):
        if not isinstance(child, Member):
            raise ValueError('Invalid value for child')
        self.children.append(child)
        

