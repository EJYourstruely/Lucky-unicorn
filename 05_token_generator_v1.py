"""COmponent 3  (random tokens) V1
Generates random choice of token in random order"""

import random

tokens = ["unicorn", "horses", "donkey", "zebra"]

# Testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')