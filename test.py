prastevila = [2]
trenutno = 3
while trenutno < 200:
    if not 0 in [trenutno % n for n in prastevila]:
        prastevila.append(trenutno)
    trenutno += 2
print(prastevila)