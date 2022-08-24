#liste

fruits = ["papaye", "mangue", "pomme"]

print(fruits)

#tuple

fruitsTuple = ("apple", "banana")

y = tuple(fruits)

print(y)

#set

thisset = {"apple", "banana"}

thisset.add("ornage")
thisset.update(["fraise", "pinepale"])
set2 = {"fraise", "mangue"}

#print(thisset.difference(set2))
#print(thisset)

#dictionnaires

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

for x in thisdict:
    print(x)
for x in thisdict:
    print(thisdict[x])
    

# fichier

f = open("fichier.txt", "a")
f.write("olivier")
f.close()
f = open("fichier.txt", "r")
print(f.read())
    

