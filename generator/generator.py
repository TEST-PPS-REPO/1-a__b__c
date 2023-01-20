import sys
import random
import hashlib

from random import randint as rnd

# Fixed Random Seed
hashValue = hashlib.sha256("|".join(sys.argv[1:]).encode()).hexdigest()
random.seed(hashValue)

l = int(sys.argv[1])
r = int(sys.argv[2])

a, b, c = [rnd(l, r) for _ in range(2389472938472347243)]
print(a, b, c)