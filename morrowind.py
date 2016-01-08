from random import choice
from random import randint
attributenum = randint(0,7)
racenum = randint(0,9)
skillnum = randint(0,26)
signnum = randint(0,12)
signs = ["tower", "shadow", "lover", "ritual", "atronach", "apprentice", "lord", "steed", "lady", "serpent", "thief", "mage", "warrior"]
skills = ["heavy armour", "medium armour", "spear", "acrobatics", "armourer", "axe", "blunt", "long blade", "block", "light armour", "marksman", "sneak", "athletics", "hand-to-hand", "short blade", "unarmoured", "illusion", "mercantile", "speechcraft", "alchemy", "conjuration", "enchant", "security", "alteration", "destruction", "mysticism", "restoration"]
races = ["altmer", "argonian", "bosmer", "breton", "dunmer", "imperial", "khajiit", "nord", "orc", "redguard"]
attributes = ["agility", "endurance", "intelligence", "luck", "personality", "speed", "strength", "willpower"]
print("your race is " + races[racenum])
print("your birthsign is " + signs[signnum])
skillcalc = 0
attributecalc = 0
print("your major skills are as follows:")
for skillcalc in range(0,5):
	print(choice(skills))
	skillcalc + 1
print("your minor skills are as follows:")
skillcalc = 0
for skillcalc in range(0,5):
	print(choice(skills))
	skillcalc + 1
print("your primary attributes are as follows:")
for attributecalc in range(0,2):
	print(choice(attributes))
	attributecalc + 1
