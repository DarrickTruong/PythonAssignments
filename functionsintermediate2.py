# 1.1
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
# print(x)

# 1.2
students[0]['last_name'] = 'Bryant'
# print(students)

# 1.3
sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# 1.4
z[0]['y'] = 30
# print(z[0]['y'])

# 2
def iterateDictionary(some_list):
    for val in some_list:
        print(val)

# iterateDictionary(students)

students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# 3
def iterateDictionary2(key_name, some_list):
    for val in range(len(some_list)):
        print(some_list[val][key_name])

# iterateDictionary2('first_name', students)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# 4
def printInfo(some_dict):
    for key in some_dict:
        print(len(dojo[key]), key)
        for val in some_dict:
            print(some_dict[key])
            break

printInfo(dojo)