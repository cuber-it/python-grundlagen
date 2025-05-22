import random
 
tipp = [1, 2, 3, 4, 5, 6]
ziehung = random.sample(range(1,50), 6)
 
treffer = []
for zahl in tipp:
    if zahl in ziehung:
        treffer.append(zahl)
print(tipp)
print(ziehung)
print(treffer)
 
treffer = list(set(tipp).intersection(set(ziehung)))
print(treffer)
 
treffer = [zahl for zahl in tipp if zahl in ziehung] # List comprehension
print(treffer)