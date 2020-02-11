import csv
import numpy as np


class Player:
    def __init__(self, name, initiative):
        self.name = name
        self. initiative = initiative


class Enemy:
    def __init__(self, Name, HP, init, EAC, KAC):
        self.name = Name
        self.HP = int(HP)
        self.init = int(init)
        self.EAC = int(EAC)
        self.KAC = int(KAC)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


characters = []
number_players = int(input("How many PC's:\n"))
encounter_name = input('Encounter Name:\n')
encounter_name = encounter_name + '.csv'
encounter_path = "Encounters/" + encounter_name

with open(encounter_path, 'r') as f:
    reader = csv.reader(f)
    encounter = list(reader)
for i in encounter:
    print(i)
print('\n')
encounter.pop(0)

for i in encounter:
    init = np.random.randint(1, 20) + int(i[2])
    for j in range(int(i[1])):
        characters.append([Enemy(i[0], i[5], i[2], i[3], i[4]), init])


for i in range(number_players):
    name = input('Player Name:\n')
    init = int(input(f"{name}'s init:\n"))
    characters.append([name, init])

characters.sort(key=lambda characters: characters[1], reverse=True)

for i in characters:
    print(i)