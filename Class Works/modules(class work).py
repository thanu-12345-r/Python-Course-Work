import random

random.seed(100)
print(random.randint(1,6))
print(random.uniform(1,6))
names=['Thanmai','Rojasri','mohanapriya','navya','renuka']
print(random.choice(names))
print(random.choices(names,k=3))
random.shuffle(names)
print(names)

