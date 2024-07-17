
adress = ['applewood',34,'berrywood','alabama',18967]

dict_adress = {'houseNum':34,'street':'applewood','city':'berrywood','state':'alabama','pin':18967}

dict_adress2 = {'state':'alabama','street':'applewood','houseNum':34,'city':'berrywood','pin':18967}

#printing the dictionary

print(dict_adress)
print(dict_adress['houseNum'])

#printing all VALUES and KEYS of the dictionary

print(dict_adress.values())
print(dict_adress.keys())

#printing each pair 1 by 1

for key in dict_adress:
    print(key,dict_adress[key])

#checking if a keys is in a dictionary

if 'apartment' in dict_adress:
    print(dict_adress['apartment'])
else:
    print("We couldn't find the key you were looking for! Try again later!")

if 'state' in dict_adress:
    print(dict_adress['state'])
else:
    print("We couldn't find the key you were looking for! Try again later!")

#adding a new key and value

dict_adress['apartment'] = 'cherrywood'
print(dict_adress)

#deleting key and value pairs

del dict_adress['apartment']
print(dict_adress)

#changing values (Can't change existing keys)

dict_adress['pin'] = 54321
print(dict_adress)

#adding list in dictionaries

dict_adress['family'] = ['bob','joe','anna','ellie']
print(dict_adress)

#printing item inside the list

print(dict_adress['family'][1])

#making a dictionary in a dictionary

classroom = {
    'student1': {
        'name':'bobby',
        'score':96,
        'age':10,
        'grade':5,
    },
    'student2': {
        'name':'lily',
        'score':94,
        'age':11,
        'grade':6,
    }
}