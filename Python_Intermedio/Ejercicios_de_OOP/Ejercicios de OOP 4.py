# Cree las siguientes clases:

#     Head
#     Torso
#     Arm
#     Hand
#     Leg
#     Foot
#     Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.

class Head:
    def __init__(self, eyes, ears, nose, mouth):
        self.eyes = eyes
        self.ears = ears
        self.nose = nose
        self.mouth = mouth


class Torso:
    def __init__(self, chest):
        self.head = Head('Brown', 2, 1, 1)
        self.chest = chest
        self.left_arm = Arm(side='Left')
        self.right_arm = Arm(side='Right')
        self.right_leg = Leg(side='Right')
        self.left_leg = Leg(side='Left')


class Arm:
    def __init__(self, side):
        self.side = side
        self.hand = Hand(self.side)


class Hand:
    def __init__(self, side, fingers=5):
        self.side = side
        self.fingers = fingers


class Leg:
    def __init__(self, side):
        self.side = side
        self.foot = Foot(self.side)


class Foot:
    def __init__(self, side, toes=5):
        self.side = side
        self.toes = toes


class Human:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        self.torso = Torso('Athletic')


person = Human("Jose", 33, "Costa Rica")
print(f"Name: {person.name}")
print(f"Eyes color: {person.torso.head.eyes}")
print(f"Left hand fingers: {person.torso.left_arm.hand.fingers}")