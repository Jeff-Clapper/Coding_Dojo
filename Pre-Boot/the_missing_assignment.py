vowels = ['a','e','i','o','u','y']
non_vowel = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

name = input('Write what you will: ')
name = name.lower()
name = str(name)

vowel = 0
cons = 0

for letter in name:
    if letter in vowels:
        vowel += 1 
    elif letter in non_vowel:
        cons += 1

print(vowel)
print(cons)


