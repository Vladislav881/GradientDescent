from fiveMetOpt import function
import random

step = 2


n = random.sample(range(2, 10**3), 100)
k = random.sample(range(1, 10**3), 100)

for n in range(len(n)):
    for k in range(len(k)):
        function(n, k)