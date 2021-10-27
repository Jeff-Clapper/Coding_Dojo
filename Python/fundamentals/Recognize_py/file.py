"""Not sure I understood this assignment"""

num1 = 42 #this creates a variable containing the int 42
num2 = 2.3 #this creates a variable containing the fload 2.3
boolean = True #this sets a boolean value to true
string = 'Hello World' #creates variable congining the string Hello World"
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Creates a list containing pizza toppings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #cretes a dictionary of a persion profile
fruit = ('blueberry', 'strawberry', 'banana') #creates a tuple containing fruit
print(type(fruit)) #prints the type of data fruit contains. In this case, a tuple
print(pizza_toppings[1]) #prints the second item within the "pizza topping" list 
pizza_toppings.append('Mushrooms') #adds mushrooms to the end of the pizza_topping list
print(person['name']) #prints the value assigned to the key "name" within the person dictionary
person['name'] = 'George' #sets the value of the name key to George within the person dictionary
person['eye_color'] = 'blue' #creates a key "eye color" and sets it to blue in the person dictionary
print(fruit[2]) #prints the 3rd item in the fruit tuple

if num1 > 45:  #initiates an if-then statement where num1 is compared to the given int. In this case it would skip the if portion
    print("It's greater")
else:
    print("It's lower") #the else condition would be activated in this case

if len(string) < 5:  #initiates an if-then statement where the number if characters in the string is analyzed
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:           #in this case, the else command would be the one run
    print("Just right!")

for x in range(5):  #initiates a for loop. I belive this will print x 5 times
    print(x)
for x in range(2,5): #initiates a for loop that prints x starting at two and ending at 5. This would print x 3 times
    print(x)
for x in range(2,10,3): #initiates a for loop that prints x starting at two and ending at 10, while skipping 3 numbers in between.
    print(x)  #in this case, I believ X will be printed 3 times
x = 0 #sets value of X to 0
while(x < 5): #initiates a while loop that will print x and then add 1 to it until it is equal to or greater than 5
    print(x)
    x += 1

pizza_toppings.pop() #this removes the last item the list, while still retaining the value for further use
pizza_toppings.pop(1) #this removes the 2nd value in a list, while still retaining the value for further use

print(person) #This prints the dictionary "person"
person.pop('eye_color') #This removes the key-value pair "eye color"
print(person) #this prints the dictionary "person"

for topping in pizza_toppings: #a for loop that analyzes individual topping the the pizza topping list. 
    if topping == 'Pepperoni': #if statement comparing the topping for a specific value
        continue    #This causes the loop to go back to the top (as if the step and been run) and continues the process
    print('After 1st if statement') #prints a statement if topping isn't pepperoni
    if topping == 'Olives': #this if statement will end the for loop if the topping is olive
        break

def print_hello_ten_times(): #creates a function
    for num in range(10):
        print('Hello')

print_hello_ten_times() #calls the created function
 
def print_hello_x_times(x):  #creates a function that requires an argument
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #calls the function while providing the argument

def print_hello_x_or_ten_times(x = 10): #creates a function that accepts an argument, but defines a default if not provided
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #calls the function,accepting the default value of 10
print_hello_x_or_ten_times(4) #calls the function, accepting the argument provided


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)