import re

f = open("rna_codon_table.txt")

table = {}

for line in f:

    line = line.strip()
    line = [ (codon.split(' ')[0], codon.split(' ')[1]) for codon in re.split(r'[ ]{2,3}', line) if codon]

    for r in line:

        table[r[0]] = r[1]

print(table)

f.close()

print("--------------------------------------------------------------------------------")

def translation(rna):

    protein = ""

    for start in range(0, len(rna), 3):

        if table[rna[start:start+3]] != "Stop":

            protein += table[rna[start:start+3]]

    return protein

rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

out = translation(rna)
print(out)

print("--------------------------------------------------------------------------------")

f = open("rosalind_prot.txt")

rna = f.read()
rna = rna.strip()

out = translation(rna)
print(out)

f.close()
