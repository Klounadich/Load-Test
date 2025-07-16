import random
import string
charactres = string.ascii_letters 
passs = string.digits
print ("Get a random users ?")
input()

randomUsername = ''.join(random.choice(charactres) for i in range(10))
print(f"Username:{randomUsername}")
randomPassword=''.join(random.choice(passs)  for i in range(10))
print(f"Password:{randomPassword}")
