superheroes = ['Batman','Spiderman','hawk']
#name = input("Enter your name:")
#print( name + " is the " + superheroes[1])

#superheroes[1] = "hawk"

print(superheroes)

#to print second superhero

#length_superheroes = len(superheros)
#two_superheroes = superheroes[1:length_superheroes-1]
#print(two_superheroes)

#two_superheroes = superheroes[1:3]
#print(two_superheroes)


#print(superheroes[2:])
#superheroes.remove('hawk')
#superheroes.append('Wonder')
#print(superheroes[2:])

#del superheroes[1]
#print (superheroes)

woman = ['jean grey','storm']
all_superheroes = [superheroes, woman]
print(all_superheroes)

#all_superheroes.append(superheroes)
#print(all_superheroes)

all_superheroes.extend(superheroes)
print(all_superheroes)

all_superheroes.extend(woman)
print(all_superheroes)

all_superheroes.insert(0,'antman')
print(all_superheroes)

if 'storm' in all_superheroes:
    all_superheroes.remove('storm')

    print(all_superheroes)

    print(len(all_superheroes))

    #pop
    a = all_superheroes.pop(0)
    print (all_superheroes)
    print(a)

    #clearing all the items from the list
    all_superheroes.clear()
    print(all_superheroes)


    