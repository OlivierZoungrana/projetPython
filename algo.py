'''
palyndrone
s1= input('entrer un mot: ')
s2= "".join(list(s1)[::-1])
if(s2 == s1):
    print(s1, 'est un palyndrome')
else:
    print('nest pas un palyndrome')
'''

def removeDuplicate(l):
    SET= set(l)
    L = list(SET)
    return L

#print(removeDuplicate([1,1,3,6,6]))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("john", 36)

print(p1.name)
print(p1.age)

