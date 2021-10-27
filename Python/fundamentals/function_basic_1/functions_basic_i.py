#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#prediction: prints the number 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#Prediction: This will return an error

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#Prediction: This will print 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#Prediction: This will print the number 5


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#Prediction: This will print 5 once


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#prediction: This will print 3 and 5 but not add

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#Prediction: This will print "2 5"

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#Prediction: This will print 100 and will return the value of 10, which will then be printed by the print statement

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#Prediction: print 7, print 14, print 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#prediction: print 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#Prediction: print 500, prints 300, print 500
#Special note: i missed the extra print(b) after the defining block

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#Prediction: print 500, print 500, print 300, print 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#Prediction: print 500, print 500, print 300, print 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#Prediction: print 1, error as bar has not been defined yet

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#Prediction: print 1, print 3, print 5, print 105