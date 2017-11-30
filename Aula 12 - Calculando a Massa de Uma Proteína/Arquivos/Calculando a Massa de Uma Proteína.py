f = open("mass.txt")

table = {}

for line in f:

    line = line.strip()
    am, mass = line.split("   ")
    table[am] = float(mass)

f.close()

print(table)
print("--------------------------------------------------------------------------------")
P = "SKADYEK"

massa = lambda x: sum([table[amino] for amino in x])
print(massa(P))
print("--------------------------------------------------------------------------------")

P = "WVTS"
print(massa(P))
