import random
import string

length = 32
characters = string.ascii_letters + string.digits
random_string = ''.join(random.choices(characters, k=length))
print(random_string)