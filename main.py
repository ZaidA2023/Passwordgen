import random

def ranspec():
    special = ['!','"','@','#','$','%','^','&','*','(',')','-','_','+','=','\\\\','|','{','[','}',']',';',':','<','>',',','.','?','/','`','~']
    return special[random.randint(0,30)]

def rannum():
    return random.randint(0, 9)

def ranalph():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    wah = alphabet[random.randint(0,25)]
    return wah

password = ""
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(20):
    x = random.randint(0,2)
    if x == 0:
        password = password + ranspec()
    elif x==1:
        password = password + str(rannum())
    elif x==2:
        password = password + ranalph()
print(password)