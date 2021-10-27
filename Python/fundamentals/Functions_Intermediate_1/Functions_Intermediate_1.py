#section 1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = "Bryant"
sports_directory['soccer'[0]] = "Andres"
z[0]['y'] = 30


#Section 2
def iterateDictionary(a_list_of_dictionaries):
    for x in a_list_of_dictionaries:
        print(f'first_name - {x["first_name"]}, last_name - {x["last_name"]}')

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
print('\n')

#Section 3
def iterateDictionary2(key_name, somelist):
    for lexi in somelist:
        print(lexi[key_name])

iterateDictionary2('first_name', students) 
print('\n')
iterateDictionary2('last_name', students) 
print('\n')

#Section 4
def printInfo(lexi):
    for valor in lexi.values():
        print(len(valor))
        for element in valor:
            print(element)
        print('\n')


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
