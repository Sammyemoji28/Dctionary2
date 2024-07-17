
user = input("Type a random sentance! ")

'''vowels = {'a':0,'e':0,'i':0,'o':0,'u':0}

for i in user:
    if i in vowels:
        vowels[i]+=1

print(vowels)
'''
#2nd approach

vowel_list = ['a','e','i','o','u']

vowel_dict = {}

for letter in user:
    if letter in vowel_list:
        if letter in vowel_dict:
            vowel_dict[letter] +=1
        else:
            vowel_dict[letter] = 1

print(vowel_dict)