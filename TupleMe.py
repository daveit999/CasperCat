#When compared with lists, tuples are simple data structures. Use them
#when you want to store a set of values that should not be changed throughout
#the life of a program


dim = (200, 50)
print(dim[0])
print(dim)


man = (500, 40)
print(man)

#Looping Through All Values in a Tuple

for mann in man:
    print(mann)

print('Original man')
for mann in man:
    print(mann)
    
man = (1000, 90)
print('\nModified man')
for mann in man:
    print(mann)
    
    
dave = (65, 1956)
print(dave)
