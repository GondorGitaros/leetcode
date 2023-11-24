from math import log 

jolist = []
rosszlist = []

for i in range(1, 10000):
    a = 0.01 * float(i)
    b = a

    if a == 0.0 or b <= 0.0 or b == 1.0:
        continue

    c = log(a, b)

    if round(a**c, 2) == round(b, 2):
        jolist.append(round(a, 2))
    else:
        rosszlist.append(round(a, 2))


print("Jók: ", end="")
for i in jolist:
    print(i, end=", ")
if rosszlist == []:
    print("\nMindegyik szám jó volt")
else:
    print("\nEzek nem jók: ", end="")
    for i in rosszlist:
        print(i, end=", ")