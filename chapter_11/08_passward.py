import random
import string
setOfStr = string.ascii_letters +string.digits+string.punctuation
pass_len = int(input("Enter length of passward needed  : "))
passward = "".join([random.choice(setOfStr) for i in range (pass_len)])
print(passward)

