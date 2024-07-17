
userNum = input("Type a random number! ")

digits = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

for i in userNum:
    if i in digits:
        digits[i]+=1

pangram = True

for j in digits.values():
    if j == 0:
        pangram = False

if pangram == True:
    print("Your number is a pangram! ")
else:
    print("Your number is not a pangram! ")