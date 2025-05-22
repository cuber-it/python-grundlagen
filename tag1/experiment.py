import csv

x = open("data.csv", "r")
y = csv.reader(x)
for z in y:
    if len(z) > 0:
        if z[0] != "name":
            print("Der Name ist " + z[0] + " und die Zahl ist " + str(float(z[1]) * 1.19))
    else:
        continue
x.close()
