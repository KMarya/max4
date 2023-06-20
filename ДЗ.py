s = input('Введите слово: ')
r = reversed(s)
ispal = True
for a in s[:len(s)//2]:
    if a != next(r):
        ispal = False
        break
print("True" if ispal else "False")



