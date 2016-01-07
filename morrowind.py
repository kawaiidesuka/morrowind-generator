from random import sample
from random import randint
attributenum = randint(0,7)
racenum = randint(0,9)
skillnum = randint(0,26)
signnum = randint(0,12)
signs = ["tower", "shadow", "lover", "ritual", "atronach", "apprentice", "lord", "steed", "lady", "serpent", "thief", "mage", "warrior"]
skills = ["heavy armour", "medium armour", "spear", "acrobatics", "armourer", "axe", "blunt", "long blade", "block", "light armour", "marksman", "sneak", "athletics", "hand-to-hand", "short blade", "unarmoured", "illusion", "mercantile", "speechcraft", "alchemy", "conjuration", "enchant", "security", "alteration", "destruction", "mysticism", "restoration"]
races = ["altmer", "argonian", "bosmer", "breton", "dunmer", "imperial", "khajiit", "nord", "orc", "redguard"]
attributes = ["agility", "endurance", "intelligence", "luck", "personality", "speed", "strength", "willpower"]
print races[racenum]
print signs[signnum]
print sample(skills, 10)
print sample(attributes, 2)
