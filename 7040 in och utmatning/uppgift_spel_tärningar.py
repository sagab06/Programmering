import random

t1 = random.randrange(1, 7)
t2 = random.randrange(1, 7)
print(t1)
print(t2)

if t1 == t2:
    print("Du vann")
elif t1 + 1 == t2 or t1 == t2 + 1:
    print("stege")
    #stege
elif t1 == 6:
    print("Du vann")
elif t2 == 6:
    print("Du vann")


else:
    print("Du vann inte")