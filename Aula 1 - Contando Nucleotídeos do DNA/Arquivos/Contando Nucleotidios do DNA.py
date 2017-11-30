f = open("rosalind_dna.txt")
dna = f.read()

print("   --> Rosalind DNA <--")
print("Quantidade de Amostras do DNA: %d" % len(dna))
print("Quantidade de Adenina: %d" % dna.count('A'))
print("Quantidade de Timina: %d" % dna.count('T'))
print("Quantidade de Guanina: %d" % dna.count('G'))
print("Quantidade de Citosina: %d" % dna.count('C'))

f.close()
