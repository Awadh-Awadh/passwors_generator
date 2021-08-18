import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G',
'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',
'Z']

nums = ['0','1','2','3','4','5','6','7','8','9']

secs = ['!','@','#','$','*','(',')','&']

print("Welcome to password generator\n")
print("-"*40)

letrl =  int(input("How many letters would you like to be included?\n\n"))
numrl = int(input("How many numbers would you like to be included?\n\n"))
symrl = int(input("How many symbols would you want to be included?\n"))

'''
random.choice() returns a random element from the list.

random.sample()

sampling without replacement :use random.sapmle: 
which returns a list with the number of elements passed as the second arg
random.sample(list, number of elenments)

random.choices

sampling with replacements
random.choices(list k=no of elements)
Specify the number of elements you want to get with the argument k. Since elements are chosen with replacement, 
k can be larger than the number of elements in the original list.
'''
random_str = random.sample(letters, letrl)
random_num = random.sample(nums, numrl)
random_symb = random.sample(secs,k=symrl)
password = random_str + random_num + random_symb
# con = "".join(password)
print(password)
random.shuffle(password)
res = ''.join(password)

print (f"Your password is\n {res}")
