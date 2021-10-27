#Basic
for x in range(0,151):
    print(x)

#Mulitples of Five
for x in range(5,1001,5):
    print(x)

#Counting, the Dojo Way
for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

#Whoa. That sucker's huge (hehe)
total = 0
for x in range(1,500000,2):
    total = total + x
    print(x)
print(total)

#Countdown by Fours
for x in range(2018, -1, -4):
    print(x)

# Flexible Counter
lowNum = 11
highNum = 112
mult = 8
for x in range(lowNum,highNum):
    if x % mult == 0:
        print(x)
