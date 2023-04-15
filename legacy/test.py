import random
from customtools import *

p = [i for i in range(1,1000000)]
random.shuffle(p)
p1 = p
random.shuffle(p1)
z = [complex(p[a],p1[a]) for a in range(99999)]
print("ready")
for c in z:
    abs(c)
print("done")
for c in z:
    mod(c)
print("done")
for c in z:
    fmod(c)
print("done")