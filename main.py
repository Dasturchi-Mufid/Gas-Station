from random import sample
import string

a = ''.join(sample(string.ascii_letters + string.digits, 15))
print(a)