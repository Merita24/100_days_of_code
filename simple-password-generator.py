import random
from collections import Counter
import string

gen=lambda n:''.join(random.choice(string.ascii_letters+string.digits+string.punctuation) for _ in range(n))
password=gen(12)
counts=Counter(password)
print(f"Password generated:{password}")
print(f"Character counts:{counts}")
